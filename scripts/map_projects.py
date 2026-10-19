import os
import json
from pathlib import Path

# Directories to ignore
IGNORE_DIRS = {
    ".git", ".vscode", "__pycache__", "venv", "env", "node_modules", 
    "dist", "build", ".pytest_cache", "logs", "dados"
}

# Extensions to include (source code)
INCLUDE_EXTS = {
    ".py", ".js", ".html", ".css", ".json", ".md", ".env", 
    ".txt", ".sql", ".ps1", ".bat", ".yaml", ".yml"
}

def generate_tree(dir_path: Path, prefix: str = "") -> str:
    tree_str = ""
    try:
        entries = sorted(list(dir_path.iterdir()), key=lambda x: (not x.is_dir(), x.name.lower()))
    except PermissionError:
        return ""
        
    entries = [e for e in entries if e.name not in IGNORE_DIRS]
    
    for i, entry in enumerate(entries):
        is_last = (i == len(entries) - 1)
        connector = "└── " if is_last else "├── "
        
        if entry.is_dir():
            tree_str += f"{prefix}{connector}{entry.name}/\n"
            extension = "    " if is_last else "│   "
            tree_str += generate_tree(entry, prefix + extension)
        else:
            if entry.suffix.lower() in INCLUDE_EXTS or entry.name.startswith("."):
                tree_str += f"{prefix}{connector}{entry.name}\n"
    return tree_str

projects = {
    "RPA": {
        "path": Path("C:/Projetos/RPA"),
        "context": Path("C:/Users/USER/.second_brain/projects/rpa_context.md")
    },
    "WRPE_Recorder": {
        "path": Path("C:/Projetos/WRPE_Recorder"),
        "context": Path("C:/Users/USER/.second_brain/projects/wrpe_recorder_context.md")
    },
    "AutomationTest_122844": {
        "path": Path("C:/Projetos/AutomationTest_122844"),
        "context": Path("C:/Users/USER/.second_brain/projects/automationtest_122844_context.md")
    }
}

for name, info in projects.items():
    if info["path"].exists() and info["context"].exists():
        print(f"Mapping {name}...")
        tree = generate_tree(info["path"])
        
        content = info["context"].read_text(encoding="utf-8")
        
        # Remove old tree if it exists to avoid duplication
        if "## Mapa Completo de Arquivos (Source Code)" in content:
            content = content.split("## Mapa Completo de Arquivos (Source Code)")[0].strip() + "\n\n"
            
        tree_section = f"## Mapa Completo de Arquivos (Source Code)\n\n> Mapa gerado automaticamente. Exclui dependências, logs e dados para economizar tokens.\n\n```text\n{info['path'].name}/\n{tree}```\n"
        
        info["context"].write_text(content + "\n\n" + tree_section, encoding="utf-8")
        print(f"Updated {info['context'].name}")

print("Mapping complete!")
