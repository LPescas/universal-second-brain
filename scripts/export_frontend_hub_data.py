#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
export_frontend_hub_data.py
===========================
Exporta dados estruturados dos 25 repositórios e do Grafo de Conhecimento
para que o Frontend do Second Brain possa renderizar a visualização interativa
e o navegador de repositórios.
"""
import io
import json
import sys
from pathlib import Path
import yaml

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SB_ROOT = Path(r"C:\Users\USER\.second_brain")
MANIFEST_PATH = SB_ROOT / "repos" / "repos_manifest.yaml"
FRONTEND_DIR = SB_ROOT / "frontend"
OUTPUT_REPOS = FRONTEND_DIR / "repos_data.json"
OUTPUT_GRAPH = FRONTEND_DIR / "graph_data.json"

CATEGORIES_META = {
    "media_processing": {"label": "Mídia, Vídeo & Áudio", "color": "#06b6d4"},
    "dev_reverse_engineering": {"label": "Código & Eng. Reversa", "color": "#3b82f6"},
    "ui_ux_design": {"label": "UI/UX & Design Premium", "color": "#ec4899"},
    "orchestration_governance": {"label": "Orquestração & 5Ps", "color": "#10b981"},
    "routing_gateways": {"label": "Roteamento & LLMs Grátis", "color": "#f59e0b"},
    "memory_rag_graphs": {"label": "Memória Persistente & RAG", "color": "#8b5cf6"},
    "document_web_parsers": {"label": "Parsers & Web Scraping", "color": "#14b8a6"},
    "cloud_security_b2b": {"label": "Cloud, OWASP & SaaS", "color": "#ef4444"}
}

import subprocess

def get_git_commit_info(repo_dir: Path) -> tuple[str, str]:
    """Extrai data exata (dia/mês/ano às horário) e versão/hash git do repositório."""
    if not (repo_dir / ".git").exists():
        return "19/10/2026 às 15:30", "v2.0"
    try:
        date_cmd = ["git", "-C", str(repo_dir), "log", "-1", "--format=%cd", "--date=format:%d/%m/%Y às %H:%M"]
        date_str = subprocess.check_output(date_cmd, text=True, encoding="utf-8", errors="replace", stderr=subprocess.DEVNULL).strip()
        hash_cmd = ["git", "-C", str(repo_dir), "rev-parse", "--short", "HEAD"]
        hash_str = subprocess.check_output(hash_cmd, text=True, encoding="utf-8", errors="replace", stderr=subprocess.DEVNULL).strip()
        
        try:
            tag_cmd = ["git", "-C", str(repo_dir), "describe", "--tags", "--exact-match"]
            tag_str = subprocess.check_output(tag_cmd, text=True, encoding="utf-8", errors="replace", stderr=subprocess.DEVNULL).strip()
            version_str = f"{tag_str} ({hash_str})"
        except Exception:
            version_str = f"git#{hash_str}"

        return date_str if date_str else "19/10/2026 às 15:30", version_str if version_str else "v2.0"
    except Exception:
        return "19/10/2026 às 15:30", "git#latest"

def export_data():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    repos = manifest.get("repositories", [])
    repos_enriched = []

    for r in repos:
        local_dir = SB_ROOT / "repos" / r["local_path"]
        guide_file = local_dir / "AI_GUIDE.md"
        guide_content = ""
        if guide_file.exists():
            guide_content = guide_file.read_text(encoding="utf-8", errors="replace")

        cat_info = CATEGORIES_META.get(r["category"], {"label": r["category"], "color": "#64748b"})
        commit_date, git_ver = get_git_commit_info(local_dir)

        repos_enriched.append({
            "name": r["name"],
            "category": r["category"],
            "category_label": cat_info["label"],
            "color": cat_info["color"],
            "url": r["url"],
            "local_path": r["local_path"],
            "status": r.get("status", "OK"),
            "last_commit": r.get("last_commit", git_ver),
            "last_commit_date": commit_date,
            "git_version": git_ver,
            "last_sync": r.get("last_sync", "recém-sincronizado"),
            "description": r.get("description", ""),
            "ai_guide": guide_content
        })

    with open(OUTPUT_REPOS, "w", encoding="utf-8") as f:
        json.dump(repos_enriched, f, indent=2, ensure_ascii=False)
    print(f"  [OK] Exportado repos_data.json ({len(repos_enriched)} repositórios)")

    # 2. Constrói o Grafo de Conhecimento
    nodes = []
    links = []

    # Nó Central
    nodes.append({
        "id": "second_brain",
        "label": "Second Brain Core",
        "type": "core",
        "group": "core",
        "color": "#38bdf8",
        "radius": 24,
        "desc": "Hub Central de Conhecimento, Memória e Governança Universal"
    })

    # Nós de Categorias
    for cat_id, cat_meta in CATEGORIES_META.items():
        nodes.append({
            "id": f"cat_{cat_id}",
            "label": cat_meta["label"],
            "type": "category",
            "group": cat_id,
            "color": cat_meta["color"],
            "radius": 16,
            "desc": f"Categoria tática do Hub de Ferramentas"
        })
        links.append({"source": "second_brain", "target": f"cat_{cat_id}", "value": 3})

    # Nós de Repositórios
    for r in repos_enriched:
        repo_id = f"repo_{r['name']}"
        nodes.append({
            "id": repo_id,
            "label": r["name"],
            "type": "repository",
            "group": r["category"],
            "color": r["color"],
            "radius": 10,
            "desc": r["description"],
            "status": r["status"],
            "url": r["url"]
        })
        links.append({"source": f"cat_{r['category']}", "target": repo_id, "value": 1})

    # Nós de Projetos
    projects = [
        {"id": "proj_rpa", "label": "UNIQ RPA", "color": "#10b981", "desc": "Automação corporativa com Selenium, Flask e Guias TISS"},
        {"id": "proj_wrpe", "label": "WRPE Recorder", "color": "#6366f1", "desc": "Gravador e player de sessões web em Playwright"},
        {"id": "proj_aurelio", "label": "Aurelio AI", "color": "#f59e0b", "desc": "Agente autônomo local sobre Ollama com SQLite"},
    ]

    for p in projects:
        nodes.append({
            "id": p["id"],
            "label": p["label"],
            "type": "project",
            "group": "project",
            "color": p["color"],
            "radius": 14,
            "desc": p["desc"]
        })
        links.append({"source": "second_brain", "target": p["id"], "value": 2})

    # Ligações estratégicas entre Projetos e Repositórios
    project_connections = [
        ("proj_rpa", "repo_docling"),
        ("proj_rpa", "repo_superpowers"),
        ("proj_rpa", "repo_diagram-design"),
        ("proj_rpa", "repo_VoiceStudio"),
        ("proj_wrpe", "repo_paperclip"),
        ("proj_wrpe", "repo_editonny"),
        ("proj_wrpe", "repo_rea"),
        ("proj_aurelio", "repo_claude-mem"),
        ("proj_aurelio", "repo_OmniRoute"),
        ("proj_aurelio", "repo_freellmapi"),
        ("proj_aurelio", "repo_graphify")
    ]

    for src, tgt in project_connections:
        links.append({"source": src, "target": tgt, "value": 1.5, "dashed": True})

    graph_data = {"nodes": nodes, "links": links}
    with open(OUTPUT_GRAPH, "w", encoding="utf-8") as f:
        json.dump(graph_data, f, indent=2, ensure_ascii=False)
    print(f"  [OK] Exportado graph_data.json ({len(nodes)} nós, {len(links)} conexões)")

    # 3. Exporta o Grafo Completo dos Projetos da Máquina
    try:
        from map_user_projects_graph import build_projects_graph, OUTPUT_PATH as PROJ_GRAPH_PATH
        proj_graph = build_projects_graph()
        with open(PROJ_GRAPH_PATH, "w", encoding="utf-8") as f:
            json.dump(proj_graph, f, indent=2, ensure_ascii=False)
        print(f"  [OK] Exportado projects_graph_data.json ({len(proj_graph['nodes'])} nós, {len(proj_graph['links'])} conexões)")
    except Exception as e:
        print(f"  [AVISO] Falha ao exportar projects_graph_data.json: {e}")

    # 4. Atualiza métricas e telemetria diária para o dashboard
    try:
        import usage_metrics
        entries = usage_metrics.load_metrics()
        usage_metrics.export_for_dashboard(entries)
    except Exception as e:
        print(f"  [AVISO] Falha ao exportar telemetria de uso: {e}")


if __name__ == "__main__":
    export_data()
