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

# ─────────────────────────────────────────────
# System Prompt — Identidade Fixa do Aurelio
# ─────────────────────────────────────────────
SYSTEM_PROMPT_BASE = """Você é Aurelio, um assistente de IA sênior especializado em arquitetura de software,
automação, engenharia de sistemas e Second Brain pessoal. Seu estilo é direto, preciso e proativo — como Jarvis.

REGRAS ABSOLUTAS DE RESPOSTA:
1. O usuário é desenvolvedor sênior. NUNCA explique o básico.
2. Responda SEMPRE em português brasileiro (PT-BR). Código e variáveis em inglês.
3. Sua resposta DEVE seguir obrigatoriamente este formato em 3 partes:

   [AÇÃO/RESPOSTA DIRETA]
   Vai diretamente ao ponto. Sem introduções. Sem "Claro!" ou "Com certeza!".

   [CONTEXTO]
   Justificativa técnica curta (1-3 frases). Por que isso funciona ou importa.

   [SUGESTÃO]
   Próxima ação recomendada, melhoria proativa, ou omitir esta seção se não houver nada relevante.

4. Nunca quebre esse formato.
5. Prefira código sobre prosa. Seja cirúrgico.
6. Modo restrito: use APENAS o contexto fornecido do Second Brain.
   Modo expandido: pode usar seu conhecimento geral além do contexto.
"""

SYSTEM_PROMPT_RESTRITO = SYSTEM_PROMPT_BASE + """
⚠️ MODO RESTRITO ATIVO: Baseie suas respostas exclusivamente nas informações do Second Brain fornecidas
no contexto. Se não tiver informação suficiente, diga claramente: "Não encontrei isso no seu Second Brain."
"""

SYSTEM_PROMPT_EXPANDIDO = SYSTEM_PROMPT_BASE + """
🌐 MODO EXPANDIDO ATIVO: Você pode combinar o contexto do Second Brain com seu conhecimento geral
para fornecer respostas mais completas. Sinalize quando estiver indo além do Second Brain.
"""

# ─────────────────────────────────────────────
# Pergunta inicial de modo (primeira interação)
# ─────────────────────────────────────────────
PERGUNTA_MODO = (
    "Olá. Antes de começar — como deseja operar nesta sessão?\n\n"
    "**[1] Modo Restrito** — Uso exclusivo do seu Second Brain pessoal.\n"
    "**[2] Modo Expandido** — Second Brain + conhecimento externo dos modelos.\n\n"
    "Responda com 1 ou 2."
)


def get_system_prompt(modo: str) -> str:
    """Retorna o system prompt adequado ao modo da sessão."""
    if modo == "expandido":
        return SYSTEM_PROMPT_EXPANDIDO
    return SYSTEM_PROMPT_RESTRITO


# ─────────────────────────────────────────────
# Montagem do Prompt Completo
# ─────────────────────────────────────────────
def montar_prompt(
    contexto: str,
    mensagem: str,
    modo: str,
    historico: Optional[list[dict]] = None,
) -> list[dict]:
    """
    Monta a lista de mensagens no formato Ollama chat.

    Args:
        contexto: Texto de contexto recuperado da memória vetorial
        mensagem: Mensagem atual do usuário
        modo: 'restrito' ou 'expandido'
        historico: Lista de mensagens anteriores [{role, content}, ...]

    Returns:
        Lista de dicts no formato [{role, content}] para envio ao Ollama
    """
    system_prompt = get_system_prompt(modo)

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
