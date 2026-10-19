#!/usr/bin/env python3
"""
codex-bridge.py — Second Brain Middleware for Codex/OpenAI API

Intercepts every Codex call and prepends Second Brain context (MASTER_INDEX
+ behavioral rules + relevant project/knowledge) before sending.

Usage:
    python codex-bridge.py "refactor the lancamento adapter"
    python codex-bridge.py --domain rpa "add new guia validation"
    python codex-bridge.py --stdin  (reads prompt from stdin)

When Codex CLI is installed:
    The PS profile alias `codex` points here, making injection transparent.
"""

import sys
import json
import argparse
import subprocess
from pathlib import Path
from typing import Optional

import yaml  # pip install pyyaml

BRAIN_ROOT = Path.home() / ".second_brain"
MASTER_INDEX = BRAIN_ROOT / "MASTER_INDEX.yaml"
GLOBAL_RULES = BRAIN_ROOT / "global_rules.md"
BEHAVIOR = BRAIN_ROOT / "behavioral_patterns.yaml"
ENFORCEMENT = BRAIN_ROOT / "active_behavior_rules.yaml"

# Token budget for injected context (compressed)
MAX_INJECTION_CHARS = 3000


def load_file(path: Path, max_chars: int = MAX_INJECTION_CHARS) -> str:
    """Load file content, truncated to max_chars if needed."""
    if not path.exists():
        return f"[NOT FOUND: {path}]"
    content = path.read_text(encoding="utf-8")
    if len(content) > max_chars:
        return content[:max_chars] + f"\n... [truncated at {max_chars} chars]"
    return content


def load_yaml_file(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def detect_domain(prompt: str, index: dict) -> Optional[tuple[str, str]]:
    """
    Match prompt against MASTER_INDEX project domains and knowledge triggers.
    Returns (type, context_path) or None.
    """
    prompt_lower = prompt.lower()

    # Check projects first
    projects = index.get("projects", {})
    for project_name, project_data in projects.items():
        domain_keywords = project_data.get("domain", [])
        for keyword in domain_keywords:
            if keyword in prompt_lower:
                context_path = BRAIN_ROOT / project_data.get("context", "")
                return ("project", str(context_path))

    # Check knowledge domains
    knowledge = index.get("knowledge", {})
    for domain_name, domain_data in knowledge.items():
        triggers = domain_data.get("triggers", [])
        for trigger in triggers:
            if trigger in prompt_lower:
                knowledge_path = BRAIN_ROOT / domain_data.get("file", "")
                return ("knowledge", str(knowledge_path))

    return None


def build_context_injection(prompt: str) -> str:
    """
    Build the Second Brain context block to prepend to the Codex prompt.
    Only loads relevant context (lazy loading).
    """
    index = load_yaml_file(MASTER_INDEX)

    # Always-load section (compressed)
    behavior = load_yaml_file(BEHAVIOR)
    enforcement = load_yaml_file(ENFORCEMENT)

    # Extract critical rules from enforcement (most relevant ones)
    comm_rules = enforcement.get("communication_rules", [])
    code_rules = enforcement.get("code_rules", [])
    governance_rules = enforcement.get("governance_rules", [])

    enforced_summary = "\n".join([
        f"- [{r['id']}] {r['rule']}"
        for r in (comm_rules + code_rules + governance_rules)
        if r.get("enforcement") in ("BLOCK_RESPONSE_IF_VIOLATED", "BLOCK_OUTPUT_IF_VIOLATED", "MANDATORY_CHECK")
    ])

    # Detect domain and load specific context
    domain_match = detect_domain(prompt, index)
    domain_context = ""
    if domain_match:
        domain_type, context_path = domain_match
        domain_context = f"\n## Relevant Context ({domain_type})\n{load_file(Path(context_path), max_chars=1500)}"

    # Build code style summary from behavioral_patterns
    code_style = behavior.get("code_style", {})
    py_style = code_style.get("python", {})
    js_style = code_style.get("javascript", {})

    style_block = f"""Python: typing={py_style.get('typing', 'strict')}, print={py_style.get('print_forbidden', True) and 'FORBIDDEN' or 'ok'}, max_line={py_style.get('max_line_length', 120)}
JS: prefer={js_style.get('prefer', 'const')}, semicolons={js_style.get('semicolons', True)}"""

    context_block = f"""# SECOND BRAIN CONTEXT INJECTION
# Generated: {Path(MASTER_INDEX).stat().st_mtime if MASTER_INDEX.exists() else 'unknown'}

## Enforced Rules (non-negotiable)
{enforced_summary}

## Code Style
{style_block}

## Communication
- Respond in PT-BR. Code/variables in English.
- Senior level only. No basic explanations.
- No emoji.
{domain_context}

---
## User Prompt
"""

    return context_block


def run_codex(prompt: str, extra_args: list[str]) -> int:
    """Execute the real Codex CLI with injected context."""
    context = build_context_injection(prompt)
    full_prompt = context + prompt

    # Try to find Codex
    codex_candidates = ["codex-cli", "openai-codex", "codex"]
    codex_cmd = None
    for candidate in codex_candidates:
        result = subprocess.run(["where", candidate], capture_output=True, text=True)
        if result.returncode == 0:
            lines = result.stdout.strip().splitlines()
            # Skip this script itself
            for line in lines:
                if "codex-bridge" not in line:
                    codex_cmd = candidate
                    break

    if not codex_cmd:
        print("[CODEX BRIDGE] Codex CLI not found. Printing injected prompt instead.")
        print("=" * 60)
        print(full_prompt)
        print("=" * 60)
        return 0

    cmd = [codex_cmd] + extra_args + [full_prompt]
    result = subprocess.run(cmd)
    return result.returncode


def main() -> None:
    parser = argparse.ArgumentParser(description="Second Brain Middleware for Codex")
    parser.add_argument("prompt", nargs="?", help="The prompt to send")
    parser.add_argument("--domain", help="Force a specific domain (rpa, recorder, etc.)")
    parser.add_argument("--stdin", action="store_true", help="Read prompt from stdin")
    parser.add_argument("--dry-run", action="store_true", help="Print injected prompt, do not call Codex")
    parser.add_argument("--show-context", action="store_true", help="Print context injection block")
    args, unknown = parser.parse_known_args()

    if args.stdin:
        prompt = sys.stdin.read().strip()
    elif args.prompt:
        prompt = args.prompt
    else:
        parser.print_help()
        sys.exit(1)

    if args.show_context:
        print(build_context_injection(prompt))
        return

    if args.dry_run:
        context = build_context_injection(prompt)
        print(context + prompt)
        return

    sys.exit(run_codex(prompt, unknown))


if __name__ == "__main__":
    main()
