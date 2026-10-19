#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validador_regras.py -- Validador Estrutural de Regras e Governança do Second Brain
"""
import os
import sys
import unicodedata
import logging
from pathlib import Path

logger = logging.getLogger("GovernancaValidador")

class ValidadorRegras:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.pastas_principais = [
            "core", "backend", "frontend", "scripts",
            "knowledge", "projects", "repos", "integrations", ".agents"
        ]
        self.arquivos_criticos = [
            "MASTER_INDEX.yaml",
            "global_rules.md",
            "projeto_second_brain.md",
            "README.md",
            "scripts/repo_sync_engine.py",
            "repos/repos_manifest.yaml",
            "knowledge/installed_assets_catalog.md"
        ]

    def _remover_acentos(self, texto):
        return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

    def validar_estrutura(self):
        """Verifica a presença das pastas macro-estruturais do Second Brain."""
        erros = []
        for pasta in self.pastas_principais:
            p = self.root_dir / pasta
            if not p.exists() or not p.is_dir():
                erros.append(f"Pasta estrutural ausente: {pasta}")
        return erros

    def validar_arquivos_criticos(self):
        """Verifica os arquivos centrais de arquitetura e funcionamento."""
        erros = []
        for rel_path in self.arquivos_criticos:
            p = self.root_dir / rel_path
            if not p.exists():
                erros.append(f"Arquivo crítico não encontrado: {rel_path}")
        return erros

    def validar_documentacao_md(self, caminho_relativo="."):
        """Valida se todas as subpastas possuem documentação .md com o cabeçalho obrigatório."""
        erros = []
        base_path = self.root_dir / caminho_relativo
        if not base_path.exists():
            return []

        cabecalho_obrigatorio = "REGRA DE GOVERNANÇA GLOBAL"

        ignorar = ["__pycache__", ".git", "node_modules", ".venv", "venv"]

        for root, dirs, files in os.walk(base_path):
            if any(ign in root for ign in ignorar):
                continue

            # Se for repositório externo clonado em repos/, valida apenas a categoria macro
            rel_to_sb = Path(root).relative_to(self.root_dir)
            parts = rel_to_sb.parts
            if len(parts) >= 3 and parts[0] == "repos":
                # É subpasta interna de um repo clonado (ex: repos/media_processing/VoiceStudio/...)
                # A responsabilidade de governança interna do repo é do próprio repo
                continue

            md_files = [f for f in files if f.endswith(".md")]
            if not md_files:
                erros.append(f"Subpasta sem documentação .md local: {rel_to_sb}")
            else:
                for md in md_files:
                    caminho_md = Path(root) / md
                    try:
                        conteudo = caminho_md.read_text(encoding="utf-8", errors="replace")
                        if cabecalho_obrigatorio not in conteudo and md not in ["README.md", "second-brain-expansion.md", "cursorrules_template.md"]:
                            # Verifica se o arquivo é um arquivo padrão de documentação que deve ter o cabeçalho
                            if "_" in md:
                                erros.append(f"Arquivo '{rel_to_sb}/{md}' sem cabeçalho obrigatório de governança.")
                    except Exception as e:
                        erros.append(f"Erro ao ler '{rel_to_sb}/{md}': {str(e)}")

        return erros

    def validar_nomenclatura(self):
        """Garante que nenhum script Python possua acentos ou caracteres inválidos."""
        erros = []
        scripts_dir = self.root_dir / "scripts"
        if scripts_dir.exists():
            for f in scripts_dir.glob("*.py"):
                nome_sem_acento = self._remover_acentos(f.name)
                if nome_sem_acento != f.name:
                    erros.append(f"Script com acentuação no nome: {f.name}")
        return erros
