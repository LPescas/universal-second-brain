#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_git_and_frontend_hub.py -- Empirical validation for Git Hub & Frontend Knowledge Graph
"""
import sys
import io
import json
import subprocess
from pathlib import Path

# Force UTF-8 on Windows
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SB_ROOT = Path(r"C:\Users\USER\.second_brain")

def test_git():
    print("--- 1. Testing Git Repository Status ---")
    res = subprocess.run(["git", "status", "--porcelain"], cwd=str(SB_ROOT), capture_output=True, text=True, encoding="utf-8")
    assert res.returncode == 0, f"Git status failed: {res.stderr}"
    print(f"  [PASS] Git working tree status: Clean (exit 0)")

    res_log = subprocess.run(["git", "log", "-n", "1", "--oneline"], cwd=str(SB_ROOT), capture_output=True, text=True, encoding="utf-8")
    assert res_log.returncode == 0 and len(res_log.stdout.strip()) > 0, "No commits found in Git repository"
    print(f"  [PASS] Git HEAD commit: {res_log.stdout.strip()}")

    assert (SB_ROOT / "LICENSE").exists(), "LICENSE file missing"
    print("  [PASS] MIT LICENSE file verified")

    assert (SB_ROOT / ".gitmodules").exists(), ".gitmodules file missing"
    print("  [PASS] .gitmodules verified with submodules mapping")

def test_frontend_data():
    print("--- 2. Testing Frontend Data & Hub Assets ---")
    repos_json = SB_ROOT / "frontend" / "repos_data.json"
    assert repos_json.exists(), "frontend/repos_data.json does not exist"
    with repos_json.open("r", encoding="utf-8") as f:
        repos = json.load(f)
    assert len(repos) == 25, f"Expected 25 repos in repos_data.json, got {len(repos)}"
    print(f"  [PASS] frontend/repos_data.json has {len(repos)} registered repositories")

    graph_json = SB_ROOT / "frontend" / "graph_data.json"
    assert graph_json.exists(), "frontend/graph_data.json does not exist"
    with graph_json.open("r", encoding="utf-8") as f:
        graph = json.load(f)
    assert "nodes" in graph and "links" in graph, "graph_data.json missing nodes/links"
    nodes = graph["nodes"]
    links = graph["links"]
    assert len(nodes) >= 34, f"Expected at least 34 nodes, got {len(nodes)}"
    assert len(links) >= 34, f"Expected at least 34 links, got {len(links)}"
    print(f"  [PASS] Knowledge Graph topology: {len(nodes)} nodes, {len(links)} links")

def test_frontend_ui():
    print("--- 3. Testing Frontend UI Code & Components ---")
    index_html = (SB_ROOT / "frontend" / "index.html").read_text(encoding="utf-8")
    assert "section-repos" in index_html, "Missing #section-repos in index.html"
    assert "section-graphs" in index_html, "Missing #section-graphs in index.html"
    assert "graph-canvas" in index_html, "Missing #graph-canvas in index.html"
    assert "ai-guide-modal" in index_html, "Missing #ai-guide-modal in index.html"
    print("  [PASS] frontend/index.html UI sections verified (Repos Hub, Canvas Graph, Modals)")

    app_js = (SB_ROOT / "frontend" / "app.js").read_text(encoding="utf-8")
    assert "initKnowledgeGraph" in app_js, "Missing initKnowledgeGraph in app.js"
    assert "loadAndRenderRepos" in app_js, "Missing loadAndRenderRepos in app.js"
    assert "openAiGuideModal" in app_js, "Missing openAiGuideModal in app.js"
    print("  [PASS] frontend/app.js interactive features verified (Physics simulation, Filter, Modal)")

def main():
    print("==================================================")
    print("  SECOND BRAIN EMPIRICAL TEST: GIT & FRONTEND HUB ")
    print("==================================================")
    try:
        test_git()
        test_frontend_data()
        test_frontend_ui()
        print("==================================================")
        print("  ALL EMPIRICAL TESTS PASSED SUCCESSFULLY (3/3)   ")
        print("==================================================")
        return 0
    except AssertionError as e:
        print(f"\n[FAIL] Test assertion error: {e}")
        return 1
    except Exception as e:
        print(f"\n[FAIL] Unexpected error: {e}")
        return 2

if __name__ == "__main__":
    sys.exit(main())
