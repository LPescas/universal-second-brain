"""
core/orchestrator.py — Orquestrador Central do Sistema Aurelio

O CORAÇÃO DO SISTEMA. Todo input passa obrigatoriamente por aqui.
Nada deve bypassar este pipeline.

Fluxo Imutável:
1. Receber input
2. Definir/verificar modo da sessão
3. Buscar contexto (memória híbrida)
4. Montar prompt (identidade Aurelio)
5. Gerar resposta (Ollama + fallback)
6. Salvar no banco relacional
7. Atualizar embeddings vetoriais
8. Verificar gatilhos proativos
9. Retornar resposta
"""

import logging
import sys
import os
from uuid import uuid4
from typing import Optional

# Garantir que o root do projeto esteja no path
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from database import db
from memory import memory
from agent import agent
from models import model_manager

# ─────────────────────────────────────────────
# Configuração de Logging
# ─────────────────────────────────────────────
LOG_PATH = os.path.join(ROOT, "logs", "app.log")
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────
# Inicialização do Sistema
# ─────────────────────────────────────────────
def inicializar_sistema() -> None:
    """
    Inicializa o banco de dados e valida que o Ollama está acessível.
    Deve ser chamado uma vez na inicialização da aplicação.
    """
    logger.info("=== Iniciando Sistema Aurelio ===")
    db.inicializar_banco()

    status = model_manager.status_sistema()
    if status["ollama_online"]:
        logger.info(
            "Ollama online. Modelos disponíveis: %s",
            status["modelos_locais"]
        )
    else:
        logger.warning("Ollama offline ou inacessível. Verificar se está rodando.")

    logger.info("Sistema inicializado com sucesso.")


# ─────────────────────────────────────────────
# Gestão de Sessão
# ─────────────────────────────────────────────
def nova_sessao() -> str:
    """
    Cria uma nova sessão com ID único.
    O modo ainda não está definido — será perguntado na primeira interação.

    Returns:
        session_id: UUID da sessão criada
    """
    session_id = str(uuid4())
    # Cria no banco com modo 'pendente' — será definido na primeira resposta do usuário
    db.criar_sessao(session_id, modo="pendente")
    logger.info("Nova sessão criada: %s", session_id)
    return session_id


def obter_ou_criar_sessao(session_id: Optional[str] = None) -> str:
    """
    Retorna um session_id existente ou cria um novo.
    """
    if session_id:
        modo = db.obter_modo_sessao(session_id)
        if modo:
            return session_id
    return nova_sessao()


# ─────────────────────────────────────────────
# Pipeline Principal (IMUTÁVEL)
# ─────────────────────────────────────────────
def pipeline_principal(
    mensagem: str,
    session_id: str,
    modelo: str = model_manager.MODEL_ATUAL,
) -> dict:
    """
    O pipeline único e imutável do Aurelio. Todo input passa aqui.

    Args:
        mensagem: Texto enviado pelo usuário
        session_id: ID da sessão atual
        modelo: Modelo Ollama a usar (com fallback automático)

    Returns:
        dict com chaves:
            - resposta (str): Texto gerado pelo Aurelio
            - modo (str): Modo utilizado na sessão
            - modelo_usado (str): Modelo que gerou a resposta
            - sugestao_proativa (str|None): Sugestão proativa se detectada
    """
    logger.info("Pipeline iniciado | sessão=%s | modelo=%s | msg_len=%d",
                session_id, modelo, len(mensagem))

    # ── STEP 1: Verificar modo da sessão ──────────────────────
    modo = db.obter_modo_sessao(session_id)

    # Se modo ainda pendente, verificar se o usuário está respondendo à pergunta de modo
    if modo == "pendente":
        modo_detectado = agent.detectar_modo(mensagem)
        if modo_detectado:
            db.definir_modo_sessao(session_id, modo_detectado)
            modo = modo_detectado
            logger.info("Modo definido como '%s' para sessão %s", modo, session_id)
            resposta_confirmacao = (
                f"✅ Modo **{modo.capitalize()}** ativado.\n\n"
                f"{'Usarei apenas seu Second Brain.' if modo == 'restrito' else 'Combinarei seu Second Brain com conhecimento externo.'}\n\n"
                "Pode perguntar."
            )
            db.salvar_mensagem(session_id, "user", mensagem)
            db.salvar_mensagem(session_id, "assistant", resposta_confirmacao)
            return {
                "resposta": resposta_confirmacao,
                "modo": modo,
                "modelo_usado": "sistema",
                "sugestao_proativa": None,
            }
        else:
            # Usuário não respondeu ao modo — retornar a pergunta novamente
            return {
                "resposta": agent.PERGUNTA_MODO,
                "modo": "pendente",
                "modelo_usado": "sistema",
                "sugestao_proativa": None,
            }

    # ── STEP 2: Buscar contexto (busca híbrida vetorial + recência) ──
    logger.info("Buscando contexto para sessão %s...", session_id)
    contexto = memory.buscar_contexto(session_id, mensagem)
    logger.debug("Contexto recuperado: %d chars", len(contexto))

    # ── STEP 3: Montar historico e prompt ─────────────────────
    historico = db.buscar_historico(session_id, limite=20)
    prompt_msgs = agent.montar_prompt(
        contexto=contexto,
        mensagem=mensagem,
        modo=modo,
        historico=historico,
    )

    # ── STEP 4: Gerar resposta via Ollama (com fallback) ──────
    logger.info("Gerando resposta | modelo=%s | modo=%s", modelo, modo)
    try:
        resposta = model_manager.gerar_resposta(
            mensagens=prompt_msgs,
            modelo=modelo,
            temperatura=0.7,
        )
        modelo_usado = modelo
    except RuntimeError as e:
        logger.error("Falha crítica na geração: %s", e)
        resposta = (
            "⚠️ Não consegui gerar resposta no momento. "
            "Verifique se o Ollama está rodando e tente novamente."
        )
        modelo_usado = "nenhum"

    # ── STEP 5: Salvar interação no banco relacional ──────────
    memory.salvar_interacao(session_id, mensagem, resposta)

    # ── STEP 6: Atualizar embeddings vetoriais ────────────────
    memory.atualizar_embeddings(mensagem, resposta)

    # ── STEP 7: Verificar gatilhos proativos ─────────────────
    repeticoes = db.contar_repeticoes(session_id, tipo="user")
    sugestao_proativa = agent.verificar_modo_proativo(repeticoes, threshold=3)
    if sugestao_proativa:
        logger.info("Sugestão proativa ativada para sessão %s", session_id)

    logger.info("Pipeline concluído | modelo=%s | resposta=%d chars",
                modelo_usado, len(resposta))

    return {
        "resposta": resposta,
        "modo": modo,
        "modelo_usado": modelo_usado,
        "sugestao_proativa": sugestao_proativa,
    }


# ─────────────────────────────────────────────
# Primeira Interação (Flow de Boas-vindas)
# ─────────────────────────────────────────────
def primeira_interacao(session_id: str) -> str:
    """
    Retorna a mensagem de boas-vindas e a pergunta de modo.
    Deve ser chamado ao iniciar uma nova sessão na interface.

    Returns:
        String com a pergunta de modo para o usuário
    """
    logger.info("Primeira interação na sessão %s", session_id)
    return agent.PERGUNTA_MODO


# ─────────────────────────────────────────────
# Ingestão de Documentos Externos
# ─────────────────────────────────────────────
def ingerir_documento_no_brain(texto: str, source: str = "manual") -> Optional[int]:
    """
    Ingere um documento externo na memória vetorial do Aurelio.
    Útil para alimentar o Second Brain com notas, artigos, READMEs, etc.

    Args:
        texto: Conteúdo do documento
        source: Identificador de origem

    Returns:
        ID do primeiro chunk, ou None
    """
    logger.info("Ingerindo documento: %d chars | source='%s'", len(texto), source)
    return memory.ingerir_documento(texto, source=source)


# ─────────────────────────────────────────────
# Reprocessamento de Embeddings (Job)
# ─────────────────────────────────────────────
def job_reprocessar_embeddings(limite: int = 50) -> int:
    """
    Job de manutenção: reprocessa registros sem embedding.
    Pode ser chamado periodicamente.
    """
    logger.info("Job: Reprocessamento de embeddings (limite=%d)...", limite)
    return memory.reprocessar_embeddings_batch(limite=limite)


# ─────────────────────────────────────────────
# Status Completo do Sistema
# ─────────────────────────────────────────────
def status_completo() -> dict:
    """Retorna status agregado de todos os subsistemas."""
    modelo_status = model_manager.status_sistema()
    return {
        "ollama": modelo_status,
        "banco": str(db.DB_PATH),
        "banco_existe": db.DB_PATH.exists() if hasattr(db.DB_PATH, "exists") else False,
    }
