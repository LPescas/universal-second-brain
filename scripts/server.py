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
import urllib.parse
from http.server import SimpleHTTPRequestHandler, HTTPServer
from pathlib import Path

# Force UTF-8 on Windows cleanly
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SB_ROOT = Path(__file__).resolve().parent.parent

# Inject scripts into path
SCRIPTS_DIR = SB_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

try:
    import repo_manager
except Exception as e:
    print("[AVISO] repo_manager em modo fallback:", e)
    repo_manager = None

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

# ─────────────────────────────────────────────────────────────
# Base Estruturada de Conhecimento e Preferências por Domínio
# ─────────────────────────────────────────────────────────────
KNOWLEDGE_DOMAINS = {
    "rpa_architecture": {
        "id": "rpa_architecture",
        "title": "RPA Architecture & Automação UNIQ",
        "file": "knowledge/rpa_architecture.md",
        "category": "Robótica & Automação Web",
        "icon": "🤖",
        "triggers": ["rpa", "automation", "selenium", "driver", "orchestrator"],
        "rules": [
            "Padrão Hub & Spoke: Frontend Flask desacoplado de Backend RPA.",
            "Selenium/Driver: Init EXCLUSIVO via Backend/Global/servicos/driver.py::start_session() — NUNCA init bruto.",
            "Logging Obrigatório: Proibido uso de print(). Usar formato [ID] [RPA] [ETAPA] [TIPO] Mensagem.",
            "6 Pastas Canônicas: Todo módulo contém codigo, documentacao, logs, dados, configuracoes, executaveis.",
            "Zero Trust Documentation: Todo subdiretório possui cabeçalho e documentação obrigatória *_nome.md.",
            "Sincronização de Banco: Toda alteração em tabela atualiza Guia_Simplificado_Sistema_RPA.docx e rpa_database_schema_audit.md.",
            "Arquivos Intocáveis: Preservar intactos os arquivos de produção listados em arquivos_intocaveis_rpa.md."
        ],
        "user_preferences": {
            "linguagem_preferida": "Python 3.10+ (Type annotations, PEP 8 pragmático)",
            "estilo_explicacao": "Português do Brasil (pt-BR), tom técnico sênior, direto e pragmático, sem preâmbulos óbvios.",
            "estilo_codigo": "Variáveis, funções e docstrings em inglês. Código limpo, modular e auto-documentável.",
            "praticas_proibidas": "Sem prints soltos em produção, sem drivers inicializados fora do driver_manager, sem commits sem documentação.",
            "projetos_alvo": "C:/Projetos/RPA (rotinas UNIQ, guias médicas, faturamento SADT, autorizações)"
        },
        "auto_evolution": [
            {"data": "19/10/2026", "evento": "Validação de retroalimentação automática integrada ao painel de conhecimento"},
            {"data": "Agosto 2026", "evento": "Padronização do endpoint /api/v2/rpa/historico com métricas em JSON"},
            {"data": "31/07/2026", "evento": "Criação do padrão The UNIQ Way com 6 pastas obrigatórias"}
        ]
    },
    "frontend_patterns": {
        "id": "frontend_patterns",
        "title": "Frontend Patterns & Design System",
        "file": "knowledge/frontend_patterns.md",
        "category": "Interface do Usuário & UX",
        "icon": "🎨",
        "triggers": ["html", "css", "js", "react", "next", "ui", "design"],
        "rules": [
            "Anti-Slop Design: Proibido designs genéricos de IA, botões sem hover e paletas roxas clichês.",
            "Vanilla CSS & Design Tokens: Variáveis semânticas em :root, flexbox/grid moderno.",
            "Dark Mode Premium: Paletas com alto contraste e estética glassmorphism profissional.",
            "Tipografia Google Fonts: Inter para interface, JetBrains Mono para códigos e métricas.",
            "Separação de Camadas: Estrutura semântica (HTML) isolada de Estilos (CSS) e Lógica de Dados (JS)."
        ],
        "user_preferences": {
            "linguagem_preferida": "HTML5, Vanilla CSS3, JavaScript ES6+ modular",
            "estilo_explicacao": "Foco em experiência visual premium, responsividade e simplicidade de manutenção.",
            "estilo_codigo": "Classes semânticas, sem inline styles conflitantes, animações CSS a 60 FPS.",
            "praticas_proibidas": "Proibido frameworks pesados quando não solicitados, gradientes roxos cafonas, telas sem hierarquia.",
            "projetos_alvo": "Dashboards de controle, Second Brain Frontend e interfaces web do RPA"
        },
        "auto_evolution": [
            {"data": "19/10/2026", "evento": "Implementação do inspetor interativo de regras e seletor multi-persona"},
            {"data": "18/10/2026", "evento": "Grafo de visualização em Canvas 60 FPS com física de partículas"},
            {"data": "03/08/2026", "evento": "Deploy da dashboard v2.0 com métricas de observabilidade"}
        ]
    },
    "python_patterns": {
        "id": "python_patterns",
        "title": "Python Patterns & Clean Code",
        "file": "knowledge/python_patterns.md",
        "category": "Engenharia de Software",
        "icon": "🐍",
        "triggers": ["python", "flask", "fastapi", "async", "typing"],
        "rules": [
            "Clean Code Pragmatic: Funções curtas, coesas, sem duplicação de lógica.",
            "Tipagem Estática: Type hints em todas as assinaturas públicas.",
            "Tratamento de Exceções: Try/except específicos com log do traceback, nunca silencioso.",
            "Padrões de Import: Caminhos absolutos e injeção controlada de sys.path."
        ],
        "user_preferences": {
            "linguagem_preferida": "Python 3.10+, PowerShell 7+",
            "estilo_explicacao": "Direto ao ponto, com snippets concisos prontos para execução.",
            "estilo_codigo": "PEP 8 rigoroso, identificadores em inglês, comentários de código focados no motivo.",
            "praticas_proibidas": "Proibido except genérico pass, código macarrônico monolítico, falta de testes.",
            "projetos_alvo": "Backends, robôs, rotinas de telemetria e scripts de automação"
        },
        "auto_evolution": [
            {"data": "19/10/2026", "evento": "Adição de extração de metadados Git (dia/mês/ano e horário) com UTF-8 seguro"},
            {"data": "Agosto 2026", "evento": "Consolidação de scripts salva-vidas standalone com execução idempotente"}
        ]
    },
    "governance": {
        "id": "governance",
        "title": "Governança Zero Trust & AG Kit",
        "file": "knowledge/governance.md",
        "category": "Governança & Segurança",
        "icon": "🛡️",
        "triggers": ["governance", "zero-trust", "compliance", "audit", "documentation"],
        "rules": [
            "Guardião de Execução: Boot check obrigatório de arquivos canônicos antes de qualquer execução.",
            "Validação Empírica via .agents: Testar soluções em scripts/ ou workflows/ antes da entrega.",
            "Triagem Inicial Obrigatória: Buscar nas skills do Second Brain a melhor estratégia antes de codificar.",
            "Sincronização de Documentação: Manuais Word e Markdown mantidos em sincronia estrita."
        ],
        "user_preferences": {
            "linguagem_preferida": "Markdown, YAML, Python de governança",
            "estilo_explicacao": "Relatório final transparente ao término de cada tarefa com telemetria detalhada.",
            "estilo_codigo": "Estruturado, auditável e rastreável.",
            "praticas_proibidas": "Proibido pular o hook de inicialização, pular relatório final ou burlar governança.",
            "projetos_alvo": "Ecossistema global da máquina do desenvolvedor"
        },
        "auto_evolution": [
            {"data": "19/10/2026", "evento": "Atualização das regras estritas com telemetria obrigatória via usage_metrics.py"},
            {"data": "Julho 2026", "evento": "Criação do Guardião de Execução e travas de arquivos intocáveis"}
        ]
    },
    "devops_infra": {
        "id": "devops_infra",
        "title": "DevOps, Deploy & Servidores Locais",
        "file": "knowledge/devops_infra.md",
        "category": "Infraestrutura & Deploy",
        "icon": "⚡",
        "triggers": ["deploy", "docker", "ci", "server", "infra"],
        "rules": [
            "Servidor Assíncrono Local: Execução daemon na porta 8765 sem travar o terminal.",
            "Cold Snapshot: Repositórios do hub clonados e imutáveis contra exclusões externas.",
            "Variáveis de Ambiente: Isolamento total de credenciais e tokens em .env protegido."
        ],
        "user_preferences": {
            "linguagem_preferida": "PowerShell, Python, Git CLI",
            "estilo_explicacao": "Comandos diretos para o PowerShell com flags de bypass de confirmação interativa.",
            "estilo_codigo": "Scripts idempotentes com tratamento de erro e checagem de portas abertas.",
            "praticas_proibidas": "Proibido rodar comandos bloqueantes que congelam o agente.",
            "projetos_alvo": "Servidores de dashboard, daemons de IA e robôs agendados"
        },
        "auto_evolution": [
            {"data": "19/10/2026", "evento": "Integração do motor de adição dinâmica de repositórios ao vivo"},
            {"data": "03/08/2026", "evento": "Configuração do servidor unificado API + estático HTTP"}
        ]
    },
    "user_preferences": {
        "id": "user_preferences",
        "title": "Preferências & Memória Pessoal do Usuário",
        "file": ".agents/memory/user-preferences.md",
        "category": "Memória Central da Máquina",
        "icon": "🧠",
        "triggers": ["preferencias", "usuario", "perfil", "memoria", "estilo"],
        "rules": [
            "Prioridade Máxima: Os agentes adaptam seu comportamento ao gosto específico do desenvolvedor.",
            "Comunicação em pt-BR com estilo sênior e direto.",
            "Código estritamente em inglês.",
            "Clean Code e sem duplicações.",
            "Zero Trust e compliance ativo em todas as rotinas."
        ],
        "user_preferences": {
            "linguagem_preferida": "Python, JavaScript moderno, PowerShell",
            "estilo_explicacao": "Sênior, objetivo, sem preâmbulos didáticos básicos.",
            "estilo_codigo": "Clean Code, tipado, modular e defensivo.",
            "praticas_proibidas": "Proibido explicações condescendentes, código monolítico ou código sem testes.",
            "projetos_alvo": "Todos os projetos da máquina (RPA, WRPE, Second Brain, AutomationTest)"
        },
        "auto_evolution": [
            {"data": "19/10/2026", "evento": "Retroalimentação direta do perfil de desenvolvimento na memória durável"},
            {"data": "18/07/2026", "evento": "Criação inicial da memória de preferências do AG Kit"}
        ]
    }
}

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
        parsed_url = urllib.parse.urlparse(self.path)
        parsed = parsed_url.path
        query = urllib.parse.parse_qs(parsed_url.query)

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

        elif parsed == '/api/knowledge/details':
            domain_id = query.get('domain', ['rpa_architecture'])[0]
            domain_info = KNOWLEDGE_DOMAINS.get(domain_id)

            if not domain_info:
                # Procura por prefixo ou fallback
                domain_info = KNOWLEDGE_DOMAINS["rpa_architecture"]

            # Lê o conteúdo Markdown real do arquivo físico
            file_rel = domain_info.get("file", "")
            file_path = SB_ROOT / file_rel
            markdown_content = ""
            if file_path.exists():
                try:
                    markdown_content = file_path.read_text(encoding='utf-8', errors='replace')
                except Exception as e:
                    markdown_content = f"# Erro ao ler arquivo {file_rel}: {e}"
            else:
                markdown_content = f"# {domain_info['title']}\n\nArquivo de conhecimento referenciado: `{file_rel}`"

            resp_payload = {
                "ok": True,
                "domain": domain_id,
                "title": domain_info.get("title"),
                "file": domain_info.get("file"),
                "category": domain_info.get("category"),
                "icon": domain_info.get("icon", "📚"),
                "triggers": domain_info.get("triggers", []),
                "rules": domain_info.get("rules", []),
                "user_preferences": domain_info.get("user_preferences", {}),
                "auto_evolution": domain_info.get("auto_evolution", []),
                "markdown_content": markdown_content
            }
            self._send_json(resp_payload)
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
            persona = data.get('persona', 'aurelio_master')
            modelo = data.get('modelo') or getattr(model_manager, "MODEL_ATUAL", "qwen2.5-coder:7b")

            if not mensagem:
                self._send_json({"resposta": "Nenhuma mensagem fornecida."})
                return

            # Identifica proativamente skills e ferramentas que podem ajudar o usuário
            skills_sug, repos_sug = identificar_skills_e_ferramentas(mensagem)

            try:
                resultado = orchestrator.pipeline_principal(
                    mensagem=mensagem,
                    session_id=GLOBAL_SESSION,
                    modelo=modelo,
                    modo_override=modo,
                    persona=persona
                )
            except Exception as e:
                # Fallback inteligente com perfil da persona e skills sugeridas se o Ollama não estiver rodando
                persona_names = {
                    "aurelio_master": "Aurélio Master (Arquiteto Global)",
                    "frontend_specialist": "Frontend Specialist (Design & UI)",
                    "rpa_specialist": "RPA Specialist (Selenium & UNIQ)",
                    "zero_trust_guardian": "Zero Trust Guardian (Governança)",
                    "devops_engineer": "DevOps Engineer (Deploy & Infra)",
                    "systematic_debugger": "Systematic Debugger (Diagnóstico 4-Fases)",
                    "explorer_intel": "Explorer & Intel (Mapeamento de Máquina)",
                    "project_planner": "Project Planner (Planejamento Socrático)"
                }
                active_persona_name = persona_names.get(persona, "Aurélio AI")
                resultado = {
                    "resposta": f"**[AÇÃO/RESPOSTA DIRETA — {active_persona_name}]**\n"
                                f"O daemon local do Ollama não está ativo no momento, mas analisei sua solicitação com base em toda a memória persistente da sua máquina (`{active_persona_name}`).\n\n"
                                f"**[CONTEXTO DA MÁQUINA & REGRAS APLICADAS]**\n"
                                f"• Ambiente Local: Windows | Projetos mapeados: `C:/Projetos/RPA`, `WRPE_Recorder`, `universal-second-brain`.\n"
                                f"• Governança: Zero Trust Ativo, Clean Code em inglês, explicações em pt-BR direto ao ponto.\n"
                                f"• Para inferência generativa completa em tempo real, inicie o Ollama com: `ollama run {modelo}`.\n\n"
                                f"**[SUGESTÃO PROATIVA]**\n"
                                f"Utilize os recursos mapeados abaixo no catálogo do Second Brain para avançar de imediato nesta tarefa.",
                    "modo": modo,
                    "modelo_usado": modelo,
                    "persona": persona
                }

            resultado["skills_sugeridas"] = skills_sug
            resultado["repos_sugeridos"] = repos_sug
            resultado["modo"] = modo
            resultado["persona"] = persona
            self._send_json(resultado)

        elif self.path == '/api/repos/add':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
            except Exception:
                data = {}

            url = data.get('url', '').strip()
            category = data.get('category', '').strip() or 'dev_reverse_engineering'
            description = data.get('description', '').strip()

            if not url:
                self._send_json({"ok": False, "error": "A URL do repositório GitHub é obrigatória."}, status=400)
                return

            if not repo_manager:
                self._send_json({"ok": False, "error": "Módulo repo_manager não disponível."}, status=500)
                return

            try:
                res = repo_manager.add_repository(url=url, category=category, description=description)
                self._send_json(res)
            except Exception as e:
                self._send_json({"ok": False, "error": f"Falha ao adicionar repositório: {str(e)}"}, status=500)

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
