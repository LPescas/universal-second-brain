#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
guardiao_execucao.py -- Guardião de Execução Zero Trust do Second Brain
======================================================================
Bloqueia qualquer execução se a arquitetura, arquivos críticos ou documentação
local de governança estiverem corrompidos ou ausentes.
"""
import sys
import logging
from pathlib import Path

# Ajuste de import relativo / absoluto
CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from leitor_documentacao import LeitorDocumentacao
from validador_regras import ValidadorRegras

GOVERNANCA_ATIVA = True

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("GuardiaoSecondBrain")


def registrar_log(id_log, modulo, etapa, tipo, mensagem):
    msg = f"[{id_log}] [{modulo.upper()}] [{etapa.upper()}] [{tipo.upper()}] {mensagem}"
    if tipo.upper() == "ERRO":
        logger.error(msg)
    elif tipo.upper() == "ALERTA":
        logger.warning(msg)
    else:
        logger.info(msg)


def validar_execucao(projeto_root=r"C:\Users\USER\.second_brain"):
    if not GOVERNANCA_ATIVA:
        registrar_log("000", "GLOBAL", "GOVERNANCA", "ALERTA", "⚠️ Bypass de governança ativado.")
        return True

    registrar_log("000", "SECOND_BRAIN", "GOVERNANCA", "INFO", "Auditoria Zero Trust iniciada.")
    leitor = LeitorDocumentacao(projeto_root)
    validador = ValidadorRegras(projeto_root)

    if not leitor.ler_documento_principal():
        registrar_log("999", "SECOND_BRAIN", "GOVERNANCA", "ERRO", "Documento mestre ausente!")
        return False

    erros = []
    erros.extend(validador.validar_estrutura())
    erros.extend(validador.validar_arquivos_criticos())
    erros.extend(validador.validar_nomenclatura())

    if erros:
        for err in erros:
            registrar_log("XXX", "SECOND_BRAIN", "VALIDACAO", "ERRO", err)
        return False

    registrar_log("100", "SECOND_BRAIN", "GOVERNANCA", "INFO", "Todas as regras cumpridas. Execução autorizada.")
    return True


if __name__ == "__main__":
    sucesso = validar_execucao()
    sys.exit(0 if sucesso else 1)
