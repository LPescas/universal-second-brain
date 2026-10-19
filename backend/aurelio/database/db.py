"""
database/db.py — Segunda Memória Persistente do Second Brain (Aurelio)

Responsável por:
- Criação e migração do schema SQLite
- CRUD de conversas, mensagens, projetos e memória vetorial
- Controle de crescimento (máx. 1000 registros ativos + arquivamento)
"""

import sqlite3
import logging
import os
from datetime import datetime
from pathlib import Path

# ─────────────────────────────────────────────
# Configuração
# ─────────────────────────────────────────────
DB_PATH = Path(__file__).parent.parent / "data" / "aurelio.db"
MAX_REGISTROS_ATIVOS = 1000

logger = logging.getLogger(__name__)


def get_connection() -> sqlite3.Connection:
    """Retorna uma conexão com o banco SQLite, criando o arquivo se necessário."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row  # Retorna dicts em vez de tuples
    conn.execute("PRAGMA journal_mode=WAL;")  # Write-Ahead Log para melhor concorrência
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


# ─────────────────────────────────────────────
# Migração / Criação de Tabelas
# ─────────────────────────────────────────────
def inicializar_banco() -> None:
    """Cria todas as tabelas se não existirem. Idempotente."""
    with get_connection() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS conversas (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT UNIQUE NOT NULL,
                modo      TEXT NOT NULL DEFAULT 'restrito',
                data_inicio DATETIME NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS mensagens (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                conversa_id TEXT NOT NULL,
                tipo        TEXT NOT NULL CHECK(tipo IN ('user', 'assistant')),
                conteudo    TEXT NOT NULL,
                timestamp   DATETIME NOT NULL DEFAULT (datetime('now')),
                FOREIGN KEY (conversa_id) REFERENCES conversas(session_id)
            );

            CREATE TABLE IF NOT EXISTS projetos (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                nome         TEXT NOT NULL,
                descricao    TEXT,
                versao       INTEGER NOT NULL DEFAULT 1,
                atualizado_em DATETIME NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS memoria (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                texto     TEXT NOT NULL,
                embedding BLOB,
                source    TEXT,
                timestamp DATETIME NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS memoria_arquivo (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                texto     TEXT NOT NULL,
                embedding BLOB,
                source    TEXT,
                timestamp DATETIME NOT NULL,
                arquivado_em DATETIME NOT NULL DEFAULT (datetime('now'))
            );

            CREATE INDEX IF NOT EXISTS idx_mensagens_conversa
                ON mensagens(conversa_id, timestamp);

            CREATE INDEX IF NOT EXISTS idx_memoria_timestamp
                ON memoria(timestamp DESC);
        """)
    logger.info("Banco de dados inicializado com sucesso em: %s", DB_PATH)


# ─────────────────────────────────────────────
# Conversas / Sessões
# ─────────────────────────────────────────────
def criar_sessao(session_id: str, modo: str = "restrito") -> None:
    """Registra uma nova sessão/conversa no banco."""
    with get_connection() as conn:
        conn.execute(
            "INSERT OR IGNORE INTO conversas (session_id, modo) VALUES (?, ?)",
            (session_id, modo),
        )
    logger.info("Sessão criada: %s | modo: %s", session_id, modo)


def definir_modo_sessao(session_id: str, modo: str) -> None:
    """Atualiza o modo (restrito/expandido) de uma sessão."""
    with get_connection() as conn:
        conn.execute(
            "UPDATE conversas SET modo = ? WHERE session_id = ?",
            (modo, session_id),
        )
    logger.info("Modo atualizado para '%s' na sessão %s", modo, session_id)


def obter_modo_sessao(session_id: str) -> str | None:
    """Retorna o modo da sessão ou None se não existir."""
    with get_connection() as conn:
        row = conn.execute(
            "SELECT modo FROM conversas WHERE session_id = ?", (session_id,)
        ).fetchone()
    return row["modo"] if row else None


# ─────────────────────────────────────────────
# Mensagens
# ─────────────────────────────────────────────
def salvar_mensagem(session_id: str, tipo: str, conteudo: str) -> None:
    """Persiste uma mensagem (user ou assistant) no histórico."""
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO mensagens (conversa_id, tipo, conteudo) VALUES (?, ?, ?)",
            (session_id, tipo, conteudo),
        )
    logger.debug("Mensagem salva [%s] na sessão %s", tipo, session_id)


def buscar_historico(session_id: str, limite: int = 30) -> list[dict]:
    """Retorna o histórico recente de mensagens de uma sessão."""
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT tipo, conteudo, timestamp
            FROM mensagens
            WHERE conversa_id = ?
            ORDER BY timestamp ASC
            LIMIT ?
            """,
            (session_id, limite),
        ).fetchall()
    return [dict(r) for r in rows]


def contar_repeticoes(session_id: str, tipo: str = "user") -> dict[str, int]:
    """
    Conta quantas vezes cada conteúdo único aparece no histórico.
    Usado pelo modo proativo para detectar padrões repetitivos.
    """
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT conteudo, COUNT(*) as total
            FROM mensagens
            WHERE conversa_id = ? AND tipo = ?
            GROUP BY conteudo
            HAVING COUNT(*) >= 2
            ORDER BY total DESC
            """,
            (session_id, tipo),
        ).fetchall()
    return {r["conteudo"]: r["total"] for r in rows}


# ─────────────────────────────────────────────
# Memória Vetorial
# ─────────────────────────────────────────────
def salvar_memoria(texto: str, embedding: bytes | None, source: str = "") -> int:
    """Insere um registro de memória vetorial. Retorna o ID gerado."""
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO memoria (texto, embedding, source) VALUES (?, ?, ?)",
            (texto, embedding, source),
        )
        mem_id = cursor.lastrowid
    logger.debug("Memória salva [id=%s]", mem_id)
    # Controle de crescimento: arquivar excedente após cada insert
    controlar_crescimento()
    return mem_id


def atualizar_embedding(mem_id: int, embedding: bytes) -> None:
    """Atualiza o embedding de um registro de memória existente."""
    with get_connection() as conn:
        conn.execute(
            "UPDATE memoria SET embedding = ? WHERE id = ?",
            (embedding, mem_id),
        )
    logger.debug("Embedding atualizado [id=%s]", mem_id)


def buscar_memorias_recentes(limite: int = 100) -> list[dict]:
    """Retorna os registros mais recentes da memória vetorial."""
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, texto, embedding, timestamp FROM memoria ORDER BY timestamp DESC LIMIT ?",
            (limite,),
        ).fetchall()
    return [dict(r) for r in rows]


# ─────────────────────────────────────────────
# Controle de Crescimento (Arquivamento)
# ─────────────────────────────────────────────
def controlar_crescimento() -> int:
    """
    Mantém no máximo MAX_REGISTROS_ATIVOS na tabela memoria.
    Registros mais antigos são movidos para memoria_arquivo.
    Retorna quantos registros foram arquivados.
    """
    with get_connection() as conn:
        total = conn.execute("SELECT COUNT(*) as c FROM memoria").fetchone()["c"]
        excedente = total - MAX_REGISTROS_ATIVOS
        if excedente <= 0:
            return 0

        # Mover os mais antigos para arquivo
        conn.execute(
            """
            INSERT INTO memoria_arquivo (texto, embedding, source, timestamp)
            SELECT texto, embedding, source, timestamp
            FROM memoria
            ORDER BY timestamp ASC
            LIMIT ?
            """,
            (excedente,),
        )
        conn.execute(
            """
            DELETE FROM memoria
            WHERE id IN (
                SELECT id FROM memoria ORDER BY timestamp ASC LIMIT ?
            )
            """,
            (excedente,),
        )
    logger.info("%d registros de memória arquivados.", excedente)
    return excedente


# ─────────────────────────────────────────────
# Projetos
# ─────────────────────────────────────────────
def salvar_projeto(nome: str, descricao: str = "") -> int:
    """Cria ou atualiza (versiona) um projeto no banco."""
    with get_connection() as conn:
        existente = conn.execute(
            "SELECT id, versao FROM projetos WHERE nome = ?", (nome,)
        ).fetchone()

        if existente:
            nova_versao = existente["versao"] + 1
            conn.execute(
                "UPDATE projetos SET descricao = ?, versao = ?, atualizado_em = datetime('now') WHERE id = ?",
                (descricao, nova_versao, existente["id"]),
            )
            return existente["id"]
        else:
            cursor = conn.execute(
                "INSERT INTO projetos (nome, descricao) VALUES (?, ?)",
                (nome, descricao),
            )
            return cursor.lastrowid
