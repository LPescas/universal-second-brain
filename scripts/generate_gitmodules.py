#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_gitmodules.py -- Generates .gitmodules file from repos_manifest.yaml
"""
import yaml
from pathlib import Path

def main():
    sb_root = Path(__file__).resolve().parent.parent
    manifest_path = sb_root / "repos" / "repos_manifest.yaml"
    with manifest_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    lines = []
    for repo in data.get("repositories", []):
        submodule_path = f"repos/{repo['local_path'].replace(chr(92), '/')}"
        url = repo["url"]
        if not url.endswith(".git"):
            url += ".git"
        lines.append(f'[submodule "{submodule_path}"]')
        lines.append(f'\tpath = {submodule_path}')
        lines.append(f'\turl = {url}')

    gitmodules_path = sb_root / ".gitmodules"
    gitmodules_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated {gitmodules_path} with {len(data.get('repositories', []))} submodules.")

if __name__ == "__main__":
    main()
