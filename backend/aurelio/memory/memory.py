"""
memory/memory.py — Gestão de Memória e Contexto do Aurelio

Responsável por:
- Busca Híbrida (semântica 0.7 + recência 0.3) com top-5 resultados
- Montagem de contexto com limite MAX_CONTEXT = 12000 chars
- Salvar interações no banco relacional
- Atualizar e gerar embeddings vetoriais via Ollama local
- Reprocessamento em batch de embeddings pendentes
"""

import logging
import math
import struct
from datetime import datetime
from typing import Optional

from database import db
from models import model_manager

logger = logging.getLogger(__name__)

MAX_CONTEXT = 12000  # Limite de contexto em caracteres
TOP_K = 5            # Top resultados da busca híbrida


# ─────────────────────────────────────────────
# Serialização de Vetores
# ─────────────────────────────────────────────
def _vetor_para_bytes(vetor: list[float]) -> bytes:
    return struct.pack(f"{len(vetor)}f", *vetor)


def _bytes_para_vetor(raw: bytes) -> list[float]:
    n = len(raw) // 4
    return list(struct.unpack(f"{n}f", raw))


# ─────────────────────────────────────────────
# Similaridade Cosseno
# ─────────────────────────────────────────────
def _similaridade_cosseno(v1: list[float], v2: list[float]) -> float:
    """Calcula similaridade cosseno entre dois vetores."""
    if not v1 or not v2 or len(v1) != len(v2):
        return 0.0
    dot = sum(a * b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a * a for a in v1))
    mag2 = math.sqrt(sum(b * b for b in v2))
    if mag1 == 0 or mag2 == 0:
        return 0.0
    return dot / (mag1 * mag2)


# ─────────────────────────────────────────────
# Score de Recência
# ─────────────────────────────────────────────
def _score_recencia(timestamp_str: str) -> float:
    """
    Retorna score de recência normalizado [0, 1].
    Registros de hoje = 1.0; decay de 30 dias até ~0.0.
    """
    try:
        ts = datetime.fromisoformat(timestamp_str)
        agora = datetime.now()
        delta_dias = (agora - ts).total_seconds() / 86400
        # Decay exponencial com meia-vida de 7 dias
        return math.exp(-0.1 * delta_dias)
    except Exception:
        return 0.0


# ─────────────────────────────────────────────
# Busca Semântica
# ─────────────────────────────────────────────
def _buscar_semanticamente(query_vec: list[float], memorias: list[dict]) -> list[tuple[dict, float]]:
    """
    Calcula similaridade cosseno da query contra todos os registros de memória.
    Retorna lista de (memoria_dict, score_semantico).
    """
    resultados = []
    for mem in memorias:
        if not mem.get("embedding"):
            continue
        try:
            mem_vec = _bytes_para_vetor(mem["embedding"])
            score = _similaridade_cosseno(query_vec, mem_vec)
            resultados.append((mem, score))
        except Exception as e:
            logger.warning("Erro ao calcular similaridade para mem_id=%s: %s", mem.get("id"), e)

    return sorted(resultados, key=lambda x: x[1], reverse=True)


# ─────────────────────────────────────────────
# Busca Híbrida Principal (0.7 * sem + 0.3 * rec)
# ─────────────────────────────────────────────
def buscar_contexto(session_id: str, mensagem: str) -> str:
    """
    Busca híbrida: semantica (0.7) + recência (0.3).
    Retorna string de contexto pronta para o prompt, limitada a MAX_CONTEXT.

    Args:
        session_id: ID da sessão atual
        mensagem: Mensagem do usuário para usar como query de busca

    Returns:
        String formatada com contexto relevante + histórico recente
    """
    partes: list[str] = []

    # 1. Histórico recente da sessão
    historico = db.buscar_historico(session_id, limite=10)
    if historico:
        partes_hist = []
        for msg in historico[-6:]:  # Últimas 6 mensagens
            role = "Você" if msg["tipo"] == "user" else "Aurelio"
            partes_hist.append(f"{role}: {msg['conteudo']}")
        partes.append("### Histórico Recente\n" + "\n".join(partes_hist))

    # 2. Busca vetorial na memória
    query_vec = model_manager.gerar_embedding(mensagem)
    memorias = db.buscar_memorias_recentes(limite=200)

    if query_vec and memorias:
        ranked = _buscar_semanticamente(query_vec, memorias)

        resultados_hibridos = []
        for mem, sem_score in ranked[:20]:  # Candidatos para re-ranking
            rec_score = _score_recencia(mem.get("timestamp", ""))
            score_final = (0.7 * sem_score) + (0.3 * rec_score)
            resultados_hibridos.append((mem, score_final))

        # Ordenar e pegar top-5
        top_5 = sorted(resultados_hibridos, key=lambda x: x[1], reverse=True)[:TOP_K]

        if top_5:
            partes_mem = []
            for mem, score in top_5:
                partes_mem.append(f"[Score: {score:.2f}] {mem['texto']}")
            partes.append("### Memória Relevante\n" + "\n".join(partes_mem))

            logger.debug("Busca híbrida: %d resultados, top score=%.3f", len(top_5), top_5[0][1])

    # 3. Montar contexto e limitar a MAX_CONTEXT
    contexto_completo = "\n\n".join(partes)
    if len(contexto_completo) > MAX_CONTEXT:
        contexto_completo = contexto_completo[:MAX_CONTEXT]
        logger.debug("Contexto truncado para %d chars.", MAX_CONTEXT)

    return contexto_completo


# ─────────────────────────────────────────────
# Salvar Interação Relacional
# ─────────────────────────────────────────────
def salvar_interacao(session_id: str, mensagem_user: str, resposta_assistant: str) -> None:
    """
    Persiste a troca de mensagens (user + assistant) no banco relacional.

    Args:
        session_id: ID da sessão
        mensagem_user: Mensagem enviada pelo usuário
        resposta_assistant: Resposta gerada pelo Aurelio
    """
    db.salvar_mensagem(session_id, "user", mensagem_user)
    db.salvar_mensagem(session_id, "assistant", resposta_assistant)
    logger.debug("Interação salva para sessão %s", session_id)


# ─────────────────────────────────────────────
# Atualizar Embeddings (Novo Registro)
# ─────────────────────────────────────────────
def atualizar_embeddings(mensagem_user: str, resposta_assistant: str) -> None:
    """
    Gera e salva embeddings para a interação atual na memória vetorial.
    Combina user + assistant num único registro de contexto.

    Args:
        mensagem_user: Mensagem do usuário
        resposta_assistant: Resposta do Aurelio
    """
    texto_combinado = f"Usuário: {mensagem_user}\nAurelio: {resposta_assistant}"

    try:
        vetor = model_manager.gerar_embedding(texto_combinado)
        if vetor:
            blob = _vetor_para_bytes(vetor)
            db.salvar_memoria(
                texto=texto_combinado,
                embedding=blob,
                source="interacao_live"
            )
            logger.debug("Embedding atualizado para nova interação (%d chars).", len(texto_combinado))
        else:
            # Salva sem embedding (será reprocessado em batch)
            db.salvar_memoria(
                texto=texto_combinado,
                embedding=None,
                source="interacao_sem_embedding"
            )
            logger.warning("Embedding não gerado — registrado para reprocessamento.")
    except Exception as e:
        logger.error("Erro ao salvar embedding: %s", e)


# ─────────────────────────────────────────────
# Reprocessamento em Batch (registros sem embedding)
# ─────────────────────────────────────────────
def reprocessar_embeddings_batch(limite: int = 50) -> int:
    """
    Reprocessa registros de memória que não possuem embedding.
    Útil para rodar como job periódico.

    Args:
        limite: Máximo de registros a processar por chamada

    Returns:
        Número de embeddings gerados com sucesso
    """
    memorias = db.buscar_memorias_recentes(limite=200)
    sem_embedding = [m for m in memorias if not m.get("embedding")][:limite]

    if not sem_embedding:
        logger.info("Nenhum registro sem embedding encontrado.")
        return 0

    sucessos = 0
    for mem in sem_embedding:
        try:
            vetor = model_manager.gerar_embedding(mem["texto"])
            if vetor:
                blob = _vetor_para_bytes(vetor)
                db.atualizar_embedding(mem["id"], blob)
                sucessos += 1
        except Exception as e:
            logger.error("Falha ao reprocessar embedding id=%s: %s", mem["id"], e)

    logger.info("Batch de embeddings concluído: %d/%d processados.", sucessos, len(sem_embedding))
    return sucessos


# ─────────────────────────────────────────────
# Ingestão Manual de Documentos
# ─────────────────────────────────────────────
def ingerir_documento(texto: str, source: str = "manual") -> Optional[int]:
    """
    Ingere um documento externo (nota, arquivo, artigo) na memória vetorial.
    Chunks de até 1000 chars são gerados automaticamente.

    Args:
        texto: Conteúdo do documento
        source: Identificador de origem (ex: 'notion', 'arquivo_local', 'manual')

    Returns:
        ID do primeiro chunk salvo, ou None em caso de erro
    """
    CHUNK_SIZE = 1000
    OVERLAP = 100

    chunks = []
    for i in range(0, len(texto), CHUNK_SIZE - OVERLAP):
        chunk = texto[i:i + CHUNK_SIZE].strip()
        if chunk:
            chunks.append(chunk)

    primeiro_id = None
    for chunk in chunks:
        try:
            vetor = model_manager.gerar_embedding(chunk)
            blob = _vetor_para_bytes(vetor) if vetor else None
            mem_id = db.salvar_memoria(chunk, blob, source=source)
            if primeiro_id is None:
                primeiro_id = mem_id
        except Exception as e:
            logger.error("Erro ao ingerir chunk: %s", e)

    logger.info("Documento ingerido: %d chunks de '%s'", len(chunks), source)
    return primeiro_id
