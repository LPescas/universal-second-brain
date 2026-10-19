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

    def test_06_dashboard_clean_and_removed_tabs(self):
        """Validates that Por Projeto, Histórico, and Evolução were completely removed."""
        index_html = os.path.join(BASE_DIR, "frontend", "index.html")
        with open(index_html, "r", encoding="utf-8") as f:
            html = f.read()

        self.assertNotIn("Por Projeto", html)
        self.assertNotIn('data-section="history"', html)
        self.assertNotIn('data-section="evolution"', html)
        self.assertNotIn('id="section-history"', html)
        self.assertNotIn('id="section-evolution"', html)

    def test_07_repos_hub_git_commit_metadata_and_add_box(self):
        """Validates commit date format (dia/mês/ano às horário) and dynamic add box."""
        index_html = os.path.join(BASE_DIR, "frontend", "index.html")
        with open(index_html, "r", encoding="utf-8") as f:
            html = f.read()

        self.assertIn("add-repo-box", html)
        self.assertIn("new-repo-url", html)
        self.assertIn("add-repo-btn", html)

        repos_data_path = os.path.join(BASE_DIR, "frontend", "repos_data.json")
        with open(repos_data_path, "r", encoding="utf-8") as f:
            repos = json.load(f)

        self.assertGreaterEqual(len(repos), 25)
        for r in repos:
            self.assertIn("last_commit_date", r)
            self.assertIn("git_version", r)
            self.assertIn("às", r["last_commit_date"], f"Commit date '{r['last_commit_date']}' must contain 'às'")

    def test_08_knowledge_domains_and_details_api(self):
        """Validates KNOWLEDGE_DOMAINS and user preferences."""
        import server
        self.assertIn("rpa_architecture", server.KNOWLEDGE_DOMAINS)
        self.assertIn("frontend_patterns", server.KNOWLEDGE_DOMAINS)
        self.assertIn("python_patterns", server.KNOWLEDGE_DOMAINS)
        self.assertIn("user_preferences", server.KNOWLEDGE_DOMAINS)

        rpa = server.KNOWLEDGE_DOMAINS["rpa_architecture"]
        self.assertGreaterEqual(len(rpa["rules"]), 5)
        self.assertIn("user_preferences", rpa)
        self.assertIn("linguagem_preferida", rpa["user_preferences"])

    def test_09_aurelio_ai_personas_and_visibility(self):
        """Validates Aurelio AI persona selector, mind banner, and fixed visibility."""
        index_html = os.path.join(BASE_DIR, "frontend", "index.html")
        with open(index_html, "r", encoding="utf-8") as f:
            html = f.read()

        self.assertIn("aurelio-persona-select", html)
        self.assertIn("aurelio-mind-banner", html)
        self.assertNotIn('id="section-aurelio" class="section" style="display: none', html, "Aurelio must NOT have inline display: none")

        backend_aurelio = os.path.join(BASE_DIR, "backend", "aurelio")
        if backend_aurelio not in sys.path:
            sys.path.insert(0, backend_aurelio)
        from agent import agent
        self.assertIn("aurelio_master", agent.PERSONAS_DEFINITIONS)
        self.assertIn("frontend_specialist", agent.PERSONAS_DEFINITIONS)
        self.assertIn("rpa_specialist", agent.PERSONAS_DEFINITIONS)
        self.assertIn("zero_trust_guardian", agent.PERSONAS_DEFINITIONS)
        self.assertGreaterEqual(len(agent.PERSONAS_DEFINITIONS), 8)


if __name__ == "__main__":
    unittest.main()
