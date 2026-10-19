#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
server.py — Servidor Integrado de API e Dashboard do Second Brain
================================================================
Fornece:
- Servidor estático para o Frontend (HTML5, Canvas, CSS, JS)
- Endpoint POST /api/chat: Pipeline principal do Aurelio AI (Ollama Local)
- Endpoint GET /api/aurelio/status: Status e modelos do Ollama local
- Endpoint POST /api/aurelio/model: Troca dinâmica de modelo Ollama
- Endpoint GET /api/telemetry: Dados de telemetria diária e censo
- Recomendador inteligente de Skills e Ferramentas do Hub integrado
"""
import sys
import os
import json
import urllib.request
import urllib.error
from http.server import SimpleHTTPRequestHandler, HTTPServer
from pathlib import Path

# Force UTF-8 on Windows cleanly
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SB_ROOT = Path(__file__).resolve().parent.parent

# Inject Aurelio into path
BACKEND_DIR = SB_ROOT / "backend" / "aurelio"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

try:
    from core import orchestrator
    from database import db
    from models import model_manager
    orchestrator.inicializar_sistema()
    GLOBAL_SESSION = orchestrator.nova_sessao()
except Exception as e:
    print("[AVISO] Aurelio local em modo fallback:", e)
    GLOBAL_SESSION = "default"

# ─────────────────────────────────────────────────────────────
# Banco de Regras e Gatilhos para Sugestão de Skills & Repositórios
# ─────────────────────────────────────────────────────────────
SKILLS_TRIGGERS = [
    {"name": "@frontend-design", "desc": "Design premium sem visual genérico, tokens e tipografia", "terms": ["frontend", "design", "css", "ui", "ux", "visual", "layout", "tela"]},
    {"name": "@clean-code", "desc": "Padrões pragmáticos, código conciso, direto e sem duplicação", "terms": ["clean code", "refatorar", "refactor", "qualidade", "limpar código"]},
    {"name": "@testing-patterns", "desc": "Padrões de testes unitários, mocks e TDD rigoroso", "terms": ["teste", "test", "tdd", "unitario", "mock", "assert"]},
    {"name": "@rpa_governance", "desc": "Governança Zero Trust e cabeçalhos obrigatórios em pastas", "terms": ["rpa", "governanca", "zero trust", "padrao pasta", "compliance"]},
    {"name": "@systematic-debugging", "desc": "Metodologia em 4 fases para investigar causas raiz", "terms": ["debug", "erro", "bug", "crash", "falha", "investigar"]},
    {"name": "@architecture", "desc": "Tomada de decisão arquitetural, ADRs e compensações", "terms": ["arquitetura", "estrutura", "adr", "projeto", "sistema"]},
    {"name": "@nextjs-react-expert", "desc": "Otimização de bundle e eliminação de waterfalls", "terms": ["react", "next", "render", "hook", "componente"]},
    {"name": "@api-patterns", "desc": "Design de APIs REST/GraphQL, paginação e versionamento", "terms": ["api", "rest", "endpoint", "rota", "payload", "json"]},
    {"name": "@database-design", "desc": "Modelagem relacional, índices e schemas otimizados", "terms": ["banco", "database", "sqlite", "sql", "tabela", "schema"]}
]

REPOS_TRIGGERS = [
    {"name": "docling", "cat": "document_web_parsers", "desc": "Parser multimodal para PDFs complexos e tabelas", "terms": ["pdf", "extrair pdf", "tabela pdf", "documento"]},
    {"name": "VoiceStudio", "cat": "media_processing", "desc": "Síntese neural TTS e clonagem vocal offline", "terms": ["voz", "audio", "som", "tts", "falar", "sintetizar"]},
    {"name": "impeccable", "cat": "ui_ux_design", "desc": "Design tokens de classe mundial e microinterações", "terms": ["design tokens", "microinteracao", "animacao ui", "estilo"]},
    {"name": "rea", "cat": "dev_reverse_engineering", "desc": "Engenharia reversa e inspeção de binários .exe/.dll", "terms": ["engenharia reversa", "descompilar", "dll", "binario", "exe"]},
    {"name": "paperclip", "cat": "media_processing", "desc": "Conversão de screenshots diretamente em código frontend", "terms": ["screenshot to code", "imagem para codigo", "print para html"]},
    {"name": "OmniRoute", "cat": "routing_gateways", "desc": "Roteamento inteligente de LLMs com custo zero", "terms": ["roteamento", "llm gratis", "balanceamento", "fallback llm"]},
    {"name": "graphify", "cat": "memory_rag_graphs", "desc": "Transforma código e banco de dados em grafos de conhecimento", "terms": ["grafo", "knowledge graph", "relacionamento", "grafo codigo"]},
    {"name": "security-audit-skill", "cat": "cloud_security_b2b", "desc": "Varredura estática de vulnerabilidades OWASP", "terms": ["seguranca", "owasp", "vulnerabilidade", "brecha", "segredo"]},
    {"name": "rpa", "cat": "projects", "desc": "Suíte de automação e faturamento de guias médicas UNIQ RPA", "terms": ["rpa", "faturamento", "guia", "operadora", "sadt", "fattiss"]}
]

def identificar_skills_e_ferramentas(msg: str) -> tuple[list[dict], list[dict]]:
    """Identifica skills e repositórios relevantes com base no texto do usuário."""
    txt = msg.lower()
    skills_found = []
    for s in SKILLS_TRIGGERS:
        if any(term in txt for term in s["terms"]):
            skill_clean = s["name"].lstrip("@")
            skills_found.append({
                "name": s["name"],
                "skill": skill_clean,
                "desc": s["desc"],
                "motivo": s["desc"]
            })

    repos_found = []
    for r in REPOS_TRIGGERS:
        if any(term in txt for term in r["terms"]):
            repos_found.append({
                "name": r["name"],
                "repo": r["name"],
                "category": r["cat"],
                "desc": r["desc"],
                "motivo": r["desc"]
            })

    return skills_found[:3], repos_found[:3]

class SecondBrainHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Mapeia rota raiz para frontend/
        clean_path = path.split('?')[0].split('#')[0]
        if clean_path in ('/', '/index.html'):
            return str(SB_ROOT / "frontend" / "index.html")
        if clean_path.startswith('/frontend/'):
            return str(SB_ROOT / clean_path.lstrip('/'))
        if (SB_ROOT / "frontend" / clean_path.lstrip('/')).exists():
            return str(SB_ROOT / "frontend" / clean_path.lstrip('/'))
        return super().translate_path(path)

    def do_OPTIONS(self):
        self.send_response(200, 'ok')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-type')
        self.end_headers()

    def do_GET(self):
        parsed = self.path.split('?')[0]

        if parsed == '/api/aurelio/status':
            # Checa Ollama local
            ollama_url = "http://localhost:11434/api/tags"
            ollama_online = False
            installed_models = []
            try:
                req = urllib.request.Request(ollama_url, headers={"User-Agent": "SecondBrain/2.0"})
                with urllib.request.urlopen(req, timeout=3) as resp:
                    if resp.status == 200:
                        ollama_online = True
                        data = json.loads(resp.read().decode('utf-8'))
                        installed_models = [m.get("name", "") for m in data.get("models", [])]
            except Exception:
                ollama_online = False

            active_model = getattr(model_manager, "MODEL_ATUAL", "qwen2.5-coder:7b")

            recommended = [
                {"name": "qwen2.5-coder:7b", "ram": "4.7 GB", "recommended": True, "desc": "Melhor raciocínio, arquitetura e código (PT-BR fluente)"},
                {"name": "qwen2.5:3b", "ram": "2.2 GB", "recommended": False, "desc": "Ultra-leve e veloz para máquinas com memória restrita"},
                {"name": "hermes3:8b", "ram": "5.0 GB", "recommended": False, "desc": "Especialista em comportamento agêntico e instruções"},
                {"name": "mistral", "ram": "4.5 GB", "recommended": False, "desc": "Modelo equilibrado padrão para texto geral"}
            ]

            payload = {
                "online": ollama_online,
                "ollama_online": ollama_online,
                "modelo_atual": active_model,
                "active_model": active_model,
                "installed_models": installed_models,
                "recommended_models": recommended
            }
            self._send_json(payload)
            return

        elif parsed == '/api/telemetry':
            metrics_file = SB_ROOT / "scripts" / "metrics_export.json"
            if metrics_file.exists():
                data = json.loads(metrics_file.read_text(encoding='utf-8'))
                self._send_json(data)
            else:
                self._send_json({"error": "Telemetria não encontrada"})
            return

        elif parsed == '/api/projects_graph':
            proj_graph_file = SB_ROOT / "frontend" / "projects_graph_data.json"
            if proj_graph_file.exists():
                data = json.loads(proj_graph_file.read_text(encoding='utf-8'))
                self._send_json(data)
            else:
                self._send_json({"error": "Grafo de projetos não encontrado"})
            return

        super().do_GET()

    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
            except Exception:
                data = {}

            mensagem = data.get('mensagem', '').strip()
            modo = data.get('modo', 'restrito')

            if not mensagem:
                self._send_json({"resposta": "Nenhuma mensagem fornecida."})
                return

            # Identifica proativamente skills e ferramentas que podem ajudar o usuário
            skills_sug, repos_sug = identificar_skills_e_ferramentas(mensagem)

            try:
                resultado = orchestrator.pipeline_principal(mensagem, GLOBAL_SESSION)
            except Exception as e:
                # Fallback inteligente com as skills sugeridas se o Ollama não estiver rodando
                resultado = {
                    "resposta": f"**[AÇÃO/RESPOSTA DIRETA]**\nO daemon do Ollama não está ativo no momento, mas o Second Brain analisou sua solicitação.\n\n"
                                f"**[CONTEXTO]**\nPara executar consultas com inteligência generativa local, inicie o Ollama com o modelo `qwen2.5-coder:7b`.\n\n"
                                f"**[SUGESTÃO]**\nVocê pode utilizar as skills mapeadas no catálogo para resolver essa demanda de imediato."
                }

            resultado["skills_sugeridas"] = skills_sug
            resultado["repos_sugeridos"] = repos_sug
            resultado["modo"] = modo
            self._send_json(resultado)

        elif self.path == '/api/aurelio/model':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                model = data.get('modelo') or data.get('model') or 'qwen2.5-coder:7b'
                model_manager.definir_modelo_atual(model)
                self._send_json({"ok": True, "status": "ok", "active_model": model, "modelo_atual": model})
            except Exception as e:
                self._send_json({"ok": False, "status": "error", "error": str(e)}, status=400)

        else:
            self.send_response(404)
            self.end_headers()

    def _send_json(self, payload: dict, status: int = 200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(payload, ensure_ascii=False).encode('utf-8'))

def run(port=8765):
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, SecondBrainHandler)
    print(f'Starting Second Brain API + Static Server on port {port} (http://localhost:{port}/)...')
    httpd.serve_forever()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    run(port)
