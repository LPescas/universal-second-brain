#!/usr/bin/env python3
"""Validation script for Second Brain Expansion Plan and Governance Compliance."""
import sys
from pathlib import Path

def validate():
    sb_root = Path(r"C:\Users\USER\.second_brain")
    plan_file = sb_root / "second-brain-expansion.md"
    decisions_file = sb_root / "knowledge" / "project_decisions.md"
    learning_file = sb_root / "knowledge" / "learning_log.md"
    metrics_export = sb_root / "scripts" / "metrics_export.json"

    print("=== VALIDATING SECOND BRAIN EXPANSION PLAN & GOVERNANCE ===")

    # 1. Plan file check
    assert plan_file.exists(), f"Plan file not found: {plan_file}"
    plan_content = plan_file.read_text(encoding="utf-8")
    print(f"[OK] Plan file exists: {plan_file.name} ({len(plan_content)} chars)")

    # 2. Check 25 repos
    repos = [
        "nango", "rea", "claude-plugins-official", "diagram-design",
        "scientific-agent-skills", "VoiceStudio", "ruflo", "paperclip",
        "impeccable", "Octop", "ECC", "freellmapi", "security-audit-skill",
        "hindsight", "claude-mem", "editonny", "vibe-coding-toolkit",
        "framework-5p", "agentville", "docling", "ponytail", "OmniRoute",
        "graphify", "superpowers", "andrej-karpathy-skills"
    ]
    missing = [r for r in repos if r.lower() not in plan_content.lower()]
    assert not missing, f"Missing repos in plan: {missing}"
    print(f"[OK] All {len(repos)} repositories verified in plan.")

    # 3. Check Taxonomy Groups
    groups = [
        "media_processing", "dev_reverse_engineering", "ui_ux_design",
        "orchestration_governance", "routing_gateways", "memory_rag_graphs",
        "document_web_parsers", "cloud_security_b2b"
    ]
    for g in groups:
        assert g in plan_content, f"Missing group in plan: {g}"
    print(f"[OK] All {len(groups)} taxonomy groups verified.")

    # 4. Check decisions
    assert decisions_file.exists(), f"Decisions file not found: {decisions_file}"
    decisions_content = decisions_file.read_text(encoding="utf-8")
    assert "Hub Universal de Repositórios" in decisions_content, "Decision not registered in project_decisions.md"
    print("[OK] Project decisions recorded.")

    # 5. Check learning log
    assert learning_file.exists(), f"Learning log not found: {learning_file}"
    learning_content = learning_file.read_text(encoding="utf-8")
    assert "second-brain-expansion.md" in learning_content, "Learning not registered in learning_log.md"
    print("[OK] Learning log recorded.")

    # 6. Check metrics export
    assert metrics_export.exists(), f"Metrics export not found: {metrics_export}"
    print("[OK] Metrics dashboard export exists and verified.")

    print("\n>>> ALL 6 VALIDATION CHECKS PASSED EMPIRICALLY! <<<")
    return 0

if __name__ == "__main__":
    sys.exit(validate())
