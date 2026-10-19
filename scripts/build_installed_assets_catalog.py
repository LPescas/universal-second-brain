#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_installed_assets_catalog.py -- Gerador do Catálogo Mestre de Assets do Second Brain
========================================================================================
Varre e indexa todas as skills, agentes, workflows e repositórios instalados no
Second Brain, gerando `C:\\Users\\USER\\.second_brain\\knowledge\\installed_assets_catalog.md`.
"""
import io
import re
import sys
from pathlib import Path
import yaml

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SB_ROOT = Path(r"C:\Users\USER\.second_brain")
AGENTS_ROOT = SB_ROOT / ".agents"
KNOWLEDGE_ROOT = SB_ROOT / "knowledge"
REPOS_ROOT = SB_ROOT / "repos"
OUTPUT_FILE = KNOWLEDGE_ROOT / "installed_assets_catalog.md"


def extract_frontmatter(file_path: Path) -> dict:
    try:
        content = file_path.read_text(encoding="utf-8", errors="replace")
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if match:
            fm_text = match.group(1)
            return yaml.safe_load(fm_text) or {}
    except Exception:
        pass
    return {}


def scan_skills() -> list:
    skills = []
    skills_dir = AGENTS_ROOT / "skills"
    if skills_dir.exists():
        for skill_folder in sorted(skills_dir.iterdir()):
            if skill_folder.is_dir():
                skill_md = skill_folder / "SKILL.md"
                if skill_md.exists():
                    fm = extract_frontmatter(skill_md)
                    name = fm.get("name", skill_folder.name)
                    desc = fm.get("description", "Sem descrição")
                    skills.append({
                        "name": name,
                        "path": f".agents/skills/{skill_folder.name}/SKILL.md",
                        "description": desc.strip().replace("\n", " ")
                    })
    return skills


def scan_agents() -> list:
    agents = []
    agent_dir = AGENTS_ROOT / "agent"
    if agent_dir.exists():
        for agent_file in sorted(agent_dir.glob("*.md")):
            fm = extract_frontmatter(agent_file)
            name = fm.get("name", agent_file.stem)
            desc = fm.get("description", "Especialista do ecossistema .agents")
            skills = fm.get("skills", [])
            agents.append({
                "name": name,
                "file": agent_file.name,
                "description": desc.strip().replace("\n", " ") if isinstance(desc, str) else str(desc),
                "skills": skills if isinstance(skills, list) else [skills]
            })
    return agents


def scan_workflows() -> list:
    workflows = []
    wf_dir = AGENTS_ROOT / "workflows"
    if wf_dir.exists():
        for wf_file in sorted(wf_dir.glob("*.md")):
            fm = extract_frontmatter(wf_file)
            cmd = f"/{wf_file.stem}"
            desc = fm.get("description", f"Workflow {cmd}")
            workflows.append({
                "command": cmd,
                "file": wf_file.name,
                "description": desc.strip().replace("\n", " ") if isinstance(desc, str) else str(desc)
            })
    return workflows


def scan_repos() -> list:
    manifest_file = REPOS_ROOT / "repos_manifest.yaml"
    repos = []
    if manifest_file.exists():
        try:
            with open(manifest_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                repos = data.get("repositories", [])
        except Exception:
            pass
    return repos


def main():
    print("Catalogando assets do Second Brain...")
    skills = scan_skills()
    agents = scan_agents()
    workflows = scan_workflows()
    repos = scan_repos()

    lines = [
        "# 📚 Catálogo Geral de Recursos do Second Brain (Master Assets Catalog)",
        "",
        "> **Última Atualização:** Automática via `build_installed_assets_catalog.py`  ",
        "> **Propósito:** Ponto único de descoberta de ferramentas, agentes, skills e repositórios para redução de tokens e reutilização inteligente.",
        "",
        "---",
        "",
        f"## 📊 Sumário Executivo de Ativos",
        f"- **Repositórios Especializados:** {len(repos)} repositórios (Cold Snapshot integrado)",
        f"- **Agentes Especialistas:** {len(agents)} personas ativas em `.agents/agent/`",
        f"- **Skills Operacionais:** {len(skills)} manuais e rotinas em `.agents/skills/`",
        f"- **Workflows de Comando:** {len(workflows)} atalhos em `.agents/workflows/`",
        "",
        "---",
        "",
        "## 🗂️ 1. Repositórios Especializados Integrados (Hub Local)",
        "",
        "| Repositório | Categoria | Localização Local | Status | Propósito Principal |",
        "| :--- | :--- | :--- | :---: | :--- |"
    ]

    for r in repos:
        name = r.get("name", "")
        cat = r.get("category", "")
        loc = r.get("local_path", "")
        stat = r.get("status", "OK")
        desc = r.get("description", "").replace("\n", " ")
        lines.append(f"| **{name}** | `{cat}` | `repos/{loc}` | `{stat}` | {desc} |")

    lines.extend([
        "",
        "---",
        "",
        "## 🤖 2. Agentes de IA Especialistas (`.agents/agent/`)",
        "",
        "| Agente | Arquivo | Habilidades Associadas | Missão Central |",
        "| :--- | :--- | :--- | :--- |"
    ])

    for a in agents:
        name = a.get("name", "")
        file = a.get("file", "")
        skills_str = ", ".join(f"`{s}`" for s in a.get("skills", [])[:3])
        if len(a.get("skills", [])) > 3:
            skills_str += f" (+{len(a.get('skills', [])) - 3})"
        desc = a.get("description", "")
        lines.append(f"| **@{name}** | `{file}` | {skills_str} | {desc} |")

    lines.extend([
        "",
        "---",
        "",
        "## ⚡ 3. Workflows de Comando (`.agents/workflows/`)",
        "",
        "| Comando | Arquivo | Aplicação / Quando Usar |",
        "| :--- | :--- | :--- |"
    ])

    for w in workflows:
        cmd = w.get("command", "")
        file = w.get("file", "")
        desc = w.get("description", "")
        lines.append(f"| **`{cmd}`** | `{file}` | {desc} |")

    lines.extend([
        "",
        "---",
        "",
        "## 🛠️ 4. Skills e Manuais de Engenharia (`.agents/skills/`)",
        "",
        "| Skill | Arquivo | Escopo de Aplicação |",
        "| :--- | :--- | :--- |"
    ])

    for s in skills:
        name = s.get("name", "")
        p = s.get("path", "")
        desc = s.get("description", "")
        lines.append(f"| **`@{name}`** | `{p}` | {desc} |")

    lines.extend([
        "",
        "---",
        "",
        "## 🔄 5. Diretriz de Consulta Mandatória",
        "Sempre que qualquer agente receber uma tarefa:",
        "1. Consulte este catálogo antes de propor novas implementações ou pesquisar na web.",
        "2. Identifique se já existe um repositório, agente ou skill pronto para resolver a demanda.",
        "3. Emita a confirmação de uso da ferramenta para garantir economia máxima de tokens."
    ])

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Catálogo mestre gerado em: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
