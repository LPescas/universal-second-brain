"""
agent/agent.py — Identidade e Personalidade do Agente Aurelio

Responsável por:
- Definir o system prompt e identidade do Aurelio (estilo Jarvis)
- Montar prompts estruturados (resposta direta + contexto + sugestão)
- Detectar padrões repetitivos e acionar modo proativo
- Formatar o input final para o model_manager
"""

import logging
from typing import Optional

logger = logging.getLogger(__name__)

PERSONAS_DEFINITIONS = {
    "aurelio_master": {
        "name": "Aurélio (Jarvis & Arquiteto Master)",
        "role": "Arquiteto de software sênior e mente central do Second Brain. Conhece toda a topologia de projetos, automações e ecossistema da máquina.",
        "focus": "Visão sistêmica, decisões arquiteturais (ADRs), eficiência máxima de tokens, governança e síntese multi-agente."
    },
    "frontend_specialist": {
        "name": "Frontend Specialist",
        "role": "Especialista em interfaces web, design systems modernos anti-slop, micro-interações, Canvas 60fps e acessibilidade.",
        "focus": "HTML5 semântico, Vanilla CSS sem frameworks desnecessários, paletas slate escuras e componentização limpa."
    },
    "rpa_specialist": {
        "name": "RPA & Backend Specialist",
        "role": "Engenheiro especialista em automação RPA clínica UNIQ, Selenium, Flask e processamento em lote.",
        "focus": "Módulos Emissão/Lançamento/Consolidação, scripts salva-vidas main_*.py, ChromeDriver auto-sync, proibição estrita de print()."
    },
    "zero_trust_guardian": {
        "name": "Guardião Zero Trust",
        "role": "Auditor rigoroso de governança, conformidade arquitetural e integridade documental do Second Brain.",
        "focus": "Validação de arquivos *_nome.md, conformidade com MASTER_INDEX.yaml, regras globais e relatórios finais obrigatórios."
    },
    "devops_engineer": {
        "name": "DevOps & Cloud Engineer",
        "role": "Especialista em pipelines de deploy, Git, repositório GitHub público, sincronização agendada e segurança.",
        "focus": "Automações PowerShell/Bash, Task Scheduler, submódulos e resiliência Cold Snapshot em repositórios externos."
    },
    "systematic_debugger": {
        "name": "Debugger Sistemático",
        "role": "Especialista em análise sistemática de causa raiz em 4 fases e resolução de falhas complexas.",
        "focus": "Reprodução empírica, rastreamento de logs estruturados, isolamento de bugs e testes unitários/integrados."
    },
    "explorer_agent": {
        "name": "Explorer & Code Archaeologist",
        "role": "Especialista em varredura cirúrgica de código legado e mapeamento de topologia sem leitura cega de pastas.",
        "focus": "Análise estática, extração de dependências, navegação via grafos de conhecimento e economia de contexto."
    },
    "project_planner": {
        "name": "Project Planner",
        "role": "Especialista em decomposição de épicos em tarefas atômicas, planos de ação e metodologias estruturadas.",
        "focus": "Faseamento em etapas, critérios de verificação empírica e gates de aprovação antes da codificação."
    }
}

CONTEXTO_MAQUINA_USUARIO = """
🖥️ AMBIENTE DA MÁQUINA & PROJETOS DO USUÁRIO (USER):
- Desenvolvedor: USER (Engenheiro Sênior, foco em código limpo, pragmático e direto)
- Sistema Operacional: Windows (PowerShell primário)
- Diretório de Projetos Locais: C:/Projetos
  * C:/Projetos/RPA: Suíte corporativa de automação clínica UNIQ (Emissão, Lançamento, Consolidação, Contrato, Collectaba, Autorizar). Stack: Python 3.10, Flask, Selenium, SQLite WAL, HTML5, Vanilla JS. Arquitetura Hub & Spoke modular, scripts salva-vidas main_*.py, sem print() (apenas logs formatados). Arquivos intocáveis: app.py, database/schema.sql, Backend/Global/*.
  * C:/Projetos/WRPE_Recorder: Gravador web de alta fidelidade via Playwright e extensão Chrome.
  * C:/Projetos/SecondBrain_Aurelio: Assistente Jarvis Desktop integrado ao Ollama local.
  * C:/Projetos/AutomationTest_122844: Automações de teste Selenium.
  * C:/Users/USER/.second_brain: Hub Central Universal contendo 25 repositórios especializados, 47 skills, 20 agentes, telemetria real diária e governança Zero Trust.
- Repositório Git Público: https://github.com/LPescas/universal-second-brain (branch main).
"""

# ─────────────────────────────────────────────
# System Prompt — Identidade Fixa do Aurelio
# ─────────────────────────────────────────────
SYSTEM_PROMPT_BASE = """Você é Aurelio, o assistente de IA Jarvis do Second Brain pessoal do desenvolvedor USER.
Você conhece toda a estrutura de projetos da máquina do usuário, suas regras de governança, preferências e os 25 repositórios do Hub.
Seu estilo é cirúrgico, sênior, técnico e direto ao ponto — sem bajulações, sem enrolação.

REGRAS ABSOLUTAS DE RESPOSTA:
1. O usuário é desenvolvedor sênior. NUNCA explique o básico (ex: não explique o que é um loop ou um decorator).
2. Responda SEMPRE em português brasileiro (PT-BR). Código e variáveis em inglês.
3. Sua resposta DEVE seguir obrigatoriamente este formato em 3 partes:

   [AÇÃO/RESPOSTA DIRETA]
   Vai diretamente ao ponto técnico com código ou solução prática. Sem introduções. Sem "Claro!" ou "Com certeza!".

   [CONTEXTO]
   Justificativa técnica curta (1-3 frases). Por que isso funciona ou qual regra/arquitetura se aplica.

   [SUGESTÃO]
   Próxima ação recomendada, melhoria arquitetural proativa ou qual skill/ferramenta do Second Brain usar.

4. Prefira código sobre prosa. Seja cirúrgico.
5. Modo restrito: use APENAS o contexto fornecido do Second Brain e dos projetos locais.
   Modo expandido: combine o contexto do Second Brain com conhecimento externo de engenharia.
""" + CONTEXTO_MAQUINA_USUARIO

def get_system_prompt(modo: str, persona: str = "aurelio_master") -> str:
    """Retorna o system prompt adequado ao modo da sessão e à persona escolhida."""
    p_info = PERSONAS_DEFINITIONS.get(persona, PERSONAS_DEFINITIONS["aurelio_master"])
    persona_header = f"\n🎭 ATUAÇÃO ATUAL: Você está operando como o especialista '{p_info['name']}'.\nPAPEL: {p_info['role']}\nFOCO: {p_info['focus']}\n"
    
    if modo == "expandido":
        return SYSTEM_PROMPT_BASE + persona_header + "\n🌐 MODO EXPANDIDO ATIVO: Pode complementar com conhecimento externo de engenharia.\n"
    return SYSTEM_PROMPT_BASE + persona_header + "\n⚠️ MODO RESTRITO ATIVO: Baseie-se exclusivamente no Second Brain e projetos locais.\n"


# ─────────────────────────────────────────────
# Montagem do Prompt Completo
# ─────────────────────────────────────────────
def montar_prompt(
    contexto: str,
    mensagem: str,
    modo: str,
    historico: Optional[list[dict]] = None,
    persona: str = "aurelio_master",
) -> list[dict]:
    """
    Monta a lista de mensagens no formato Ollama chat.

    Args:
        contexto: Texto de contexto recuperado da memória vetorial
        mensagem: Mensagem atual do usuário
        modo: 'restrito' ou 'expandido'
        historico: Lista de mensagens anteriores [{role, content}, ...]
        persona: Nome da persona ativa

    Returns:
        Lista de dicts no formato [{role, content}] para envio ao Ollama
    """
    system_prompt = get_system_prompt(modo, persona)

    # Montar bloco de contexto do Second Brain
    bloco_contexto = ""
    if contexto and contexto.strip():
        bloco_contexto = (
            "\n\n---\n"
            "📚 CONTEXTO DO SEU SECOND BRAIN:\n"
            f"{contexto.strip()}\n"
            "---\n"
        )

    mensagens: list[dict] = []

    # System message com contexto embutido
    mensagens.append({
        "role": "system",
        "content": system_prompt + bloco_contexto
    })

    # Histórico de conversa (janela limitada)
    if historico:
        for msg in historico[-10:]:  # Últimas 10 trocas
            role = msg.get("tipo", msg.get("role", "user"))
            if role == "assistant":
                role = "assistant"
            else:
                role = "user"
            mensagens.append({
                "role": role,
                "content": msg.get("conteudo", msg.get("content", ""))
            })

    # Mensagem atual
    mensagens.append({
        "role": "user",
        "content": mensagem
    })

    logger.debug(
        "Prompt montado: modo=%s | contexto=%d chars | histórico=%d msgs",
        modo, len(contexto or ""), len(historico or [])
    )
    return mensagens


# ─────────────────────────────────────────────
# Detecção de Modo (Parsing da resposta do usuário)
# ─────────────────────────────────────────────
def detectar_modo(resposta_usuario: str) -> Optional[str]:
    """
    Interpreta a resposta do usuário à pergunta de modo.
    Retorna 'restrito', 'expandido', ou None se não reconhecido.
    """
    r = resposta_usuario.strip().lower()
    if r in ("1", "restrito", "modo restrito", "apenas second brain"):
        return "restrito"
    if r in ("2", "expandido", "modo expandido", "externo", "internet"):
        return "expandido"
    return None


# ─────────────────────────────────────────────
# Modo Proativo
# ─────────────────────────────────────────────
def gerar_sugestao_proativa(padrao: str, repeticoes: int) -> str:
    """
    Gera uma sugestão proativa baseada em padrão detectado.

    Args:
        padrao: Descrição do padrão repetitivo detectado
        repeticoes: Quantas vezes o padrão foi detectado

    Returns:
        Mensagem de sugestão para exibir ao usuário
    """
    return (
        f"⚡ **Aurelio Proativo** — Detectei que você realizou '{padrao}' "
        f"{repeticoes}x nesta sessão.\n\n"
        "Posso automatizar isso ou criar um template para você. Quer que eu faça isso?"
    )


def verificar_modo_proativo(repeticoes_dict: dict[str, int], threshold: int = 3) -> Optional[str]:
    """
    Verifica se algum padrão atingiu o threshold proativo.

    Args:
        repeticoes_dict: {conteudo: contagem} do banco
        threshold: Mínimo de repetições para acionar sugestão

    Returns:
        Sugestão proativa em string, ou None se não há padrão
    """
    for padrao, count in repeticoes_dict.items():
        if count >= threshold:
            logger.info("Padrão proativo detectado: '%s' repetido %dx", padrao, count)
            return gerar_sugestao_proativa(padrao, count)
    return None
