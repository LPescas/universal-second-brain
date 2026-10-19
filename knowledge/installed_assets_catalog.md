# 📚 Catálogo Geral de Recursos do Second Brain (Master Assets Catalog)

> **Última Atualização:** Automática via `build_installed_assets_catalog.py`  
> **Propósito:** Ponto único de descoberta de ferramentas, agentes, skills e repositórios para redução de tokens e reutilização inteligente.

---

## 📊 Sumário Executivo de Ativos
- **Repositórios Especializados:** 25 repositórios (Cold Snapshot integrado)
- **Agentes Especialistas:** 20 personas ativas em `.agents/agent/`
- **Skills Operacionais:** 47 manuais e rotinas em `.agents/skills/`
- **Workflows de Comando:** 13 atalhos em `.agents/workflows/`

---

## 🗂️ 1. Repositórios Especializados Integrados (Hub Local)

| Repositório | Categoria | Localização Local | Status | Propósito Principal |
| :--- | :--- | :--- | :---: | :--- |
| **VoiceStudio** | `media_processing` | `repos/media_processing/VoiceStudio` | `OK` | Síntese TTS, clonagem vocal e estúdio de processamento de áudio com IA |
| **editonny** | `media_processing` | `repos/media_processing/editonny` | `OK` | Edição automatizada de vídeo e imagem com IA |
| **diagram-design** | `media_processing` | `repos/media_processing/diagram-design` | `OK` | Padronização e blueprints de diagramas visuais e ASCII para documentação técnica |
| **paperclip** | `media_processing` | `repos/media_processing/paperclip` | `OK` | Extração visual e conversão de designs/telas para código fonte |
| **rea** | `dev_reverse_engineering` | `repos/dev_reverse_engineering/rea` | `OK` | Engenharia reversa, análise de binários e descompilação assistida por LLM |
| **ECC** | `dev_reverse_engineering` | `repos/dev_reverse_engineering/ECC` | `OK` | Everything Claude Code — coletânea de prompts, workflows e ferramentas CLI para Claude |
| **vibe-coding-toolkit** | `dev_reverse_engineering` | `repos/dev_reverse_engineering/vibe-coding-toolkit` | `OK` | Boilerplates ultra-rápidos e snippets de prototipagem ágil para qualquer stack |
| **andrej-karpathy-skills** | `dev_reverse_engineering` | `repos/dev_reverse_engineering/andrej-karpathy-skills` | `OK` | Princípios de Deep Learning, nanoGPT e boas práticas de ML por Andrej Karpathy |
| **superpowers** | `dev_reverse_engineering` | `repos/dev_reverse_engineering/superpowers` | `OK` | Habilidades mestras de TDD rigoroso, debugging sistemático e desenvolvimento disciplinado |
| **impeccable** | `ui_ux_design` | `repos/ui_ux_design/impeccable` | `OK` | Princípios anti-slop de design de interfaces — micro-interações, tipografia e acabamento premium |
| **ruflo** | `orchestration_governance` | `repos/orchestration_governance/ruflo` | `OK` | Runtime de orquestração multi-agente de alta velocidade com suporte a workflows paralelos |
| **agentville** | `orchestration_governance` | `repos/orchestration_governance/agentville` | `OK` | Ambiente de simulação e colaboração entre agentes de IA especializados |
| **framework-5p** | `orchestration_governance` | `repos/orchestration_governance/framework-5p` | `OK` | Metodologia dos 5Ps para estruturação e governança de projetos e negócios |
| **claude-plugins-official** | `orchestration_governance` | `repos/orchestration_governance/claude-plugins-official` | `OK` | Catálogo oficial de extensões e plugins da Anthropic para Claude Code e Claude.ai |
| **OmniRoute** | `routing_gateways` | `repos/routing_gateways/OmniRoute` | `OK` | Roteador inteligente de LLMs com fallback automático, balanceamento e custo zero |
| **freellmapi** | `routing_gateways` | `repos/routing_gateways/freellmapi` | `OK` | Gateway agregador de provedores de LLMs gratuitos com API compatível com OpenAI |
| **claude-mem** | `memory_rag_graphs` | `repos/memory_rag_graphs/claude-mem` | `OK` | Sistema de memória contínua cross-session para agentes de IA com persistência em arquivos |
| **hindsight** | `memory_rag_graphs` | `repos/memory_rag_graphs/hindsight` | `OK` | Avaliação reflexiva de contexto RAG e memória adaptativa pós-execução |
| **graphify** | `memory_rag_graphs` | `repos/memory_rag_graphs/graphify` | `OK` | Converte código, documentos e repositórios em Grafos de Conhecimento relacionais |
| **docling** | `document_web_parsers` | `repos/document_web_parsers/docling` | `OK` | Extrator e parser multimodal ultra-acurado de PDF, Word, Excel e tabelas para Markdown |
| **ponytail** | `document_web_parsers` | `repos/document_web_parsers/ponytail` | `OK` | Scraper web headless ultrarrápido sem overhead de navegador completo |
| **scientific-agent-skills** | `document_web_parsers` | `repos/document_web_parsers/scientific-agent-skills` | `OK` | Skills especializadas para pesquisa científica, cálculos, leitura de artigos e dados acadêmicos |
| **security-audit-skill** | `cloud_security_b2b` | `repos/cloud_security_b2b/security-audit-skill` | `OK` | Skill oficial Cloudflare para auditoria de vulnerabilidades OWASP e postura de segurança |
| **Octop** | `cloud_security_b2b` | `repos/cloud_security_b2b/Octop` | `OK` | Gestão e automação de infraestrutura multi-cloud unificada da Tencent Cloud |
| **nango** | `cloud_security_b2b` | `repos/cloud_security_b2b/nango` | `OK` | Conector unificado para 250+ integrações SaaS com suporte a OAuth, webhooks e sincronização |

---

## 🤖 2. Agentes de IA Especialistas (`.agents/agent/`)

| Agente | Arquivo | Habilidades Associadas | Missão Central |
| :--- | :--- | :--- | :--- |
| **@backend-specialist** | `backend-specialist.md` | `clean-code, nodejs-best-practices, python-patterns, api-patterns, database-design, mcp-builder, lint-and-validate, powershell-windows, bash-linux, rust-pro` | Expert backend architect for Node.js, Python, and modern serverless/edge systems. Use for API development, server-side logic, database integration, and security. Triggers on backend, server, api, endpoint, database, auth. |
| **@code-archaeologist** | `code-archaeologist.md` | `clean-code, simplify-code, code-review-checklist` | Expert in legacy code, refactoring, and understanding undocumented systems. Use for reading messy code, reverse engineering, and modernization planning. Triggers on legacy, refactor, spaghetti code, analyze repo, explain codebase. |
| **@database-architect** | `database-architect.md` | `clean-code, database-design` | Expert database architect for schema design, query optimization, migrations, and modern serverless databases. Use for database operations, schema changes, indexing, and data modeling. Triggers on database, sql, schema, migration, query, postgres, index, table. |
| **@debugger** | `debugger.md` | `clean-code, systematic-debugging` | Expert in systematic debugging, root cause analysis, and crash investigation. Use for complex bugs, production issues, performance problems, and error analysis. Triggers on bug, error, crash, not working, broken, investigate, fix. |
| **@devops-engineer** | `devops-engineer.md` | `clean-code, deployment-procedures, server-management, powershell-windows, bash-linux` | Expert in deployment, server management, CI/CD, and production operations. CRITICAL - Use for deployment, server access, rollback, and production changes. HIGH RISK operations. Triggers on deploy, production, server, pm2, ssh, release, rollback, ci/cd. |
| **@documentation-writer** | `documentation-writer.md` | `clean-code, documentation-templates` | Expert in technical documentation. Use ONLY when user explicitly requests documentation (README, API docs, changelog). DO NOT auto-invoke during normal development. |
| **@explorer-agent** | `explorer-agent.md` | `clean-code, architecture, plan-writing, brainstorming, systematic-debugging` | Advanced codebase discovery, deep architectural analysis, and proactive research agent. The eyes and ears of the framework. Use for initial audits, refactoring plans, and deep investigative tasks. |
| **@frontend-specialist** | `frontend-specialist.md` | `clean-code, design-spec, nextjs-react-expert, frontend-architecture, web-design-guidelines, tailwind-patterns, frontend-design, lint-and-validate` | Senior Frontend Architect who builds maintainable React/Next.js systems with performance-first mindset. Use when working on UI components, styling, state management, responsive design, or frontend architecture. Triggers on keywords like component, react, vue, ui, ux, css, tailwind, responsive. |
| **@game-developer** | `game-developer.md` | `clean-code, game-development` | Game development across all platforms (PC, Web, Mobile, VR/AR). Use when building games with Unity, Godot, Unreal, Phaser, Three.js, or any game engine. Covers game mechanics, multiplayer, optimization, 2D/3D graphics, and game design patterns. |
| **@mobile-developer** | `mobile-developer.md` | `clean-code, design-spec, mobile-design` | Expert in React Native and Flutter mobile development. Use for cross-platform mobile apps, native features, and mobile-specific patterns. Triggers on mobile, react native, flutter, ios, android, app store, expo. |
| **@orchestrator** | `orchestrator.md` | `clean-code, parallel-agents, behavioral-modes, plan-writing, brainstorming, architecture, lint-and-validate, powershell-windows, bash-linux, coordinator-mode, memory-system, context-compression, verify-changes` | Multi-agent coordination and task orchestration with coordinator mode. Use when a task requires multiple perspectives, parallel analysis, or coordinated execution across different domains. Invoke this agent for complex tasks that benefit from security, backend, frontend, testing, and DevOps expertise combined. |
| **@penetration-tester** | `penetration-tester.md` | `clean-code, vulnerability-scanner, red-team-tactics, api-patterns` | Expert in offensive security, penetration testing, red team operations, and vulnerability exploitation. Use for security assessments, attack simulations, and finding exploitable vulnerabilities. Triggers on pentest, exploit, attack, hack, breach, pwn, redteam, offensive. |
| **@performance-optimizer** | `performance-optimizer.md` | `clean-code, performance-profiling` | Expert in performance optimization, profiling, Core Web Vitals, and bundle optimization. Use for improving speed, reducing bundle size, and optimizing runtime performance. Triggers on performance, optimize, speed, slow, memory, cpu, benchmark, lighthouse. |
| **@product-manager** | `product-manager.md` | `plan-writing, brainstorming, clean-code` | Expert in product requirements, user stories, and acceptance criteria. Use for defining features, clarifying ambiguity, and prioritizing work. Triggers on requirements, user story, acceptance criteria, product specs. |
| **@product-owner** | `product-owner.md` | `plan-writing, brainstorming, clean-code` | Strategic facilitator bridging business needs and technical execution. Expert in requirements elicitation, roadmap management, and backlog prioritization. Triggers on requirements, user story, backlog, MVP, PRD, stakeholder. |
| **@project-planner** | `project-planner.md` | `clean-code, app-builder, plan-writing, brainstorming` | Smart project planning agent. Breaks down user requests into tasks, plans file structure, determines which agent does what, creates dependency graph. Use when starting new projects or planning major features. |
| **@qa-automation-engineer** | `qa-automation-engineer.md` | `webapp-testing, testing-patterns, web-design-guidelines, clean-code, lint-and-validate` | Specialist in test automation infrastructure and E2E testing. Focuses on Playwright, Cypress, CI pipelines, and breaking the system. Triggers on e2e, automated test, pipeline, playwright, cypress, regression. |
| **@security-auditor** | `security-auditor.md` | `clean-code, vulnerability-scanner, red-team-tactics, api-patterns` | Elite cybersecurity expert. Think like an attacker, defend like an expert. OWASP 2025, supply chain security, zero trust architecture. Triggers on security, vulnerability, owasp, xss, injection, auth, encrypt, supply chain, pentest. |
| **@seo-specialist** | `seo-specialist.md` | `clean-code, seo-fundamentals, geo-fundamentals` | SEO and GEO (Generative Engine Optimization) expert. Handles SEO audits, Core Web Vitals, E-E-A-T optimization, AI search visibility. Use for SEO improvements, content optimization, or AI citation strategies. |
| **@test-engineer** | `test-engineer.md` | `clean-code, testing-patterns, tdd-workflow, webapp-testing, code-review-checklist, lint-and-validate` | Expert in testing, TDD, and test automation. Use for writing tests, improving coverage, debugging test failures. Triggers on test, spec, coverage, jest, pytest, playwright, e2e, unit test. |

---

## ⚡ 3. Workflows de Comando (`.agents/workflows/`)

| Comando | Arquivo | Aplicação / Quando Usar |
| :--- | :--- | :--- |
| **`/brainstorm`** | `brainstorm.md` | Structured brainstorming for projects and features. Explores multiple options before implementation. |
| **`/coordinate`** | `coordinate.md` | Advanced multi-agent coordination with parallel dispatch and synthesis. Use for complex tasks requiring multiple specialist perspectives. |
| **`/create`** | `create.md` | Create new application command. Triggers App Builder skill and starts interactive dialogue with user. |
| **`/debug`** | `debug.md` | Debugging command. Activates DEBUG mode for systematic problem investigation. |
| **`/deploy`** | `deploy.md` | Deployment command for production releases. Pre-flight checks and deployment execution. |
| **`/enhance`** | `enhance.md` | Add or update features in existing application. Used for iterative development. |
| **`/orchestrate`** | `orchestrate.md` | Coordinate multiple agents for complex tasks. Use for multi-perspective analysis, comprehensive reviews, or tasks requiring different domain expertise. |
| **`/plan`** | `plan.md` | Create project plan using project-planner agent. No code writing - only plan file generation. |
| **`/preview`** | `preview.md` | Preview server start, stop, and status check. Local development server management. |
| **`/remember`** | `remember.md` | Save information to persistent memory for cross-session recall. Stores preferences, conventions, decisions, and context. |
| **`/status`** | `status.md` | Display agent and project status. Progress tracking and status board. |
| **`/test`** | `test.md` | Test generation and test running command. Creates and executes tests for code. |
| **`/verify`** | `verify.md` | Verify code changes work by running them. Proves through execution, not just inspection. |

---

## 🛠️ 4. Skills e Manuais de Engenharia (`.agents/skills/`)

| Skill | Arquivo | Escopo de Aplicação |
| :--- | :--- | :--- |
| **`@api-patterns`** | `.agents/skills/api-patterns/SKILL.md` | API design principles and decision-making. REST vs GraphQL vs tRPC selection, response formats, versioning, pagination. |
| **`@app-builder`** | `.agents/skills/app-builder/SKILL.md` | Main application building orchestrator. Creates full-stack applications from natural language requests. Determines project type, selects tech stack, coordinates agents. |
| **`@architecture`** | `.agents/skills/architecture/SKILL.md` | Architectural decision-making framework. Requirements analysis, trade-off evaluation, ADR documentation. Use when making architecture decisions or analyzing system design. |
| **`@bash-linux`** | `.agents/skills/bash-linux/SKILL.md` | Bash/Linux terminal patterns. Critical commands, piping, error handling, scripting. Use when working on macOS or Linux systems. |
| **`@batch-operations`** | `.agents/skills/batch-operations/SKILL.md` | Apply operations across multiple files simultaneously. Pattern-based bulk modifications, search-and-replace across codebases, consistent changes to many files at once. |
| **`@behavioral-modes`** | `.agents/skills/behavioral-modes/SKILL.md` | AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior based on task type. |
| **`@brainstorming`** | `.agents/skills/brainstorming/SKILL.md` | Socratic questioning protocol + user communication. MANDATORY for complex requests, new features, or unclear requirements. Includes progress reporting and error handling. |
| **`@clean-code`** | `.agents/skills/clean-code/SKILL.md` | Pragmatic coding standards - concise, direct, no over-engineering, no unnecessary comments |
| **`@code-review-checklist`** | `.agents/skills/code-review-checklist/SKILL.md` | Code review guidelines covering code quality, security, and best practices. |
| **`@code-review-graph`** | `.agents/skills/code-review-graph/SKILL.md` | Token-efficient code review using Tree-sitter AST graphs and MCP. Cuts AI token usage on large codebases by computing the blast radius of changes instead of reading entire codebases. Uses a SQLite graph database for structural analysis. |
| **`@context-compression`** | `.agents/skills/context-compression/SKILL.md` | Manage and compress conversation context in long sessions. Detect when context is growing large, summarize completed work phases, archive old findings while preserving key decisions. Prevents context degradation. |
| **`@coordinator-mode`** | `.agents/skills/coordinator-mode/SKILL.md` | Advanced multi-agent orchestration with parallel workers, synthesis protocols, and coordinator lifecycle. Use when complex tasks require multiple agents working in parallel with intelligent result synthesis. |
| **`@database-design`** | `.agents/skills/database-design/SKILL.md` | Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases. |
| **`@deployment-procedures`** | `.agents/skills/deployment-procedures/SKILL.md` | Production deployment principles and decision-making. Safe deployment workflows, rollback strategies, and verification. Teaches thinking, not scripts. |
| **`@design-spec`** | `.agents/skills/design-spec/SKILL.md` | How to author a DESIGN.md file — the machine-readable design-token + human-rationale format that must exist before any UI is built. YAML front-matter token schema (colors, typography, spacing, rounded, components), type system, token references, and canonical section order. |
| **`@documentation-templates`** | `.agents/skills/documentation-templates/SKILL.md` | Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation. |
| **`@frontend-architecture`** | `.agents/skills/frontend-architecture/SKILL.md` | How to organize frontend code — separation of concerns (UI / logic / data / type), file responsibility, state tiers, API services, schema validation, and framework conventions for React/Next and Vue. Structural rules, not visual design. |
| **`@frontend-design`** | `.agents/skills/frontend-design/SKILL.md` | Anti-slop frontend design for web UI — landing pages, portfolios, marketing/product sites, and redesigns. Reads the brief, infers the right direction, and ships interfaces that don't look templated. Real design systems when applicable, audit-first on redesigns, strict pre-flight check. NOT for mobile apps. |
| **`@game-development`** | `.agents/skills/game-development/SKILL.md` | Game development orchestrator. Routes to platform-specific skills based on project needs. |
| **`@geo-fundamentals`** | `.agents/skills/geo-fundamentals/SKILL.md` | Generative Engine Optimization for AI search engines (ChatGPT, Claude, Perplexity). |
| **`@i18n-localization`** | `.agents/skills/i18n-localization/SKILL.md` | Internationalization and localization patterns. Detecting hardcoded strings, managing translations, locale files, RTL support. |
| **`@intelligent-routing`** | `.agents/skills/intelligent-routing/SKILL.md` | Automatic agent selection and intelligent task routing. Analyzes user requests and automatically selects the best specialist agent(s) without requiring explicit user mentions. |
| **`@lint-and-validate`** | `.agents/skills/lint-and-validate/SKILL.md` | Automatic quality control, linting, and static analysis procedures. Use after every code modification to ensure syntax correctness and project standards. Triggers on keywords: lint, format, check, validate, types, static analysis. |
| **`@mcp-builder`** | `.agents/skills/mcp-builder/SKILL.md` | MCP (Model Context Protocol) server and client engineering. Protocol design, schemas, transports, extensions, security, and migration. |
| **`@memory-system`** | `.agents/skills/memory-system/SKILL.md` | Persistent cross-session memory management. Enables agents to remember user preferences, project conventions, and past decisions across different sessions using a structured MEMORY.md index and topic files. |
| **`@mobile-design`** | `.agents/skills/mobile-design/SKILL.md` | Mobile-first design thinking and decision-making for iOS and Android apps. Touch interaction, performance patterns, platform conventions. Teaches principles, not fixed values. Use when building React Native, Flutter, or native mobile apps. |
| **`@nextjs-react-expert`** | `.agents/skills/nextjs-react-expert/SKILL.md` | React and Next.js performance optimization from Vercel Engineering. Use when building React components, optimizing performance, eliminating waterfalls, reducing bundle size, reviewing code for performance issues, or implementing server/client-side optimizations. |
| **`@nodejs-best-practices`** | `.agents/skills/nodejs-best-practices/SKILL.md` | Node.js development principles and decision-making. Framework selection, async patterns, security, and architecture. Teaches thinking, not copying. |
| **`@parallel-agents`** | `.agents/skills/parallel-agents/SKILL.md` | Multi-agent orchestration patterns. Use when multiple independent tasks can run with different domain expertise or when comprehensive analysis requires multiple perspectives. |
| **`@performance-profiling`** | `.agents/skills/performance-profiling/SKILL.md` | Performance profiling principles. Measurement, analysis, and optimization techniques. |
| **`@plan-writing`** | `.agents/skills/plan-writing/SKILL.md` | Structured task planning with clear breakdowns, dependencies, and verification criteria. Use when implementing features, refactoring, or any multi-step work. |
| **`@powershell-windows`** | `.agents/skills/powershell-windows/SKILL.md` | PowerShell Windows patterns. Critical pitfalls, operator syntax, error handling. |
| **`@python-patterns`** | `.agents/skills/python-patterns/SKILL.md` | Python development principles and decision-making. Framework selection, async patterns, type hints, project structure. Teaches thinking, not copying. |
| **`@red-team-tactics`** | `.agents/skills/red-team-tactics/SKILL.md` | Red team tactics principles based on MITRE ATT&CK. Attack phases, detection evasion, reporting. |
| **`@rust-pro`** | `.agents/skills/rust-pro/SKILL.md` | Master modern Rust (2024 edition) with async patterns, advanced type system features, and production-ready systems programming. Expert in the current Rust ecosystem including Tokio, axum, and modern crates. Use PROACTIVELY for Rust development, performance optimization, or systems programming. |
| **`@seo-fundamentals`** | `.agents/skills/seo-fundamentals/SKILL.md` | SEO fundamentals, E-E-A-T, Core Web Vitals, and Google algorithm principles. |
| **`@server-management`** | `.agents/skills/server-management/SKILL.md` | Server management principles and decision-making. Process management, monitoring strategy, and scaling decisions. Teaches thinking, not commands. |
| **`@simplify-code`** | `.agents/skills/simplify-code/SKILL.md` | Reduce complexity of over-engineered code. Identify unnecessary abstractions, remove dead code, flatten deep nesting, and simplify logic while preserving behavior. |
| **`@skillify`** | `.agents/skills/skillify/SKILL.md` | Auto-create new skills from repetitive workflows. When you notice yourself doing the same multi-step process repeatedly, extract it into a reusable SKILL.md that any agent can use. |
| **`@systematic-debugging`** | `.agents/skills/systematic-debugging/SKILL.md` | 4-phase systematic debugging methodology with root cause analysis and evidence-based verification. Use when debugging complex issues. |
| **`@tailwind-patterns`** | `.agents/skills/tailwind-patterns/SKILL.md` | Tailwind CSS v4 principles. CSS-first configuration, container queries, modern patterns, design token architecture. |
| **`@tdd-workflow`** | `.agents/skills/tdd-workflow/SKILL.md` | Test-Driven Development workflow principles. RED-GREEN-REFACTOR cycle. |
| **`@testing-patterns`** | `.agents/skills/testing-patterns/SKILL.md` | Testing patterns and principles. Unit, integration, mocking strategies. |
| **`@verify-changes`** | `.agents/skills/verify-changes/SKILL.md` | Prove code works by running it, not just checking it exists. Verification through execution rather than inspection. Use after writing or modifying code to ensure it actually functions correctly. |
| **`@vulnerability-scanner`** | `.agents/skills/vulnerability-scanner/SKILL.md` | Advanced vulnerability analysis principles. OWASP 2025, Supply Chain Security, attack surface mapping, risk prioritization. |
| **`@web-design-guidelines`** | `.agents/skills/web-design-guidelines/SKILL.md` | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practices". |
| **`@webapp-testing`** | `.agents/skills/webapp-testing/SKILL.md` | Web application testing principles. E2E, Playwright, deep audit strategies. |

---

## 🔄 5. Diretriz de Consulta Mandatória
Sempre que qualquer agente receber uma tarefa:
1. Consulte este catálogo antes de propor novas implementações ou pesquisar na web.
2. Identifique se já existe um repositório, agente ou skill pronto para resolver a demanda.
3. Emita a confirmação de uso da ferramenta para garantir economia máxima de tokens.