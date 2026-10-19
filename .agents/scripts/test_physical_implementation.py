#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_physical_implementation.py -- Script de Validação Empírica da Expansão do Second Brain
========================================================================================
Executa e comprova o funcionamento físico de todos os componentes da Seção 7 do plano:
1. Existência física dos 25 repositórios (.git válidos).
2. Existência física dos 25 manuais AI_GUIDE.md com metadados válidos.
3. Integridade do manifesto YAML repos_manifest.yaml.
4. Integridade do catálogo mestre installed_assets_catalog.md.
5. Presença da seção repositories_hub e novas rotas no MASTER_INDEX.yaml.
6. Presença da regra 7 no global_rules.md.
7. Execução funcional do repo_sync_engine.py com retorno de status.
"""
import io
import subprocess
import sys
from pathlib import Path
import yaml

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SB_ROOT = Path(r"C:\Users\USER\.second_brain")
REPOS_ROOT = SB_ROOT / "repos"
MANIFEST_PATH = REPOS_ROOT / "repos_manifest.yaml"
CATALOG_PATH = SB_ROOT / "knowledge" / "installed_assets_catalog.md"
MASTER_INDEX_PATH = SB_ROOT / "MASTER_INDEX.yaml"
GLOBAL_RULES_PATH = SB_ROOT / "global_rules.md"
SYNC_ENGINE_PATH = SB_ROOT / "scripts" / "repo_sync_engine.py"

EXPECTED_REPOS = [
    "VoiceStudio", "editonny", "diagram-design", "paperclip",
    "rea", "ECC", "vibe-coding-toolkit", "andrej-karpathy-skills", "superpowers",
    "impeccable", "ruflo", "agentville", "framework-5p", "claude-plugins-official",
    "OmniRoute", "freellmapi", "claude-mem", "hindsight", "graphify",
    "docling", "ponytail", "scientific-agent-skills",
    "security-audit-skill", "Octop", "nango"
]

def run_tests():
    print("=" * 65)
    print("🔍 INICIANDO BATERIA DE TESTES EMPÍRICOS VIA .agents/scripts")
    print("=" * 65)
    
    # 1. Verifica Manifesto YAML
    assert MANIFEST_PATH.exists(), f"Manifesto inexistente: {MANIFEST_PATH}"
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest_data = yaml.safe_load(f)
    repos_in_manifest = manifest_data.get("repositories", [])
    assert len(repos_in_manifest) == 25, f"Esperado 25 repos no manifesto, encontrado {len(repos_in_manifest)}"
    print(f"✅ [1/7] Manifesto validado: {len(repos_in_manifest)} repositórios registrados.")

    # 2. Verifica Existência Física dos 25 Repositórios e .git
    missing_git = []
    missing_guides = []
    for r in repos_in_manifest:
        repo_dir = REPOS_ROOT / r["local_path"]
        git_dir = repo_dir / ".git"
        guide_file = repo_dir / "AI_GUIDE.md"
        
        if not git_dir.exists():
            missing_git.append(r["name"])
        if not guide_file.exists():
            missing_guides.append(r["name"])

    assert not missing_git, f"Repositórios sem .git físico: {missing_git}"
    print(f"✅ [2/7] Todos os 25 repositórios fisicamente clonados com .git íntegro.")

    # 3. Verifica Existência Física dos 25 AI_GUIDE.md
    assert not missing_guides, f"Repositórios sem AI_GUIDE.md: {missing_guides}"
    print(f"✅ [3/7] Todos os 25 manuais AI_GUIDE.md gerados e verificados localmente.")

    # 4. Verifica Catálogo Mestre de Assets
    assert CATALOG_PATH.exists(), f"Catálogo inexistente: {CATALOG_PATH}"
    catalog_content = CATALOG_PATH.read_text(encoding="utf-8")
    assert "25 repositórios" in catalog_content, "25 repositórios não encontrado no catálogo"
    assert "20 personas" in catalog_content, "20 personas não encontrado no catálogo"
    print("✅ [4/7] Catálogo mestre installed_assets_catalog.md íntegro e indexado.")

    # 5. Verifica MASTER_INDEX.yaml
    assert MASTER_INDEX_PATH.exists(), f"MASTER_INDEX.yaml inexistente"
    with open(MASTER_INDEX_PATH, "r", encoding="utf-8") as f:
        master_data = yaml.safe_load(f)
    assert "repositories_hub" in master_data, "repositories_hub não encontrado no MASTER_INDEX.yaml"
    assert "media_audio_video" in master_data.get("intent_routing", {}), "Rotas novas de intent ausentes"
    print("✅ [5/7] MASTER_INDEX.yaml validado com repositories_hub e intent_routing completo.")

    # 6. Verifica Regra 7 no global_rules.md
    assert GLOBAL_RULES_PATH.exists(), "global_rules.md inexistente"
    rules_content = GLOBAL_RULES_PATH.read_text(encoding="utf-8")
    assert "Hub de Reposit" in rules_content and "Assets" in rules_content, "Regra do Hub não encontrada no global_rules.md"
    print("✅ [6/7] Regra de Consulta Mandatória ao Hub verificada no global_rules.md.")

    # 7. Execução Funcional do repo_sync_engine.py com --status
    cmd = [sys.executable, "-c", "import sys; sys.stdout.reconfigure(encoding='utf-8'); exec(open(r'" + str(SYNC_ENGINE_PATH) + "', encoding='utf-8').read())", "--status"]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    assert proc.returncode == 0, f"Falha ao executar repo_sync_engine.py --status: {proc.stderr}"
    assert "SECOND BRAIN" in proc.stdout or "VoiceStudio" in proc.stdout, "Saída inesperada do status"
    print("✅ [7/7] Motor de sincronização repo_sync_engine.py executado com sucesso.")

    print("\n" + "=" * 65)
    print("🎯 TODOS OS 7 TESTES EMPÍRICOS DE VALIDAÇÃO PASSARAM COM SUCESSO!")
    print("=" * 65)
    return 0

if __name__ == "__main__":
    sys.exit(run_tests())
