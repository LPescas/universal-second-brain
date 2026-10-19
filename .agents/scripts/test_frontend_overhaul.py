# -*- coding: utf-8 -*-
"""
Empirical Test Suite: Frontend Overhaul & Aurelio AI Integration
Validates real telemetry, project topology graphs, and Ollama/Aurelio endpoints.
"""

import os
import sys
import json
import unittest

# Ensure repo root is on sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)


class TestFrontendOverhaul(unittest.TestCase):

    def test_01_system_census(self):
        """Validates that system census counts real skills, agents, workflows and repos."""
        import usage_metrics
        census = usage_metrics.get_system_census()
        self.assertIn("skills_count", census)
        self.assertIn("agents_count", census)
        self.assertIn("workflows_count", census)
        self.assertIn("repos_count", census)

        self.assertGreaterEqual(census["skills_count"], 45, "Should have at least 45 skills mapped")
        self.assertGreaterEqual(census["agents_count"], 15, "Should have at least 15 agents mapped")
        self.assertGreaterEqual(census["workflows_count"], 10, "Should have at least 10 workflows mapped")
        self.assertEqual(census["repos_count"], 25, "Should have exactly 25 repositories in hub")

    def test_02_daily_timeline(self):
        """Validates daily aggregation timeline."""
        import usage_metrics
        entries = usage_metrics.load_metrics()
        timeline = usage_metrics.compute_daily_timeline(entries)
        self.assertIsInstance(timeline, list)
        if entries:
            self.assertGreater(len(timeline), 0)
            self.assertIn("date", timeline[-1])
            self.assertIn("total_tokens", timeline[-1])
            self.assertIn("interactions", timeline[-1])

    def test_03_projects_graph_data(self):
        """Validates topology generation for machine user projects."""
        graph_path = os.path.join(BASE_DIR, "frontend", "projects_graph_data.json")
        self.assertTrue(os.path.exists(graph_path), "projects_graph_data.json must exist")

        with open(graph_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIn("nodes", data)
        self.assertIn("links", data)
        self.assertGreaterEqual(len(data["nodes"]), 20, "Should have at least 20 nodes mapped")
        self.assertGreaterEqual(len(data["links"]), 25, "Should have at least 25 links mapped")

        # Verify key project nodes exist
        node_ids = {n["id"] for n in data["nodes"]}
        for expected_id in ["workspace_root", "proj_rpa", "proj_wrpe", "proj_aurelio", "proj_sb"]:
            self.assertIn(expected_id, node_ids, f"Node {expected_id} must be in graph")

    def test_04_server_routes_and_recommendations(self):
        """Validates server handler logic and Aurelio skill recommendation triggers."""
        import server
        
        # Test SKILLS_TRIGGERS
        skills_sug, repos_sug = server.identificar_skills_e_ferramentas("como fazer o design de uma interface frontend bonita?")
        skill_names = [r["skill"] for r in skills_sug if "skill" in r]
        self.assertIn("frontend-design", skill_names)

        skills_sug2, repos_sug2 = server.identificar_skills_e_ferramentas("preciso arrumar a automação do robô rpa e faturamento")
        repo_names = [r["repo"] for r in repos_sug2 if "repo" in r]
        self.assertIn("rpa", repo_names)

    def test_05_frontend_files_integrity(self):
        """Validates HTML, CSS, and JS integration elements."""
        index_html = os.path.join(BASE_DIR, "frontend", "index.html")
        style_css = os.path.join(BASE_DIR, "frontend", "style.css")
        app_js = os.path.join(BASE_DIR, "frontend", "app.js")

        with open(index_html, "r", encoding="utf-8") as f:
            html = f.read()
        self.assertIn("val-tokens-today", html)
        self.assertIn("val-census", html)
        self.assertIn("graph-view-projects", html)
        self.assertIn("aurelio-model-select", html)

        with open(style_css, "r", encoding="utf-8") as f:
            css = f.read()
        self.assertIn(".graph-view-pill-group", css)
        self.assertIn(".timeline-mode-toggle", css)
        self.assertIn(".aurelio-chat-header", css)

        with open(app_js, "r", encoding="utf-8") as f:
            js = f.read()
        self.assertIn("projects_graph_data.json", js)
        self.assertIn("initAurelioChat", js)
        self.assertIn("checkOllamaStatus", js)


if __name__ == "__main__":
    unittest.main()
