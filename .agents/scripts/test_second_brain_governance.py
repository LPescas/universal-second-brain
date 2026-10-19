#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_second_brain_governance.py -- Teste Empírico de Governança Zero Trust do Second Brain
========================================================================================
Valida empiricamente que o Second Brain está 100% em conformidade com as regras
da Skill Global de Governança RPA (Zero Trust):
1. Existência e integridade do README.md e projeto_second_brain.md
2. Existência e funcionamento do Guardião de Execução em core/governanca/
3. Presença obrigatória de *_nome.md com cabeçalho de governança nas subpastas
4. Validação de ausência de acentos nos nomes de scripts Python
5. Execução limpa do guardião de governança retornando código 0
"""
import io
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SB_ROOT = Path(r"C:\Users\USER\.second_brain")

def test_governance():
    print("=" * 65)
    print("🛡️ TESTE EMPÍRICO DE GOVERNANÇA ZERO TRUST — SECOND BRAIN")
    print("=" * 65)

    # 1. Documentos Mestres
    readme = SB_ROOT / "README.md"
    master_doc = SB_ROOT / "projeto_second_brain.md"
    assert readme.exists(), "README.md não encontrado na raiz!"
    assert master_doc.exists(), "projeto_second_brain.md não encontrado na raiz!"
    print("✅ [1/5] Documentos mestres (README.md e projeto_second_brain.md) verificados.")

    # 2. Módulo de Governança Core
    core_gov = SB_ROOT / "core" / "governanca"
    guardiao = core_gov / "guardiao_execucao.py"
    leitor = core_gov / "leitor_documentacao.py"
    validador = core_gov / "validador_regras.py"
    assert guardiao.exists() and leitor.exists() and validador.exists(), "Módulos do Guardião ausentes!"
    print("✅ [2/5] Módulo de governança core/governanca/ completo e verificado.")

    # 3. Documentação das Subpastas (*_nome.md) com cabeçalho obrigatório
    subpastas_chave = [
        ("core", "core_second_brain.md"),
        ("core/governanca", "governanca_core.md"),
        ("backend", "backend_second_brain.md"),
        ("backend/aurelio", "aurelio_backend.md"),
        ("frontend", "frontend_second_brain.md"),
        ("scripts", "scripts_second_brain.md"),
        ("knowledge", "knowledge_second_brain.md"),
        ("projects", "projects_second_brain.md"),
        ("integrations", "integrations_second_brain.md"),
        ("repos", "repos_second_brain.md"),
        ("repos/media_processing", "media_processing_repos.md"),
        ("repos/dev_reverse_engineering", "dev_reverse_engineering_repos.md"),
        ("repos/ui_ux_design", "ui_ux_design_repos.md"),
        ("repos/orchestration_governance", "orchestration_governance_repos.md"),
        ("repos/routing_gateways", "routing_gateways_repos.md"),
        ("repos/memory_rag_graphs", "memory_rag_graphs_repos.md"),
        ("repos/document_web_parsers", "document_web_parsers_repos.md"),
        ("repos/cloud_security_b2b", "cloud_security_b2b_repos.md"),
        (".agents", "agents_second_brain.md")
    ]

    for rel_folder, md_file in subpastas_chave:
        target = SB_ROOT / rel_folder / md_file
        assert target.exists(), f"Documentação obrigatória não encontrada: {rel_folder}/{md_file}"
        content = target.read_text(encoding="utf-8", errors="replace")
        assert "REGRA DE GOVERNANÇA GLOBAL" in content, f"Cabeçalho ausente em {rel_folder}/{md_file}"

    print(f"✅ [3/5] Todas as {len(subpastas_chave)} subpastas chave possuem documentação *_nome.md com cabeçalho Zero Trust.")

    # 4. Convenção de Nomenclatura (Sem Acentos em .py)
    scripts_dir = SB_ROOT / "scripts"
    for py_file in scripts_dir.glob("*.py"):
        assert all(ord(c) < 128 for c in py_file.name), f"Script Python contém acento no nome: {py_file.name}"
    print("✅ [4/5] Regra de nomenclatura limpa (sem acentos nos scripts .py) cumprida.")

    # 5. Execução do Guardião
    proc = subprocess.run([sys.executable, str(guardiao)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    assert proc.returncode == 0, f"Guardião de execução reprovou o projeto: {proc.stderr}"
    print("✅ [5/5] Guardião de Execução Zero Trust executado com retorno 0 (Aprovado).")

    print("\n" + "=" * 65)
    print("🎯 TODOS OS 5 TESTES DE GOVERNANÇA PASSARAM COM SUCESSO!")
    print("=" * 65)
    return 0

if __name__ == "__main__":
    sys.exit(test_governance())
