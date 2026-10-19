# Contexto do Projeto: UNIQ Recorder (WRPE)

> Carregamento sob demanda. Ler apenas quando o intent envolve recorder, WRPE, ou gravação.

---

## Visão Geral
Solução de gravação e reprodução de interações web de alta fidelidade. Microsserviço isolado que captura cliques, formulários e navegação, reproduzindo autonomamente via motor híbrido Playwright + Selenium.

## Arquitetura
- **Tipo**: Microsserviço standalone
- **Caminho**: `C:\Projetos\WRPE_Recorder`
- **Entry Point**: `main_uniq_recorder.py`
- **Motor**: Híbrido Playwright + Selenium
- **API**: REST local
- **DB**: SQLite (`uniq_rpa_recorder.db`)
- **Extensão**: Chrome Extension para captura de interações

## Estrutura (6 Pastas Padrão UNIQ)
- `codigo/` — API REST, ORM (SQLAlchemy), Engine de automação
- `documentacao/` — Manual de uso, painel admin HTML
- `dados/` — SQLite local e caches
- `configuracoes/` — .env e parâmetros
- `executaveis/` — Scripts .bat de instalação, extensão Chrome
- `logs/` — Logs de execução, screenshots de falhas

## Regras Críticas
1. Governança Zero-Trust (mesma do RPA): todo subdir tem `*_nome.md`
2. Guardião de Execução em `core/governanca/` valida tudo no boot
3. Sem arquivos Python soltos (exceto `main_uniq_recorder.py`)
4. Sem acentos em nomes de arquivo

## Stack Técnica
Python 3.x, Playwright, Selenium, SQLAlchemy, SQLite, Chrome Extension, HTML/JS

---

## Decisões Técnicas

| Data | Decisão | Motivo |
|------|---------|--------|
| 2026-07-31 | Motor híbrido Playwright + Selenium | Playwright para gravação moderna, Selenium para compatibilidade legada |
| 2026-07-31 | SQLAlchemy como ORM | Abstração de banco sem lock-in de vendor |
| 2026-07-31 | REST API local | Desacoplamento do frontend RPA principal |

## Problemas Conhecidos

| Problema | Solução | Status |
|---------|---------|--------|
| Extensão Chrome requer instalação manual | Script .bat em `executaveis/` | Documentado |

## Pendências / Melhorias Futuras

- [ ] API REST para integração com o painel principal do RPA
- [ ] Upload de gravações para nuvem

---

## Histórico

| Data       | Descrição                                           |
|------------|-----------------------------------------------------|
| 2026-07-31 | Contexto inicial criado para o Second Brain         |
| 2026-08-03 | v2.0: Adicionadas decisões técnicas e pendências    |


## Mapa Completo de Arquivos (Source Code)

> Mapa gerado automaticamente. Exclui dependências, logs e dados para economizar tokens.

```text
WRPE_Recorder/
├── .agent/
│   ├── .shared/
│   │   └── ui-ux-pro-max/
│   │       ├── data/
│   │       │   ├── stacks/
│   │       └── scripts/
│   │           ├── core.py
│   │           ├── design_system.py
│   │           └── search.py
│   ├── agents/
│   │   ├── backend-specialist.md
│   │   ├── code-archaeologist.md
│   │   ├── database-architect.md
│   │   ├── debugger.md
│   │   ├── devops-engineer.md
│   │   ├── documentation-writer.md
│   │   ├── explorer-agent.md
│   │   ├── frontend-specialist.md
│   │   ├── game-developer.md
│   │   ├── mobile-developer.md
│   │   ├── orchestrator.md
│   │   ├── penetration-tester.md
│   │   ├── performance-optimizer.md
│   │   ├── product-manager.md
│   │   ├── product-owner.md
│   │   ├── project-planner.md
│   │   ├── qa-automation-engineer.md
│   │   ├── security-auditor.md
│   │   ├── seo-specialist.md
│   │   └── test-engineer.md
│   ├── rules/
│   │   └── GEMINI.md
│   ├── scripts/
│   │   ├── auto_preview.py
│   │   ├── checklist.py
│   │   ├── session_manager.py
│   │   └── verify_all.py
│   ├── skills/
│   │   ├── api-patterns/
│   │   │   ├── scripts/
│   │   │   │   └── api_validator.py
│   │   │   ├── api-style.md
│   │   │   ├── auth.md
│   │   │   ├── documentation.md
│   │   │   ├── graphql.md
│   │   │   ├── rate-limiting.md
│   │   │   ├── response.md
│   │   │   ├── rest.md
│   │   │   ├── security-testing.md
│   │   │   ├── SKILL.md
│   │   │   ├── trpc.md
│   │   │   └── versioning.md
│   │   ├── app-builder/
│   │   │   ├── templates/
│   │   │   │   ├── astro-static/
│   │   │   │   │   └── TEMPLATE.md
│   │   │   │   ├── chrome-extension/
│   │   │   │   │   └── TEMPLATE.md
│   │   │   │   ├── cli-tool/
│   │   │   │   │   └── TEMPLATE.md
│   │   │   │   ├── electron-desktop/
│   │   │   │   │   └── TEMPLATE.md
│   │   │   │   ├── express-api/
│   │   │   │   │   └── TEMPLATE.md
│   │   │   │   ├── flutter-app/
│   │   │   │   │   └── TEMPLATE.md
│   │   │   │   ├── monorepo-turborepo/
│   │   │   │   │   └── TEMPLATE.md
│   │   │   │   ├── nextjs-fullstack/
│   │   │   │   │   └── TEMPLATE.md
│   │   │   │   ├── nextjs-saas/
│   │   │   │   │   └── TEMPLATE.md
│   │   │   │   ├── nextjs-static/
│   │   │   │   │   └── TEMPLATE.md
│   │   │   │   ├── nuxt-app/
│   │   │   │   │   └── TEMPLATE.md
│   │   │   │   ├── python-fastapi/
│   │   │   │   │   └── TEMPLATE.md
│   │   │   │   ├── react-native-app/
│   │   │   │   │   └── TEMPLATE.md
│   │   │   │   └── SKILL.md
│   │   │   ├── agent-coordination.md
│   │   │   ├── feature-building.md
│   │   │   ├── project-detection.md
│   │   │   ├── scaffolding.md
│   │   │   ├── SKILL.md
│   │   │   └── tech-stack.md
│   │   ├── architecture/
│   │   │   ├── context-discovery.md
│   │   │   ├── examples.md
│   │   │   ├── pattern-selection.md
│   │   │   ├── patterns-reference.md
│   │   │   ├── SKILL.md
│   │   │   └── trade-off-analysis.md
│   │   ├── bash-linux/
│   │   │   └── SKILL.md
│   │   ├── batch-operations/
│   │   │   └── SKILL.md
│   │   ├── behavioral-modes/
│   │   │   └── SKILL.md
│   │   ├── brainstorming/
│   │   │   ├── dynamic-questioning.md
│   │   │   └── SKILL.md
│   │   ├── clean-code/
│   │   │   └── SKILL.md
│   │   ├── code-review-checklist/
│   │   │   └── SKILL.md
│   │   ├── code-review-graph/
│   │   │   └── SKILL.md
│   │   ├── context-compression/
│   │   │   └── SKILL.md
│   │   ├── coordinator-mode/
│   │   │   └── SKILL.md
│   │   ├── database-design/
│   │   │   ├── scripts/
│   │   │   │   └── schema_validator.py
│   │   │   ├── database-selection.md
│   │   │   ├── indexing.md
│   │   │   ├── migrations.md
│   │   │   ├── optimization.md
│   │   │   ├── orm-selection.md
│   │   │   ├── schema-design.md
│   │   │   └── SKILL.md
│   │   ├── deployment-procedures/
│   │   │   └── SKILL.md
│   │   ├── documentation-templates/
│   │   │   └── SKILL.md
│   │   ├── frontend-design/
│   │   │   ├── scripts/
│   │   │   │   ├── accessibility_checker.py
│   │   │   │   └── ux_audit.py
│   │   │   ├── animation-guide.md
│   │   │   ├── color-system.md
│   │   │   ├── decision-trees.md
│   │   │   ├── motion-graphics.md
│   │   │   ├── SKILL.md
│   │   │   ├── typography-system.md
│   │   │   ├── ux-psychology.md
│   │   │   └── visual-effects.md
│   │   ├── game-development/
│   │   │   ├── 2d-games/
│   │   │   │   └── SKILL.md
│   │   │   ├── 3d-games/
│   │   │   │   └── SKILL.md
│   │   │   ├── game-art/
│   │   │   │   └── SKILL.md
│   │   │   ├── game-audio/
│   │   │   │   └── SKILL.md
│   │   │   ├── game-design/
│   │   │   │   └── SKILL.md
│   │   │   ├── mobile-games/
│   │   │   │   └── SKILL.md
│   │   │   ├── multiplayer/
│   │   │   │   └── SKILL.md
│   │   │   ├── pc-games/
│   │   │   │   └── SKILL.md
│   │   │   ├── vr-ar/
│   │   │   │   └── SKILL.md
│   │   │   ├── web-games/
│   │   │   │   └── SKILL.md
│   │   │   └── SKILL.md
│   │   ├── geo-fundamentals/
│   │   │   ├── scripts/
│   │   │   │   └── geo_checker.py
│   │   │   └── SKILL.md
│   │   ├── i18n-localization/
│   │   │   ├── scripts/
│   │   │   │   └── i18n_checker.py
│   │   │   └── SKILL.md
│   │   ├── intelligent-routing/
│   │   │   └── SKILL.md
│   │   ├── lint-and-validate/
│   │   │   ├── scripts/
│   │   │   │   ├── lint_runner.py
│   │   │   │   └── type_coverage.py
│   │   │   └── SKILL.md
│   │   ├── mcp-builder/
│   │   │   └── SKILL.md
│   │   ├── memory-system/
│   │   │   └── SKILL.md
│   │   ├── mobile-design/
│   │   │   ├── scripts/
│   │   │   │   └── mobile_audit.py
│   │   │   ├── decision-trees.md
│   │   │   ├── mobile-backend.md
│   │   │   ├── mobile-color-system.md
│   │   │   ├── mobile-debugging.md
│   │   │   ├── mobile-design-thinking.md
│   │   │   ├── mobile-navigation.md
│   │   │   ├── mobile-performance.md
│   │   │   ├── mobile-testing.md
│   │   │   ├── mobile-typography.md
│   │   │   ├── platform-android.md
│   │   │   ├── platform-ios.md
│   │   │   ├── SKILL.md
│   │   │   └── touch-psychology.md
│   │   ├── nextjs-react-expert/
│   │   │   ├── scripts/
│   │   │   │   ├── convert_rules.py
│   │   │   │   └── react_performance_checker.py
│   │   │   ├── 1-async-eliminating-waterfalls.md
│   │   │   ├── 2-bundle-bundle-size-optimization.md
│   │   │   ├── 3-server-server-side-performance.md
│   │   │   ├── 4-client-client-side-data-fetching.md
│   │   │   ├── 5-rerender-re-render-optimization.md
│   │   │   ├── 6-rendering-rendering-performance.md
│   │   │   ├── 7-js-javascript-performance.md
│   │   │   ├── 8-advanced-advanced-patterns.md
│   │   │   ├── 9-cache-components.md
│   │   │   └── SKILL.md
│   │   ├── nodejs-best-practices/
│   │   │   └── SKILL.md
│   │   ├── parallel-agents/
│   │   │   └── SKILL.md
│   │   ├── performance-profiling/
│   │   │   ├── scripts/
│   │   │   │   └── lighthouse_audit.py
│   │   │   └── SKILL.md
│   │   ├── plan-writing/
│   │   │   └── SKILL.md
│   │   ├── powershell-windows/
│   │   │   └── SKILL.md
│   │   ├── python-patterns/
│   │   │   └── SKILL.md
│   │   ├── red-team-tactics/
│   │   │   └── SKILL.md
│   │   ├── rust-pro/
│   │   │   └── SKILL.md
│   │   ├── seo-fundamentals/
│   │   │   ├── scripts/
│   │   │   │   └── seo_checker.py
│   │   │   └── SKILL.md
│   │   ├── server-management/
│   │   │   └── SKILL.md
│   │   ├── simplify-code/
│   │   │   └── SKILL.md
│   │   ├── skillify/
│   │   │   └── SKILL.md
│   │   ├── systematic-debugging/
│   │   │   └── SKILL.md
│   │   ├── tailwind-patterns/
│   │   │   └── SKILL.md
│   │   ├── tdd-workflow/
│   │   │   └── SKILL.md
│   │   ├── testing-patterns/
│   │   │   ├── scripts/
│   │   │   │   └── test_runner.py
│   │   │   └── SKILL.md
│   │   ├── verify-changes/
│   │   │   └── SKILL.md
│   │   ├── vulnerability-scanner/
│   │   │   ├── scripts/
│   │   │   │   └── security_scan.py
│   │   │   ├── checklists.md
│   │   │   └── SKILL.md
│   │   ├── web-design-guidelines/
│   │   │   └── SKILL.md
│   │   ├── webapp-testing/
│   │   │   ├── scripts/
│   │   │   │   └── playwright_runner.py
│   │   │   └── SKILL.md
│   │   └── doc.md
│   ├── workflows/
│   │   ├── brainstorm.md
│   │   ├── coordinate.md
│   │   ├── create.md
│   │   ├── debug.md
│   │   ├── deploy.md
│   │   ├── enhance.md
│   │   ├── orchestrate.md
│   │   ├── plan.md
│   │   ├── preview.md
│   │   ├── remember.md
│   │   ├── status.md
│   │   ├── test.md
│   │   ├── ui-ux-pro-max.md
│   │   └── verify.md
│   ├── ARCHITECTURE.md
│   └── mcp_config.json
├── .venv/
│   ├── Include/
│   │   └── site/
│   │       └── python3.14/
│   │           └── greenlet/
│   ├── Lib/
│   │   └── site-packages/
│   │       ├── _pytest/
│   │       │   ├── _code/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── code.py
│   │       │   │   └── source.py
│   │       │   ├── _io/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── pprint.py
│   │       │   │   ├── saferepr.py
│   │       │   │   ├── terminalwriter.py
│   │       │   │   └── wcwidth.py
│   │       │   ├── _py/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── error.py
│   │       │   │   └── path.py
│   │       │   ├── assertion/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── rewrite.py
│   │       │   │   ├── truncate.py
│   │       │   │   └── util.py
│   │       │   ├── config/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── argparsing.py
│   │       │   │   ├── compat.py
│   │       │   │   ├── exceptions.py
│   │       │   │   └── findpaths.py
│   │       │   ├── mark/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── expression.py
│   │       │   │   └── structures.py
│   │       │   ├── __init__.py
│   │       │   ├── _argcomplete.py
│   │       │   ├── _version.py
│   │       │   ├── cacheprovider.py
│   │       │   ├── capture.py
│   │       │   ├── compat.py
│   │       │   ├── debugging.py
│   │       │   ├── deprecated.py
│   │       │   ├── doctest.py
│   │       │   ├── faulthandler.py
│   │       │   ├── fixtures.py
│   │       │   ├── freeze_support.py
│   │       │   ├── helpconfig.py
│   │       │   ├── hookspec.py
│   │       │   ├── junitxml.py
│   │       │   ├── legacypath.py
│   │       │   ├── logging.py
│   │       │   ├── main.py
│   │       │   ├── monkeypatch.py
│   │       │   ├── nodes.py
│   │       │   ├── outcomes.py
│   │       │   ├── pastebin.py
│   │       │   ├── pathlib.py
│   │       │   ├── pytester.py
│   │       │   ├── pytester_assertions.py
│   │       │   ├── python.py
│   │       │   ├── python_api.py
│   │       │   ├── raises.py
│   │       │   ├── recwarn.py
│   │       │   ├── reports.py
│   │       │   ├── runner.py
│   │       │   ├── scope.py
│   │       │   ├── setuponly.py
│   │       │   ├── setupplan.py
│   │       │   ├── skipping.py
│   │       │   ├── stash.py
│   │       │   ├── stepwise.py
│   │       │   ├── subtests.py
│   │       │   ├── terminal.py
│   │       │   ├── terminalprogress.py
│   │       │   ├── threadexception.py
│   │       │   ├── timing.py
│   │       │   ├── tmpdir.py
│   │       │   ├── tracemalloc.py
│   │       │   ├── unittest.py
│   │       │   ├── unraisableexception.py
│   │       │   ├── warning_types.py
│   │       │   └── warnings.py
│   │       ├── annotated_doc/
│   │       │   ├── __init__.py
│   │       │   ├── main.py
│   │       ├── annotated_doc-0.0.4.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       ├── annotated_types/
│   │       │   ├── __init__.py
│   │       │   └── test_cases.py
│   │       ├── annotated_types-0.7.0.dist-info/
│   │       │   ├── licenses/
│   │       ├── anyio/
│   │       │   ├── _backends/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _asyncio.py
│   │       │   │   └── _trio.py
│   │       │   ├── _core/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _asyncio_selector_thread.py
│   │       │   │   ├── _contextmanagers.py
│   │       │   │   ├── _eventloop.py
│   │       │   │   ├── _exceptions.py
│   │       │   │   ├── _fileio.py
│   │       │   │   ├── _resources.py
│   │       │   │   ├── _signals.py
│   │       │   │   ├── _sockets.py
│   │       │   │   ├── _streams.py
│   │       │   │   ├── _subprocesses.py
│   │       │   │   ├── _synchronization.py
│   │       │   │   ├── _tasks.py
│   │       │   │   ├── _tempfile.py
│   │       │   │   ├── _testing.py
│   │       │   │   └── _typedattr.py
│   │       │   ├── abc/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _eventloop.py
│   │       │   │   ├── _resources.py
│   │       │   │   ├── _sockets.py
│   │       │   │   ├── _streams.py
│   │       │   │   ├── _subprocesses.py
│   │       │   │   ├── _tasks.py
│   │       │   │   └── _testing.py
│   │       │   ├── streams/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── buffered.py
│   │       │   │   ├── file.py
│   │       │   │   ├── memory.py
│   │       │   │   ├── stapled.py
│   │       │   │   ├── text.py
│   │       │   │   └── tls.py
│   │       │   ├── __init__.py
│   │       │   ├── from_thread.py
│   │       │   ├── functools.py
│   │       │   ├── lowlevel.py
│   │       │   ├── pytest_plugin.py
│   │       │   ├── to_interpreter.py
│   │       │   ├── to_process.py
│   │       │   └── to_thread.py
│   │       ├── anyio-4.13.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       │   ├── top_level.txt
│   │       ├── attr/
│   │       │   ├── __init__.py
│   │       │   ├── _cmp.py
│   │       │   ├── _compat.py
│   │       │   ├── _config.py
│   │       │   ├── _funcs.py
│   │       │   ├── _make.py
│   │       │   ├── _next_gen.py
│   │       │   ├── _version_info.py
│   │       │   ├── converters.py
│   │       │   ├── exceptions.py
│   │       │   ├── filters.py
│   │       │   ├── setters.py
│   │       │   ├── validators.py
│   │       ├── attrs/
│   │       │   ├── __init__.py
│   │       │   ├── converters.py
│   │       │   ├── exceptions.py
│   │       │   ├── filters.py
│   │       │   ├── setters.py
│   │       │   └── validators.py
│   │       ├── attrs-26.1.0.dist-info/
│   │       │   ├── licenses/
│   │       ├── certifi/
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── core.py
│   │       ├── certifi-2026.4.22.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── cffi/
│   │       │   ├── __init__.py
│   │       │   ├── _imp_emulation.py
│   │       │   ├── _shimmed_dist_utils.py
│   │       │   ├── api.py
│   │       │   ├── backend_ctypes.py
│   │       │   ├── cffi_opcode.py
│   │       │   ├── commontypes.py
│   │       │   ├── cparser.py
│   │       │   ├── error.py
│   │       │   ├── ffiplatform.py
│   │       │   ├── lock.py
│   │       │   ├── model.py
│   │       │   ├── pkgconfig.py
│   │       │   ├── recompiler.py
│   │       │   ├── setuptools_ext.py
│   │       │   ├── vengine_cpy.py
│   │       │   ├── vengine_gen.py
│   │       │   └── verifier.py
│   │       ├── cffi-2.0.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       │   ├── top_level.txt
│   │       ├── charset_normalizer/
│   │       │   ├── cli/
│   │       │   │   ├── __init__.py
│   │       │   │   └── __main__.py
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── api.py
│   │       │   ├── cd.py
│   │       │   ├── constant.py
│   │       │   ├── legacy.py
│   │       │   ├── md.py
│   │       │   ├── models.py
│   │       │   ├── utils.py
│   │       │   └── version.py
│   │       ├── charset_normalizer-3.4.7.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       │   ├── top_level.txt
│   │       ├── click/
│   │       │   ├── __init__.py
│   │       │   ├── _compat.py
│   │       │   ├── _termui_impl.py
│   │       │   ├── _textwrap.py
│   │       │   ├── _utils.py
│   │       │   ├── _winconsole.py
│   │       │   ├── core.py
│   │       │   ├── decorators.py
│   │       │   ├── exceptions.py
│   │       │   ├── formatting.py
│   │       │   ├── globals.py
│   │       │   ├── parser.py
│   │       │   ├── shell_completion.py
│   │       │   ├── termui.py
│   │       │   ├── testing.py
│   │       │   ├── types.py
│   │       │   └── utils.py
│   │       ├── click-8.4.0.dist-info/
│   │       │   ├── licenses/
│   │       │   │   └── LICENSE.txt
│   │       ├── colorama/
│   │       │   ├── tests/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── ansi_test.py
│   │       │   │   ├── ansitowin32_test.py
│   │       │   │   ├── initialise_test.py
│   │       │   │   ├── isatty_test.py
│   │       │   │   ├── utils.py
│   │       │   │   └── winterm_test.py
│   │       │   ├── __init__.py
│   │       │   ├── ansi.py
│   │       │   ├── ansitowin32.py
│   │       │   ├── initialise.py
│   │       │   ├── win32.py
│   │       │   └── winterm.py
│   │       ├── colorama-0.4.6.dist-info/
│   │       │   ├── licenses/
│   │       │   │   └── LICENSE.txt
│   │       ├── dotenv/
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── cli.py
│   │       │   ├── ipython.py
│   │       │   ├── main.py
│   │       │   ├── parser.py
│   │       │   ├── variables.py
│   │       │   └── version.py
│   │       ├── fastapi/
│   │       │   ├── .agents/
│   │       │   │   └── skills/
│   │       │   │       └── fastapi/
│   │       │   │           ├── references/
│   │       │   │           │   ├── dependencies.md
│   │       │   │           │   ├── other-tools.md
│   │       │   │           │   └── streaming.md
│   │       │   │           └── SKILL.md
│   │       │   ├── _compat/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── shared.py
│   │       │   │   └── v2.py
│   │       │   ├── dependencies/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── models.py
│   │       │   │   └── utils.py
│   │       │   ├── middleware/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── asyncexitstack.py
│   │       │   │   ├── cors.py
│   │       │   │   ├── gzip.py
│   │       │   │   ├── httpsredirect.py
│   │       │   │   ├── trustedhost.py
│   │       │   │   └── wsgi.py
│   │       │   ├── openapi/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── constants.py
│   │       │   │   ├── docs.py
│   │       │   │   ├── models.py
│   │       │   │   └── utils.py
│   │       │   ├── security/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── api_key.py
│   │       │   │   ├── base.py
│   │       │   │   ├── http.py
│   │       │   │   ├── oauth2.py
│   │       │   │   ├── open_id_connect_url.py
│   │       │   │   └── utils.py
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── applications.py
│   │       │   ├── background.py
│   │       │   ├── cli.py
│   │       │   ├── concurrency.py
│   │       │   ├── datastructures.py
│   │       │   ├── encoders.py
│   │       │   ├── exception_handlers.py
│   │       │   ├── exceptions.py
│   │       │   ├── logger.py
│   │       │   ├── param_functions.py
│   │       │   ├── params.py
│   │       │   ├── requests.py
│   │       │   ├── responses.py
│   │       │   ├── routing.py
│   │       │   ├── sse.py
│   │       │   ├── staticfiles.py
│   │       │   ├── templating.py
│   │       │   ├── testclient.py
│   │       │   ├── types.py
│   │       │   ├── utils.py
│   │       │   └── websockets.py
│   │       ├── fastapi-0.136.1.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       ├── greenlet/
│   │       │   ├── platform/
│   │       │   │   ├── __init__.py
│   │       │   ├── tests/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── fail_clearing_run_switches.py
│   │       │   │   ├── fail_cpp_exception.py
│   │       │   │   ├── fail_initialstub_already_started.py
│   │       │   │   ├── fail_slp_switch.py
│   │       │   │   ├── fail_switch_three_greenlets.py
│   │       │   │   ├── fail_switch_three_greenlets2.py
│   │       │   │   ├── fail_switch_two_greenlets.py
│   │       │   │   ├── leakcheck.py
│   │       │   │   ├── test_contextvars.py
│   │       │   │   ├── test_cpp.py
│   │       │   │   ├── test_extension_interface.py
│   │       │   │   ├── test_gc.py
│   │       │   │   ├── test_generator.py
│   │       │   │   ├── test_generator_nested.py
│   │       │   │   ├── test_greenlet.py
│   │       │   │   ├── test_greenlet_trash.py
│   │       │   │   ├── test_interpreter_shutdown.py
│   │       │   │   ├── test_leaks.py
│   │       │   │   ├── test_stack_saved.py
│   │       │   │   ├── test_throw.py
│   │       │   │   ├── test_tracing.py
│   │       │   │   ├── test_version.py
│   │       │   │   └── test_weakref.py
│   │       │   ├── __init__.py
│   │       ├── greenlet-3.5.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── h11/
│   │       │   ├── __init__.py
│   │       │   ├── _abnf.py
│   │       │   ├── _connection.py
│   │       │   ├── _events.py
│   │       │   ├── _headers.py
│   │       │   ├── _readers.py
│   │       │   ├── _receivebuffer.py
│   │       │   ├── _state.py
│   │       │   ├── _util.py
│   │       │   ├── _version.py
│   │       │   ├── _writers.py
│   │       ├── h11-0.16.0.dist-info/
│   │       │   ├── licenses/
│   │       │   │   └── LICENSE.txt
│   │       │   ├── top_level.txt
│   │       ├── httpcore/
│   │       │   ├── _async/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── connection.py
│   │       │   │   ├── connection_pool.py
│   │       │   │   ├── http11.py
│   │       │   │   ├── http2.py
│   │       │   │   ├── http_proxy.py
│   │       │   │   ├── interfaces.py
│   │       │   │   └── socks_proxy.py
│   │       │   ├── _backends/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── anyio.py
│   │       │   │   ├── auto.py
│   │       │   │   ├── base.py
│   │       │   │   ├── mock.py
│   │       │   │   ├── sync.py
│   │       │   │   └── trio.py
│   │       │   ├── _sync/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── connection.py
│   │       │   │   ├── connection_pool.py
│   │       │   │   ├── http11.py
│   │       │   │   ├── http2.py
│   │       │   │   ├── http_proxy.py
│   │       │   │   ├── interfaces.py
│   │       │   │   └── socks_proxy.py
│   │       │   ├── __init__.py
│   │       │   ├── _api.py
│   │       │   ├── _exceptions.py
│   │       │   ├── _models.py
│   │       │   ├── _ssl.py
│   │       │   ├── _synchronization.py
│   │       │   ├── _trace.py
│   │       │   ├── _utils.py
│   │       ├── httpcore-1.0.9.dist-info/
│   │       │   ├── licenses/
│   │       │   │   └── LICENSE.md
│   │       ├── httpx/
│   │       │   ├── _transports/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── asgi.py
│   │       │   │   ├── base.py
│   │       │   │   ├── default.py
│   │       │   │   ├── mock.py
│   │       │   │   └── wsgi.py
│   │       │   ├── __init__.py
│   │       │   ├── __version__.py
│   │       │   ├── _api.py
│   │       │   ├── _auth.py
│   │       │   ├── _client.py
│   │       │   ├── _config.py
│   │       │   ├── _content.py
│   │       │   ├── _decoders.py
│   │       │   ├── _exceptions.py
│   │       │   ├── _main.py
│   │       │   ├── _models.py
│   │       │   ├── _multipart.py
│   │       │   ├── _status_codes.py
│   │       │   ├── _types.py
│   │       │   ├── _urlparse.py
│   │       │   ├── _urls.py
│   │       │   ├── _utils.py
│   │       ├── httpx-0.28.1.dist-info/
│   │       │   ├── licenses/
│   │       │   │   └── LICENSE.md
│   │       │   ├── entry_points.txt
│   │       ├── idna/
│   │       │   ├── __init__.py
│   │       │   ├── codec.py
│   │       │   ├── compat.py
│   │       │   ├── core.py
│   │       │   ├── idnadata.py
│   │       │   ├── intranges.py
│   │       │   ├── package_data.py
│   │       │   └── uts46data.py
│   │       ├── idna-3.15.dist-info/
│   │       │   ├── licenses/
│   │       │   │   └── LICENSE.md
│   │       ├── iniconfig/
│   │       │   ├── __init__.py
│   │       │   ├── _parse.py
│   │       │   ├── _version.py
│   │       │   ├── exceptions.py
│   │       ├── iniconfig-2.3.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── outcome/
│   │       │   ├── __init__.py
│   │       │   ├── _impl.py
│   │       │   ├── _util.py
│   │       │   ├── _version.py
│   │       ├── outcome-1.3.0.post0.dist-info/
│   │       │   ├── top_level.txt
│   │       ├── packaging/
│   │       │   ├── licenses/
│   │       │   │   ├── __init__.py
│   │       │   │   └── _spdx.py
│   │       │   ├── __init__.py
│   │       │   ├── _elffile.py
│   │       │   ├── _manylinux.py
│   │       │   ├── _musllinux.py
│   │       │   ├── _parser.py
│   │       │   ├── _structures.py
│   │       │   ├── _tokenizer.py
│   │       │   ├── dependency_groups.py
│   │       │   ├── direct_url.py
│   │       │   ├── errors.py
│   │       │   ├── markers.py
│   │       │   ├── metadata.py
│   │       │   ├── pylock.py
│   │       │   ├── requirements.py
│   │       │   ├── specifiers.py
│   │       │   ├── tags.py
│   │       │   ├── utils.py
│   │       │   └── version.py
│   │       ├── packaging-26.2.dist-info/
│   │       │   ├── licenses/
│   │       ├── PIL/
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── _binary.py
│   │       │   ├── _deprecate.py
│   │       │   ├── _tkinter_finder.py
│   │       │   ├── _typing.py
│   │       │   ├── _util.py
│   │       │   ├── _version.py
│   │       │   ├── AvifImagePlugin.py
│   │       │   ├── BdfFontFile.py
│   │       │   ├── BlpImagePlugin.py
│   │       │   ├── BmpImagePlugin.py
│   │       │   ├── BufrStubImagePlugin.py
│   │       │   ├── ContainerIO.py
│   │       │   ├── CurImagePlugin.py
│   │       │   ├── DcxImagePlugin.py
│   │       │   ├── DdsImagePlugin.py
│   │       │   ├── EpsImagePlugin.py
│   │       │   ├── ExifTags.py
│   │       │   ├── features.py
│   │       │   ├── FitsImagePlugin.py
│   │       │   ├── FliImagePlugin.py
│   │       │   ├── FontFile.py
│   │       │   ├── FpxImagePlugin.py
│   │       │   ├── FtexImagePlugin.py
│   │       │   ├── GbrImagePlugin.py
│   │       │   ├── GdImageFile.py
│   │       │   ├── GifImagePlugin.py
│   │       │   ├── GimpGradientFile.py
│   │       │   ├── GimpPaletteFile.py
│   │       │   ├── GribStubImagePlugin.py
│   │       │   ├── Hdf5StubImagePlugin.py
│   │       │   ├── IcnsImagePlugin.py
│   │       │   ├── IcoImagePlugin.py
│   │       │   ├── Image.py
│   │       │   ├── ImageChops.py
│   │       │   ├── ImageCms.py
│   │       │   ├── ImageColor.py
│   │       │   ├── ImageDraw.py
│   │       │   ├── ImageDraw2.py
│   │       │   ├── ImageEnhance.py
│   │       │   ├── ImageFile.py
│   │       │   ├── ImageFilter.py
│   │       │   ├── ImageFont.py
│   │       │   ├── ImageGrab.py
│   │       │   ├── ImageMath.py
│   │       │   ├── ImageMode.py
│   │       │   ├── ImageMorph.py
│   │       │   ├── ImageOps.py
│   │       │   ├── ImagePalette.py
│   │       │   ├── ImagePath.py
│   │       │   ├── ImageQt.py
│   │       │   ├── ImageSequence.py
│   │       │   ├── ImageShow.py
│   │       │   ├── ImageStat.py
│   │       │   ├── ImageText.py
│   │       │   ├── ImageTk.py
│   │       │   ├── ImageTransform.py
│   │       │   ├── ImageWin.py
│   │       │   ├── ImImagePlugin.py
│   │       │   ├── ImtImagePlugin.py
│   │       │   ├── IptcImagePlugin.py
│   │       │   ├── Jpeg2KImagePlugin.py
│   │       │   ├── JpegImagePlugin.py
│   │       │   ├── JpegPresets.py
│   │       │   ├── McIdasImagePlugin.py
│   │       │   ├── MicImagePlugin.py
│   │       │   ├── MpegImagePlugin.py
│   │       │   ├── MpoImagePlugin.py
│   │       │   ├── MspImagePlugin.py
│   │       │   ├── PaletteFile.py
│   │       │   ├── PalmImagePlugin.py
│   │       │   ├── PcdImagePlugin.py
│   │       │   ├── PcfFontFile.py
│   │       │   ├── PcxImagePlugin.py
│   │       │   ├── PdfImagePlugin.py
│   │       │   ├── PdfParser.py
│   │       │   ├── PixarImagePlugin.py
│   │       │   ├── PngImagePlugin.py
│   │       │   ├── PpmImagePlugin.py
│   │       │   ├── PsdImagePlugin.py
│   │       │   ├── PSDraw.py
│   │       │   ├── QoiImagePlugin.py
│   │       │   ├── report.py
│   │       │   ├── SgiImagePlugin.py
│   │       │   ├── SpiderImagePlugin.py
│   │       │   ├── SunImagePlugin.py
│   │       │   ├── TarIO.py
│   │       │   ├── TgaImagePlugin.py
│   │       │   ├── TiffImagePlugin.py
│   │       │   ├── TiffTags.py
│   │       │   ├── WalImageFile.py
│   │       │   ├── WebPImagePlugin.py
│   │       │   ├── WmfImagePlugin.py
│   │       │   ├── XbmImagePlugin.py
│   │       │   ├── XpmImagePlugin.py
│   │       │   └── XVThumbImagePlugin.py
│   │       ├── pillow-12.2.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── pip/
│   │       │   ├── _internal/
│   │       │   │   ├── cli/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── autocompletion.py
│   │       │   │   │   ├── base_command.py
│   │       │   │   │   ├── cmdoptions.py
│   │       │   │   │   ├── command_context.py
│   │       │   │   │   ├── index_command.py
│   │       │   │   │   ├── main.py
│   │       │   │   │   ├── main_parser.py
│   │       │   │   │   ├── parser.py
│   │       │   │   │   ├── progress_bars.py
│   │       │   │   │   ├── req_command.py
│   │       │   │   │   ├── spinners.py
│   │       │   │   │   └── status_codes.py
│   │       │   │   ├── commands/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── cache.py
│   │       │   │   │   ├── check.py
│   │       │   │   │   ├── completion.py
│   │       │   │   │   ├── configuration.py
│   │       │   │   │   ├── debug.py
│   │       │   │   │   ├── download.py
│   │       │   │   │   ├── freeze.py
│   │       │   │   │   ├── hash.py
│   │       │   │   │   ├── help.py
│   │       │   │   │   ├── index.py
│   │       │   │   │   ├── inspect.py
│   │       │   │   │   ├── install.py
│   │       │   │   │   ├── list.py
│   │       │   │   │   ├── lock.py
│   │       │   │   │   ├── search.py
│   │       │   │   │   ├── show.py
│   │       │   │   │   ├── uninstall.py
│   │       │   │   │   └── wheel.py
│   │       │   │   ├── distributions/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   ├── installed.py
│   │       │   │   │   ├── sdist.py
│   │       │   │   │   └── wheel.py
│   │       │   │   ├── index/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── collector.py
│   │       │   │   │   ├── package_finder.py
│   │       │   │   │   └── sources.py
│   │       │   │   ├── locations/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _distutils.py
│   │       │   │   │   ├── _sysconfig.py
│   │       │   │   │   └── base.py
│   │       │   │   ├── metadata/
│   │       │   │   │   ├── importlib/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── _compat.py
│   │       │   │   │   │   ├── _dists.py
│   │       │   │   │   │   └── _envs.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _json.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   └── pkg_resources.py
│   │       │   │   ├── models/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── candidate.py
│   │       │   │   │   ├── direct_url.py
│   │       │   │   │   ├── format_control.py
│   │       │   │   │   ├── index.py
│   │       │   │   │   ├── installation_report.py
│   │       │   │   │   ├── link.py
│   │       │   │   │   ├── release_control.py
│   │       │   │   │   ├── scheme.py
│   │       │   │   │   ├── search_scope.py
│   │       │   │   │   ├── selection_prefs.py
│   │       │   │   │   ├── target_python.py
│   │       │   │   │   └── wheel.py
│   │       │   │   ├── network/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── auth.py
│   │       │   │   │   ├── cache.py
│   │       │   │   │   ├── download.py
│   │       │   │   │   ├── lazy_wheel.py
│   │       │   │   │   ├── session.py
│   │       │   │   │   ├── utils.py
│   │       │   │   │   └── xmlrpc.py
│   │       │   │   ├── operations/
│   │       │   │   │   ├── install/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── wheel.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── check.py
│   │       │   │   │   ├── freeze.py
│   │       │   │   │   └── prepare.py
│   │       │   │   ├── req/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── constructors.py
│   │       │   │   │   ├── pep723.py
│   │       │   │   │   ├── req_dependency_group.py
│   │       │   │   │   ├── req_file.py
│   │       │   │   │   ├── req_install.py
│   │       │   │   │   ├── req_set.py
│   │       │   │   │   └── req_uninstall.py
│   │       │   │   ├── resolution/
│   │       │   │   │   ├── legacy/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── resolver.py
│   │       │   │   │   ├── resolvelib/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── base.py
│   │       │   │   │   │   ├── candidates.py
│   │       │   │   │   │   ├── factory.py
│   │       │   │   │   │   ├── found_candidates.py
│   │       │   │   │   │   ├── provider.py
│   │       │   │   │   │   ├── reporter.py
│   │       │   │   │   │   ├── requirements.py
│   │       │   │   │   │   └── resolver.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── base.py
│   │       │   │   ├── utils/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _jaraco_text.py
│   │       │   │   │   ├── _log.py
│   │       │   │   │   ├── appdirs.py
│   │       │   │   │   ├── compat.py
│   │       │   │   │   ├── compatibility_tags.py
│   │       │   │   │   ├── datetime.py
│   │       │   │   │   ├── deprecation.py
│   │       │   │   │   ├── direct_url_helpers.py
│   │       │   │   │   ├── egg_link.py
│   │       │   │   │   ├── entrypoints.py
│   │       │   │   │   ├── filesystem.py
│   │       │   │   │   ├── filetypes.py
│   │       │   │   │   ├── glibc.py
│   │       │   │   │   ├── hashes.py
│   │       │   │   │   ├── logging.py
│   │       │   │   │   ├── misc.py
│   │       │   │   │   ├── packaging.py
│   │       │   │   │   ├── pylock.py
│   │       │   │   │   ├── retry.py
│   │       │   │   │   ├── subprocess.py
│   │       │   │   │   ├── temp_dir.py
│   │       │   │   │   ├── unpacking.py
│   │       │   │   │   ├── urls.py
│   │       │   │   │   ├── virtualenv.py
│   │       │   │   │   └── wheel.py
│   │       │   │   ├── vcs/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── bazaar.py
│   │       │   │   │   ├── git.py
│   │       │   │   │   ├── mercurial.py
│   │       │   │   │   ├── subversion.py
│   │       │   │   │   └── versioncontrol.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── build_env.py
│   │       │   │   ├── cache.py
│   │       │   │   ├── configuration.py
│   │       │   │   ├── exceptions.py
│   │       │   │   ├── main.py
│   │       │   │   ├── pyproject.py
│   │       │   │   ├── self_outdated_check.py
│   │       │   │   └── wheel_builder.py
│   │       │   ├── _vendor/
│   │       │   │   ├── cachecontrol/
│   │       │   │   │   ├── caches/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── file_cache.py
│   │       │   │   │   │   └── redis_cache.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _cmd.py
│   │       │   │   │   ├── adapter.py
│   │       │   │   │   ├── cache.py
│   │       │   │   │   ├── controller.py
│   │       │   │   │   ├── filewrapper.py
│   │       │   │   │   ├── heuristics.py
│   │       │   │   │   ├── LICENSE.txt
│   │       │   │   │   ├── serialize.py
│   │       │   │   │   └── wrapper.py
│   │       │   │   ├── certifi/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __main__.py
│   │       │   │   │   ├── core.py
│   │       │   │   ├── distlib/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── compat.py
│   │       │   │   │   ├── LICENSE.txt
│   │       │   │   │   ├── resources.py
│   │       │   │   │   ├── scripts.py
│   │       │   │   │   ├── util.py
│   │       │   │   ├── distro/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __main__.py
│   │       │   │   │   ├── distro.py
│   │       │   │   ├── idna/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── codec.py
│   │       │   │   │   ├── compat.py
│   │       │   │   │   ├── core.py
│   │       │   │   │   ├── idnadata.py
│   │       │   │   │   ├── intranges.py
│   │       │   │   │   ├── LICENSE.md
│   │       │   │   │   ├── package_data.py
│   │       │   │   │   └── uts46data.py
│   │       │   │   ├── msgpack/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── exceptions.py
│   │       │   │   │   ├── ext.py
│   │       │   │   │   └── fallback.py
│   │       │   │   ├── packaging/
│   │       │   │   │   ├── licenses/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── _spdx.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _elffile.py
│   │       │   │   │   ├── _manylinux.py
│   │       │   │   │   ├── _musllinux.py
│   │       │   │   │   ├── _parser.py
│   │       │   │   │   ├── _structures.py
│   │       │   │   │   ├── _tokenizer.py
│   │       │   │   │   ├── dependency_groups.py
│   │       │   │   │   ├── direct_url.py
│   │       │   │   │   ├── errors.py
│   │       │   │   │   ├── markers.py
│   │       │   │   │   ├── metadata.py
│   │       │   │   │   ├── pylock.py
│   │       │   │   │   ├── requirements.py
│   │       │   │   │   ├── specifiers.py
│   │       │   │   │   ├── tags.py
│   │       │   │   │   ├── utils.py
│   │       │   │   │   └── version.py
│   │       │   │   ├── pkg_resources/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── platformdirs/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __main__.py
│   │       │   │   │   ├── android.py
│   │       │   │   │   ├── api.py
│   │       │   │   │   ├── macos.py
│   │       │   │   │   ├── unix.py
│   │       │   │   │   ├── version.py
│   │       │   │   │   └── windows.py
│   │       │   │   ├── pygments/
│   │       │   │   │   ├── filters/
│   │       │   │   │   │   └── __init__.py
│   │       │   │   │   ├── formatters/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── _mapping.py
│   │       │   │   │   ├── lexers/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── _mapping.py
│   │       │   │   │   │   └── python.py
│   │       │   │   │   ├── styles/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── _mapping.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __main__.py
│   │       │   │   │   ├── console.py
│   │       │   │   │   ├── filter.py
│   │       │   │   │   ├── formatter.py
│   │       │   │   │   ├── lexer.py
│   │       │   │   │   ├── modeline.py
│   │       │   │   │   ├── plugin.py
│   │       │   │   │   ├── regexopt.py
│   │       │   │   │   ├── scanner.py
│   │       │   │   │   ├── sphinxext.py
│   │       │   │   │   ├── style.py
│   │       │   │   │   ├── token.py
│   │       │   │   │   ├── unistring.py
│   │       │   │   │   └── util.py
│   │       │   │   ├── pyproject_hooks/
│   │       │   │   │   ├── _in_process/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── _in_process.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _impl.py
│   │       │   │   ├── requests/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __version__.py
│   │       │   │   │   ├── _internal_utils.py
│   │       │   │   │   ├── adapters.py
│   │       │   │   │   ├── api.py
│   │       │   │   │   ├── auth.py
│   │       │   │   │   ├── certs.py
│   │       │   │   │   ├── compat.py
│   │       │   │   │   ├── cookies.py
│   │       │   │   │   ├── exceptions.py
│   │       │   │   │   ├── help.py
│   │       │   │   │   ├── hooks.py
│   │       │   │   │   ├── models.py
│   │       │   │   │   ├── packages.py
│   │       │   │   │   ├── sessions.py
│   │       │   │   │   ├── status_codes.py
│   │       │   │   │   ├── structures.py
│   │       │   │   │   └── utils.py
│   │       │   │   ├── resolvelib/
│   │       │   │   │   ├── resolvers/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── abstract.py
│   │       │   │   │   │   ├── criterion.py
│   │       │   │   │   │   ├── exceptions.py
│   │       │   │   │   │   └── resolution.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── providers.py
│   │       │   │   │   ├── reporters.py
│   │       │   │   │   └── structs.py
│   │       │   │   ├── rich/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __main__.py
│   │       │   │   │   ├── _cell_widths.py
│   │       │   │   │   ├── _emoji_codes.py
│   │       │   │   │   ├── _emoji_replace.py
│   │       │   │   │   ├── _export_format.py
│   │       │   │   │   ├── _extension.py
│   │       │   │   │   ├── _fileno.py
│   │       │   │   │   ├── _inspect.py
│   │       │   │   │   ├── _log_render.py
│   │       │   │   │   ├── _loop.py
│   │       │   │   │   ├── _null_file.py
│   │       │   │   │   ├── _palettes.py
│   │       │   │   │   ├── _pick.py
│   │       │   │   │   ├── _ratio.py
│   │       │   │   │   ├── _spinners.py
│   │       │   │   │   ├── _stack.py
│   │       │   │   │   ├── _timer.py
│   │       │   │   │   ├── _win32_console.py
│   │       │   │   │   ├── _windows.py
│   │       │   │   │   ├── _windows_renderer.py
│   │       │   │   │   ├── _wrap.py
│   │       │   │   │   ├── abc.py
│   │       │   │   │   ├── align.py
│   │       │   │   │   ├── ansi.py
│   │       │   │   │   ├── bar.py
│   │       │   │   │   ├── box.py
│   │       │   │   │   ├── cells.py
│   │       │   │   │   ├── color.py
│   │       │   │   │   ├── color_triplet.py
│   │       │   │   │   ├── columns.py
│   │       │   │   │   ├── console.py
│   │       │   │   │   ├── constrain.py
│   │       │   │   │   ├── containers.py
│   │       │   │   │   ├── control.py
│   │       │   │   │   ├── default_styles.py
│   │       │   │   │   ├── diagnose.py
│   │       │   │   │   ├── emoji.py
│   │       │   │   │   ├── errors.py
│   │       │   │   │   ├── file_proxy.py
│   │       │   │   │   ├── filesize.py
│   │       │   │   │   ├── highlighter.py
│   │       │   │   │   ├── json.py
│   │       │   │   │   ├── jupyter.py
│   │       │   │   │   ├── layout.py
│   │       │   │   │   ├── live.py
│   │       │   │   │   ├── live_render.py
│   │       │   │   │   ├── logging.py
│   │       │   │   │   ├── markup.py
│   │       │   │   │   ├── measure.py
│   │       │   │   │   ├── padding.py
│   │       │   │   │   ├── pager.py
│   │       │   │   │   ├── palette.py
│   │       │   │   │   ├── panel.py
│   │       │   │   │   ├── pretty.py
│   │       │   │   │   ├── progress.py
│   │       │   │   │   ├── progress_bar.py
│   │       │   │   │   ├── prompt.py
│   │       │   │   │   ├── protocol.py
│   │       │   │   │   ├── region.py
│   │       │   │   │   ├── repr.py
│   │       │   │   │   ├── rule.py
│   │       │   │   │   ├── scope.py
│   │       │   │   │   ├── screen.py
│   │       │   │   │   ├── segment.py
│   │       │   │   │   ├── spinner.py
│   │       │   │   │   ├── status.py
│   │       │   │   │   ├── style.py
│   │       │   │   │   ├── styled.py
│   │       │   │   │   ├── syntax.py
│   │       │   │   │   ├── table.py
│   │       │   │   │   ├── terminal_theme.py
│   │       │   │   │   ├── text.py
│   │       │   │   │   ├── theme.py
│   │       │   │   │   ├── themes.py
│   │       │   │   │   ├── traceback.py
│   │       │   │   │   └── tree.py
│   │       │   │   ├── tomli/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _parser.py
│   │       │   │   │   ├── _re.py
│   │       │   │   │   ├── _types.py
│   │       │   │   ├── tomli_w/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _writer.py
│   │       │   │   ├── truststore/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _api.py
│   │       │   │   │   ├── _macos.py
│   │       │   │   │   ├── _openssl.py
│   │       │   │   │   ├── _ssl_constants.py
│   │       │   │   │   ├── _windows.py
│   │       │   │   ├── urllib3/
│   │       │   │   │   ├── contrib/
│   │       │   │   │   │   ├── emscripten/
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   ├── connection.py
│   │       │   │   │   │   │   ├── emscripten_fetch_worker.js
│   │       │   │   │   │   │   ├── fetch.py
│   │       │   │   │   │   │   ├── request.py
│   │       │   │   │   │   │   └── response.py
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── pyopenssl.py
│   │       │   │   │   │   └── socks.py
│   │       │   │   │   ├── http2/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── connection.py
│   │       │   │   │   │   └── probe.py
│   │       │   │   │   ├── util/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── connection.py
│   │       │   │   │   │   ├── proxy.py
│   │       │   │   │   │   ├── request.py
│   │       │   │   │   │   ├── response.py
│   │       │   │   │   │   ├── retry.py
│   │       │   │   │   │   ├── ssl_.py
│   │       │   │   │   │   ├── ssl_match_hostname.py
│   │       │   │   │   │   ├── ssltransport.py
│   │       │   │   │   │   ├── timeout.py
│   │       │   │   │   │   ├── url.py
│   │       │   │   │   │   ├── util.py
│   │       │   │   │   │   └── wait.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _base_connection.py
│   │       │   │   │   ├── _collections.py
│   │       │   │   │   ├── _request_methods.py
│   │       │   │   │   ├── _version.py
│   │       │   │   │   ├── connection.py
│   │       │   │   │   ├── connectionpool.py
│   │       │   │   │   ├── exceptions.py
│   │       │   │   │   ├── fields.py
│   │       │   │   │   ├── filepost.py
│   │       │   │   │   ├── LICENSE.txt
│   │       │   │   │   ├── poolmanager.py
│   │       │   │   │   └── response.py
│   │       │   │   ├── __init__.py
│   │       │   │   └── vendor.txt
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── __pip-runner__.py
│   │       ├── pip-26.1.1.dist-info/
│   │       │   ├── licenses/
│   │       │   │   ├── src/
│   │       │   │   │   └── pip/
│   │       │   │   │       └── _vendor/
│   │       │   │   │           ├── cachecontrol/
│   │       │   │   │           │   └── LICENSE.txt
│   │       │   │   │           ├── certifi/
│   │       │   │   │           ├── distlib/
│   │       │   │   │           │   └── LICENSE.txt
│   │       │   │   │           ├── distro/
│   │       │   │   │           ├── idna/
│   │       │   │   │           │   └── LICENSE.md
│   │       │   │   │           ├── msgpack/
│   │       │   │   │           ├── packaging/
│   │       │   │   │           ├── pkg_resources/
│   │       │   │   │           ├── platformdirs/
│   │       │   │   │           ├── pygments/
│   │       │   │   │           ├── pyproject_hooks/
│   │       │   │   │           ├── requests/
│   │       │   │   │           ├── resolvelib/
│   │       │   │   │           ├── rich/
│   │       │   │   │           ├── tomli/
│   │       │   │   │           ├── tomli_w/
│   │       │   │   │           ├── truststore/
│   │       │   │   │           └── urllib3/
│   │       │   │   │               └── LICENSE.txt
│   │       │   │   ├── AUTHORS.txt
│   │       │   │   └── LICENSE.txt
│   │       │   ├── entry_points.txt
│   │       ├── playwright/
│   │       │   ├── _impl/
│   │       │   │   ├── __pyinstaller/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── hook-playwright.async_api.py
│   │       │   │   │   └── hook-playwright.sync_api.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _api_structures.py
│   │       │   │   ├── _artifact.py
│   │       │   │   ├── _assertions.py
│   │       │   │   ├── _async_base.py
│   │       │   │   ├── _browser.py
│   │       │   │   ├── _browser_context.py
│   │       │   │   ├── _browser_type.py
│   │       │   │   ├── _cdp_session.py
│   │       │   │   ├── _clock.py
│   │       │   │   ├── _connection.py
│   │       │   │   ├── _console_message.py
│   │       │   │   ├── _debugger.py
│   │       │   │   ├── _dialog.py
│   │       │   │   ├── _download.py
│   │       │   │   ├── _driver.py
│   │       │   │   ├── _element_handle.py
│   │       │   │   ├── _errors.py
│   │       │   │   ├── _event_context_manager.py
│   │       │   │   ├── _fetch.py
│   │       │   │   ├── _file_chooser.py
│   │       │   │   ├── _frame.py
│   │       │   │   ├── _glob.py
│   │       │   │   ├── _greenlets.py
│   │       │   │   ├── _har_router.py
│   │       │   │   ├── _helper.py
│   │       │   │   ├── _impl_to_api_mapping.py
│   │       │   │   ├── _input.py
│   │       │   │   ├── _js_handle.py
│   │       │   │   ├── _json_pipe.py
│   │       │   │   ├── _local_utils.py
│   │       │   │   ├── _locator.py
│   │       │   │   ├── _map.py
│   │       │   │   ├── _network.py
│   │       │   │   ├── _object_factory.py
│   │       │   │   ├── _page.py
│   │       │   │   ├── _path_utils.py
│   │       │   │   ├── _playwright.py
│   │       │   │   ├── _screencast.py
│   │       │   │   ├── _selectors.py
│   │       │   │   ├── _set_input_files_helpers.py
│   │       │   │   ├── _str_utils.py
│   │       │   │   ├── _stream.py
│   │       │   │   ├── _sync_base.py
│   │       │   │   ├── _tracing.py
│   │       │   │   ├── _transport.py
│   │       │   │   ├── _video.py
│   │       │   │   ├── _waiter.py
│   │       │   │   ├── _web_error.py
│   │       │   │   └── _writable_stream.py
│   │       │   ├── async_api/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _context_manager.py
│   │       │   │   └── _generated.py
│   │       │   ├── driver/
│   │       │   │   ├── package/
│   │       │   │   │   ├── bin/
│   │       │   │   │   │   ├── install_media_pack.ps1
│   │       │   │   │   │   ├── install_webkit_wsl.ps1
│   │       │   │   │   │   ├── reinstall_chrome_beta_win.ps1
│   │       │   │   │   │   ├── reinstall_chrome_stable_win.ps1
│   │       │   │   │   │   ├── reinstall_msedge_beta_win.ps1
│   │       │   │   │   │   ├── reinstall_msedge_dev_win.ps1
│   │       │   │   │   │   └── reinstall_msedge_stable_win.ps1
│   │       │   │   │   ├── lib/
│   │       │   │   │   │   ├── cli/
│   │       │   │   │   │   │   ├── browserActions.js
│   │       │   │   │   │   │   ├── driver.js
│   │       │   │   │   │   │   ├── installActions.js
│   │       │   │   │   │   │   ├── program.js
│   │       │   │   │   │   │   └── programWithTestStub.js
│   │       │   │   │   │   ├── client/
│   │       │   │   │   │   │   ├── android.js
│   │       │   │   │   │   │   ├── api.js
│   │       │   │   │   │   │   ├── artifact.js
│   │       │   │   │   │   │   ├── browser.js
│   │       │   │   │   │   │   ├── browserContext.js
│   │       │   │   │   │   │   ├── browserType.js
│   │       │   │   │   │   │   ├── cdpSession.js
│   │       │   │   │   │   │   ├── channelOwner.js
│   │       │   │   │   │   │   ├── clientHelper.js
│   │       │   │   │   │   │   ├── clientInstrumentation.js
│   │       │   │   │   │   │   ├── clientStackTrace.js
│   │       │   │   │   │   │   ├── clock.js
│   │       │   │   │   │   │   ├── connect.js
│   │       │   │   │   │   │   ├── connection.js
│   │       │   │   │   │   │   ├── consoleMessage.js
│   │       │   │   │   │   │   ├── coverage.js
│   │       │   │   │   │   │   ├── debugger.js
│   │       │   │   │   │   │   ├── dialog.js
│   │       │   │   │   │   │   ├── disposable.js
│   │       │   │   │   │   │   ├── download.js
│   │       │   │   │   │   │   ├── electron.js
│   │       │   │   │   │   │   ├── elementHandle.js
│   │       │   │   │   │   │   ├── errors.js
│   │       │   │   │   │   │   ├── eventEmitter.js
│   │       │   │   │   │   │   ├── events.js
│   │       │   │   │   │   │   ├── fetch.js
│   │       │   │   │   │   │   ├── fileChooser.js
│   │       │   │   │   │   │   ├── fileUtils.js
│   │       │   │   │   │   │   ├── frame.js
│   │       │   │   │   │   │   ├── harRouter.js
│   │       │   │   │   │   │   ├── input.js
│   │       │   │   │   │   │   ├── jsHandle.js
│   │       │   │   │   │   │   ├── jsonPipe.js
│   │       │   │   │   │   │   ├── localUtils.js
│   │       │   │   │   │   │   ├── locator.js
│   │       │   │   │   │   │   ├── network.js
│   │       │   │   │   │   │   ├── page.js
│   │       │   │   │   │   │   ├── platform.js
│   │       │   │   │   │   │   ├── playwright.js
│   │       │   │   │   │   │   ├── screencast.js
│   │       │   │   │   │   │   ├── selectors.js
│   │       │   │   │   │   │   ├── stream.js
│   │       │   │   │   │   │   ├── timeoutSettings.js
│   │       │   │   │   │   │   ├── tracing.js
│   │       │   │   │   │   │   ├── types.js
│   │       │   │   │   │   │   ├── video.js
│   │       │   │   │   │   │   ├── waiter.js
│   │       │   │   │   │   │   ├── webError.js
│   │       │   │   │   │   │   ├── worker.js
│   │       │   │   │   │   │   └── writableStream.js
│   │       │   │   │   │   ├── generated/
│   │       │   │   │   │   │   ├── bindingsControllerSource.js
│   │       │   │   │   │   │   ├── clockSource.js
│   │       │   │   │   │   │   ├── injectedScriptSource.js
│   │       │   │   │   │   │   ├── pollingRecorderSource.js
│   │       │   │   │   │   │   ├── storageScriptSource.js
│   │       │   │   │   │   │   ├── utilityScriptSource.js
│   │       │   │   │   │   │   └── webSocketMockSource.js
│   │       │   │   │   │   ├── protocol/
│   │       │   │   │   │   │   ├── serializers.js
│   │       │   │   │   │   │   ├── validator.js
│   │       │   │   │   │   │   └── validatorPrimitives.js
│   │       │   │   │   │   ├── remote/
│   │       │   │   │   │   │   ├── playwrightConnection.js
│   │       │   │   │   │   │   ├── playwrightPipeServer.js
│   │       │   │   │   │   │   ├── playwrightServer.js
│   │       │   │   │   │   │   ├── playwrightWebSocketServer.js
│   │       │   │   │   │   │   └── serverTransport.js
│   │       │   │   │   │   ├── server/
│   │       │   │   │   │   │   ├── android/
│   │       │   │   │   │   │   │   ├── android.js
│   │       │   │   │   │   │   │   └── backendAdb.js
│   │       │   │   │   │   │   ├── bidi/
│   │       │   │   │   │   │   │   ├── third_party/
│   │       │   │   │   │   │   │   │   ├── bidiCommands.d.js
│   │       │   │   │   │   │   │   │   ├── bidiKeyboard.js
│   │       │   │   │   │   │   │   │   ├── bidiProtocol.js
│   │       │   │   │   │   │   │   │   ├── bidiProtocolCore.js
│   │       │   │   │   │   │   │   │   ├── bidiProtocolPermissions.js
│   │       │   │   │   │   │   │   │   ├── bidiSerializer.js
│   │       │   │   │   │   │   │   │   └── firefoxPrefs.js
│   │       │   │   │   │   │   │   ├── bidiBrowser.js
│   │       │   │   │   │   │   │   ├── bidiChromium.js
│   │       │   │   │   │   │   │   ├── bidiConnection.js
│   │       │   │   │   │   │   │   ├── bidiDeserializer.js
│   │       │   │   │   │   │   │   ├── bidiExecutionContext.js
│   │       │   │   │   │   │   │   ├── bidiFirefox.js
│   │       │   │   │   │   │   │   ├── bidiInput.js
│   │       │   │   │   │   │   │   ├── bidiNetworkManager.js
│   │       │   │   │   │   │   │   ├── bidiOverCdp.js
│   │       │   │   │   │   │   │   ├── bidiPage.js
│   │       │   │   │   │   │   │   └── bidiPdf.js
│   │       │   │   │   │   │   ├── chromium/
│   │       │   │   │   │   │   │   ├── chromium.js
│   │       │   │   │   │   │   │   ├── chromiumSwitches.js
│   │       │   │   │   │   │   │   ├── crBrowser.js
│   │       │   │   │   │   │   │   ├── crConnection.js
│   │       │   │   │   │   │   │   ├── crCoverage.js
│   │       │   │   │   │   │   │   ├── crDevTools.js
│   │       │   │   │   │   │   │   ├── crDragDrop.js
│   │       │   │   │   │   │   │   ├── crExecutionContext.js
│   │       │   │   │   │   │   │   ├── crInput.js
│   │       │   │   │   │   │   │   ├── crNetworkManager.js
│   │       │   │   │   │   │   │   ├── crPage.js
│   │       │   │   │   │   │   │   ├── crPdf.js
│   │       │   │   │   │   │   │   ├── crProtocolHelper.js
│   │       │   │   │   │   │   │   ├── crServiceWorker.js
│   │       │   │   │   │   │   │   ├── defaultFontFamilies.js
│   │       │   │   │   │   │   │   └── protocol.d.js
│   │       │   │   │   │   │   ├── codegen/
│   │       │   │   │   │   │   │   ├── csharp.js
│   │       │   │   │   │   │   │   ├── java.js
│   │       │   │   │   │   │   │   ├── javascript.js
│   │       │   │   │   │   │   │   ├── jsonl.js
│   │       │   │   │   │   │   │   ├── language.js
│   │       │   │   │   │   │   │   ├── languages.js
│   │       │   │   │   │   │   │   ├── python.js
│   │       │   │   │   │   │   │   └── types.js
│   │       │   │   │   │   │   ├── dispatchers/
│   │       │   │   │   │   │   │   ├── androidDispatcher.js
│   │       │   │   │   │   │   │   ├── artifactDispatcher.js
│   │       │   │   │   │   │   │   ├── browserContextDispatcher.js
│   │       │   │   │   │   │   │   ├── browserDispatcher.js
│   │       │   │   │   │   │   │   ├── browserTypeDispatcher.js
│   │       │   │   │   │   │   │   ├── cdpSessionDispatcher.js
│   │       │   │   │   │   │   │   ├── debugControllerDispatcher.js
│   │       │   │   │   │   │   │   ├── debuggerDispatcher.js
│   │       │   │   │   │   │   │   ├── dialogDispatcher.js
│   │       │   │   │   │   │   │   ├── dispatcher.js
│   │       │   │   │   │   │   │   ├── disposableDispatcher.js
│   │       │   │   │   │   │   │   ├── electronDispatcher.js
│   │       │   │   │   │   │   │   ├── elementHandlerDispatcher.js
│   │       │   │   │   │   │   │   ├── frameDispatcher.js
│   │       │   │   │   │   │   │   ├── jsHandleDispatcher.js
│   │       │   │   │   │   │   │   ├── jsonPipeDispatcher.js
│   │       │   │   │   │   │   │   ├── localUtilsDispatcher.js
│   │       │   │   │   │   │   │   ├── networkDispatchers.js
│   │       │   │   │   │   │   │   ├── pageDispatcher.js
│   │       │   │   │   │   │   │   ├── playwrightDispatcher.js
│   │       │   │   │   │   │   │   ├── streamDispatcher.js
│   │       │   │   │   │   │   │   ├── tracingDispatcher.js
│   │       │   │   │   │   │   │   ├── webSocketRouteDispatcher.js
│   │       │   │   │   │   │   │   └── writableStreamDispatcher.js
│   │       │   │   │   │   │   ├── electron/
│   │       │   │   │   │   │   │   ├── electron.js
│   │       │   │   │   │   │   │   └── loader.js
│   │       │   │   │   │   │   ├── firefox/
│   │       │   │   │   │   │   │   ├── ffBrowser.js
│   │       │   │   │   │   │   │   ├── ffConnection.js
│   │       │   │   │   │   │   │   ├── ffExecutionContext.js
│   │       │   │   │   │   │   │   ├── ffInput.js
│   │       │   │   │   │   │   │   ├── ffNetworkManager.js
│   │       │   │   │   │   │   │   ├── ffPage.js
│   │       │   │   │   │   │   │   ├── firefox.js
│   │       │   │   │   │   │   │   └── protocol.d.js
│   │       │   │   │   │   │   ├── har/
│   │       │   │   │   │   │   │   ├── harRecorder.js
│   │       │   │   │   │   │   │   └── harTracer.js
│   │       │   │   │   │   │   ├── recorder/
│   │       │   │   │   │   │   │   ├── chat.js
│   │       │   │   │   │   │   │   ├── recorderApp.js
│   │       │   │   │   │   │   │   ├── recorderRunner.js
│   │       │   │   │   │   │   │   ├── recorderSignalProcessor.js
│   │       │   │   │   │   │   │   ├── recorderUtils.js
│   │       │   │   │   │   │   │   └── throttledFile.js
│   │       │   │   │   │   │   ├── registry/
│   │       │   │   │   │   │   │   ├── browserFetcher.js
│   │       │   │   │   │   │   │   ├── dependencies.js
│   │       │   │   │   │   │   │   ├── index.js
│   │       │   │   │   │   │   │   ├── nativeDeps.js
│   │       │   │   │   │   │   │   └── oopDownloadBrowserMain.js
│   │       │   │   │   │   │   ├── trace/
│   │       │   │   │   │   │   │   ├── recorder/
│   │       │   │   │   │   │   │   │   ├── snapshotter.js
│   │       │   │   │   │   │   │   │   ├── snapshotterInjected.js
│   │       │   │   │   │   │   │   │   └── tracing.js
│   │       │   │   │   │   │   │   └── viewer/
│   │       │   │   │   │   │   │       └── traceViewer.js
│   │       │   │   │   │   │   ├── utils/
│   │       │   │   │   │   │   │   ├── image_tools/
│   │       │   │   │   │   │   │   │   ├── colorUtils.js
│   │       │   │   │   │   │   │   │   ├── compare.js
│   │       │   │   │   │   │   │   │   ├── imageChannel.js
│   │       │   │   │   │   │   │   │   └── stats.js
│   │       │   │   │   │   │   │   ├── ascii.js
│   │       │   │   │   │   │   │   ├── comparators.js
│   │       │   │   │   │   │   │   ├── crypto.js
│   │       │   │   │   │   │   │   ├── debug.js
│   │       │   │   │   │   │   │   ├── debugLogger.js
│   │       │   │   │   │   │   │   ├── disposable.js
│   │       │   │   │   │   │   │   ├── env.js
│   │       │   │   │   │   │   │   ├── eventsHelper.js
│   │       │   │   │   │   │   │   ├── expectUtils.js
│   │       │   │   │   │   │   │   ├── fileUtils.js
│   │       │   │   │   │   │   │   ├── happyEyeballs.js
│   │       │   │   │   │   │   │   ├── hostPlatform.js
│   │       │   │   │   │   │   │   ├── httpServer.js
│   │       │   │   │   │   │   │   ├── linuxUtils.js
│   │       │   │   │   │   │   │   ├── network.js
│   │       │   │   │   │   │   │   ├── nodePlatform.js
│   │       │   │   │   │   │   │   ├── pipeTransport.js
│   │       │   │   │   │   │   │   ├── processLauncher.js
│   │       │   │   │   │   │   │   ├── profiler.js
│   │       │   │   │   │   │   │   ├── socksProxy.js
│   │       │   │   │   │   │   │   ├── spawnAsync.js
│   │       │   │   │   │   │   │   ├── task.js
│   │       │   │   │   │   │   │   ├── userAgent.js
│   │       │   │   │   │   │   │   ├── wsServer.js
│   │       │   │   │   │   │   │   ├── zipFile.js
│   │       │   │   │   │   │   │   └── zones.js
│   │       │   │   │   │   │   ├── webkit/
│   │       │   │   │   │   │   │   ├── protocol.d.js
│   │       │   │   │   │   │   │   ├── webkit.js
│   │       │   │   │   │   │   │   ├── wkBrowser.js
│   │       │   │   │   │   │   │   ├── wkConnection.js
│   │       │   │   │   │   │   │   ├── wkExecutionContext.js
│   │       │   │   │   │   │   │   ├── wkInput.js
│   │       │   │   │   │   │   │   ├── wkInterceptableRequest.js
│   │       │   │   │   │   │   │   ├── wkPage.js
│   │       │   │   │   │   │   │   ├── wkProvisionalPage.js
│   │       │   │   │   │   │   │   └── wkWorkers.js
│   │       │   │   │   │   │   ├── artifact.js
│   │       │   │   │   │   │   ├── browser.js
│   │       │   │   │   │   │   ├── browserContext.js
│   │       │   │   │   │   │   ├── browserType.js
│   │       │   │   │   │   │   ├── callLog.js
│   │       │   │   │   │   │   ├── clock.js
│   │       │   │   │   │   │   ├── console.js
│   │       │   │   │   │   │   ├── cookieStore.js
│   │       │   │   │   │   │   ├── debugController.js
│   │       │   │   │   │   │   ├── debugger.js
│   │       │   │   │   │   │   ├── deviceDescriptors.js
│   │       │   │   │   │   │   ├── deviceDescriptorsSource.json
│   │       │   │   │   │   │   ├── dialog.js
│   │       │   │   │   │   │   ├── disposable.js
│   │       │   │   │   │   │   ├── dom.js
│   │       │   │   │   │   │   ├── download.js
│   │       │   │   │   │   │   ├── errors.js
│   │       │   │   │   │   │   ├── fetch.js
│   │       │   │   │   │   │   ├── fileChooser.js
│   │       │   │   │   │   │   ├── fileUploadUtils.js
│   │       │   │   │   │   │   ├── formData.js
│   │       │   │   │   │   │   ├── frames.js
│   │       │   │   │   │   │   ├── frameSelectors.js
│   │       │   │   │   │   │   ├── harBackend.js
│   │       │   │   │   │   │   ├── helper.js
│   │       │   │   │   │   │   ├── index.js
│   │       │   │   │   │   │   ├── input.js
│   │       │   │   │   │   │   ├── instrumentation.js
│   │       │   │   │   │   │   ├── javascript.js
│   │       │   │   │   │   │   ├── launchApp.js
│   │       │   │   │   │   │   ├── localUtils.js
│   │       │   │   │   │   │   ├── macEditingCommands.js
│   │       │   │   │   │   │   ├── network.js
│   │       │   │   │   │   │   ├── overlay.js
│   │       │   │   │   │   │   ├── page.js
│   │       │   │   │   │   │   ├── pipeTransport.js
│   │       │   │   │   │   │   ├── playwright.js
│   │       │   │   │   │   │   ├── progress.js
│   │       │   │   │   │   │   ├── protocolError.js
│   │       │   │   │   │   │   ├── recorder.js
│   │       │   │   │   │   │   ├── screencast.js
│   │       │   │   │   │   │   ├── screenshotter.js
│   │       │   │   │   │   │   ├── selectors.js
│   │       │   │   │   │   │   ├── socksClientCertificatesInterceptor.js
│   │       │   │   │   │   │   ├── socksInterceptor.js
│   │       │   │   │   │   │   ├── transport.js
│   │       │   │   │   │   │   ├── types.js
│   │       │   │   │   │   │   ├── usKeyboardLayout.js
│   │       │   │   │   │   │   └── videoRecorder.js
│   │       │   │   │   │   ├── third_party/
│   │       │   │   │   │   │   └── pixelmatch.js
│   │       │   │   │   │   ├── tools/
│   │       │   │   │   │   │   ├── backend/
│   │       │   │   │   │   │   │   ├── browserBackend.js
│   │       │   │   │   │   │   │   ├── common.js
│   │       │   │   │   │   │   │   ├── config.js
│   │       │   │   │   │   │   │   ├── console.js
│   │       │   │   │   │   │   │   ├── context.js
│   │       │   │   │   │   │   │   ├── cookies.js
│   │       │   │   │   │   │   │   ├── devtools.js
│   │       │   │   │   │   │   │   ├── dialogs.js
│   │       │   │   │   │   │   │   ├── evaluate.js
│   │       │   │   │   │   │   │   ├── files.js
│   │       │   │   │   │   │   │   ├── form.js
│   │       │   │   │   │   │   │   ├── keyboard.js
│   │       │   │   │   │   │   │   ├── logFile.js
│   │       │   │   │   │   │   │   ├── mouse.js
│   │       │   │   │   │   │   │   ├── navigate.js
│   │       │   │   │   │   │   │   ├── network.js
│   │       │   │   │   │   │   │   ├── pdf.js
│   │       │   │   │   │   │   │   ├── response.js
│   │       │   │   │   │   │   │   ├── route.js
│   │       │   │   │   │   │   │   ├── runCode.js
│   │       │   │   │   │   │   │   ├── screenshot.js
│   │       │   │   │   │   │   │   ├── sessionLog.js
│   │       │   │   │   │   │   │   ├── snapshot.js
│   │       │   │   │   │   │   │   ├── storage.js
│   │       │   │   │   │   │   │   ├── tab.js
│   │       │   │   │   │   │   │   ├── tabs.js
│   │       │   │   │   │   │   │   ├── tool.js
│   │       │   │   │   │   │   │   ├── tools.js
│   │       │   │   │   │   │   │   ├── tracing.js
│   │       │   │   │   │   │   │   ├── utils.js
│   │       │   │   │   │   │   │   ├── verify.js
│   │       │   │   │   │   │   │   ├── video.js
│   │       │   │   │   │   │   │   ├── wait.js
│   │       │   │   │   │   │   │   └── webstorage.js
│   │       │   │   │   │   │   ├── cli-client/
│   │       │   │   │   │   │   │   ├── skill/
│   │       │   │   │   │   │   │   │   ├── references/
│   │       │   │   │   │   │   │   │   │   ├── element-attributes.md
│   │       │   │   │   │   │   │   │   │   ├── playwright-tests.md
│   │       │   │   │   │   │   │   │   │   ├── request-mocking.md
│   │       │   │   │   │   │   │   │   │   ├── running-code.md
│   │       │   │   │   │   │   │   │   │   ├── session-management.md
│   │       │   │   │   │   │   │   │   │   ├── storage-state.md
│   │       │   │   │   │   │   │   │   │   ├── test-generation.md
│   │       │   │   │   │   │   │   │   │   ├── tracing.md
│   │       │   │   │   │   │   │   │   │   └── video-recording.md
│   │       │   │   │   │   │   │   │   └── SKILL.md
│   │       │   │   │   │   │   │   ├── cli.js
│   │       │   │   │   │   │   │   ├── help.json
│   │       │   │   │   │   │   │   ├── minimist.js
│   │       │   │   │   │   │   │   ├── program.js
│   │       │   │   │   │   │   │   ├── registry.js
│   │       │   │   │   │   │   │   └── session.js
│   │       │   │   │   │   │   ├── cli-daemon/
│   │       │   │   │   │   │   │   ├── command.js
│   │       │   │   │   │   │   │   ├── commands.js
│   │       │   │   │   │   │   │   ├── daemon.js
│   │       │   │   │   │   │   │   ├── helpGenerator.js
│   │       │   │   │   │   │   │   └── program.js
│   │       │   │   │   │   │   ├── dashboard/
│   │       │   │   │   │   │   │   ├── dashboardApp.js
│   │       │   │   │   │   │   │   └── dashboardController.js
│   │       │   │   │   │   │   ├── mcp/
│   │       │   │   │   │   │   │   ├── browserFactory.js
│   │       │   │   │   │   │   │   ├── cdpRelay.js
│   │       │   │   │   │   │   │   ├── cli-stub.js
│   │       │   │   │   │   │   │   ├── config.d.js
│   │       │   │   │   │   │   │   ├── config.js
│   │       │   │   │   │   │   │   ├── configIni.js
│   │       │   │   │   │   │   │   ├── extensionContextFactory.js
│   │       │   │   │   │   │   │   ├── index.js
│   │       │   │   │   │   │   │   ├── log.js
│   │       │   │   │   │   │   │   ├── program.js
│   │       │   │   │   │   │   │   ├── protocol.js
│   │       │   │   │   │   │   │   └── watchdog.js
│   │       │   │   │   │   │   ├── trace/
│   │       │   │   │   │   │   │   ├── installSkill.js
│   │       │   │   │   │   │   │   ├── SKILL.md
│   │       │   │   │   │   │   │   ├── traceActions.js
│   │       │   │   │   │   │   │   ├── traceAttachments.js
│   │       │   │   │   │   │   │   ├── traceCli.js
│   │       │   │   │   │   │   │   ├── traceConsole.js
│   │       │   │   │   │   │   │   ├── traceErrors.js
│   │       │   │   │   │   │   │   ├── traceOpen.js
│   │       │   │   │   │   │   │   ├── traceParser.js
│   │       │   │   │   │   │   │   ├── traceRequests.js
│   │       │   │   │   │   │   │   ├── traceScreenshot.js
│   │       │   │   │   │   │   │   ├── traceSnapshot.js
│   │       │   │   │   │   │   │   └── traceUtils.js
│   │       │   │   │   │   │   ├── utils/
│   │       │   │   │   │   │   │   ├── mcp/
│   │       │   │   │   │   │   │   │   ├── http.js
│   │       │   │   │   │   │   │   │   ├── server.js
│   │       │   │   │   │   │   │   │   └── tool.js
│   │       │   │   │   │   │   │   ├── connect.js
│   │       │   │   │   │   │   │   └── socketConnection.js
│   │       │   │   │   │   │   └── exports.js
│   │       │   │   │   │   ├── utils/
│   │       │   │   │   │   │   └── isomorphic/
│   │       │   │   │   │   │       ├── trace/
│   │       │   │   │   │   │       │   ├── versions/
│   │       │   │   │   │   │       │   │   ├── traceV3.js
│   │       │   │   │   │   │       │   │   ├── traceV4.js
│   │       │   │   │   │   │       │   │   ├── traceV5.js
│   │       │   │   │   │   │       │   │   ├── traceV6.js
│   │       │   │   │   │   │       │   │   ├── traceV7.js
│   │       │   │   │   │   │       │   │   └── traceV8.js
│   │       │   │   │   │   │       │   ├── entries.js
│   │       │   │   │   │   │       │   ├── snapshotRenderer.js
│   │       │   │   │   │   │       │   ├── snapshotServer.js
│   │       │   │   │   │   │       │   ├── snapshotStorage.js
│   │       │   │   │   │   │       │   ├── traceLoader.js
│   │       │   │   │   │   │       │   ├── traceModel.js
│   │       │   │   │   │   │       │   ├── traceModernizer.js
│   │       │   │   │   │   │       │   └── traceUtils.js
│   │       │   │   │   │   │       ├── ariaSnapshot.js
│   │       │   │   │   │   │       ├── assert.js
│   │       │   │   │   │   │       ├── colors.js
│   │       │   │   │   │   │       ├── cssParser.js
│   │       │   │   │   │   │       ├── cssTokenizer.js
│   │       │   │   │   │   │       ├── formatUtils.js
│   │       │   │   │   │   │       ├── headers.js
│   │       │   │   │   │   │       ├── imageUtils.js
│   │       │   │   │   │   │       ├── jsonSchema.js
│   │       │   │   │   │   │       ├── locatorGenerators.js
│   │       │   │   │   │   │       ├── locatorParser.js
│   │       │   │   │   │   │       ├── locatorUtils.js
│   │       │   │   │   │   │       ├── lruCache.js
│   │       │   │   │   │   │       ├── manualPromise.js
│   │       │   │   │   │   │       ├── mimeType.js
│   │       │   │   │   │   │       ├── multimap.js
│   │       │   │   │   │   │       ├── protocolFormatter.js
│   │       │   │   │   │   │       ├── protocolMetainfo.js
│   │       │   │   │   │   │       ├── rtti.js
│   │       │   │   │   │   │       ├── selectorParser.js
│   │       │   │   │   │   │       ├── semaphore.js
│   │       │   │   │   │   │       ├── stackTrace.js
│   │       │   │   │   │   │       ├── stringUtils.js
│   │       │   │   │   │   │       ├── time.js
│   │       │   │   │   │   │       ├── timeoutRunner.js
│   │       │   │   │   │   │       ├── types.js
│   │       │   │   │   │   │       ├── urlMatch.js
│   │       │   │   │   │   │       ├── utilityScriptSerializers.js
│   │       │   │   │   │   │       └── yaml.js
│   │       │   │   │   │   ├── utilsBundleImpl/
│   │       │   │   │   │   │   ├── index.js
│   │       │   │   │   │   ├── vite/
│   │       │   │   │   │   │   ├── dashboard/
│   │       │   │   │   │   │   │   ├── assets/
│   │       │   │   │   │   │   │   │   ├── index-BAOybkp8.js
│   │       │   │   │   │   │   │   │   └── index-CZAYOG76.css
│   │       │   │   │   │   │   │   └── index.html
│   │       │   │   │   │   │   ├── htmlReport/
│   │       │   │   │   │   │   │   ├── index.html
│   │       │   │   │   │   │   │   ├── report.css
│   │       │   │   │   │   │   │   └── report.js
│   │       │   │   │   │   │   ├── recorder/
│   │       │   │   │   │   │   │   ├── assets/
│   │       │   │   │   │   │   │   │   ├── codeMirrorModule-C8KMvO9L.js
│   │       │   │   │   │   │   │   │   ├── codeMirrorModule-DYBRYzYX.css
│   │       │   │   │   │   │   │   │   ├── index-BSjZa4pk.css
│   │       │   │   │   │   │   │   │   └── index-CqAYX1I3.js
│   │       │   │   │   │   │   │   ├── index.html
│   │       │   │   │   │   │   └── traceViewer/
│   │       │   │   │   │   │       ├── assets/
│   │       │   │   │   │   │       │   ├── codeMirrorModule-DS0FLvoc.js
│   │       │   │   │   │   │       │   ├── defaultSettingsView-GTWI-W_B.js
│   │       │   │   │   │   │       │   └── xtermModule-CsJ4vdCR.js
│   │       │   │   │   │   │       ├── codeMirrorModule.DYBRYzYX.css
│   │       │   │   │   │   │       ├── defaultSettingsView.B4dS75f0.css
│   │       │   │   │   │   │       ├── index.C5466mMT.js
│   │       │   │   │   │   │       ├── index.CzXZzn5A.css
│   │       │   │   │   │   │       ├── index.html
│   │       │   │   │   │   │       ├── snapshot.html
│   │       │   │   │   │   │       ├── sw.bundle.js
│   │       │   │   │   │   │       ├── uiMode.Btcz36p_.css
│   │       │   │   │   │   │       ├── uiMode.html
│   │       │   │   │   │   │       ├── uiMode.Vipi55dB.js
│   │       │   │   │   │   │       └── xtermModule.DYP7pi_n.css
│   │       │   │   │   │   ├── androidServerImpl.js
│   │       │   │   │   │   ├── bootstrap.js
│   │       │   │   │   │   ├── browserServerImpl.js
│   │       │   │   │   │   ├── inprocess.js
│   │       │   │   │   │   ├── inProcessFactory.js
│   │       │   │   │   │   ├── mcpBundle.js
│   │       │   │   │   │   ├── mcpBundleImpl.js
│   │       │   │   │   │   ├── outofprocess.js
│   │       │   │   │   │   ├── serverRegistry.js
│   │       │   │   │   │   ├── utils.js
│   │       │   │   │   │   ├── utilsBundle.js
│   │       │   │   │   │   ├── zipBundle.js
│   │       │   │   │   │   ├── zipBundleImpl.js
│   │       │   │   │   │   ├── zodBundle.js
│   │       │   │   │   │   └── zodBundleImpl.js
│   │       │   │   │   ├── types/
│   │       │   │   │   ├── api.json
│   │       │   │   │   ├── browsers.json
│   │       │   │   │   ├── cli.js
│   │       │   │   │   ├── index.js
│   │       │   │   │   ├── package.json
│   │       │   │   │   ├── protocol.yml
│   │       │   │   │   ├── README.md
│   │       │   │   │   └── ThirdPartyNotices.txt
│   │       │   │   └── README.md
│   │       │   ├── sync_api/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _context_manager.py
│   │       │   │   └── _generated.py
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── _repo_version.py
│   │       ├── playwright-1.59.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       │   ├── top_level.txt
│   │       ├── pluggy/
│   │       │   ├── __init__.py
│   │       │   ├── _callers.py
│   │       │   ├── _hooks.py
│   │       │   ├── _manager.py
│   │       │   ├── _result.py
│   │       │   ├── _tracing.py
│   │       │   ├── _version.py
│   │       │   ├── _warnings.py
│   │       ├── pluggy-1.6.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── pycparser/
│   │       │   ├── __init__.py
│   │       │   ├── _ast_gen.py
│   │       │   ├── ast_transforms.py
│   │       │   ├── c_ast.py
│   │       │   ├── c_generator.py
│   │       │   ├── c_lexer.py
│   │       │   └── c_parser.py
│   │       ├── pycparser-3.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── pydantic/
│   │       │   ├── _internal/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _config.py
│   │       │   │   ├── _core_metadata.py
│   │       │   │   ├── _core_utils.py
│   │       │   │   ├── _dataclasses.py
│   │       │   │   ├── _decorators.py
│   │       │   │   ├── _decorators_v1.py
│   │       │   │   ├── _discriminated_union.py
│   │       │   │   ├── _docs_extraction.py
│   │       │   │   ├── _fields.py
│   │       │   │   ├── _forward_ref.py
│   │       │   │   ├── _generate_schema.py
│   │       │   │   ├── _generics.py
│   │       │   │   ├── _git.py
│   │       │   │   ├── _import_utils.py
│   │       │   │   ├── _internal_dataclass.py
│   │       │   │   ├── _known_annotated_metadata.py
│   │       │   │   ├── _mock_val_ser.py
│   │       │   │   ├── _model_construction.py
│   │       │   │   ├── _namespace_utils.py
│   │       │   │   ├── _repr.py
│   │       │   │   ├── _schema_gather.py
│   │       │   │   ├── _schema_generation_shared.py
│   │       │   │   ├── _serializers.py
│   │       │   │   ├── _signature.py
│   │       │   │   ├── _typing_extra.py
│   │       │   │   ├── _utils.py
│   │       │   │   ├── _validate_call.py
│   │       │   │   └── _validators.py
│   │       │   ├── deprecated/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── class_validators.py
│   │       │   │   ├── config.py
│   │       │   │   ├── copy_internals.py
│   │       │   │   ├── decorator.py
│   │       │   │   ├── json.py
│   │       │   │   ├── parse.py
│   │       │   │   └── tools.py
│   │       │   ├── experimental/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── arguments_schema.py
│   │       │   │   ├── missing_sentinel.py
│   │       │   │   └── pipeline.py
│   │       │   ├── plugin/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _loader.py
│   │       │   │   └── _schema_validator.py
│   │       │   ├── v1/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _hypothesis_plugin.py
│   │       │   │   ├── annotated_types.py
│   │       │   │   ├── class_validators.py
│   │       │   │   ├── color.py
│   │       │   │   ├── config.py
│   │       │   │   ├── dataclasses.py
│   │       │   │   ├── datetime_parse.py
│   │       │   │   ├── decorator.py
│   │       │   │   ├── env_settings.py
│   │       │   │   ├── error_wrappers.py
│   │       │   │   ├── errors.py
│   │       │   │   ├── fields.py
│   │       │   │   ├── generics.py
│   │       │   │   ├── json.py
│   │       │   │   ├── main.py
│   │       │   │   ├── mypy.py
│   │       │   │   ├── networks.py
│   │       │   │   ├── parse.py
│   │       │   │   ├── schema.py
│   │       │   │   ├── tools.py
│   │       │   │   ├── types.py
│   │       │   │   ├── typing.py
│   │       │   │   ├── utils.py
│   │       │   │   ├── validators.py
│   │       │   │   └── version.py
│   │       │   ├── __init__.py
│   │       │   ├── _migration.py
│   │       │   ├── alias_generators.py
│   │       │   ├── aliases.py
│   │       │   ├── annotated_handlers.py
│   │       │   ├── class_validators.py
│   │       │   ├── color.py
│   │       │   ├── config.py
│   │       │   ├── dataclasses.py
│   │       │   ├── datetime_parse.py
│   │       │   ├── decorator.py
│   │       │   ├── env_settings.py
│   │       │   ├── error_wrappers.py
│   │       │   ├── errors.py
│   │       │   ├── fields.py
│   │       │   ├── functional_serializers.py
│   │       │   ├── functional_validators.py
│   │       │   ├── generics.py
│   │       │   ├── json.py
│   │       │   ├── json_schema.py
│   │       │   ├── main.py
│   │       │   ├── mypy.py
│   │       │   ├── networks.py
│   │       │   ├── parse.py
│   │       │   ├── root_model.py
│   │       │   ├── schema.py
│   │       │   ├── tools.py
│   │       │   ├── type_adapter.py
│   │       │   ├── types.py
│   │       │   ├── typing.py
│   │       │   ├── utils.py
│   │       │   ├── validate_call_decorator.py
│   │       │   ├── validators.py
│   │       │   ├── version.py
│   │       │   └── warnings.py
│   │       ├── pydantic-2.13.4.dist-info/
│   │       │   ├── licenses/
│   │       ├── pydantic_core/
│   │       │   ├── __init__.py
│   │       │   ├── core_schema.py
│   │       ├── pydantic_core-2.46.4.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── sboms/
│   │       │   │   └── pydantic-core.cyclonedx.json
│   │       ├── pyee/
│   │       │   ├── __init__.py
│   │       │   ├── asyncio.py
│   │       │   ├── base.py
│   │       │   ├── cls.py
│   │       │   ├── executor.py
│   │       │   ├── trio.py
│   │       │   ├── twisted.py
│   │       │   └── uplift.py
│   │       ├── pyee-13.0.1.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── pygments/
│   │       │   ├── filters/
│   │       │   │   └── __init__.py
│   │       │   ├── formatters/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _mapping.py
│   │       │   │   ├── bbcode.py
│   │       │   │   ├── groff.py
│   │       │   │   ├── html.py
│   │       │   │   ├── img.py
│   │       │   │   ├── irc.py
│   │       │   │   ├── latex.py
│   │       │   │   ├── other.py
│   │       │   │   ├── pangomarkup.py
│   │       │   │   ├── rtf.py
│   │       │   │   ├── svg.py
│   │       │   │   ├── terminal.py
│   │       │   │   └── terminal256.py
│   │       │   ├── lexers/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _ada_builtins.py
│   │       │   │   ├── _asy_builtins.py
│   │       │   │   ├── _cl_builtins.py
│   │       │   │   ├── _cocoa_builtins.py
│   │       │   │   ├── _csound_builtins.py
│   │       │   │   ├── _css_builtins.py
│   │       │   │   ├── _googlesql_builtins.py
│   │       │   │   ├── _julia_builtins.py
│   │       │   │   ├── _lasso_builtins.py
│   │       │   │   ├── _lilypond_builtins.py
│   │       │   │   ├── _lua_builtins.py
│   │       │   │   ├── _luau_builtins.py
│   │       │   │   ├── _mapping.py
│   │       │   │   ├── _mql_builtins.py
│   │       │   │   ├── _mysql_builtins.py
│   │       │   │   ├── _openedge_builtins.py
│   │       │   │   ├── _php_builtins.py
│   │       │   │   ├── _postgres_builtins.py
│   │       │   │   ├── _qlik_builtins.py
│   │       │   │   ├── _scheme_builtins.py
│   │       │   │   ├── _scilab_builtins.py
│   │       │   │   ├── _sourcemod_builtins.py
│   │       │   │   ├── _sql_builtins.py
│   │       │   │   ├── _stan_builtins.py
│   │       │   │   ├── _stata_builtins.py
│   │       │   │   ├── _tsql_builtins.py
│   │       │   │   ├── _usd_builtins.py
│   │       │   │   ├── _vbscript_builtins.py
│   │       │   │   ├── _vim_builtins.py
│   │       │   │   ├── actionscript.py
│   │       │   │   ├── ada.py
│   │       │   │   ├── agile.py
│   │       │   │   ├── algebra.py
│   │       │   │   ├── ambient.py
│   │       │   │   ├── amdgpu.py
│   │       │   │   ├── ampl.py
│   │       │   │   ├── apdlexer.py
│   │       │   │   ├── apl.py
│   │       │   │   ├── archetype.py
│   │       │   │   ├── arrow.py
│   │       │   │   ├── arturo.py
│   │       │   │   ├── asc.py
│   │       │   │   ├── asm.py
│   │       │   │   ├── asn1.py
│   │       │   │   ├── automation.py
│   │       │   │   ├── bare.py
│   │       │   │   ├── basic.py
│   │       │   │   ├── bdd.py
│   │       │   │   ├── berry.py
│   │       │   │   ├── bibtex.py
│   │       │   │   ├── blueprint.py
│   │       │   │   ├── boa.py
│   │       │   │   ├── bqn.py
│   │       │   │   ├── business.py
│   │       │   │   ├── c_cpp.py
│   │       │   │   ├── c_like.py
│   │       │   │   ├── capnproto.py
│   │       │   │   ├── carbon.py
│   │       │   │   ├── cddl.py
│   │       │   │   ├── chapel.py
│   │       │   │   ├── clean.py
│   │       │   │   ├── codeql.py
│   │       │   │   ├── comal.py
│   │       │   │   ├── compiled.py
│   │       │   │   ├── configs.py
│   │       │   │   ├── console.py
│   │       │   │   ├── cplint.py
│   │       │   │   ├── crystal.py
│   │       │   │   ├── csound.py
│   │       │   │   ├── css.py
│   │       │   │   ├── d.py
│   │       │   │   ├── dalvik.py
│   │       │   │   ├── data.py
│   │       │   │   ├── dax.py
│   │       │   │   ├── devicetree.py
│   │       │   │   ├── diff.py
│   │       │   │   ├── dns.py
│   │       │   │   ├── dotnet.py
│   │       │   │   ├── dsls.py
│   │       │   │   ├── dylan.py
│   │       │   │   ├── ecl.py
│   │       │   │   ├── eiffel.py
│   │       │   │   ├── elm.py
│   │       │   │   ├── elpi.py
│   │       │   │   ├── email.py
│   │       │   │   ├── erlang.py
│   │       │   │   ├── esoteric.py
│   │       │   │   ├── ezhil.py
│   │       │   │   ├── factor.py
│   │       │   │   ├── fantom.py
│   │       │   │   ├── felix.py
│   │       │   │   ├── fift.py
│   │       │   │   ├── floscript.py
│   │       │   │   ├── forth.py
│   │       │   │   ├── fortran.py
│   │       │   │   ├── foxpro.py
│   │       │   │   ├── freefem.py
│   │       │   │   ├── func.py
│   │       │   │   ├── functional.py
│   │       │   │   ├── futhark.py
│   │       │   │   ├── gcodelexer.py
│   │       │   │   ├── gdscript.py
│   │       │   │   ├── gleam.py
│   │       │   │   ├── go.py
│   │       │   │   ├── grammar_notation.py
│   │       │   │   ├── graph.py
│   │       │   │   ├── graphics.py
│   │       │   │   ├── graphql.py
│   │       │   │   ├── graphviz.py
│   │       │   │   ├── gsql.py
│   │       │   │   ├── hare.py
│   │       │   │   ├── haskell.py
│   │       │   │   ├── haxe.py
│   │       │   │   ├── hdl.py
│   │       │   │   ├── hexdump.py
│   │       │   │   ├── html.py
│   │       │   │   ├── idl.py
│   │       │   │   ├── igor.py
│   │       │   │   ├── inferno.py
│   │       │   │   ├── installers.py
│   │       │   │   ├── int_fiction.py
│   │       │   │   ├── iolang.py
│   │       │   │   ├── j.py
│   │       │   │   ├── javascript.py
│   │       │   │   ├── jmespath.py
│   │       │   │   ├── jslt.py
│   │       │   │   ├── json5.py
│   │       │   │   ├── jsonnet.py
│   │       │   │   ├── jsx.py
│   │       │   │   ├── julia.py
│   │       │   │   ├── jvm.py
│   │       │   │   ├── kuin.py
│   │       │   │   ├── kusto.py
│   │       │   │   ├── ldap.py
│   │       │   │   ├── lean.py
│   │       │   │   ├── lilypond.py
│   │       │   │   ├── lisp.py
│   │       │   │   ├── macaulay2.py
│   │       │   │   ├── make.py
│   │       │   │   ├── maple.py
│   │       │   │   ├── markup.py
│   │       │   │   ├── math.py
│   │       │   │   ├── matlab.py
│   │       │   │   ├── maxima.py
│   │       │   │   ├── meson.py
│   │       │   │   ├── mime.py
│   │       │   │   ├── minecraft.py
│   │       │   │   ├── mips.py
│   │       │   │   ├── ml.py
│   │       │   │   ├── modeling.py
│   │       │   │   ├── modula2.py
│   │       │   │   ├── mojo.py
│   │       │   │   ├── monte.py
│   │       │   │   ├── mosel.py
│   │       │   │   ├── ncl.py
│   │       │   │   ├── nimrod.py
│   │       │   │   ├── nit.py
│   │       │   │   ├── nix.py
│   │       │   │   ├── numbair.py
│   │       │   │   ├── oberon.py
│   │       │   │   ├── objective.py
│   │       │   │   ├── ooc.py
│   │       │   │   ├── openscad.py
│   │       │   │   ├── other.py
│   │       │   │   ├── parasail.py
│   │       │   │   ├── parsers.py
│   │       │   │   ├── pascal.py
│   │       │   │   ├── pawn.py
│   │       │   │   ├── pddl.py
│   │       │   │   ├── perl.py
│   │       │   │   ├── phix.py
│   │       │   │   ├── php.py
│   │       │   │   ├── pointless.py
│   │       │   │   ├── pony.py
│   │       │   │   ├── praat.py
│   │       │   │   ├── procfile.py
│   │       │   │   ├── prolog.py
│   │       │   │   ├── promql.py
│   │       │   │   ├── prql.py
│   │       │   │   ├── ptx.py
│   │       │   │   ├── python.py
│   │       │   │   ├── q.py
│   │       │   │   ├── qlik.py
│   │       │   │   ├── qvt.py
│   │       │   │   ├── r.py
│   │       │   │   ├── rdf.py
│   │       │   │   ├── rebol.py
│   │       │   │   ├── rego.py
│   │       │   │   ├── rell.py
│   │       │   │   ├── resource.py
│   │       │   │   ├── ride.py
│   │       │   │   ├── rita.py
│   │       │   │   ├── rnc.py
│   │       │   │   ├── roboconf.py
│   │       │   │   ├── robotframework.py
│   │       │   │   ├── ruby.py
│   │       │   │   ├── rust.py
│   │       │   │   ├── sas.py
│   │       │   │   ├── savi.py
│   │       │   │   ├── scdoc.py
│   │       │   │   ├── scripting.py
│   │       │   │   ├── sgf.py
│   │       │   │   ├── shell.py
│   │       │   │   ├── sieve.py
│   │       │   │   ├── slash.py
│   │       │   │   ├── smalltalk.py
│   │       │   │   ├── smithy.py
│   │       │   │   ├── smv.py
│   │       │   │   ├── snobol.py
│   │       │   │   ├── solidity.py
│   │       │   │   ├── soong.py
│   │       │   │   ├── sophia.py
│   │       │   │   ├── special.py
│   │       │   │   ├── spice.py
│   │       │   │   ├── sql.py
│   │       │   │   ├── srcinfo.py
│   │       │   │   ├── stata.py
│   │       │   │   ├── supercollider.py
│   │       │   │   ├── tablegen.py
│   │       │   │   ├── tact.py
│   │       │   │   ├── tal.py
│   │       │   │   ├── tcl.py
│   │       │   │   ├── teal.py
│   │       │   │   ├── templates.py
│   │       │   │   ├── teraterm.py
│   │       │   │   ├── testing.py
│   │       │   │   ├── text.py
│   │       │   │   ├── textedit.py
│   │       │   │   ├── textfmts.py
│   │       │   │   ├── theorem.py
│   │       │   │   ├── thingsdb.py
│   │       │   │   ├── tlb.py
│   │       │   │   ├── tls.py
│   │       │   │   ├── tnt.py
│   │       │   │   ├── trafficscript.py
│   │       │   │   ├── typoscript.py
│   │       │   │   ├── typst.py
│   │       │   │   ├── ul4.py
│   │       │   │   ├── unicon.py
│   │       │   │   ├── urbi.py
│   │       │   │   ├── usd.py
│   │       │   │   ├── varnish.py
│   │       │   │   ├── verification.py
│   │       │   │   ├── verifpal.py
│   │       │   │   ├── vip.py
│   │       │   │   ├── vyper.py
│   │       │   │   ├── web.py
│   │       │   │   ├── webassembly.py
│   │       │   │   ├── webidl.py
│   │       │   │   ├── webmisc.py
│   │       │   │   ├── wgsl.py
│   │       │   │   ├── whiley.py
│   │       │   │   ├── wowtoc.py
│   │       │   │   ├── wren.py
│   │       │   │   ├── x10.py
│   │       │   │   ├── xorg.py
│   │       │   │   ├── yang.py
│   │       │   │   ├── yara.py
│   │       │   │   └── zig.py
│   │       │   ├── styles/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _mapping.py
│   │       │   │   ├── abap.py
│   │       │   │   ├── algol.py
│   │       │   │   ├── algol_nu.py
│   │       │   │   ├── arduino.py
│   │       │   │   ├── autumn.py
│   │       │   │   ├── borland.py
│   │       │   │   ├── bw.py
│   │       │   │   ├── coffee.py
│   │       │   │   ├── colorful.py
│   │       │   │   ├── default.py
│   │       │   │   ├── dracula.py
│   │       │   │   ├── emacs.py
│   │       │   │   ├── friendly.py
│   │       │   │   ├── friendly_grayscale.py
│   │       │   │   ├── fruity.py
│   │       │   │   ├── gh_dark.py
│   │       │   │   ├── gruvbox.py
│   │       │   │   ├── igor.py
│   │       │   │   ├── inkpot.py
│   │       │   │   ├── lightbulb.py
│   │       │   │   ├── lilypond.py
│   │       │   │   ├── lovelace.py
│   │       │   │   ├── manni.py
│   │       │   │   ├── material.py
│   │       │   │   ├── monokai.py
│   │       │   │   ├── murphy.py
│   │       │   │   ├── native.py
│   │       │   │   ├── nord.py
│   │       │   │   ├── onedark.py
│   │       │   │   ├── paraiso_dark.py
│   │       │   │   ├── paraiso_light.py
│   │       │   │   ├── pastie.py
│   │       │   │   ├── perldoc.py
│   │       │   │   ├── rainbow_dash.py
│   │       │   │   ├── rrt.py
│   │       │   │   ├── sas.py
│   │       │   │   ├── solarized.py
│   │       │   │   ├── staroffice.py
│   │       │   │   ├── stata_dark.py
│   │       │   │   ├── stata_light.py
│   │       │   │   ├── tango.py
│   │       │   │   ├── trac.py
│   │       │   │   ├── vim.py
│   │       │   │   ├── vs.py
│   │       │   │   ├── xcode.py
│   │       │   │   └── zenburn.py
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── cmdline.py
│   │       │   ├── console.py
│   │       │   ├── filter.py
│   │       │   ├── formatter.py
│   │       │   ├── lexer.py
│   │       │   ├── modeline.py
│   │       │   ├── plugin.py
│   │       │   ├── regexopt.py
│   │       │   ├── scanner.py
│   │       │   ├── sphinxext.py
│   │       │   ├── style.py
│   │       │   ├── token.py
│   │       │   ├── unistring.py
│   │       │   └── util.py
│   │       ├── pygments-2.20.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       ├── pymysql/
│   │       │   ├── constants/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── CLIENT.py
│   │       │   │   ├── COMMAND.py
│   │       │   │   ├── CR.py
│   │       │   │   ├── ER.py
│   │       │   │   ├── FIELD_TYPE.py
│   │       │   │   ├── FLAG.py
│   │       │   │   └── SERVER_STATUS.py
│   │       │   ├── __init__.py
│   │       │   ├── _auth.py
│   │       │   ├── charset.py
│   │       │   ├── connections.py
│   │       │   ├── converters.py
│   │       │   ├── cursors.py
│   │       │   ├── err.py
│   │       │   ├── optionfile.py
│   │       │   ├── protocol.py
│   │       │   └── times.py
│   │       ├── pymysql-1.1.3.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── PySocks-1.7.1.dist-info/
│   │       │   ├── top_level.txt
│   │       ├── pytest/
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       ├── pytest-9.0.3.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       │   ├── top_level.txt
│   │       ├── pytest_asyncio/
│   │       │   ├── __init__.py
│   │       │   ├── plugin.py
│   │       ├── pytest_asyncio-1.3.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       │   ├── top_level.txt
│   │       ├── python_dotenv-1.2.2.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       │   ├── top_level.txt
│   │       ├── requests/
│   │       │   ├── __init__.py
│   │       │   ├── __version__.py
│   │       │   ├── _internal_utils.py
│   │       │   ├── _types.py
│   │       │   ├── adapters.py
│   │       │   ├── api.py
│   │       │   ├── auth.py
│   │       │   ├── certs.py
│   │       │   ├── compat.py
│   │       │   ├── cookies.py
│   │       │   ├── exceptions.py
│   │       │   ├── help.py
│   │       │   ├── hooks.py
│   │       │   ├── models.py
│   │       │   ├── packages.py
│   │       │   ├── sessions.py
│   │       │   ├── status_codes.py
│   │       │   ├── structures.py
│   │       │   └── utils.py
│   │       ├── requests-2.34.2.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── selenium/
│   │       │   ├── common/
│   │       │   │   ├── __init__.py
│   │       │   │   └── exceptions.py
│   │       │   ├── webdriver/
│   │       │   │   ├── chrome/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── options.py
│   │       │   │   │   ├── remote_connection.py
│   │       │   │   │   ├── service.py
│   │       │   │   │   └── webdriver.py
│   │       │   │   ├── chromium/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── options.py
│   │       │   │   │   ├── remote_connection.py
│   │       │   │   │   ├── service.py
│   │       │   │   │   └── webdriver.py
│   │       │   │   ├── common/
│   │       │   │   │   ├── actions/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── action_builder.py
│   │       │   │   │   │   ├── input_device.py
│   │       │   │   │   │   ├── interaction.py
│   │       │   │   │   │   ├── key_actions.py
│   │       │   │   │   │   ├── key_input.py
│   │       │   │   │   │   ├── mouse_button.py
│   │       │   │   │   │   ├── pointer_actions.py
│   │       │   │   │   │   ├── pointer_input.py
│   │       │   │   │   │   ├── wheel_actions.py
│   │       │   │   │   │   └── wheel_input.py
│   │       │   │   │   ├── bidi/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── _event_manager.py
│   │       │   │   │   │   ├── bluetooth.py
│   │       │   │   │   │   ├── browser.py
│   │       │   │   │   │   ├── browsing_context.py
│   │       │   │   │   │   ├── cdp.py
│   │       │   │   │   │   ├── common.py
│   │       │   │   │   │   ├── console.py
│   │       │   │   │   │   ├── emulation.py
│   │       │   │   │   │   ├── input.py
│   │       │   │   │   │   ├── log.py
│   │       │   │   │   │   ├── network.py
│   │       │   │   │   │   ├── permissions.py
│   │       │   │   │   │   ├── script.py
│   │       │   │   │   │   ├── session.py
│   │       │   │   │   │   ├── speculation.py
│   │       │   │   │   │   ├── storage.py
│   │       │   │   │   │   ├── user_agent_client_hints.py
│   │       │   │   │   │   └── webextension.py
│   │       │   │   │   ├── devtools/
│   │       │   │   │   │   ├── latest/
│   │       │   │   │   │   │   └── __init__.py
│   │       │   │   │   │   ├── v146/
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   ├── accessibility.py
│   │       │   │   │   │   │   ├── animation.py
│   │       │   │   │   │   │   ├── audits.py
│   │       │   │   │   │   │   ├── autofill.py
│   │       │   │   │   │   │   ├── background_service.py
│   │       │   │   │   │   │   ├── bluetooth_emulation.py
│   │       │   │   │   │   │   ├── browser.py
│   │       │   │   │   │   │   ├── cache_storage.py
│   │       │   │   │   │   │   ├── cast.py
│   │       │   │   │   │   │   ├── console.py
│   │       │   │   │   │   │   ├── css.py
│   │       │   │   │   │   │   ├── debugger.py
│   │       │   │   │   │   │   ├── device_access.py
│   │       │   │   │   │   │   ├── device_orientation.py
│   │       │   │   │   │   │   ├── dom.py
│   │       │   │   │   │   │   ├── dom_debugger.py
│   │       │   │   │   │   │   ├── dom_snapshot.py
│   │       │   │   │   │   │   ├── dom_storage.py
│   │       │   │   │   │   │   ├── emulation.py
│   │       │   │   │   │   │   ├── event_breakpoints.py
│   │       │   │   │   │   │   ├── extensions.py
│   │       │   │   │   │   │   ├── fed_cm.py
│   │       │   │   │   │   │   ├── fetch.py
│   │       │   │   │   │   │   ├── file_system.py
│   │       │   │   │   │   │   ├── headless_experimental.py
│   │       │   │   │   │   │   ├── heap_profiler.py
│   │       │   │   │   │   │   ├── indexed_db.py
│   │       │   │   │   │   │   ├── input_.py
│   │       │   │   │   │   │   ├── inspector.py
│   │       │   │   │   │   │   ├── io.py
│   │       │   │   │   │   │   ├── layer_tree.py
│   │       │   │   │   │   │   ├── log.py
│   │       │   │   │   │   │   ├── media.py
│   │       │   │   │   │   │   ├── memory.py
│   │       │   │   │   │   │   ├── network.py
│   │       │   │   │   │   │   ├── overlay.py
│   │       │   │   │   │   │   ├── page.py
│   │       │   │   │   │   │   ├── performance.py
│   │       │   │   │   │   │   ├── performance_timeline.py
│   │       │   │   │   │   │   ├── preload.py
│   │       │   │   │   │   │   ├── profiler.py
│   │       │   │   │   │   │   ├── pwa.py
│   │       │   │   │   │   │   ├── runtime.py
│   │       │   │   │   │   │   ├── schema.py
│   │       │   │   │   │   │   ├── security.py
│   │       │   │   │   │   │   ├── service_worker.py
│   │       │   │   │   │   │   ├── smart_card_emulation.py
│   │       │   │   │   │   │   ├── storage.py
│   │       │   │   │   │   │   ├── system_info.py
│   │       │   │   │   │   │   ├── target.py
│   │       │   │   │   │   │   ├── tethering.py
│   │       │   │   │   │   │   ├── tracing.py
│   │       │   │   │   │   │   ├── util.py
│   │       │   │   │   │   │   ├── web_audio.py
│   │       │   │   │   │   │   └── web_authn.py
│   │       │   │   │   │   ├── v147/
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   ├── accessibility.py
│   │       │   │   │   │   │   ├── animation.py
│   │       │   │   │   │   │   ├── audits.py
│   │       │   │   │   │   │   ├── autofill.py
│   │       │   │   │   │   │   ├── background_service.py
│   │       │   │   │   │   │   ├── bluetooth_emulation.py
│   │       │   │   │   │   │   ├── browser.py
│   │       │   │   │   │   │   ├── cache_storage.py
│   │       │   │   │   │   │   ├── cast.py
│   │       │   │   │   │   │   ├── console.py
│   │       │   │   │   │   │   ├── css.py
│   │       │   │   │   │   │   ├── debugger.py
│   │       │   │   │   │   │   ├── device_access.py
│   │       │   │   │   │   │   ├── device_orientation.py
│   │       │   │   │   │   │   ├── dom.py
│   │       │   │   │   │   │   ├── dom_debugger.py
│   │       │   │   │   │   │   ├── dom_snapshot.py
│   │       │   │   │   │   │   ├── dom_storage.py
│   │       │   │   │   │   │   ├── emulation.py
│   │       │   │   │   │   │   ├── event_breakpoints.py
│   │       │   │   │   │   │   ├── extensions.py
│   │       │   │   │   │   │   ├── fed_cm.py
│   │       │   │   │   │   │   ├── fetch.py
│   │       │   │   │   │   │   ├── file_system.py
│   │       │   │   │   │   │   ├── headless_experimental.py
│   │       │   │   │   │   │   ├── heap_profiler.py
│   │       │   │   │   │   │   ├── indexed_db.py
│   │       │   │   │   │   │   ├── input_.py
│   │       │   │   │   │   │   ├── inspector.py
│   │       │   │   │   │   │   ├── io.py
│   │       │   │   │   │   │   ├── layer_tree.py
│   │       │   │   │   │   │   ├── log.py
│   │       │   │   │   │   │   ├── media.py
│   │       │   │   │   │   │   ├── memory.py
│   │       │   │   │   │   │   ├── network.py
│   │       │   │   │   │   │   ├── overlay.py
│   │       │   │   │   │   │   ├── page.py
│   │       │   │   │   │   │   ├── performance.py
│   │       │   │   │   │   │   ├── performance_timeline.py
│   │       │   │   │   │   │   ├── preload.py
│   │       │   │   │   │   │   ├── profiler.py
│   │       │   │   │   │   │   ├── pwa.py
│   │       │   │   │   │   │   ├── runtime.py
│   │       │   │   │   │   │   ├── schema.py
│   │       │   │   │   │   │   ├── security.py
│   │       │   │   │   │   │   ├── service_worker.py
│   │       │   │   │   │   │   ├── smart_card_emulation.py
│   │       │   │   │   │   │   ├── storage.py
│   │       │   │   │   │   │   ├── system_info.py
│   │       │   │   │   │   │   ├── target.py
│   │       │   │   │   │   │   ├── tethering.py
│   │       │   │   │   │   │   ├── tracing.py
│   │       │   │   │   │   │   ├── util.py
│   │       │   │   │   │   │   ├── web_audio.py
│   │       │   │   │   │   │   ├── web_authn.py
│   │       │   │   │   │   │   └── web_mcp.py
│   │       │   │   │   │   └── v148/
│   │       │   │   │   │       ├── __init__.py
│   │       │   │   │   │       ├── accessibility.py
│   │       │   │   │   │       ├── animation.py
│   │       │   │   │   │       ├── audits.py
│   │       │   │   │   │       ├── autofill.py
│   │       │   │   │   │       ├── background_service.py
│   │       │   │   │   │       ├── bluetooth_emulation.py
│   │       │   │   │   │       ├── browser.py
│   │       │   │   │   │       ├── cache_storage.py
│   │       │   │   │   │       ├── cast.py
│   │       │   │   │   │       ├── console.py
│   │       │   │   │   │       ├── crash_report_context.py
│   │       │   │   │   │       ├── css.py
│   │       │   │   │   │       ├── debugger.py
│   │       │   │   │   │       ├── device_access.py
│   │       │   │   │   │       ├── device_orientation.py
│   │       │   │   │   │       ├── dom.py
│   │       │   │   │   │       ├── dom_debugger.py
│   │       │   │   │   │       ├── dom_snapshot.py
│   │       │   │   │   │       ├── dom_storage.py
│   │       │   │   │   │       ├── emulation.py
│   │       │   │   │   │       ├── event_breakpoints.py
│   │       │   │   │   │       ├── extensions.py
│   │       │   │   │   │       ├── fed_cm.py
│   │       │   │   │   │       ├── fetch.py
│   │       │   │   │   │       ├── file_system.py
│   │       │   │   │   │       ├── headless_experimental.py
│   │       │   │   │   │       ├── heap_profiler.py
│   │       │   │   │   │       ├── indexed_db.py
│   │       │   │   │   │       ├── input_.py
│   │       │   │   │   │       ├── inspector.py
│   │       │   │   │   │       ├── io.py
│   │       │   │   │   │       ├── layer_tree.py
│   │       │   │   │   │       ├── log.py
│   │       │   │   │   │       ├── media.py
│   │       │   │   │   │       ├── memory.py
│   │       │   │   │   │       ├── network.py
│   │       │   │   │   │       ├── overlay.py
│   │       │   │   │   │       ├── page.py
│   │       │   │   │   │       ├── performance.py
│   │       │   │   │   │       ├── performance_timeline.py
│   │       │   │   │   │       ├── preload.py
│   │       │   │   │   │       ├── profiler.py
│   │       │   │   │   │       ├── pwa.py
│   │       │   │   │   │       ├── runtime.py
│   │       │   │   │   │       ├── schema.py
│   │       │   │   │   │       ├── security.py
│   │       │   │   │   │       ├── service_worker.py
│   │       │   │   │   │       ├── smart_card_emulation.py
│   │       │   │   │   │       ├── storage.py
│   │       │   │   │   │       ├── system_info.py
│   │       │   │   │   │       ├── target.py
│   │       │   │   │   │       ├── tethering.py
│   │       │   │   │   │       ├── tracing.py
│   │       │   │   │   │       ├── util.py
│   │       │   │   │   │       ├── web_audio.py
│   │       │   │   │   │       ├── web_authn.py
│   │       │   │   │   │       └── web_mcp.py
│   │       │   │   │   ├── fedcm/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── account.py
│   │       │   │   │   │   └── dialog.py
│   │       │   │   │   ├── linux/
│   │       │   │   │   ├── macos/
│   │       │   │   │   ├── windows/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── action_chains.py
│   │       │   │   │   ├── alert.py
│   │       │   │   │   ├── api_request_context.py
│   │       │   │   │   ├── bidi-mutation-listener.js
│   │       │   │   │   ├── by.py
│   │       │   │   │   ├── desired_capabilities.py
│   │       │   │   │   ├── driver_finder.py
│   │       │   │   │   ├── keys.py
│   │       │   │   │   ├── log.py
│   │       │   │   │   ├── mutation-listener.js
│   │       │   │   │   ├── options.py
│   │       │   │   │   ├── print_page_options.py
│   │       │   │   │   ├── proxy.py
│   │       │   │   │   ├── selenium_manager.py
│   │       │   │   │   ├── service.py
│   │       │   │   │   ├── timeouts.py
│   │       │   │   │   ├── utils.py
│   │       │   │   │   ├── virtual_authenticator.py
│   │       │   │   │   ├── webdriver.py
│   │       │   │   │   └── window.py
│   │       │   │   ├── edge/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── options.py
│   │       │   │   │   ├── remote_connection.py
│   │       │   │   │   ├── service.py
│   │       │   │   │   └── webdriver.py
│   │       │   │   ├── firefox/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── firefox_profile.py
│   │       │   │   │   ├── options.py
│   │       │   │   │   ├── remote_connection.py
│   │       │   │   │   ├── service.py
│   │       │   │   │   ├── webdriver.py
│   │       │   │   │   └── webdriver_prefs.json
│   │       │   │   ├── ie/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── options.py
│   │       │   │   │   ├── service.py
│   │       │   │   │   └── webdriver.py
│   │       │   │   ├── remote/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── bidi_connection.py
│   │       │   │   │   ├── client_config.py
│   │       │   │   │   ├── command.py
│   │       │   │   │   ├── errorhandler.py
│   │       │   │   │   ├── fedcm.py
│   │       │   │   │   ├── file_detector.py
│   │       │   │   │   ├── findElements.js
│   │       │   │   │   ├── getAttribute.js
│   │       │   │   │   ├── isDisplayed.js
│   │       │   │   │   ├── locator_converter.py
│   │       │   │   │   ├── mobile.py
│   │       │   │   │   ├── remote_connection.py
│   │       │   │   │   ├── script_key.py
│   │       │   │   │   ├── server.py
│   │       │   │   │   ├── shadowroot.py
│   │       │   │   │   ├── switch_to.py
│   │       │   │   │   ├── utils.py
│   │       │   │   │   ├── webdriver.py
│   │       │   │   │   ├── webelement.py
│   │       │   │   │   └── websocket_connection.py
│   │       │   │   ├── safari/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── options.py
│   │       │   │   │   ├── permissions.py
│   │       │   │   │   ├── remote_connection.py
│   │       │   │   │   ├── service.py
│   │       │   │   │   └── webdriver.py
│   │       │   │   ├── support/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── abstract_event_listener.py
│   │       │   │   │   ├── color.py
│   │       │   │   │   ├── event_firing_webdriver.py
│   │       │   │   │   ├── events.py
│   │       │   │   │   ├── expected_conditions.py
│   │       │   │   │   ├── relative_locator.py
│   │       │   │   │   ├── select.py
│   │       │   │   │   ├── ui.py
│   │       │   │   │   └── wait.py
│   │       │   │   ├── webkitgtk/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── options.py
│   │       │   │   │   ├── service.py
│   │       │   │   │   └── webdriver.py
│   │       │   │   ├── wpewebkit/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── options.py
│   │       │   │   │   ├── service.py
│   │       │   │   │   └── webdriver.py
│   │       │   │   ├── __init__.py
│   │       │   ├── __init__.py
│   │       ├── selenium-4.44.0.dist-info/
│   │       ├── sniffio/
│   │       │   ├── _tests/
│   │       │   │   ├── __init__.py
│   │       │   │   └── test_sniffio.py
│   │       │   ├── __init__.py
│   │       │   ├── _impl.py
│   │       │   ├── _version.py
│   │       ├── sniffio-1.3.1.dist-info/
│   │       │   ├── top_level.txt
│   │       ├── sortedcontainers/
│   │       │   ├── __init__.py
│   │       │   ├── sorteddict.py
│   │       │   ├── sortedlist.py
│   │       │   └── sortedset.py
│   │       ├── sortedcontainers-2.4.0.dist-info/
│   │       │   ├── top_level.txt
│   │       ├── sqlalchemy/
│   │       │   ├── connectors/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── aioodbc.py
│   │       │   │   ├── asyncio.py
│   │       │   │   └── pyodbc.py
│   │       │   ├── cyextension/
│   │       │   │   ├── __init__.py
│   │       │   ├── dialects/
│   │       │   │   ├── mssql/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── aioodbc.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   ├── information_schema.py
│   │       │   │   │   ├── json.py
│   │       │   │   │   ├── provision.py
│   │       │   │   │   ├── pymssql.py
│   │       │   │   │   └── pyodbc.py
│   │       │   │   ├── mysql/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── aiomysql.py
│   │       │   │   │   ├── asyncmy.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   ├── cymysql.py
│   │       │   │   │   ├── dml.py
│   │       │   │   │   ├── enumerated.py
│   │       │   │   │   ├── expression.py
│   │       │   │   │   ├── json.py
│   │       │   │   │   ├── mariadb.py
│   │       │   │   │   ├── mariadbconnector.py
│   │       │   │   │   ├── mysqlconnector.py
│   │       │   │   │   ├── mysqldb.py
│   │       │   │   │   ├── provision.py
│   │       │   │   │   ├── pymysql.py
│   │       │   │   │   ├── pyodbc.py
│   │       │   │   │   ├── reflection.py
│   │       │   │   │   ├── reserved_words.py
│   │       │   │   │   └── types.py
│   │       │   │   ├── oracle/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   ├── cx_oracle.py
│   │       │   │   │   ├── dictionary.py
│   │       │   │   │   ├── oracledb.py
│   │       │   │   │   ├── provision.py
│   │       │   │   │   ├── types.py
│   │       │   │   │   └── vector.py
│   │       │   │   ├── postgresql/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _psycopg_common.py
│   │       │   │   │   ├── array.py
│   │       │   │   │   ├── asyncpg.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   ├── dml.py
│   │       │   │   │   ├── ext.py
│   │       │   │   │   ├── hstore.py
│   │       │   │   │   ├── json.py
│   │       │   │   │   ├── named_types.py
│   │       │   │   │   ├── operators.py
│   │       │   │   │   ├── pg8000.py
│   │       │   │   │   ├── pg_catalog.py
│   │       │   │   │   ├── provision.py
│   │       │   │   │   ├── psycopg.py
│   │       │   │   │   ├── psycopg2.py
│   │       │   │   │   ├── psycopg2cffi.py
│   │       │   │   │   ├── ranges.py
│   │       │   │   │   └── types.py
│   │       │   │   ├── sqlite/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── aiosqlite.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   ├── dml.py
│   │       │   │   │   ├── json.py
│   │       │   │   │   ├── provision.py
│   │       │   │   │   ├── pysqlcipher.py
│   │       │   │   │   └── pysqlite.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _typing.py
│   │       │   │   └── type_migration_guidelines.txt
│   │       │   ├── engine/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _py_processors.py
│   │       │   │   ├── _py_row.py
│   │       │   │   ├── _py_util.py
│   │       │   │   ├── base.py
│   │       │   │   ├── characteristics.py
│   │       │   │   ├── create.py
│   │       │   │   ├── cursor.py
│   │       │   │   ├── default.py
│   │       │   │   ├── events.py
│   │       │   │   ├── interfaces.py
│   │       │   │   ├── mock.py
│   │       │   │   ├── processors.py
│   │       │   │   ├── reflection.py
│   │       │   │   ├── result.py
│   │       │   │   ├── row.py
│   │       │   │   ├── strategies.py
│   │       │   │   ├── url.py
│   │       │   │   └── util.py
│   │       │   ├── event/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── api.py
│   │       │   │   ├── attr.py
│   │       │   │   ├── base.py
│   │       │   │   ├── legacy.py
│   │       │   │   └── registry.py
│   │       │   ├── ext/
│   │       │   │   ├── asyncio/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   ├── engine.py
│   │       │   │   │   ├── exc.py
│   │       │   │   │   ├── result.py
│   │       │   │   │   ├── scoping.py
│   │       │   │   │   └── session.py
│   │       │   │   ├── declarative/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── extensions.py
│   │       │   │   ├── mypy/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── apply.py
│   │       │   │   │   ├── decl_class.py
│   │       │   │   │   ├── infer.py
│   │       │   │   │   ├── names.py
│   │       │   │   │   ├── plugin.py
│   │       │   │   │   └── util.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── associationproxy.py
│   │       │   │   ├── automap.py
│   │       │   │   ├── baked.py
│   │       │   │   ├── compiler.py
│   │       │   │   ├── horizontal_shard.py
│   │       │   │   ├── hybrid.py
│   │       │   │   ├── indexable.py
│   │       │   │   ├── instrumentation.py
│   │       │   │   ├── mutable.py
│   │       │   │   ├── orderinglist.py
│   │       │   │   └── serializer.py
│   │       │   ├── future/
│   │       │   │   ├── __init__.py
│   │       │   │   └── engine.py
│   │       │   ├── orm/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _orm_constructors.py
│   │       │   │   ├── _typing.py
│   │       │   │   ├── attributes.py
│   │       │   │   ├── base.py
│   │       │   │   ├── bulk_persistence.py
│   │       │   │   ├── clsregistry.py
│   │       │   │   ├── collections.py
│   │       │   │   ├── context.py
│   │       │   │   ├── decl_api.py
│   │       │   │   ├── decl_base.py
│   │       │   │   ├── dependency.py
│   │       │   │   ├── descriptor_props.py
│   │       │   │   ├── dynamic.py
│   │       │   │   ├── evaluator.py
│   │       │   │   ├── events.py
│   │       │   │   ├── exc.py
│   │       │   │   ├── identity.py
│   │       │   │   ├── instrumentation.py
│   │       │   │   ├── interfaces.py
│   │       │   │   ├── loading.py
│   │       │   │   ├── mapped_collection.py
│   │       │   │   ├── mapper.py
│   │       │   │   ├── path_registry.py
│   │       │   │   ├── persistence.py
│   │       │   │   ├── properties.py
│   │       │   │   ├── query.py
│   │       │   │   ├── relationships.py
│   │       │   │   ├── scoping.py
│   │       │   │   ├── session.py
│   │       │   │   ├── state.py
│   │       │   │   ├── state_changes.py
│   │       │   │   ├── strategies.py
│   │       │   │   ├── strategy_options.py
│   │       │   │   ├── sync.py
│   │       │   │   ├── unitofwork.py
│   │       │   │   ├── util.py
│   │       │   │   └── writeonly.py
│   │       │   ├── pool/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── base.py
│   │       │   │   ├── events.py
│   │       │   │   └── impl.py
│   │       │   ├── sql/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _dml_constructors.py
│   │       │   │   ├── _elements_constructors.py
│   │       │   │   ├── _orm_types.py
│   │       │   │   ├── _py_util.py
│   │       │   │   ├── _selectable_constructors.py
│   │       │   │   ├── _typing.py
│   │       │   │   ├── annotation.py
│   │       │   │   ├── base.py
│   │       │   │   ├── cache_key.py
│   │       │   │   ├── coercions.py
│   │       │   │   ├── compiler.py
│   │       │   │   ├── crud.py
│   │       │   │   ├── ddl.py
│   │       │   │   ├── default_comparator.py
│   │       │   │   ├── dml.py
│   │       │   │   ├── elements.py
│   │       │   │   ├── events.py
│   │       │   │   ├── expression.py
│   │       │   │   ├── functions.py
│   │       │   │   ├── lambdas.py
│   │       │   │   ├── naming.py
│   │       │   │   ├── operators.py
│   │       │   │   ├── roles.py
│   │       │   │   ├── schema.py
│   │       │   │   ├── selectable.py
│   │       │   │   ├── sqltypes.py
│   │       │   │   ├── traversals.py
│   │       │   │   ├── type_api.py
│   │       │   │   ├── util.py
│   │       │   │   └── visitors.py
│   │       │   ├── testing/
│   │       │   │   ├── fixtures/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   ├── mypy.py
│   │       │   │   │   ├── orm.py
│   │       │   │   │   └── sql.py
│   │       │   │   ├── plugin/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── bootstrap.py
│   │       │   │   │   ├── plugin_base.py
│   │       │   │   │   └── pytestplugin.py
│   │       │   │   ├── suite/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_cte.py
│   │       │   │   │   ├── test_ddl.py
│   │       │   │   │   ├── test_deprecations.py
│   │       │   │   │   ├── test_dialect.py
│   │       │   │   │   ├── test_insert.py
│   │       │   │   │   ├── test_reflection.py
│   │       │   │   │   ├── test_results.py
│   │       │   │   │   ├── test_rowcount.py
│   │       │   │   │   ├── test_select.py
│   │       │   │   │   ├── test_sequence.py
│   │       │   │   │   ├── test_types.py
│   │       │   │   │   ├── test_unicode_ddl.py
│   │       │   │   │   └── test_update_delete.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── assertions.py
│   │       │   │   ├── assertsql.py
│   │       │   │   ├── asyncio.py
│   │       │   │   ├── config.py
│   │       │   │   ├── engines.py
│   │       │   │   ├── entities.py
│   │       │   │   ├── exclusions.py
│   │       │   │   ├── pickleable.py
│   │       │   │   ├── profiling.py
│   │       │   │   ├── provision.py
│   │       │   │   ├── requirements.py
│   │       │   │   ├── schema.py
│   │       │   │   ├── util.py
│   │       │   │   └── warnings.py
│   │       │   ├── util/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _collections.py
│   │       │   │   ├── _concurrency_py3k.py
│   │       │   │   ├── _has_cy.py
│   │       │   │   ├── _py_collections.py
│   │       │   │   ├── compat.py
│   │       │   │   ├── concurrency.py
│   │       │   │   ├── deprecations.py
│   │       │   │   ├── langhelpers.py
│   │       │   │   ├── preloaded.py
│   │       │   │   ├── queue.py
│   │       │   │   ├── tool_support.py
│   │       │   │   ├── topological.py
│   │       │   │   └── typing.py
│   │       │   ├── __init__.py
│   │       │   ├── events.py
│   │       │   ├── exc.py
│   │       │   ├── inspection.py
│   │       │   ├── log.py
│   │       │   ├── schema.py
│   │       │   └── types.py
│   │       ├── sqlalchemy-2.0.49.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── starlette/
│   │       │   ├── middleware/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── authentication.py
│   │       │   │   ├── base.py
│   │       │   │   ├── cors.py
│   │       │   │   ├── errors.py
│   │       │   │   ├── exceptions.py
│   │       │   │   ├── gzip.py
│   │       │   │   ├── httpsredirect.py
│   │       │   │   ├── sessions.py
│   │       │   │   ├── trustedhost.py
│   │       │   │   └── wsgi.py
│   │       │   ├── __init__.py
│   │       │   ├── _exception_handler.py
│   │       │   ├── _utils.py
│   │       │   ├── applications.py
│   │       │   ├── authentication.py
│   │       │   ├── background.py
│   │       │   ├── concurrency.py
│   │       │   ├── config.py
│   │       │   ├── convertors.py
│   │       │   ├── datastructures.py
│   │       │   ├── endpoints.py
│   │       │   ├── exceptions.py
│   │       │   ├── formparsers.py
│   │       │   ├── requests.py
│   │       │   ├── responses.py
│   │       │   ├── routing.py
│   │       │   ├── schemas.py
│   │       │   ├── staticfiles.py
│   │       │   ├── status.py
│   │       │   ├── templating.py
│   │       │   ├── testclient.py
│   │       │   ├── types.py
│   │       │   └── websockets.py
│   │       ├── starlette-1.0.0.dist-info/
│   │       │   ├── licenses/
│   │       │   │   └── LICENSE.md
│   │       ├── trio/
│   │       │   ├── _core/
│   │       │   │   ├── _tests/
│   │       │   │   │   ├── type_tests/
│   │       │   │   │   │   ├── nursery_start.py
│   │       │   │   │   │   └── run.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_asyncgen.py
│   │       │   │   │   ├── test_cancelled.py
│   │       │   │   │   ├── test_exceptiongroup_gc.py
│   │       │   │   │   ├── test_guest_mode.py
│   │       │   │   │   ├── test_instrumentation.py
│   │       │   │   │   ├── test_io.py
│   │       │   │   │   ├── test_ki.py
│   │       │   │   │   ├── test_local.py
│   │       │   │   │   ├── test_mock_clock.py
│   │       │   │   │   ├── test_parking_lot.py
│   │       │   │   │   ├── test_run.py
│   │       │   │   │   ├── test_thread_cache.py
│   │       │   │   │   ├── test_tutil.py
│   │       │   │   │   ├── test_unbounded_queue.py
│   │       │   │   │   ├── test_windows.py
│   │       │   │   │   └── tutil.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _asyncgens.py
│   │       │   │   ├── _concat_tb.py
│   │       │   │   ├── _entry_queue.py
│   │       │   │   ├── _exceptions.py
│   │       │   │   ├── _generated_instrumentation.py
│   │       │   │   ├── _generated_io_epoll.py
│   │       │   │   ├── _generated_io_kqueue.py
│   │       │   │   ├── _generated_io_windows.py
│   │       │   │   ├── _generated_run.py
│   │       │   │   ├── _generated_windows_ffi.py
│   │       │   │   ├── _instrumentation.py
│   │       │   │   ├── _io_common.py
│   │       │   │   ├── _io_epoll.py
│   │       │   │   ├── _io_kqueue.py
│   │       │   │   ├── _io_windows.py
│   │       │   │   ├── _ki.py
│   │       │   │   ├── _local.py
│   │       │   │   ├── _mock_clock.py
│   │       │   │   ├── _parking_lot.py
│   │       │   │   ├── _run.py
│   │       │   │   ├── _run_context.py
│   │       │   │   ├── _thread_cache.py
│   │       │   │   ├── _traps.py
│   │       │   │   ├── _unbounded_queue.py
│   │       │   │   ├── _wakeup_socketpair.py
│   │       │   │   └── _windows_cffi.py
│   │       │   ├── _subprocess_platform/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── kqueue.py
│   │       │   │   ├── waitid.py
│   │       │   │   └── windows.py
│   │       │   ├── _tests/
│   │       │   │   ├── tools/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_gen_exports.py
│   │       │   │   │   ├── test_mypy_annotate.py
│   │       │   │   │   └── test_sync_requirements.py
│   │       │   │   ├── type_tests/
│   │       │   │   │   ├── check_wraps.py
│   │       │   │   │   ├── open_memory_channel.py
│   │       │   │   │   ├── path.py
│   │       │   │   │   ├── subprocesses.py
│   │       │   │   │   └── task_status.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── check_type_completeness.py
│   │       │   │   ├── module_with_deprecations.py
│   │       │   │   ├── pytest_plugin.py
│   │       │   │   ├── test_abc.py
│   │       │   │   ├── test_channel.py
│   │       │   │   ├── test_contextvars.py
│   │       │   │   ├── test_deprecate.py
│   │       │   │   ├── test_deprecate_strict_exception_groups_false.py
│   │       │   │   ├── test_dtls.py
│   │       │   │   ├── test_exports.py
│   │       │   │   ├── test_fakenet.py
│   │       │   │   ├── test_file_io.py
│   │       │   │   ├── test_highlevel_generic.py
│   │       │   │   ├── test_highlevel_open_tcp_listeners.py
│   │       │   │   ├── test_highlevel_open_tcp_stream.py
│   │       │   │   ├── test_highlevel_open_unix_stream.py
│   │       │   │   ├── test_highlevel_serve_listeners.py
│   │       │   │   ├── test_highlevel_socket.py
│   │       │   │   ├── test_highlevel_ssl_helpers.py
│   │       │   │   ├── test_path.py
│   │       │   │   ├── test_repl.py
│   │       │   │   ├── test_scheduler_determinism.py
│   │       │   │   ├── test_signals.py
│   │       │   │   ├── test_socket.py
│   │       │   │   ├── test_ssl.py
│   │       │   │   ├── test_subprocess.py
│   │       │   │   ├── test_sync.py
│   │       │   │   ├── test_testing.py
│   │       │   │   ├── test_testing_raisesgroup.py
│   │       │   │   ├── test_threads.py
│   │       │   │   ├── test_timeouts.py
│   │       │   │   ├── test_tracing.py
│   │       │   │   ├── test_trio.py
│   │       │   │   ├── test_unix_pipes.py
│   │       │   │   ├── test_util.py
│   │       │   │   ├── test_wait_for_object.py
│   │       │   │   └── test_windows_pipes.py
│   │       │   ├── _tools/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── gen_exports.py
│   │       │   │   ├── mypy_annotate.py
│   │       │   │   ├── sync_requirements.py
│   │       │   │   └── windows_ffi_build.py
│   │       │   ├── testing/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _check_streams.py
│   │       │   │   ├── _checkpoints.py
│   │       │   │   ├── _fake_net.py
│   │       │   │   ├── _memory_streams.py
│   │       │   │   ├── _network.py
│   │       │   │   ├── _raises_group.py
│   │       │   │   ├── _sequencer.py
│   │       │   │   └── _trio_test.py
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── _abc.py
│   │       │   ├── _channel.py
│   │       │   ├── _deprecate.py
│   │       │   ├── _dtls.py
│   │       │   ├── _file_io.py
│   │       │   ├── _highlevel_generic.py
│   │       │   ├── _highlevel_open_tcp_listeners.py
│   │       │   ├── _highlevel_open_tcp_stream.py
│   │       │   ├── _highlevel_open_unix_stream.py
│   │       │   ├── _highlevel_serve_listeners.py
│   │       │   ├── _highlevel_socket.py
│   │       │   ├── _highlevel_ssl_helpers.py
│   │       │   ├── _path.py
│   │       │   ├── _repl.py
│   │       │   ├── _signals.py
│   │       │   ├── _socket.py
│   │       │   ├── _ssl.py
│   │       │   ├── _subprocess.py
│   │       │   ├── _sync.py
│   │       │   ├── _threads.py
│   │       │   ├── _timeouts.py
│   │       │   ├── _unix_pipes.py
│   │       │   ├── _util.py
│   │       │   ├── _version.py
│   │       │   ├── _wait_for_object.py
│   │       │   ├── _windows_pipes.py
│   │       │   ├── abc.py
│   │       │   ├── from_thread.py
│   │       │   ├── lowlevel.py
│   │       │   ├── socket.py
│   │       │   └── to_thread.py
│   │       ├── trio-0.33.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       │   ├── top_level.txt
│   │       ├── trio_websocket/
│   │       │   ├── __init__.py
│   │       │   ├── _impl.py
│   │       │   ├── _version.py
│   │       ├── trio_websocket-0.12.2.dist-info/
│   │       │   ├── top_level.txt
│   │       ├── typing_extensions-4.15.0.dist-info/
│   │       │   ├── licenses/
│   │       ├── typing_inspection/
│   │       │   ├── __init__.py
│   │       │   ├── introspection.py
│   │       │   ├── typing_objects.py
│   │       ├── typing_inspection-0.4.2.dist-info/
│   │       │   ├── licenses/
│   │       ├── urllib3/
│   │       │   ├── contrib/
│   │       │   │   ├── emscripten/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── connection.py
│   │       │   │   │   ├── emscripten_fetch_worker.js
│   │       │   │   │   ├── fetch.py
│   │       │   │   │   ├── request.py
│   │       │   │   │   └── response.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── pyopenssl.py
│   │       │   │   └── socks.py
│   │       │   ├── http2/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── connection.py
│   │       │   │   └── probe.py
│   │       │   ├── util/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── connection.py
│   │       │   │   ├── proxy.py
│   │       │   │   ├── request.py
│   │       │   │   ├── response.py
│   │       │   │   ├── retry.py
│   │       │   │   ├── ssl_.py
│   │       │   │   ├── ssl_match_hostname.py
│   │       │   │   ├── ssltransport.py
│   │       │   │   ├── timeout.py
│   │       │   │   ├── url.py
│   │       │   │   ├── util.py
│   │       │   │   └── wait.py
│   │       │   ├── __init__.py
│   │       │   ├── _base_connection.py
│   │       │   ├── _collections.py
│   │       │   ├── _request_methods.py
│   │       │   ├── _version.py
│   │       │   ├── connection.py
│   │       │   ├── connectionpool.py
│   │       │   ├── exceptions.py
│   │       │   ├── fields.py
│   │       │   ├── filepost.py
│   │       │   ├── poolmanager.py
│   │       │   └── response.py
│   │       ├── urllib3-2.7.0.dist-info/
│   │       │   ├── licenses/
│   │       │   │   └── LICENSE.txt
│   │       ├── uvicorn/
│   │       │   ├── lifespan/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── off.py
│   │       │   │   └── on.py
│   │       │   ├── loops/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── asyncio.py
│   │       │   │   ├── auto.py
│   │       │   │   └── uvloop.py
│   │       │   ├── middleware/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── asgi2.py
│   │       │   │   ├── message_logger.py
│   │       │   │   ├── proxy_headers.py
│   │       │   │   └── wsgi.py
│   │       │   ├── protocols/
│   │       │   │   ├── http/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── auto.py
│   │       │   │   │   ├── flow_control.py
│   │       │   │   │   ├── h11_impl.py
│   │       │   │   │   └── httptools_impl.py
│   │       │   │   ├── websockets/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── auto.py
│   │       │   │   │   ├── websockets_impl.py
│   │       │   │   │   ├── websockets_sansio_impl.py
│   │       │   │   │   └── wsproto_impl.py
│   │       │   │   ├── __init__.py
│   │       │   │   └── utils.py
│   │       │   ├── supervisors/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── basereload.py
│   │       │   │   ├── multiprocess.py
│   │       │   │   ├── statreload.py
│   │       │   │   └── watchfilesreload.py
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── _compat.py
│   │       │   ├── _subprocess.py
│   │       │   ├── _types.py
│   │       │   ├── config.py
│   │       │   ├── importer.py
│   │       │   ├── logging.py
│   │       │   ├── main.py
│   │       │   ├── server.py
│   │       │   └── workers.py
│   │       ├── uvicorn-0.47.0.dist-info/
│   │       │   ├── licenses/
│   │       │   │   └── LICENSE.md
│   │       │   ├── entry_points.txt
│   │       ├── webdriver_manager/
│   │       │   ├── core/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── archive.py
│   │       │   │   ├── config.py
│   │       │   │   ├── constants.py
│   │       │   │   ├── download_manager.py
│   │       │   │   ├── driver.py
│   │       │   │   ├── driver_cache.py
│   │       │   │   ├── file_manager.py
│   │       │   │   ├── http.py
│   │       │   │   ├── logger.py
│   │       │   │   ├── manager.py
│   │       │   │   ├── os_manager.py
│   │       │   │   └── utils.py
│   │       │   ├── drivers/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── chrome.py
│   │       │   │   ├── edge.py
│   │       │   │   ├── firefox.py
│   │       │   │   ├── ie.py
│   │       │   │   └── opera.py
│   │       │   ├── __init__.py
│   │       │   ├── chrome.py
│   │       │   ├── firefox.py
│   │       │   ├── microsoft.py
│   │       │   ├── opera.py
│   │       ├── webdriver_manager-4.0.2.dist-info/
│   │       │   ├── top_level.txt
│   │       ├── websocket/
│   │       │   ├── tests/
│   │       │   │   ├── data/
│   │       │   │   │   ├── header01.txt
│   │       │   │   │   ├── header02.txt
│   │       │   │   │   └── header03.txt
│   │       │   │   ├── __init__.py
│   │       │   │   ├── echo-server.py
│   │       │   │   ├── test_abnf.py
│   │       │   │   ├── test_app.py
│   │       │   │   ├── test_cookiejar.py
│   │       │   │   ├── test_dispatcher.py
│   │       │   │   ├── test_handshake_large_response.py
│   │       │   │   ├── test_http.py
│   │       │   │   ├── test_large_payloads.py
│   │       │   │   ├── test_socket.py
│   │       │   │   ├── test_socket_bugs.py
│   │       │   │   ├── test_ssl_compat.py
│   │       │   │   ├── test_ssl_edge_cases.py
│   │       │   │   ├── test_url.py
│   │       │   │   ├── test_utils.py
│   │       │   │   └── test_websocket.py
│   │       │   ├── __init__.py
│   │       │   ├── _abnf.py
│   │       │   ├── _app.py
│   │       │   ├── _cookiejar.py
│   │       │   ├── _core.py
│   │       │   ├── _dispatcher.py
│   │       │   ├── _exceptions.py
│   │       │   ├── _handshake.py
│   │       │   ├── _http.py
│   │       │   ├── _logging.py
│   │       │   ├── _socket.py
│   │       │   ├── _ssl_compat.py
│   │       │   ├── _url.py
│   │       │   ├── _utils.py
│   │       │   ├── _wsdump.py
│   │       ├── websocket_client-1.9.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       │   ├── top_level.txt
│   │       ├── wsproto/
│   │       │   ├── __init__.py
│   │       │   ├── connection.py
│   │       │   ├── events.py
│   │       │   ├── extensions.py
│   │       │   ├── frame_protocol.py
│   │       │   ├── handshake.py
│   │       │   ├── typing.py
│   │       │   └── utilities.py
│   │       ├── wsproto-1.3.2.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── py.py
│   │       ├── socks.py
│   │       ├── sockshandler.py
│   │       └── typing_extensions.py
│   ├── Scripts/
│   │   ├── activate.bat
│   │   ├── Activate.ps1
│   │   ├── deactivate.bat
│   ├── .gitignore
├── codigo/
│   ├── __init__.py
│   ├── api.py
│   ├── codigo_desenvolvimento.md
│   ├── database.py
│   └── engine.py
├── configuracoes/
│   └── configuracoes_sistema.md
├── core/
│   └── governanca/
│       ├── governanca_core.md
│       ├── guardiao_execucao.py
│       ├── leitor_documentacao.py
│       └── validador_regras.py
├── documentacao/
│   ├── admin.html
│   ├── documentacao_especificacoes.md
│   ├── MANUAL_DE_USO.md
│   ├── plano_arquitetura_standalone.md
│   └── plano_arquitetural_gravador_rpa.md
├── executaveis/
│   ├── extension/
│   │   ├── admin.html
│   │   ├── admin.js
│   │   ├── background.js
│   │   ├── content_script.js
│   │   ├── manifest.json
│   │   ├── popup.html
│   │   └── popup.js
│   ├── Configurar_Ambiente_UNIQ.bat
│   ├── executaveis_instaladores.md
│   ├── package_extension.py
├── tests/
│   └── testes_validacao.md
├── .cursorrules
├── Iniciar_UNIQ.bat
├── main_uniq_recorder.py
├── projeto_uniq_recorder.md
├── README_UNIQ.md
├── requirements.txt
```
