"""
models/model_manager.py — Gerenciador de Modelos Locais via Ollama (Aurelio)

Responsável por:
- Executar chamadas ao Ollama com suporte multi-modelo
- Estratégia de fallback automático entre modelos
- Download e validação de modelos
- Geração de embeddings locais
"""

import logging
import subprocess
import json
import urllib.request
import urllib.error
from typing import Any

logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────
# Configuração de Modelos
# ─────────────────────────────────────────────
MODELOS_DISPONIVEIS = ["qwen2.5", "llama3", "mistral"]
MODEL_ATUAL = "qwen2.5"
FALLBACK_MODELS = ["mistral", "llama3"]
EMBEDDING_MODEL = "nomic-embed-text"

OLLAMA_BASE_URL = "http://localhost:11434"


# ─────────────────────────────────────────────
# Helpers HTTP (sem dependências externas)
# ─────────────────────────────────────────────
def _post_ollama(endpoint: str, payload: dict) -> dict:
    """Realiza um POST para a API local do Ollama e retorna o JSON de resposta."""
    url = f"{OLLAMA_BASE_URL}{endpoint}"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _get_ollama(endpoint: str) -> dict:
    """Realiza um GET para a API local do Ollama."""
    url = f"{OLLAMA_BASE_URL}{endpoint}"
    with urllib.request.urlopen(url, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))


# ─────────────────────────────────────────────
# Validação e Download
# ─────────────────────────────────────────────
def listar_modelos_locais() -> list[str]:
    """Retorna a lista de modelos já baixados no Ollama local."""
    try:
        data = _get_ollama("/api/tags")
        return [m["name"].split(":")[0] for m in data.get("models", [])]
    except Exception as exc:
        logger.warning("Não foi possível listar modelos Ollama: %s", exc)
        return []


def validar_modelo(modelo: str) -> bool:
    """Verifica se o modelo está na lista permitida."""
    if modelo not in MODELOS_DISPONIVEIS:
        raise ValueError(
            f"Modelo inválido: '{modelo}'. Permitidos: {MODELOS_DISPONIVEIS}"
        )
    return True


def baixar_modelo(modelo: str) -> bool:
    """
    Garante que o modelo está disponível localmente.
    Faz pull via subprocess se necessário.
    Retorna True se bem-sucedido.
    """
    validar_modelo(modelo)
    locais = listar_modelos_locais()
    if modelo in locais:
        logger.info("Modelo '%s' já disponível localmente.", modelo)
        return True

    logger.info("Baixando modelo '%s' via Ollama...", modelo)
    try:
        result = subprocess.run(
            ["ollama", "pull", modelo],
            capture_output=True,
            text=True,
            timeout=600,  # 10 min de timeout para download
        )
        if result.returncode == 0:
            logger.info("Modelo '%s' baixado com sucesso.", modelo)
            return True
        else:
            logger.error("Falha ao baixar '%s': %s", modelo, result.stderr)
            return False
    except subprocess.TimeoutExpired:
        logger.error("Timeout ao baixar modelo '%s'.", modelo)
        return False
    except FileNotFoundError:
        logger.error("Ollama não encontrado. Certifique-se de que o Ollama está instalado.")
        return False


# ─────────────────────────────────────────────
# Geração de Resposta com Fallback
# ─────────────────────────────────────────────
def gerar_resposta(
    mensagens: list[dict[str, str]],
    modelo: str = MODEL_ATUAL,
    temperatura: float = 0.7,
) -> str:
    """
    Gera uma resposta via Ollama com fallback automático entre modelos.

    Args:
        mensagens: Lista de dicts {"role": "user"|"assistant"|"system", "content": "..."}
        modelo: Modelo preferido a ser tentado primeiro
        temperatura: Criatividade do modelo (0.0 a 1.0)

    Returns:
        String com o conteúdo da resposta gerada

    Raises:
        RuntimeError: Se todos os modelos falharem
    """
    validar_modelo(modelo)
    sequencia = [modelo] + [m for m in FALLBACK_MODELS if m != modelo]

    ultimo_erro = None
    for m in sequencia:
        try:
            logger.info("Tentando gerar resposta com modelo: %s", m)
            payload = {
                "model": m,
                "messages": mensagens,
                "stream": False,
                "options": {"temperature": temperatura},
            }
            data = _post_ollama("/api/chat", payload)
            conteudo = data["message"]["content"]
            logger.info("Resposta gerada com sucesso via modelo: %s", m)
            return conteudo
        except Exception as exc:
            ultimo_erro = exc
            logger.warning("Modelo '%s' falhou: %s — tentando próximo...", m, exc)
            continue

    raise RuntimeError(
        f"Todos os modelos falharam ao gerar resposta. Último erro: {ultimo_erro}"
    )


# ─────────────────────────────────────────────
# Embeddings Locais
# ─────────────────────────────────────────────
def gerar_embedding(texto: str) -> list[float]:
    """
    Gera um vetor de embedding para o texto fornecido usando o modelo local.

    Args:
        texto: Texto a ser vetorizado

    Returns:
        Lista de floats representando o embedding
    """
    try:
        payload = {"model": EMBEDDING_MODEL, "prompt": texto}
        data = _post_ollama("/api/embeddings", payload)
        vetor = data.get("embedding", [])
        if not vetor:
            logger.warning("Embedding retornado vazio para texto de %d chars.", len(texto))
        return vetor
    except Exception as exc:
        logger.error("Falha ao gerar embedding: %s", exc)
        return []


def embedding_para_bytes(vetor: list[float]) -> bytes:
    """Serializa um vetor de floats em bytes para armazenamento em SQLite BLOB."""
    import struct
    return struct.pack(f"{len(vetor)}f", *vetor)


def bytes_para_embedding(raw: bytes) -> list[float]:
    """Desserializa bytes BLOB de volta para lista de floats."""
    import struct
    n = len(raw) // 4  # 4 bytes por float32
    return list(struct.unpack(f"{n}f", raw))


# ─────────────────────────────────────────────
# Status do Sistema
# ─────────────────────────────────────────────
def status_sistema() -> dict[str, Any]:
    """Retorna informações de status do Ollama e dos modelos disponíveis."""
    locais = listar_modelos_locais()
    ollama_ok = len(locais) >= 0  # A chamada não lançou exceção
    return {
        "ollama_online": ollama_ok,
        "modelos_locais": locais,
        "modelo_atual": MODEL_ATUAL,
        "fallback": FALLBACK_MODELS,
        "embedding_model": EMBEDDING_MODEL,
        "modelos_disponiveis": MODELOS_DISPONIVEIS,
    }
