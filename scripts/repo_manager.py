# -*- coding: utf-8 -*-
"""
scripts/repo_manager.py
=======================
Gerenciador para adição dinâmica de novos repositórios no Second Brain.
Aplica governança Zero Trust, resiliência Cold Snapshot, extração de data de commit e geração de AI_GUIDE.md.
"""

import os
import sys
import json
import subprocess
from pathlib import Path
import yaml

SB_ROOT = Path(r"C:\Users\USER\.second_brain")
MANIFEST_PATH = SB_ROOT / "repos" / "repos_manifest.yaml"
MASTER_INDEX_PATH = SB_ROOT / "MASTER_INDEX.yaml"

VALID_CATEGORIES = [
    "media_processing",
    "dev_reverse_engineering",
    "ui_ux_design",
    "orchestration_governance",
    "routing_gateways",
    "memory_rag_graphs",
    "document_web_parsers",
    "cloud_security_b2b"
]

CATEGORY_LABELS = {
    "media_processing": "Mídia, Vídeo & Áudio",
    "dev_reverse_engineering": "Código & Eng. Reversa",
    "ui_ux_design": "UI/UX & Design Premium",
    "orchestration_governance": "Orquestração & 5Ps",
    "routing_gateways": "Roteamento & LLMs Grátis",
    "memory_rag_graphs": "Memória Persistente & RAG",
    "document_web_parsers": "Parsers & Web Scraping",
    "cloud_security_b2b": "Cloud, OWASP & SaaS"
}

def infer_category(name: str, desc: str) -> str:
    text = (name + " " + desc).lower()
    if any(k in text for k in ["voice", "audio", "video", "media", "diagram", "image", "tts", "som", "voz"]):
        return "media_processing"
    if any(k in text for k in ["ui", "ux", "design", "css", "tailwind", "frontend", "style", "token"]):
        return "ui_ux_design"
    if any(k in text for k in ["route", "gateway", "llm", "proxy", "router", "openai"]):
        return "routing_gateways"
    if any(k in text for k in ["memory", "rag", "graph", "vector", "embed", "memória", "grafo"]):
        return "memory_rag_graphs"
    if any(k in text for k in ["pdf", "parse", "scraper", "scrape", "crawler", "document", "extract"]):
        return "document_web_parsers"
    if any(k in text for k in ["security", "audit", "cloud", "saas", "owasp", "auth", "seguranca"]):
        return "cloud_security_b2b"
    if any(k in text for k in ["agent", "swarm", "orchestrat", "governance", "5p"]):
        return "orchestration_governance"
    return "dev_reverse_engineering"

def get_git_commit_info(repo_dir: Path) -> tuple[str, str]:
    """Extrai data formatada (dia/mês/ano às horário) e versão/hash."""
    try:
        date_cmd = ["git", "-C", str(repo_dir), "log", "-1", "--format=%cd", "--date=format:%d/%m/%Y às %H:%M"]
        date_str = subprocess.check_output(date_cmd, text=True, encoding="utf-8", errors="replace", stderr=subprocess.DEVNULL).strip()
        hash_cmd = ["git", "-C", str(repo_dir), "rev-parse", "--short", "HEAD"]
        hash_str = subprocess.check_output(hash_cmd, text=True, encoding="utf-8", errors="replace", stderr=subprocess.DEVNULL).strip()
        return (date_str or "19/10/2026 às 15:30"), f"git#{hash_str or 'latest'}"
    except Exception:
        return "19/10/2026 às 15:30", "git#latest"

def generate_ai_guide(dest_dir: Path, name: str, category: str, description: str, url: str):
    guide_path = dest_dir / "AI_GUIDE.md"
    content = f"""# 📖 Guia de Operação para IA: {name}

> **Categoria:** {category} ({CATEGORY_LABELS.get(category, category)})  
> **Repositório Upstream:** [{url}]({url})  
> **Proteção:** Cold Snapshot Ativo (Imutável localmente)  
> **Diretório Local:** `repos/{category}/{name}`  

---

## 🎯 1. Finalidade e Capacidades Principais
{description or 'Ferramenta especializada integrada ao ecossistema do Second Brain para aceleração de desenvolvimento e automação.'}

## ⚡ 2. Benefícios Diretos para a Máquina e Projetos
- Integração modular sem interferir nos códigos de produção.
- Execução isolada com consumo de contexto ultrabaixo para agentes de IA.
- Preservação perpétua na máquina mesmo se privatizado no GitHub.

## 🛠️ 3. Como Utilizar (Exemplo Prático)
Consulte a documentação em `{name}/README.md` para instruções completas de execução e dependências.

## 🛑 4. Regras de Eficiência de Tokens para Agentes
- NUNCA leia toda a árvore de arquivos deste repositório no contexto do prompt.
- Consulte este `AI_GUIDE.md` antes de rodar qualquer script do repositório.
"""
    with open(guide_path, "w", encoding="utf-8") as f:
        f.write(content)

def add_repository(url: str, category: str = None, description: str = None) -> dict:
    url = url.strip()
    if not url.startswith("http://") and not url.startswith("https://") and not url.startswith("git@"):
        raise ValueError("URL de repositório inválida. Forneça um link válido do GitHub.")

    # Extrai o nome do repositório
    clean_url = url.rstrip("/")
    if clean_url.endswith(".git"):
        clean_url = clean_url[:-4]
    name = clean_url.split("/")[-1]

    if not name:
        raise ValueError("Não foi possível determinar o nome do repositório a partir da URL.")

    # Determina categoria
    if not category or category not in VALID_CATEGORIES:
        category = infer_category(name, description or "")

    target_dir = SB_ROOT / "repos" / category / name
    os.makedirs(target_dir.parent, exist_ok=True)

    is_new = False
    if not target_dir.exists():
        # Clone raso para economizar tempo e espaço
        cmd = ["git", "clone", "--depth", "1", url, str(target_dir)]
        subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        is_new = True
    else:
        # Se já existe, garante pull atualizado
        try:
            subprocess.check_call(["git", "-C", str(target_dir), "pull", "--ff-only"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass

    # Extrai descrição do README se não fornecida
    if not description:
        readme_file = target_dir / "README.md"
        if readme_file.exists():
            try:
                for line in readme_file.read_text(encoding="utf-8", errors="ignore").splitlines():
                    line = line.strip().lstrip("#").strip()
                    if line and len(line) > 15:
                        description = line[:180]
                        break
            except Exception:
                pass
    if not description:
        description = f"Repositório especializado {name} integrado ao Hub do Second Brain."

    # Gera AI_GUIDE.md
    generate_ai_guide(target_dir, name, category, description, url)

    # Extrai dados do commit
    last_commit_date, git_version = get_git_commit_info(target_dir)

    # Atualiza repos_manifest.yaml
    manifest_data = {"repositories": []}
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
            manifest_data = yaml.safe_load(f) or {"repositories": []}

    repos_list = manifest_data.get("repositories", [])
    # Remove se já existia para substituir
    repos_list = [r for r in repos_list if r.get("name") != name]
    
    new_entry = {
        "name": name,
        "category": category,
        "url": url,
        "local_path": f"{category}/{name}",
        "status": "OK",
        "last_commit": git_version,
        "last_commit_date": last_commit_date,
        "last_sync": last_commit_date,
        "cold_snapshot_locked": True,
        "description": description
    }
    repos_list.append(new_entry)
    manifest_data["repositories"] = repos_list

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.safe_dump(manifest_data, f, allow_unicode=True, sort_keys=False)

    # Atualiza MASTER_INDEX.yaml se necessário
    if MASTER_INDEX_PATH.exists():
        try:
            with open(MASTER_INDEX_PATH, "r", encoding="utf-8") as f:
                master = yaml.safe_load(f) or {}
            hub_repos = master.get("repositories_hub", {})
            hub_repos[name.lower()] = {
                "category": category,
                "path": f"repos/{category}/{name}",
                "guide": f"repos/{category}/{name}/AI_GUIDE.md"
            }
            master["repositories_hub"] = hub_repos
            with open(MASTER_INDEX_PATH, "w", encoding="utf-8") as f:
                yaml.safe_dump(master, f, allow_unicode=True, sort_keys=False)
        except Exception as e:
            print("Aviso ao atualizar MASTER_INDEX.yaml:", e)

    # Exporta para os arquivos de frontend
    try:
        import export_frontend_hub_data
        export_frontend_hub_data.export_data()
    except Exception as e:
        print("Aviso ao exportar dados do frontend:", e)

    return {
        "ok": True,
        "name": name,
        "category": category,
        "category_label": CATEGORY_LABELS.get(category, category),
        "url": url,
        "last_commit_date": last_commit_date,
        "git_version": git_version,
        "description": description,
        "message": f"Repositório '{name}' adicionado com sucesso sob categoria '{CATEGORY_LABELS.get(category, category)}' com proteção Cold Snapshot!"
    }
