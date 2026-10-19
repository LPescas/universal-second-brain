#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
leitor_documentacao.py -- Validador e Leitor de Documentação Zero Trust do Second Brain
"""
import os
import sys
import logging
from pathlib import Path

logger = logging.getLogger("GovernancaLeitor")

class LeitorDocumentacao:
    def __init__(self, projeto_root):
        self.projeto_root = Path(projeto_root)
        self.doc_principal_nome = "projeto_second_brain.md"
        
    def ler_documento_principal(self):
        """Verifica se a documentação mestre existe na raiz."""
        caminho_doc = self.projeto_root / self.doc_principal_nome
        if not caminho_doc.exists():
            # Fallback para README.md
            caminho_doc = self.projeto_root / "README.md"
            if not caminho_doc.exists():
                logger.error(f"[001] [GLOBAL] [GOVERNANCA] [ERRO] Documentação mestre '{self.doc_principal_nome}' ou 'README.md' não encontrada na raiz!")
                return False
                
        logger.info(f"[001] [GLOBAL] [GOVERNANCA] [INFO] Documento Mestre '{caminho_doc.name}' carregado.")
        return True

    def ler_documentacao_local(self, caminho_pasta):
        """Audita se a pasta especificada contém documentação .md válida."""
        pasta_alvo = self.projeto_root / caminho_pasta
        if not pasta_alvo.exists() or not pasta_alvo.is_dir():
            return False
            
        md_files = [f for f in pasta_alvo.iterdir() if f.is_file() and f.name.endswith(".md")]
        if not md_files:
            logger.warning(f"[001] [{pasta_alvo.name.upper()}] [GOVERNANCA] [ALERTA] Pasta sem documentação .md local.")
            return False
            
        logger.info(f"[001] [{pasta_alvo.name.upper()}] [GOVERNANCA] [INFO] {len(md_files)} arquivo(s) .md localizados em '{pasta_alvo.name}'.")
        return True
