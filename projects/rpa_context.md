# Contexto do Projeto: UNIQ RPA — v2.0

> Carregamento sob demanda. Ler apenas quando o intent do usuário envolve RPA.
> Atualizado: 2026-08-03 | Second Brain Evolution v2.0

---

## Visão Geral

Suíte de automação corporativa para Clínica UNIQ. Automatiza Backoffice completo:
Emissão SADT, Lançamento/Faturamento, Consolidação ETL, Contratos, CollectABA, Autorização.

- **Status**: Produção ativa
- **Criado**: 2026-07-31
- **Última alteração**: 2026-08-03
- **Responsável técnico**: USER

---

## Arquitetura

- **Tipo**: Hub & Spoke Modular (Frontend Flask + Backend Python RPA)
- **Caminho raiz**: `C:\Projetos\RPA`
- **Frontend**: Flask Web (HTML/JS/CSS) em `Frontend/`
- **Backend**: Lógica RPA em `Backend/`, cada módulo isolado
- **Global**: Serviços compartilhados em `Backend/Global/` e `Frontend/Global/`

---

## Módulos RPA (6 Robôs)

| Módulo       | Entry Point                                        | Domínio                  |
|-------------|---------------------------------------------------|--------------------------|
| Emissão     | `Backend/Emissao/main_emissao.py`                 | Guias SADT               |
| Lançamento  | `Backend/Lancamento/main_lancamento.py`           | Faturamento              |
| Consolidação| `Backend/Consolidacao/main_consolidacao.py`       | ETL                      |
| Contrato    | `Backend/Contrato/main_contrato.py`               | Contratos Prestadores    |
| CollectABA  | `Backend/CollectABA/main_collectaba.py`           | Evolutivo Atendimentos   |
| Autorizar   | `Backend/Autorizar/main_autorizar.py`             | Autorização Facial       |

---

## Estrutura de Pastas (Cada Módulo)

```
Backend/<Modulo>/
  codigo/           # Código Python principal
  documentacao/     # Docs e *_nome.md obrigatório
  logs/             # Arquivos de log gerados pelo robô
  dados/            # Arquivos de entrada/saída (CSV, XLSX)
  configuracoes/    # Configs específicas do módulo
  executaveis/      # Scripts de inicialização
```

---

## Arquivos Importantes

| Arquivo | Papel |
|---------|-------|
| `Backend/Global/infraestrutura/.env` | Única fonte de credenciais — NUNCA hardcode |
| `Backend/Global/servicos/driver.py` | Init do Selenium — sempre via `start_session()` |
| `Frontend/Global/app_uniq.py` | Servidor Flask principal (entry point web) |
| `C:/Projetos/RPA/arquivos_intocaveis_rpa.md` | Lista de arquivos que NÃO podem ser alterados sem permissão |

---

## Regras Críticas

1. **Governança Zero-Trust**: Todo subdir tem `*_nome.md`. Código sem doc = inválido.
2. **Arquivos Intocáveis**: Ver `arquivos_intocaveis_rpa.md` antes de qualquer modificação em entrypoints.
3. **6 Pastas Obrigatórias**: `codigo/`, `documentacao/`, `logs/`, `dados/`, `configuracoes/`, `executaveis/`
4. **print() PROIBIDO**: Sempre usar logger. Formato: `[ID] [RPA] [ETAPA] [TIPO] Msg`
5. **Selenium**: Nunca init bruto. Sempre `Global/servicos/driver.py::start_session()`
6. **Credenciais**: Apenas em `Backend/Global/infraestrutura/.env`. Zero hardcoded.
7. **Naming**: Sem acentos em nomes de arquivo Python. Snake_case obrigatório.

---

## Stack Técnica

| Tecnologia | Uso |
|-----------|-----|
| Python 3.x | Toda lógica RPA e backend |
| Flask | Servidor web do frontend |
| Selenium | Automação de navegador Chrome |
| SQLite | Banco de dados local para histórico/logs |
| HTML/JS/CSS | Interface web (sem framework pesado) |
| ChromeDriver | Auto-sync via serviço global |

---

## Decisões Técnicas Registradas

| Data | Decisão | Motivo |
|------|---------|--------|
| 2026-07-31 | Hub & Spoke modular em vez de monolito | Isolamento de falha entre robôs |
| 2026-07-31 | Flask em vez de FastAPI | Maturidade, templates HTML nativos |
| 2026-07-31 | SQLite em vez de PostgreSQL | Sem infra de BD externa necessária |
| 2026-07-31 | Selenium em vez de Playwright | Compatibilidade com sistema legado UNIQ |
| 2026-08-03 | Credenciais do uniq_launcher eram incorretas | Correção: usar .env, nunca hardcode |

---

## Problemas Conhecidos e Soluções

| Problema | Solução | Status |
|---------|---------|--------|
| Credenciais admin do uniq_launcher estavam erradas | Referenciar .env corretamente | Resolvido |
| Relatório mostrava 12 faltantes mas eram 17+3 erros | Lógica de contagem corrigida no módulo de relatório | Pendente verificação |
| ChromeDriver desatualizado causa falha no driver init | start_session() faz auto-sync | Resolvido |

---

## Frontend Global

- **Entry**: `Frontend/Global/app_uniq.py` (servidor Flask principal)
- **Porta padrão**: 5000
- **Templates HTML**: mapeados por rotas no orchestrator
- **Assets**: `Frontend/Global/static/`

---

## Pendências / Melhorias Futuras

- [ ] Verificar e corrigir lógica de contagem no relatório de faltantes
- [ ] Adicionar testes automatizados nos módulos críticos
- [ ] Implementar retry automático em caso de falha de Selenium

---

## Histórico

| Data       | Descrição                                             |
|------------|-------------------------------------------------------|
| 2026-07-31 | Contexto inicial criado para o Second Brain           |
| 2026-08-03 | v2.0: Enriquecido com mapa de arquivos, decisões, problemas conhecidos |


## Mapa Completo de Arquivos (Source Code)

> Mapa gerado automaticamente. Exclui dependências, logs e dados para economizar tokens.

```text
RPA/
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
├── .agents/
│   └── credentials.md
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
│   │       ├── _yaml/
│   │       │   └── __init__.py
│   │       ├── adodbapi/
│   │       │   ├── examples/
│   │       │   │   ├── db_print.py
│   │       │   │   ├── db_table_names.py
│   │       │   │   ├── xls_read.py
│   │       │   │   └── xls_write.py
│   │       │   ├── test/
│   │       │   │   ├── adodbapitest.py
│   │       │   │   ├── adodbapitestconfig.py
│   │       │   │   ├── dbapi20.py
│   │       │   │   ├── is64bit.py
│   │       │   │   ├── setuptestframework.py
│   │       │   │   ├── test_adodbapi_dbapi20.py
│   │       │   │   └── tryconnection.py
│   │       │   ├── __init__.py
│   │       │   ├── ado_consts.py
│   │       │   ├── adodbapi.py
│   │       │   ├── apibase.py
│   │       │   ├── is64bit.py
│   │       │   ├── license.txt
│   │       │   ├── process_connect_string.py
│   │       │   ├── readme.txt
│   │       │   ├── schema_table.py
│   │       │   └── setup.py
│   │       ├── aiomysql/
│   │       │   ├── sa/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── connection.py
│   │       │   │   ├── engine.py
│   │       │   │   ├── exc.py
│   │       │   │   ├── result.py
│   │       │   │   └── transaction.py
│   │       │   ├── .gitignore
│   │       │   ├── __init__.py
│   │       │   ├── _scm_version.py
│   │       │   ├── _version.py
│   │       │   ├── connection.py
│   │       │   ├── cursors.py
│   │       │   ├── log.py
│   │       │   ├── pool.py
│   │       │   └── utils.py
│   │       ├── aiomysql-0.3.2.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── alembic/
│   │       │   ├── autogenerate/
│   │       │   │   ├── compare/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── comments.py
│   │       │   │   │   ├── constraints.py
│   │       │   │   │   ├── schema.py
│   │       │   │   │   ├── server_defaults.py
│   │       │   │   │   ├── tables.py
│   │       │   │   │   ├── types.py
│   │       │   │   │   └── util.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── api.py
│   │       │   │   ├── render.py
│   │       │   │   └── rewriter.py
│   │       │   ├── ddl/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _autogen.py
│   │       │   │   ├── base.py
│   │       │   │   ├── impl.py
│   │       │   │   ├── mssql.py
│   │       │   │   ├── mysql.py
│   │       │   │   ├── oracle.py
│   │       │   │   ├── postgresql.py
│   │       │   │   └── sqlite.py
│   │       │   ├── operations/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── base.py
│   │       │   │   ├── batch.py
│   │       │   │   ├── ops.py
│   │       │   │   ├── schemaobj.py
│   │       │   │   └── toimpl.py
│   │       │   ├── runtime/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── environment.py
│   │       │   │   ├── migration.py
│   │       │   │   └── plugins.py
│   │       │   ├── script/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── base.py
│   │       │   │   ├── revision.py
│   │       │   │   └── write_hooks.py
│   │       │   ├── templates/
│   │       │   │   ├── async/
│   │       │   │   │   ├── env.py
│   │       │   │   ├── generic/
│   │       │   │   │   ├── env.py
│   │       │   │   ├── multidb/
│   │       │   │   │   ├── env.py
│   │       │   │   ├── pyproject/
│   │       │   │   │   ├── env.py
│   │       │   │   └── pyproject_async/
│   │       │   │       ├── env.py
│   │       │   ├── testing/
│   │       │   │   ├── plugin/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── bootstrap.py
│   │       │   │   ├── suite/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _autogen_fixtures.py
│   │       │   │   │   ├── test_autogen_comments.py
│   │       │   │   │   ├── test_autogen_computed.py
│   │       │   │   │   ├── test_autogen_diffs.py
│   │       │   │   │   ├── test_autogen_fks.py
│   │       │   │   │   ├── test_autogen_identity.py
│   │       │   │   │   ├── test_environment.py
│   │       │   │   │   └── test_op.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── assertions.py
│   │       │   │   ├── env.py
│   │       │   │   ├── fixtures.py
│   │       │   │   ├── requirements.py
│   │       │   │   ├── schemacompare.py
│   │       │   │   ├── util.py
│   │       │   │   └── warnings.py
│   │       │   ├── util/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── compat.py
│   │       │   │   ├── editor.py
│   │       │   │   ├── exc.py
│   │       │   │   ├── langhelpers.py
│   │       │   │   ├── messaging.py
│   │       │   │   ├── pyfiles.py
│   │       │   │   └── sqla_compat.py
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── command.py
│   │       │   ├── config.py
│   │       │   ├── context.py
│   │       │   ├── environment.py
│   │       │   ├── migration.py
│   │       │   ├── op.py
│   │       ├── alembic-1.18.4.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       │   ├── top_level.txt
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
│   │       ├── bcrypt/
│   │       │   ├── __about__.py
│   │       │   ├── __init__.py
│   │       ├── bcrypt-3.2.2.dist-info/
│   │       │   ├── top_level.txt
│   │       ├── bidict/
│   │       │   ├── __init__.py
│   │       │   ├── _abc.py
│   │       │   ├── _base.py
│   │       │   ├── _bidict.py
│   │       │   ├── _dup.py
│   │       │   ├── _exc.py
│   │       │   ├── _frozen.py
│   │       │   ├── _iter.py
│   │       │   ├── _orderedbase.py
│   │       │   ├── _orderedbidict.py
│   │       │   ├── _typing.py
│   │       │   ├── metadata.py
│   │       ├── bidict-0.23.1.dist-info/
│   │       │   ├── top_level.txt
│   │       ├── blinker/
│   │       │   ├── __init__.py
│   │       │   ├── _utilities.py
│   │       │   ├── base.py
│   │       ├── blinker-1.9.0.dist-info/
│   │       │   ├── LICENSE.txt
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
│   │       ├── click-8.3.3.dist-info/
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
│   │       ├── cryptography/
│   │       │   ├── hazmat/
│   │       │   │   ├── asn1/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── asn1.py
│   │       │   │   ├── backends/
│   │       │   │   │   ├── openssl/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── backend.py
│   │       │   │   │   └── __init__.py
│   │       │   │   ├── bindings/
│   │       │   │   │   ├── _rust/
│   │       │   │   │   │   ├── openssl/
│   │       │   │   │   ├── openssl/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── _conditional.py
│   │       │   │   │   │   └── binding.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── decrepit/
│   │       │   │   │   ├── ciphers/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── algorithms.py
│   │       │   │   │   │   └── modes.py
│   │       │   │   │   └── __init__.py
│   │       │   │   ├── primitives/
│   │       │   │   │   ├── asymmetric/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── dh.py
│   │       │   │   │   │   ├── dsa.py
│   │       │   │   │   │   ├── ec.py
│   │       │   │   │   │   ├── ed25519.py
│   │       │   │   │   │   ├── ed448.py
│   │       │   │   │   │   ├── mldsa.py
│   │       │   │   │   │   ├── mlkem.py
│   │       │   │   │   │   ├── padding.py
│   │       │   │   │   │   ├── rsa.py
│   │       │   │   │   │   ├── types.py
│   │       │   │   │   │   ├── utils.py
│   │       │   │   │   │   ├── x25519.py
│   │       │   │   │   │   └── x448.py
│   │       │   │   │   ├── ciphers/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── aead.py
│   │       │   │   │   │   ├── algorithms.py
│   │       │   │   │   │   ├── base.py
│   │       │   │   │   │   └── modes.py
│   │       │   │   │   ├── kdf/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── argon2.py
│   │       │   │   │   │   ├── concatkdf.py
│   │       │   │   │   │   ├── hkdf.py
│   │       │   │   │   │   ├── kbkdf.py
│   │       │   │   │   │   ├── pbkdf2.py
│   │       │   │   │   │   ├── scrypt.py
│   │       │   │   │   │   └── x963kdf.py
│   │       │   │   │   ├── serialization/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── base.py
│   │       │   │   │   │   ├── pkcs12.py
│   │       │   │   │   │   ├── pkcs7.py
│   │       │   │   │   │   └── ssh.py
│   │       │   │   │   ├── twofactor/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── hotp.py
│   │       │   │   │   │   └── totp.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _asymmetric.py
│   │       │   │   │   ├── _cipheralgorithm.py
│   │       │   │   │   ├── _modes.py
│   │       │   │   │   ├── _serialization.py
│   │       │   │   │   ├── cmac.py
│   │       │   │   │   ├── constant_time.py
│   │       │   │   │   ├── hashes.py
│   │       │   │   │   ├── hmac.py
│   │       │   │   │   ├── hpke.py
│   │       │   │   │   ├── keywrap.py
│   │       │   │   │   ├── padding.py
│   │       │   │   │   └── poly1305.py
│   │       │   │   ├── __init__.py
│   │       │   │   └── _oid.py
│   │       │   ├── x509/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── base.py
│   │       │   │   ├── certificate_transparency.py
│   │       │   │   ├── extensions.py
│   │       │   │   ├── general_name.py
│   │       │   │   ├── name.py
│   │       │   │   ├── ocsp.py
│   │       │   │   ├── oid.py
│   │       │   │   └── verification.py
│   │       │   ├── __about__.py
│   │       │   ├── __init__.py
│   │       │   ├── exceptions.py
│   │       │   ├── fernet.py
│   │       │   └── utils.py
│   │       ├── cryptography-48.0.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── sboms/
│   │       │   │   ├── cryptography-rust.cyclonedx.json
│   │       │   │   └── sbom.json
│   │       ├── dateutil/
│   │       │   ├── parser/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _parser.py
│   │       │   │   └── isoparser.py
│   │       │   ├── tz/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _common.py
│   │       │   │   ├── _factories.py
│   │       │   │   ├── tz.py
│   │       │   │   └── win.py
│   │       │   ├── zoneinfo/
│   │       │   │   ├── __init__.py
│   │       │   │   └── rebuild.py
│   │       │   ├── __init__.py
│   │       │   ├── _common.py
│   │       │   ├── _version.py
│   │       │   ├── easter.py
│   │       │   ├── relativedelta.py
│   │       │   ├── rrule.py
│   │       │   ├── tzwin.py
│   │       │   └── utils.py
│   │       ├── deprecated/
│   │       │   ├── __init__.py
│   │       │   ├── classic.py
│   │       │   ├── params.py
│   │       │   └── sphinx.py
│   │       ├── deprecated-1.3.1.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── dns/
│   │       │   ├── dnssecalgs/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── base.py
│   │       │   │   ├── cryptography.py
│   │       │   │   ├── dsa.py
│   │       │   │   ├── ecdsa.py
│   │       │   │   ├── eddsa.py
│   │       │   │   └── rsa.py
│   │       │   ├── quic/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _asyncio.py
│   │       │   │   ├── _common.py
│   │       │   │   ├── _sync.py
│   │       │   │   └── _trio.py
│   │       │   ├── rdtypes/
│   │       │   │   ├── ANY/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── AFSDB.py
│   │       │   │   │   ├── AMTRELAY.py
│   │       │   │   │   ├── AVC.py
│   │       │   │   │   ├── CAA.py
│   │       │   │   │   ├── CDNSKEY.py
│   │       │   │   │   ├── CDS.py
│   │       │   │   │   ├── CERT.py
│   │       │   │   │   ├── CNAME.py
│   │       │   │   │   ├── CSYNC.py
│   │       │   │   │   ├── DLV.py
│   │       │   │   │   ├── DNAME.py
│   │       │   │   │   ├── DNSKEY.py
│   │       │   │   │   ├── DS.py
│   │       │   │   │   ├── DSYNC.py
│   │       │   │   │   ├── EUI48.py
│   │       │   │   │   ├── EUI64.py
│   │       │   │   │   ├── GPOS.py
│   │       │   │   │   ├── HINFO.py
│   │       │   │   │   ├── HIP.py
│   │       │   │   │   ├── ISDN.py
│   │       │   │   │   ├── L32.py
│   │       │   │   │   ├── L64.py
│   │       │   │   │   ├── LOC.py
│   │       │   │   │   ├── LP.py
│   │       │   │   │   ├── MX.py
│   │       │   │   │   ├── NID.py
│   │       │   │   │   ├── NINFO.py
│   │       │   │   │   ├── NS.py
│   │       │   │   │   ├── NSEC.py
│   │       │   │   │   ├── NSEC3.py
│   │       │   │   │   ├── NSEC3PARAM.py
│   │       │   │   │   ├── OPENPGPKEY.py
│   │       │   │   │   ├── OPT.py
│   │       │   │   │   ├── PTR.py
│   │       │   │   │   ├── RESINFO.py
│   │       │   │   │   ├── RP.py
│   │       │   │   │   ├── RRSIG.py
│   │       │   │   │   ├── RT.py
│   │       │   │   │   ├── SMIMEA.py
│   │       │   │   │   ├── SOA.py
│   │       │   │   │   ├── SPF.py
│   │       │   │   │   ├── SSHFP.py
│   │       │   │   │   ├── TKEY.py
│   │       │   │   │   ├── TLSA.py
│   │       │   │   │   ├── TSIG.py
│   │       │   │   │   ├── TXT.py
│   │       │   │   │   ├── URI.py
│   │       │   │   │   ├── WALLET.py
│   │       │   │   │   ├── X25.py
│   │       │   │   │   └── ZONEMD.py
│   │       │   │   ├── CH/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── A.py
│   │       │   │   ├── IN/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── A.py
│   │       │   │   │   ├── AAAA.py
│   │       │   │   │   ├── APL.py
│   │       │   │   │   ├── DHCID.py
│   │       │   │   │   ├── HTTPS.py
│   │       │   │   │   ├── IPSECKEY.py
│   │       │   │   │   ├── KX.py
│   │       │   │   │   ├── NAPTR.py
│   │       │   │   │   ├── NSAP.py
│   │       │   │   │   ├── NSAP_PTR.py
│   │       │   │   │   ├── PX.py
│   │       │   │   │   ├── SRV.py
│   │       │   │   │   ├── SVCB.py
│   │       │   │   │   └── WKS.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── dnskeybase.py
│   │       │   │   ├── dsbase.py
│   │       │   │   ├── euibase.py
│   │       │   │   ├── mxbase.py
│   │       │   │   ├── nsbase.py
│   │       │   │   ├── svcbbase.py
│   │       │   │   ├── tlsabase.py
│   │       │   │   ├── txtbase.py
│   │       │   │   └── util.py
│   │       │   ├── __init__.py
│   │       │   ├── _asyncbackend.py
│   │       │   ├── _asyncio_backend.py
│   │       │   ├── _ddr.py
│   │       │   ├── _features.py
│   │       │   ├── _immutable_ctx.py
│   │       │   ├── _no_ssl.py
│   │       │   ├── _tls_util.py
│   │       │   ├── _trio_backend.py
│   │       │   ├── asyncbackend.py
│   │       │   ├── asyncquery.py
│   │       │   ├── asyncresolver.py
│   │       │   ├── btree.py
│   │       │   ├── btreezone.py
│   │       │   ├── dnssec.py
│   │       │   ├── dnssectypes.py
│   │       │   ├── e164.py
│   │       │   ├── edns.py
│   │       │   ├── entropy.py
│   │       │   ├── enum.py
│   │       │   ├── exception.py
│   │       │   ├── flags.py
│   │       │   ├── grange.py
│   │       │   ├── immutable.py
│   │       │   ├── inet.py
│   │       │   ├── ipv4.py
│   │       │   ├── ipv6.py
│   │       │   ├── message.py
│   │       │   ├── name.py
│   │       │   ├── namedict.py
│   │       │   ├── nameserver.py
│   │       │   ├── node.py
│   │       │   ├── opcode.py
│   │       │   ├── query.py
│   │       │   ├── rcode.py
│   │       │   ├── rdata.py
│   │       │   ├── rdataclass.py
│   │       │   ├── rdataset.py
│   │       │   ├── rdatatype.py
│   │       │   ├── renderer.py
│   │       │   ├── resolver.py
│   │       │   ├── reversename.py
│   │       │   ├── rrset.py
│   │       │   ├── serial.py
│   │       │   ├── set.py
│   │       │   ├── tokenizer.py
│   │       │   ├── transaction.py
│   │       │   ├── tsig.py
│   │       │   ├── tsigkeyring.py
│   │       │   ├── ttl.py
│   │       │   ├── update.py
│   │       │   ├── version.py
│   │       │   ├── versioned.py
│   │       │   ├── win32util.py
│   │       │   ├── wire.py
│   │       │   ├── xfr.py
│   │       │   ├── zone.py
│   │       │   ├── zonefile.py
│   │       │   └── zonetypes.py
│   │       ├── dnspython-2.8.0.dist-info/
│   │       │   ├── licenses/
│   │       ├── docs/
│   │       │   ├── conf.py
│   │       │   ├── make.bat
│   │       ├── docx/
│   │       │   ├── dml/
│   │       │   │   ├── __init__.py
│   │       │   │   └── color.py
│   │       │   ├── drawing/
│   │       │   │   └── __init__.py
│   │       │   ├── enum/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── base.py
│   │       │   │   ├── dml.py
│   │       │   │   ├── section.py
│   │       │   │   ├── shape.py
│   │       │   │   ├── style.py
│   │       │   │   ├── table.py
│   │       │   │   └── text.py
│   │       │   ├── image/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── bmp.py
│   │       │   │   ├── constants.py
│   │       │   │   ├── exceptions.py
│   │       │   │   ├── gif.py
│   │       │   │   ├── helpers.py
│   │       │   │   ├── image.py
│   │       │   │   ├── jpeg.py
│   │       │   │   ├── png.py
│   │       │   │   └── tiff.py
│   │       │   ├── opc/
│   │       │   │   ├── parts/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── coreprops.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── constants.py
│   │       │   │   ├── coreprops.py
│   │       │   │   ├── exceptions.py
│   │       │   │   ├── oxml.py
│   │       │   │   ├── package.py
│   │       │   │   ├── packuri.py
│   │       │   │   ├── part.py
│   │       │   │   ├── phys_pkg.py
│   │       │   │   ├── pkgreader.py
│   │       │   │   ├── pkgwriter.py
│   │       │   │   ├── rel.py
│   │       │   │   ├── shared.py
│   │       │   │   └── spec.py
│   │       │   ├── oxml/
│   │       │   │   ├── text/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── font.py
│   │       │   │   │   ├── hyperlink.py
│   │       │   │   │   ├── pagebreak.py
│   │       │   │   │   ├── paragraph.py
│   │       │   │   │   ├── parfmt.py
│   │       │   │   │   └── run.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── comments.py
│   │       │   │   ├── coreprops.py
│   │       │   │   ├── document.py
│   │       │   │   ├── drawing.py
│   │       │   │   ├── exceptions.py
│   │       │   │   ├── ns.py
│   │       │   │   ├── numbering.py
│   │       │   │   ├── parser.py
│   │       │   │   ├── section.py
│   │       │   │   ├── settings.py
│   │       │   │   ├── shape.py
│   │       │   │   ├── shared.py
│   │       │   │   ├── simpletypes.py
│   │       │   │   ├── styles.py
│   │       │   │   ├── table.py
│   │       │   │   └── xmlchemy.py
│   │       │   ├── parts/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── comments.py
│   │       │   │   ├── document.py
│   │       │   │   ├── hdrftr.py
│   │       │   │   ├── image.py
│   │       │   │   ├── numbering.py
│   │       │   │   ├── settings.py
│   │       │   │   ├── story.py
│   │       │   │   └── styles.py
│   │       │   ├── styles/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── latent.py
│   │       │   │   ├── style.py
│   │       │   │   └── styles.py
│   │       │   ├── templates/
│   │       │   │   ├── default-docx-template/
│   │       │   │   │   ├── _rels/
│   │       │   │   │   │   └── .rels
│   │       │   │   │   ├── customXml/
│   │       │   │   │   │   ├── _rels/
│   │       │   │   │   ├── docProps/
│   │       │   │   │   ├── word/
│   │       │   │   │   │   ├── _rels/
│   │       │   │   │   │   ├── theme/
│   │       │   ├── text/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── font.py
│   │       │   │   ├── hyperlink.py
│   │       │   │   ├── pagebreak.py
│   │       │   │   ├── paragraph.py
│   │       │   │   ├── parfmt.py
│   │       │   │   ├── run.py
│   │       │   │   └── tabstops.py
│   │       │   ├── __init__.py
│   │       │   ├── api.py
│   │       │   ├── blkcntnr.py
│   │       │   ├── comments.py
│   │       │   ├── document.py
│   │       │   ├── exceptions.py
│   │       │   ├── package.py
│   │       │   ├── section.py
│   │       │   ├── settings.py
│   │       │   ├── shape.py
│   │       │   ├── shared.py
│   │       │   ├── table.py
│   │       │   └── types.py
│   │       ├── docx2pdf/
│   │       │   ├── __init__.py
│   │       ├── docx2pdf-0.1.8.dist-info/
│   │       │   ├── entry_points.txt
│   │       ├── dotenv/
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── cli.py
│   │       │   ├── ipython.py
│   │       │   ├── main.py
│   │       │   ├── parser.py
│   │       │   ├── variables.py
│   │       │   └── version.py
│   │       ├── ecdsa/
│   │       │   ├── __init__.py
│   │       │   ├── _compat.py
│   │       │   ├── _rwlock.py
│   │       │   ├── _sha3.py
│   │       │   ├── _version.py
│   │       │   ├── curves.py
│   │       │   ├── der.py
│   │       │   ├── ecdh.py
│   │       │   ├── ecdsa.py
│   │       │   ├── eddsa.py
│   │       │   ├── ellipticcurve.py
│   │       │   ├── errors.py
│   │       │   ├── keys.py
│   │       │   ├── numbertheory.py
│   │       │   ├── rfc6979.py
│   │       │   ├── ssh.py
│   │       │   ├── test_curves.py
│   │       │   ├── test_der.py
│   │       │   ├── test_ecdh.py
│   │       │   ├── test_ecdsa.py
│   │       │   ├── test_eddsa.py
│   │       │   ├── test_ellipticcurve.py
│   │       │   ├── test_jacobi.py
│   │       │   ├── test_keys.py
│   │       │   ├── test_malformed_sigs.py
│   │       │   ├── test_numbertheory.py
│   │       │   ├── test_pyecdsa.py
│   │       │   ├── test_rw_lock.py
│   │       │   ├── test_sha3.py
│   │       │   └── util.py
│   │       ├── ecdsa-0.19.2.dist-info/
│   │       │   ├── top_level.txt
│   │       ├── email_validator/
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── deliverability.py
│   │       │   ├── exceptions.py
│   │       │   ├── rfc_constants.py
│   │       │   ├── syntax.py
│   │       │   ├── types.py
│   │       │   ├── validate_email.py
│   │       │   └── version.py
│   │       ├── email_validator-2.3.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       │   ├── top_level.txt
│   │       ├── engineio/
│   │       │   ├── async_drivers/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _websocket_wsgi.py
│   │       │   │   ├── aiohttp.py
│   │       │   │   ├── asgi.py
│   │       │   │   ├── eventlet.py
│   │       │   │   ├── gevent.py
│   │       │   │   ├── gevent_uwsgi.py
│   │       │   │   ├── sanic.py
│   │       │   │   ├── threading.py
│   │       │   │   └── tornado.py
│   │       │   ├── __init__.py
│   │       │   ├── async_client.py
│   │       │   ├── async_server.py
│   │       │   ├── async_socket.py
│   │       │   ├── base_client.py
│   │       │   ├── base_server.py
│   │       │   ├── base_socket.py
│   │       │   ├── client.py
│   │       │   ├── exceptions.py
│   │       │   ├── json.py
│   │       │   ├── middleware.py
│   │       │   ├── packet.py
│   │       │   ├── payload.py
│   │       │   ├── server.py
│   │       │   ├── socket.py
│   │       │   └── static_files.py
│   │       ├── et_xmlfile/
│   │       │   ├── __init__.py
│   │       │   ├── incremental_tree.py
│   │       │   └── xmlfile.py
│   │       ├── et_xmlfile-2.0.0.dist-info/
│   │       │   ├── AUTHORS.txt
│   │       │   ├── top_level.txt
│   │       ├── eventlet/
│   │       │   ├── green/
│   │       │   │   ├── http/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── client.py
│   │       │   │   │   ├── cookiejar.py
│   │       │   │   │   ├── cookies.py
│   │       │   │   │   └── server.py
│   │       │   │   ├── OpenSSL/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── crypto.py
│   │       │   │   │   ├── SSL.py
│   │       │   │   │   ├── tsafe.py
│   │       │   │   │   └── version.py
│   │       │   │   ├── urllib/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── error.py
│   │       │   │   │   ├── parse.py
│   │       │   │   │   ├── request.py
│   │       │   │   │   └── response.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _socket_nodns.py
│   │       │   │   ├── asynchat.py
│   │       │   │   ├── asyncore.py
│   │       │   │   ├── BaseHTTPServer.py
│   │       │   │   ├── builtin.py
│   │       │   │   ├── CGIHTTPServer.py
│   │       │   │   ├── ftplib.py
│   │       │   │   ├── httplib.py
│   │       │   │   ├── MySQLdb.py
│   │       │   │   ├── os.py
│   │       │   │   ├── profile.py
│   │       │   │   ├── Queue.py
│   │       │   │   ├── select.py
│   │       │   │   ├── selectors.py
│   │       │   │   ├── SimpleHTTPServer.py
│   │       │   │   ├── socket.py
│   │       │   │   ├── SocketServer.py
│   │       │   │   ├── ssl.py
│   │       │   │   ├── subprocess.py
│   │       │   │   ├── thread.py
│   │       │   │   ├── threading.py
│   │       │   │   ├── time.py
│   │       │   │   ├── urllib2.py
│   │       │   │   └── zmq.py
│   │       │   ├── greenio/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── base.py
│   │       │   │   └── py3.py
│   │       │   ├── hubs/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── asyncio.py
│   │       │   │   ├── epolls.py
│   │       │   │   ├── hub.py
│   │       │   │   ├── kqueue.py
│   │       │   │   ├── poll.py
│   │       │   │   ├── pyevent.py
│   │       │   │   ├── selects.py
│   │       │   │   └── timer.py
│   │       │   ├── support/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── greendns.py
│   │       │   │   ├── greenlets.py
│   │       │   │   ├── psycopg2_patcher.py
│   │       │   │   ├── pylib.py
│   │       │   │   ├── stacklesspypys.py
│   │       │   │   └── stacklesss.py
│   │       │   ├── zipkin/
│   │       │   │   ├── _thrift/
│   │       │   │   │   ├── zipkinCore/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── constants.py
│   │       │   │   │   │   └── ttypes.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── example/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── api.py
│   │       │   │   ├── client.py
│   │       │   │   ├── greenthread.py
│   │       │   │   ├── http.py
│   │       │   │   ├── log.py
│   │       │   │   ├── patcher.py
│   │       │   │   └── wsgi.py
│   │       │   ├── __init__.py
│   │       │   ├── _version.py
│   │       │   ├── asyncio.py
│   │       │   ├── backdoor.py
│   │       │   ├── convenience.py
│   │       │   ├── corolocal.py
│   │       │   ├── coros.py
│   │       │   ├── dagpool.py
│   │       │   ├── db_pool.py
│   │       │   ├── debug.py
│   │       │   ├── event.py
│   │       │   ├── greenpool.py
│   │       │   ├── greenthread.py
│   │       │   ├── lock.py
│   │       │   ├── patcher.py
│   │       │   ├── pools.py
│   │       │   ├── queue.py
│   │       │   ├── semaphore.py
│   │       │   ├── timeout.py
│   │       │   ├── tpool.py
│   │       │   ├── websocket.py
│   │       │   └── wsgi.py
│   │       ├── eventlet-0.41.0.dist-info/
│   │       │   ├── licenses/
│   │       ├── examples/
│   │       │   ├── example.py
│   │       │   ├── example_callproc.py
│   │       │   ├── example_callproc_oldstyle.py
│   │       │   ├── example_cursors.py
│   │       │   ├── example_executemany.py
│   │       │   ├── example_executemany_oldstyle.py
│   │       │   ├── example_oldstyle.py
│   │       │   ├── example_pool.py
│   │       │   ├── example_pool_oldstyle.py
│   │       │   ├── example_simple_sa.py
│   │       │   ├── example_simple_sa_oldstyle.py
│   │       │   ├── example_ssl.py
│   │       │   ├── example_transaction.py
│   │       │   └── example_transaction_oldstyle.py
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
│   │       ├── flask/
│   │       │   ├── json/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── provider.py
│   │       │   │   └── tag.py
│   │       │   ├── sansio/
│   │       │   │   ├── app.py
│   │       │   │   ├── blueprints.py
│   │       │   │   ├── README.md
│   │       │   │   └── scaffold.py
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── app.py
│   │       │   ├── blueprints.py
│   │       │   ├── cli.py
│   │       │   ├── config.py
│   │       │   ├── ctx.py
│   │       │   ├── debughelpers.py
│   │       │   ├── globals.py
│   │       │   ├── helpers.py
│   │       │   ├── logging.py
│   │       │   ├── sessions.py
│   │       │   ├── signals.py
│   │       │   ├── templating.py
│   │       │   ├── testing.py
│   │       │   ├── typing.py
│   │       │   ├── views.py
│   │       │   └── wrappers.py
│   │       ├── flask-3.1.3.dist-info/
│   │       │   ├── licenses/
│   │       │   │   └── LICENSE.txt
│   │       │   ├── entry_points.txt
│   │       ├── flask_limiter/
│   │       │   ├── contrib/
│   │       │   │   ├── __init__.py
│   │       │   │   └── util.py
│   │       │   ├── __init__.py
│   │       │   ├── _cli.py
│   │       │   ├── _compat.py
│   │       │   ├── _extension.py
│   │       │   ├── _limits.py
│   │       │   ├── _manager.py
│   │       │   ├── _typing.py
│   │       │   ├── _version.py
│   │       │   ├── commands.py
│   │       │   ├── constants.py
│   │       │   ├── errors.py
│   │       │   └── util.py
│   │       ├── flask_limiter-4.1.1.dist-info/
│   │       │   ├── licenses/
│   │       │   │   └── LICENSE.txt
│   │       │   ├── entry_points.txt
│   │       ├── flask_socketio/
│   │       │   ├── __init__.py
│   │       │   ├── namespace.py
│   │       │   └── test_client.py
│   │       ├── flask_socketio-5.6.1.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
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
│   │       ├── hiredis/
│   │       │   ├── __init__.py
│   │       │   └── version.py
│   │       ├── hiredis-3.3.1.dist-info/
│   │       │   ├── licenses/
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
│   │       ├── httptools/
│   │       │   ├── parser/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── errors.py
│   │       │   │   ├── protocol.py
│   │       │   ├── __init__.py
│   │       │   └── _version.py
│   │       ├── httptools-0.7.1.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
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
│   │       ├── isapi/
│   │       │   ├── doc/
│   │       │   │   └── isapi.html
│   │       │   ├── samples/
│   │       │   │   ├── advanced.py
│   │       │   │   ├── README.txt
│   │       │   │   ├── redirector.py
│   │       │   │   ├── redirector_asynch.py
│   │       │   │   ├── redirector_with_filter.py
│   │       │   │   └── test.py
│   │       │   ├── test/
│   │       │   │   ├── extension_simple.py
│   │       │   │   └── README.txt
│   │       │   ├── __init__.py
│   │       │   ├── install.py
│   │       │   ├── isapicon.py
│   │       │   ├── README.txt
│   │       │   ├── simple.py
│   │       │   └── threaded_extension.py
│   │       ├── itsdangerous/
│   │       │   ├── __init__.py
│   │       │   ├── _json.py
│   │       │   ├── encoding.py
│   │       │   ├── exc.py
│   │       │   ├── serializer.py
│   │       │   ├── signer.py
│   │       │   ├── timed.py
│   │       │   └── url_safe.py
│   │       ├── itsdangerous-2.2.0.dist-info/
│   │       │   ├── LICENSE.txt
│   │       ├── jinja2/
│   │       │   ├── __init__.py
│   │       │   ├── _identifier.py
│   │       │   ├── async_utils.py
│   │       │   ├── bccache.py
│   │       │   ├── compiler.py
│   │       │   ├── constants.py
│   │       │   ├── debug.py
│   │       │   ├── defaults.py
│   │       │   ├── environment.py
│   │       │   ├── exceptions.py
│   │       │   ├── ext.py
│   │       │   ├── filters.py
│   │       │   ├── idtracking.py
│   │       │   ├── lexer.py
│   │       │   ├── loaders.py
│   │       │   ├── meta.py
│   │       │   ├── nativetypes.py
│   │       │   ├── nodes.py
│   │       │   ├── optimizer.py
│   │       │   ├── parser.py
│   │       │   ├── runtime.py
│   │       │   ├── sandbox.py
│   │       │   ├── tests.py
│   │       │   ├── utils.py
│   │       │   └── visitor.py
│   │       ├── jinja2-3.1.6.dist-info/
│   │       │   ├── licenses/
│   │       │   │   └── LICENSE.txt
│   │       │   ├── entry_points.txt
│   │       ├── jose/
│   │       │   ├── backends/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _asn1.py
│   │       │   │   ├── base.py
│   │       │   │   ├── cryptography_backend.py
│   │       │   │   ├── ecdsa_backend.py
│   │       │   │   ├── native.py
│   │       │   │   └── rsa_backend.py
│   │       │   ├── __init__.py
│   │       │   ├── constants.py
│   │       │   ├── exceptions.py
│   │       │   ├── jwe.py
│   │       │   ├── jwk.py
│   │       │   ├── jws.py
│   │       │   ├── jwt.py
│   │       │   └── utils.py
│   │       ├── jwt/
│   │       │   ├── __init__.py
│   │       │   ├── algorithms.py
│   │       │   ├── api_jwk.py
│   │       │   ├── api_jws.py
│   │       │   ├── api_jwt.py
│   │       │   ├── exceptions.py
│   │       │   ├── help.py
│   │       │   ├── jwk_set_cache.py
│   │       │   ├── jwks_client.py
│   │       │   ├── types.py
│   │       │   ├── utils.py
│   │       │   └── warnings.py
│   │       ├── limits/
│   │       │   ├── aio/
│   │       │   │   ├── storage/
│   │       │   │   │   ├── memcached/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── bridge.py
│   │       │   │   │   │   ├── emcache.py
│   │       │   │   │   │   └── memcachio.py
│   │       │   │   │   ├── redis/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── bridge.py
│   │       │   │   │   │   ├── coredis.py
│   │       │   │   │   │   ├── redispy.py
│   │       │   │   │   │   └── valkey.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   ├── memory.py
│   │       │   │   │   └── mongodb.py
│   │       │   │   ├── __init__.py
│   │       │   │   └── strategies.py
│   │       │   ├── resources/
│   │       │   │   └── redis/
│   │       │   │       └── lua_scripts/
│   │       │   ├── storage/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── base.py
│   │       │   │   ├── memcached.py
│   │       │   │   ├── memory.py
│   │       │   │   ├── mongodb.py
│   │       │   │   ├── redis.py
│   │       │   │   ├── redis_cluster.py
│   │       │   │   └── redis_sentinel.py
│   │       │   ├── __init__.py
│   │       │   ├── _storage_scheme.py
│   │       │   ├── _version.py
│   │       │   ├── errors.py
│   │       │   ├── limits.py
│   │       │   ├── strategies.py
│   │       │   ├── typing.py
│   │       │   └── util.py
│   │       ├── limits-5.8.0.dist-info/
│   │       │   ├── licenses/
│   │       │   │   └── LICENSE.txt
│   │       ├── lxml/
│   │       │   ├── html/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _diffcommand.py
│   │       │   │   ├── _difflib.py
│   │       │   │   ├── _html5builder.py
│   │       │   │   ├── _setmixin.py
│   │       │   │   ├── builder.py
│   │       │   │   ├── clean.py
│   │       │   │   ├── defs.py
│   │       │   │   ├── diff.py
│   │       │   │   ├── ElementSoup.py
│   │       │   │   ├── formfill.py
│   │       │   │   ├── html5parser.py
│   │       │   │   ├── soupparser.py
│   │       │   │   └── usedoctest.py
│   │       │   ├── includes/
│   │       │   │   ├── extlibs/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── libexslt/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── libxml/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── libxslt/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── __init__.py
│   │       │   ├── isoschematron/
│   │       │   │   ├── resources/
│   │       │   │   │   ├── rng/
│   │       │   │   │   └── xsl/
│   │       │   │   │       ├── iso-schematron-xslt1/
│   │       │   │   │       │   └── readme.txt
│   │       │   │   └── __init__.py
│   │       │   ├── __init__.py
│   │       │   ├── _elementpath.py
│   │       │   ├── builder.py
│   │       │   ├── cssselect.py
│   │       │   ├── doctestcompare.py
│   │       │   ├── ElementInclude.py
│   │       │   ├── pyclasslookup.py
│   │       │   ├── sax.py
│   │       │   ├── usedoctest.py
│   │       ├── lxml-6.1.0.dist-info/
│   │       │   ├── licenses/
│   │       │   │   ├── LICENSE.txt
│   │       │   │   └── LICENSES.txt
│   │       │   ├── top_level.txt
│   │       ├── mako/
│   │       │   ├── ext/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── autohandler.py
│   │       │   │   ├── babelplugin.py
│   │       │   │   ├── beaker_cache.py
│   │       │   │   ├── extract.py
│   │       │   │   ├── linguaplugin.py
│   │       │   │   ├── preprocessors.py
│   │       │   │   ├── pygmentplugin.py
│   │       │   │   └── turbogears.py
│   │       │   ├── testing/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _config.py
│   │       │   │   ├── assertions.py
│   │       │   │   ├── config.py
│   │       │   │   ├── exclusions.py
│   │       │   │   ├── fixtures.py
│   │       │   │   └── helpers.py
│   │       │   ├── __init__.py
│   │       │   ├── _ast_util.py
│   │       │   ├── ast.py
│   │       │   ├── cache.py
│   │       │   ├── cmd.py
│   │       │   ├── codegen.py
│   │       │   ├── compat.py
│   │       │   ├── exceptions.py
│   │       │   ├── filters.py
│   │       │   ├── lexer.py
│   │       │   ├── lookup.py
│   │       │   ├── parsetree.py
│   │       │   ├── pygen.py
│   │       │   ├── pyparser.py
│   │       │   ├── runtime.py
│   │       │   ├── template.py
│   │       │   └── util.py
│   │       ├── mako-1.3.12.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       │   ├── top_level.txt
│   │       ├── markupsafe/
│   │       │   ├── __init__.py
│   │       │   ├── _native.py
│   │       ├── markupsafe-3.0.3.dist-info/
│   │       │   ├── licenses/
│   │       │   │   └── LICENSE.txt
│   │       │   ├── top_level.txt
│   │       ├── multipart/
│   │       │   ├── __init__.py
│   │       │   ├── decoders.py
│   │       │   ├── exceptions.py
│   │       │   └── multipart.py
│   │       ├── mysql/
│   │       │   ├── ai/
│   │       │   │   ├── genai/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── embedding.py
│   │       │   │   │   ├── generation.py
│   │       │   │   │   └── vector_store.py
│   │       │   │   ├── ml/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   ├── classifier.py
│   │       │   │   │   ├── model.py
│   │       │   │   │   ├── outlier.py
│   │       │   │   │   ├── regressor.py
│   │       │   │   │   └── transformer.py
│   │       │   │   ├── utils/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── atomic_cursor.py
│   │       │   │   │   ├── dependencies.py
│   │       │   │   │   └── utils.py
│   │       │   │   └── __init__.py
│   │       │   ├── connector/
│   │       │   │   ├── aio/
│   │       │   │   │   ├── plugins/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── authentication_kerberos_client.py
│   │       │   │   │   │   ├── authentication_ldap_sasl_client.py
│   │       │   │   │   │   ├── authentication_oci_client.py
│   │       │   │   │   │   ├── authentication_openid_connect_client.py
│   │       │   │   │   │   ├── authentication_webauthn_client.py
│   │       │   │   │   │   ├── caching_sha2_password.py
│   │       │   │   │   │   ├── mysql_clear_password.py
│   │       │   │   │   │   ├── mysql_native_password.py
│   │       │   │   │   │   └── sha256_password.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _decorating.py
│   │       │   │   │   ├── abstracts.py
│   │       │   │   │   ├── authentication.py
│   │       │   │   │   ├── charsets.py
│   │       │   │   │   ├── connection.py
│   │       │   │   │   ├── cursor.py
│   │       │   │   │   ├── logger.py
│   │       │   │   │   ├── network.py
│   │       │   │   │   ├── pooling.py
│   │       │   │   │   ├── protocol.py
│   │       │   │   │   └── utils.py
│   │       │   │   ├── django/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   ├── client.py
│   │       │   │   │   ├── compiler.py
│   │       │   │   │   ├── creation.py
│   │       │   │   │   ├── features.py
│   │       │   │   │   ├── introspection.py
│   │       │   │   │   ├── operations.py
│   │       │   │   │   ├── schema.py
│   │       │   │   │   └── validation.py
│   │       │   │   ├── locales/
│   │       │   │   │   ├── eng/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── client_error.py
│   │       │   │   │   └── __init__.py
│   │       │   │   ├── opentelemetry/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── constants.py
│   │       │   │   │   ├── context_propagation.py
│   │       │   │   │   └── instrumentation.py
│   │       │   │   ├── plugins/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── authentication_kerberos_client.py
│   │       │   │   │   ├── authentication_ldap_sasl_client.py
│   │       │   │   │   ├── authentication_oci_client.py
│   │       │   │   │   ├── authentication_openid_connect_client.py
│   │       │   │   │   ├── authentication_webauthn_client.py
│   │       │   │   │   ├── caching_sha2_password.py
│   │       │   │   │   ├── mysql_clear_password.py
│   │       │   │   │   ├── mysql_native_password.py
│   │       │   │   │   └── sha256_password.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _decorating.py
│   │       │   │   ├── _scripting.py
│   │       │   │   ├── abstracts.py
│   │       │   │   ├── authentication.py
│   │       │   │   ├── charsets.py
│   │       │   │   ├── connection.py
│   │       │   │   ├── connection_cext.py
│   │       │   │   ├── constants.py
│   │       │   │   ├── conversion.py
│   │       │   │   ├── cursor.py
│   │       │   │   ├── cursor_cext.py
│   │       │   │   ├── custom_types.py
│   │       │   │   ├── dbapi.py
│   │       │   │   ├── errorcode.py
│   │       │   │   ├── errors.py
│   │       │   │   ├── logger.py
│   │       │   │   ├── network.py
│   │       │   │   ├── optionfiles.py
│   │       │   │   ├── pooling.py
│   │       │   │   ├── protocol.py
│   │       │   │   ├── tls_ciphers.py
│   │       │   │   ├── types.py
│   │       │   │   ├── utils.py
│   │       │   │   └── version.py
│   │       │   ├── vendor/
│   │       │   │   ├── plugin/
│   │       │   └── __init__.py
│   │       ├── mysql_connector_python-9.7.0.dist-info/
│   │       │   ├── licenses/
│   │       │   │   └── LICENSE.txt
│   │       │   ├── top_level.txt
│   │       ├── numpy/
│   │       │   ├── _core/
│   │       │   │   ├── include/
│   │       │   │   │   └── numpy/
│   │       │   │   │       ├── random/
│   │       │   │   │       │   └── LICENSE.txt
│   │       │   │   ├── lib/
│   │       │   │   │   ├── npy-pkg-config/
│   │       │   │   │   ├── pkgconfig/
│   │       │   │   ├── tests/
│   │       │   │   │   ├── data/
│   │       │   │   │   │   ├── umath-validation-set-README.txt
│   │       │   │   │   ├── examples/
│   │       │   │   │   │   ├── cython/
│   │       │   │   │   │   │   └── setup.py
│   │       │   │   │   │   └── limited_api/
│   │       │   │   │   │       └── setup.py
│   │       │   │   │   ├── _locales.py
│   │       │   │   │   ├── _natype.py
│   │       │   │   │   ├── test__exceptions.py
│   │       │   │   │   ├── test_abc.py
│   │       │   │   │   ├── test_api.py
│   │       │   │   │   ├── test_argparse.py
│   │       │   │   │   ├── test_array_api_info.py
│   │       │   │   │   ├── test_array_coercion.py
│   │       │   │   │   ├── test_array_interface.py
│   │       │   │   │   ├── test_arraymethod.py
│   │       │   │   │   ├── test_arrayobject.py
│   │       │   │   │   ├── test_arrayprint.py
│   │       │   │   │   ├── test_casting_floatingpoint_errors.py
│   │       │   │   │   ├── test_casting_unittests.py
│   │       │   │   │   ├── test_conversion_utils.py
│   │       │   │   │   ├── test_cpu_dispatcher.py
│   │       │   │   │   ├── test_cpu_features.py
│   │       │   │   │   ├── test_custom_dtypes.py
│   │       │   │   │   ├── test_cython.py
│   │       │   │   │   ├── test_datetime.py
│   │       │   │   │   ├── test_defchararray.py
│   │       │   │   │   ├── test_deprecations.py
│   │       │   │   │   ├── test_dlpack.py
│   │       │   │   │   ├── test_dtype.py
│   │       │   │   │   ├── test_einsum.py
│   │       │   │   │   ├── test_errstate.py
│   │       │   │   │   ├── test_extint128.py
│   │       │   │   │   ├── test_finfo.py
│   │       │   │   │   ├── test_function_base.py
│   │       │   │   │   ├── test_getlimits.py
│   │       │   │   │   ├── test_half.py
│   │       │   │   │   ├── test_hashtable.py
│   │       │   │   │   ├── test_indexerrors.py
│   │       │   │   │   ├── test_indexing.py
│   │       │   │   │   ├── test_item_selection.py
│   │       │   │   │   ├── test_limited_api.py
│   │       │   │   │   ├── test_longdouble.py
│   │       │   │   │   ├── test_mem_overlap.py
│   │       │   │   │   ├── test_mem_policy.py
│   │       │   │   │   ├── test_memmap.py
│   │       │   │   │   ├── test_multiarray.py
│   │       │   │   │   ├── test_multiprocessing.py
│   │       │   │   │   ├── test_multithreading.py
│   │       │   │   │   ├── test_nditer.py
│   │       │   │   │   ├── test_nep50_promotions.py
│   │       │   │   │   ├── test_numeric.py
│   │       │   │   │   ├── test_numerictypes.py
│   │       │   │   │   ├── test_overrides.py
│   │       │   │   │   ├── test_print.py
│   │       │   │   │   ├── test_protocols.py
│   │       │   │   │   ├── test_records.py
│   │       │   │   │   ├── test_regression.py
│   │       │   │   │   ├── test_scalar_ctors.py
│   │       │   │   │   ├── test_scalar_methods.py
│   │       │   │   │   ├── test_scalarbuffer.py
│   │       │   │   │   ├── test_scalarinherit.py
│   │       │   │   │   ├── test_scalarmath.py
│   │       │   │   │   ├── test_scalarprint.py
│   │       │   │   │   ├── test_shape_base.py
│   │       │   │   │   ├── test_simd.py
│   │       │   │   │   ├── test_simd_module.py
│   │       │   │   │   ├── test_stringdtype.py
│   │       │   │   │   ├── test_strings.py
│   │       │   │   │   ├── test_ufunc.py
│   │       │   │   │   ├── test_umath.py
│   │       │   │   │   ├── test_umath_accuracy.py
│   │       │   │   │   ├── test_umath_complex.py
│   │       │   │   │   └── test_unicode.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _add_newdocs.py
│   │       │   │   ├── _add_newdocs_scalars.py
│   │       │   │   ├── _asarray.py
│   │       │   │   ├── _dtype.py
│   │       │   │   ├── _dtype_ctypes.py
│   │       │   │   ├── _exceptions.py
│   │       │   │   ├── _internal.py
│   │       │   │   ├── _methods.py
│   │       │   │   ├── _string_helpers.py
│   │       │   │   ├── _type_aliases.py
│   │       │   │   ├── _ufunc_config.py
│   │       │   │   ├── arrayprint.py
│   │       │   │   ├── cversions.py
│   │       │   │   ├── defchararray.py
│   │       │   │   ├── einsumfunc.py
│   │       │   │   ├── fromnumeric.py
│   │       │   │   ├── function_base.py
│   │       │   │   ├── getlimits.py
│   │       │   │   ├── memmap.py
│   │       │   │   ├── multiarray.py
│   │       │   │   ├── numeric.py
│   │       │   │   ├── numerictypes.py
│   │       │   │   ├── overrides.py
│   │       │   │   ├── printoptions.py
│   │       │   │   ├── records.py
│   │       │   │   ├── shape_base.py
│   │       │   │   ├── strings.py
│   │       │   │   ├── umath.py
│   │       │   ├── _pyinstaller/
│   │       │   │   ├── tests/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── pyinstaller-smoke.py
│   │       │   │   │   └── test_pyinstaller.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── hook-numpy.py
│   │       │   ├── _typing/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _add_docstring.py
│   │       │   │   ├── _array_like.py
│   │       │   │   ├── _char_codes.py
│   │       │   │   ├── _dtype_like.py
│   │       │   │   ├── _extended_precision.py
│   │       │   │   ├── _nbit.py
│   │       │   │   ├── _nbit_base.py
│   │       │   │   ├── _nested_sequence.py
│   │       │   │   ├── _scalars.py
│   │       │   │   ├── _shape.py
│   │       │   │   ├── _ufunc.py
│   │       │   ├── _utils/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _convertions.py
│   │       │   │   ├── _inspect.py
│   │       │   │   ├── _pep440.py
│   │       │   ├── char/
│   │       │   │   ├── __init__.py
│   │       │   ├── core/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _dtype.py
│   │       │   │   ├── _dtype_ctypes.py
│   │       │   │   ├── _internal.py
│   │       │   │   ├── _multiarray_umath.py
│   │       │   │   ├── _utils.py
│   │       │   │   ├── arrayprint.py
│   │       │   │   ├── defchararray.py
│   │       │   │   ├── einsumfunc.py
│   │       │   │   ├── fromnumeric.py
│   │       │   │   ├── function_base.py
│   │       │   │   ├── getlimits.py
│   │       │   │   ├── multiarray.py
│   │       │   │   ├── numeric.py
│   │       │   │   ├── numerictypes.py
│   │       │   │   ├── overrides.py
│   │       │   │   ├── records.py
│   │       │   │   ├── shape_base.py
│   │       │   │   └── umath.py
│   │       │   ├── ctypeslib/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _ctypeslib.py
│   │       │   ├── doc/
│   │       │   │   └── ufuncs.py
│   │       │   ├── f2py/
│   │       │   │   ├── _backends/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _backend.py
│   │       │   │   │   ├── _distutils.py
│   │       │   │   │   ├── _meson.py
│   │       │   │   ├── src/
│   │       │   │   ├── tests/
│   │       │   │   │   ├── src/
│   │       │   │   │   │   ├── abstract_interface/
│   │       │   │   │   │   ├── array_from_pyobj/
│   │       │   │   │   │   ├── assumed_shape/
│   │       │   │   │   │   │   ├── .f2py_f2cmap
│   │       │   │   │   │   ├── block_docstring/
│   │       │   │   │   │   ├── callback/
│   │       │   │   │   │   ├── cli/
│   │       │   │   │   │   ├── common/
│   │       │   │   │   │   ├── crackfortran/
│   │       │   │   │   │   ├── f2cmap/
│   │       │   │   │   │   │   ├── .f2py_f2cmap
│   │       │   │   │   │   ├── isocintrin/
│   │       │   │   │   │   ├── kind/
│   │       │   │   │   │   ├── mixed/
│   │       │   │   │   │   ├── modules/
│   │       │   │   │   │   │   ├── gh25337/
│   │       │   │   │   │   │   ├── gh26920/
│   │       │   │   │   │   ├── negative_bounds/
│   │       │   │   │   │   ├── parameter/
│   │       │   │   │   │   ├── quoted_character/
│   │       │   │   │   │   ├── regression/
│   │       │   │   │   │   ├── return_character/
│   │       │   │   │   │   ├── return_complex/
│   │       │   │   │   │   ├── return_integer/
│   │       │   │   │   │   ├── return_logical/
│   │       │   │   │   │   ├── return_real/
│   │       │   │   │   │   ├── routines/
│   │       │   │   │   │   ├── size/
│   │       │   │   │   │   ├── string/
│   │       │   │   │   │   └── value_attrspec/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_abstract_interface.py
│   │       │   │   │   ├── test_array_from_pyobj.py
│   │       │   │   │   ├── test_assumed_shape.py
│   │       │   │   │   ├── test_block_docstring.py
│   │       │   │   │   ├── test_callback.py
│   │       │   │   │   ├── test_character.py
│   │       │   │   │   ├── test_common.py
│   │       │   │   │   ├── test_crackfortran.py
│   │       │   │   │   ├── test_data.py
│   │       │   │   │   ├── test_docs.py
│   │       │   │   │   ├── test_f2cmap.py
│   │       │   │   │   ├── test_f2py2e.py
│   │       │   │   │   ├── test_isoc.py
│   │       │   │   │   ├── test_kind.py
│   │       │   │   │   ├── test_mixed.py
│   │       │   │   │   ├── test_modules.py
│   │       │   │   │   ├── test_parameter.py
│   │       │   │   │   ├── test_pyf_src.py
│   │       │   │   │   ├── test_quoted_character.py
│   │       │   │   │   ├── test_regression.py
│   │       │   │   │   ├── test_return_character.py
│   │       │   │   │   ├── test_return_complex.py
│   │       │   │   │   ├── test_return_integer.py
│   │       │   │   │   ├── test_return_logical.py
│   │       │   │   │   ├── test_return_real.py
│   │       │   │   │   ├── test_routines.py
│   │       │   │   │   ├── test_semicolon_split.py
│   │       │   │   │   ├── test_size.py
│   │       │   │   │   ├── test_string.py
│   │       │   │   │   ├── test_symbolic.py
│   │       │   │   │   ├── test_value_attrspec.py
│   │       │   │   │   └── util.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── __main__.py
│   │       │   │   ├── __version__.py
│   │       │   │   ├── _isocbind.py
│   │       │   │   ├── _src_pyf.py
│   │       │   │   ├── auxfuncs.py
│   │       │   │   ├── capi_maps.py
│   │       │   │   ├── cb_rules.py
│   │       │   │   ├── cfuncs.py
│   │       │   │   ├── common_rules.py
│   │       │   │   ├── crackfortran.py
│   │       │   │   ├── diagnose.py
│   │       │   │   ├── f2py2e.py
│   │       │   │   ├── f90mod_rules.py
│   │       │   │   ├── func2subr.py
│   │       │   │   ├── rules.py
│   │       │   │   ├── symbolic.py
│   │       │   │   ├── use_rules.py
│   │       │   ├── fft/
│   │       │   │   ├── tests/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_helper.py
│   │       │   │   │   └── test_pocketfft.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _helper.py
│   │       │   │   ├── _pocketfft.py
│   │       │   ├── lib/
│   │       │   │   ├── tests/
│   │       │   │   │   ├── data/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test__datasource.py
│   │       │   │   │   ├── test__iotools.py
│   │       │   │   │   ├── test__version.py
│   │       │   │   │   ├── test_array_utils.py
│   │       │   │   │   ├── test_arraypad.py
│   │       │   │   │   ├── test_arraysetops.py
│   │       │   │   │   ├── test_arrayterator.py
│   │       │   │   │   ├── test_format.py
│   │       │   │   │   ├── test_function_base.py
│   │       │   │   │   ├── test_histograms.py
│   │       │   │   │   ├── test_index_tricks.py
│   │       │   │   │   ├── test_io.py
│   │       │   │   │   ├── test_loadtxt.py
│   │       │   │   │   ├── test_mixins.py
│   │       │   │   │   ├── test_nanfunctions.py
│   │       │   │   │   ├── test_packbits.py
│   │       │   │   │   ├── test_polynomial.py
│   │       │   │   │   ├── test_recfunctions.py
│   │       │   │   │   ├── test_regression.py
│   │       │   │   │   ├── test_shape_base.py
│   │       │   │   │   ├── test_stride_tricks.py
│   │       │   │   │   ├── test_twodim_base.py
│   │       │   │   │   ├── test_type_check.py
│   │       │   │   │   ├── test_ufunclike.py
│   │       │   │   │   └── test_utils.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _array_utils_impl.py
│   │       │   │   ├── _arraypad_impl.py
│   │       │   │   ├── _arraysetops_impl.py
│   │       │   │   ├── _arrayterator_impl.py
│   │       │   │   ├── _datasource.py
│   │       │   │   ├── _format_impl.py
│   │       │   │   ├── _function_base_impl.py
│   │       │   │   ├── _histograms_impl.py
│   │       │   │   ├── _index_tricks_impl.py
│   │       │   │   ├── _iotools.py
│   │       │   │   ├── _nanfunctions_impl.py
│   │       │   │   ├── _npyio_impl.py
│   │       │   │   ├── _polynomial_impl.py
│   │       │   │   ├── _scimath_impl.py
│   │       │   │   ├── _shape_base_impl.py
│   │       │   │   ├── _stride_tricks_impl.py
│   │       │   │   ├── _twodim_base_impl.py
│   │       │   │   ├── _type_check_impl.py
│   │       │   │   ├── _ufunclike_impl.py
│   │       │   │   ├── _user_array_impl.py
│   │       │   │   ├── _utils_impl.py
│   │       │   │   ├── _version.py
│   │       │   │   ├── array_utils.py
│   │       │   │   ├── format.py
│   │       │   │   ├── introspect.py
│   │       │   │   ├── mixins.py
│   │       │   │   ├── npyio.py
│   │       │   │   ├── recfunctions.py
│   │       │   │   ├── scimath.py
│   │       │   │   ├── stride_tricks.py
│   │       │   │   ├── user_array.py
│   │       │   ├── linalg/
│   │       │   │   ├── tests/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_deprecations.py
│   │       │   │   │   ├── test_linalg.py
│   │       │   │   │   └── test_regression.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _linalg.py
│   │       │   ├── ma/
│   │       │   │   ├── tests/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_arrayobject.py
│   │       │   │   │   ├── test_core.py
│   │       │   │   │   ├── test_deprecations.py
│   │       │   │   │   ├── test_extras.py
│   │       │   │   │   ├── test_mrecords.py
│   │       │   │   │   ├── test_old_ma.py
│   │       │   │   │   ├── test_regression.py
│   │       │   │   │   └── test_subclassing.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── API_CHANGES.txt
│   │       │   │   ├── core.py
│   │       │   │   ├── extras.py
│   │       │   │   ├── mrecords.py
│   │       │   │   ├── testutils.py
│   │       │   ├── matrixlib/
│   │       │   │   ├── tests/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_defmatrix.py
│   │       │   │   │   ├── test_interaction.py
│   │       │   │   │   ├── test_masked_matrix.py
│   │       │   │   │   ├── test_matrix_linalg.py
│   │       │   │   │   ├── test_multiarray.py
│   │       │   │   │   ├── test_numeric.py
│   │       │   │   │   └── test_regression.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── defmatrix.py
│   │       │   ├── polynomial/
│   │       │   │   ├── tests/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_chebyshev.py
│   │       │   │   │   ├── test_classes.py
│   │       │   │   │   ├── test_hermite.py
│   │       │   │   │   ├── test_hermite_e.py
│   │       │   │   │   ├── test_laguerre.py
│   │       │   │   │   ├── test_legendre.py
│   │       │   │   │   ├── test_polynomial.py
│   │       │   │   │   ├── test_polyutils.py
│   │       │   │   │   ├── test_printing.py
│   │       │   │   │   └── test_symbol.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _polybase.py
│   │       │   │   ├── chebyshev.py
│   │       │   │   ├── hermite.py
│   │       │   │   ├── hermite_e.py
│   │       │   │   ├── laguerre.py
│   │       │   │   ├── legendre.py
│   │       │   │   ├── polynomial.py
│   │       │   │   ├── polyutils.py
│   │       │   ├── random/
│   │       │   │   ├── _examples/
│   │       │   │   │   ├── cffi/
│   │       │   │   │   │   ├── extending.py
│   │       │   │   │   │   └── parse.py
│   │       │   │   │   ├── cython/
│   │       │   │   │   └── numba/
│   │       │   │   │       ├── extending.py
│   │       │   │   │       └── extending_distributions.py
│   │       │   │   ├── lib/
│   │       │   │   ├── tests/
│   │       │   │   │   ├── data/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_direct.py
│   │       │   │   │   ├── test_extending.py
│   │       │   │   │   ├── test_generator_mt19937.py
│   │       │   │   │   ├── test_generator_mt19937_regressions.py
│   │       │   │   │   ├── test_random.py
│   │       │   │   │   ├── test_randomstate.py
│   │       │   │   │   ├── test_randomstate_regression.py
│   │       │   │   │   ├── test_regression.py
│   │       │   │   │   ├── test_seed_sequence.py
│   │       │   │   │   └── test_smoke.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _pickle.py
│   │       │   │   ├── LICENSE.md
│   │       │   ├── rec/
│   │       │   │   ├── __init__.py
│   │       │   ├── strings/
│   │       │   │   ├── __init__.py
│   │       │   ├── testing/
│   │       │   │   ├── _private/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── extbuild.py
│   │       │   │   │   ├── utils.py
│   │       │   │   ├── tests/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── test_utils.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── overrides.py
│   │       │   │   ├── print_coercion_tables.py
│   │       │   ├── tests/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── test__all__.py
│   │       │   │   ├── test_configtool.py
│   │       │   │   ├── test_ctypeslib.py
│   │       │   │   ├── test_lazyloading.py
│   │       │   │   ├── test_matlib.py
│   │       │   │   ├── test_numpy_config.py
│   │       │   │   ├── test_numpy_version.py
│   │       │   │   ├── test_public_api.py
│   │       │   │   ├── test_reloading.py
│   │       │   │   ├── test_scripts.py
│   │       │   │   └── test_warnings.py
│   │       │   ├── typing/
│   │       │   │   ├── tests/
│   │       │   │   │   ├── data/
│   │       │   │   │   │   ├── fail/
│   │       │   │   │   │   ├── misc/
│   │       │   │   │   │   ├── pass/
│   │       │   │   │   │   │   ├── arithmetic.py
│   │       │   │   │   │   │   ├── array_constructors.py
│   │       │   │   │   │   │   ├── array_like.py
│   │       │   │   │   │   │   ├── arrayprint.py
│   │       │   │   │   │   │   ├── arrayterator.py
│   │       │   │   │   │   │   ├── bitwise_ops.py
│   │       │   │   │   │   │   ├── comparisons.py
│   │       │   │   │   │   │   ├── dtype.py
│   │       │   │   │   │   │   ├── einsumfunc.py
│   │       │   │   │   │   │   ├── flatiter.py
│   │       │   │   │   │   │   ├── fromnumeric.py
│   │       │   │   │   │   │   ├── index_tricks.py
│   │       │   │   │   │   │   ├── lib_user_array.py
│   │       │   │   │   │   │   ├── lib_utils.py
│   │       │   │   │   │   │   ├── lib_version.py
│   │       │   │   │   │   │   ├── literal.py
│   │       │   │   │   │   │   ├── ma.py
│   │       │   │   │   │   │   ├── mod.py
│   │       │   │   │   │   │   ├── modules.py
│   │       │   │   │   │   │   ├── multiarray.py
│   │       │   │   │   │   │   ├── ndarray_conversion.py
│   │       │   │   │   │   │   ├── ndarray_misc.py
│   │       │   │   │   │   │   ├── ndarray_shape_manipulation.py
│   │       │   │   │   │   │   ├── nditer.py
│   │       │   │   │   │   │   ├── numeric.py
│   │       │   │   │   │   │   ├── numerictypes.py
│   │       │   │   │   │   │   ├── random.py
│   │       │   │   │   │   │   ├── recfunctions.py
│   │       │   │   │   │   │   ├── scalars.py
│   │       │   │   │   │   │   ├── shape.py
│   │       │   │   │   │   │   ├── simple.py
│   │       │   │   │   │   │   ├── ufunc_config.py
│   │       │   │   │   │   │   ├── ufunclike.py
│   │       │   │   │   │   │   ├── ufuncs.py
│   │       │   │   │   │   │   └── warnings_and_errors.py
│   │       │   │   │   │   ├── reveal/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_isfile.py
│   │       │   │   │   ├── test_runtime.py
│   │       │   │   │   └── test_typing.py
│   │       │   │   ├── __init__.py
│   │       │   │   └── mypy_plugin.py
│   │       │   ├── __config__.py
│   │       │   ├── __init__.py
│   │       │   ├── _array_api_info.py
│   │       │   ├── _configtool.py
│   │       │   ├── _distributor_init.py
│   │       │   ├── _expired_attrs_2_0.py
│   │       │   ├── _globals.py
│   │       │   ├── _pytesttester.py
│   │       │   ├── conftest.py
│   │       │   ├── dtypes.py
│   │       │   ├── exceptions.py
│   │       │   ├── matlib.py
│   │       │   ├── version.py
│   │       ├── numpy-2.4.4.dist-info/
│   │       │   ├── licenses/
│   │       │   │   ├── numpy/
│   │       │   │   │   ├── _core/
│   │       │   │   │   │   ├── include/
│   │       │   │   │   │   │   └── numpy/
│   │       │   │   │   │   │       └── libdivide/
│   │       │   │   │   │   │           └── LICENSE.txt
│   │       │   │   │   │   └── src/
│   │       │   │   │   │       ├── common/
│   │       │   │   │   │       │   └── pythoncapi-compat/
│   │       │   │   │   │       ├── highway/
│   │       │   │   │   │       ├── multiarray/
│   │       │   │   │   │       │   └── dragon4_LICENSE.txt
│   │       │   │   │   │       ├── npysort/
│   │       │   │   │   │       │   └── x86-simd-sort/
│   │       │   │   │   │       │       └── LICENSE.md
│   │       │   │   │   │       └── umath/
│   │       │   │   │   │           └── svml/
│   │       │   │   │   ├── fft/
│   │       │   │   │   │   └── pocketfft/
│   │       │   │   │   │       └── LICENSE.md
│   │       │   │   │   ├── linalg/
│   │       │   │   │   │   └── lapack_lite/
│   │       │   │   │   │       └── LICENSE.txt
│   │       │   │   │   ├── ma/
│   │       │   │   │   └── random/
│   │       │   │   │       ├── src/
│   │       │   │   │       │   ├── distributions/
│   │       │   │   │       │   │   └── LICENSE.md
│   │       │   │   │       │   ├── mt19937/
│   │       │   │   │       │   │   └── LICENSE.md
│   │       │   │   │       │   ├── pcg64/
│   │       │   │   │       │   │   └── LICENSE.md
│   │       │   │   │       │   ├── philox/
│   │       │   │   │       │   │   └── LICENSE.md
│   │       │   │   │       │   ├── sfc64/
│   │       │   │   │       │   │   └── LICENSE.md
│   │       │   │   │       │   └── splitmix64/
│   │       │   │   │       │       └── LICENSE.md
│   │       │   │   │       └── LICENSE.md
│   │       │   │   └── LICENSE.txt
│   │       │   ├── entry_points.txt
│   │       ├── numpy.libs/
│   │       ├── openpyxl/
│   │       │   ├── cell/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _writer.py
│   │       │   │   ├── cell.py
│   │       │   │   ├── read_only.py
│   │       │   │   ├── rich_text.py
│   │       │   │   └── text.py
│   │       │   ├── chart/
│   │       │   │   ├── _3d.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _chart.py
│   │       │   │   ├── area_chart.py
│   │       │   │   ├── axis.py
│   │       │   │   ├── bar_chart.py
│   │       │   │   ├── bubble_chart.py
│   │       │   │   ├── chartspace.py
│   │       │   │   ├── data_source.py
│   │       │   │   ├── descriptors.py
│   │       │   │   ├── error_bar.py
│   │       │   │   ├── label.py
│   │       │   │   ├── layout.py
│   │       │   │   ├── legend.py
│   │       │   │   ├── line_chart.py
│   │       │   │   ├── marker.py
│   │       │   │   ├── picture.py
│   │       │   │   ├── pie_chart.py
│   │       │   │   ├── pivot.py
│   │       │   │   ├── plotarea.py
│   │       │   │   ├── print_settings.py
│   │       │   │   ├── radar_chart.py
│   │       │   │   ├── reader.py
│   │       │   │   ├── reference.py
│   │       │   │   ├── scatter_chart.py
│   │       │   │   ├── series.py
│   │       │   │   ├── series_factory.py
│   │       │   │   ├── shapes.py
│   │       │   │   ├── stock_chart.py
│   │       │   │   ├── surface_chart.py
│   │       │   │   ├── text.py
│   │       │   │   ├── title.py
│   │       │   │   ├── trendline.py
│   │       │   │   └── updown_bars.py
│   │       │   ├── chartsheet/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── chartsheet.py
│   │       │   │   ├── custom.py
│   │       │   │   ├── properties.py
│   │       │   │   ├── protection.py
│   │       │   │   ├── publish.py
│   │       │   │   ├── relation.py
│   │       │   │   └── views.py
│   │       │   ├── comments/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── author.py
│   │       │   │   ├── comment_sheet.py
│   │       │   │   ├── comments.py
│   │       │   │   └── shape_writer.py
│   │       │   ├── compat/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── abc.py
│   │       │   │   ├── numbers.py
│   │       │   │   ├── product.py
│   │       │   │   ├── singleton.py
│   │       │   │   └── strings.py
│   │       │   ├── descriptors/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── base.py
│   │       │   │   ├── container.py
│   │       │   │   ├── excel.py
│   │       │   │   ├── namespace.py
│   │       │   │   ├── nested.py
│   │       │   │   ├── sequence.py
│   │       │   │   ├── serialisable.py
│   │       │   │   └── slots.py
│   │       │   ├── drawing/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── colors.py
│   │       │   │   ├── connector.py
│   │       │   │   ├── drawing.py
│   │       │   │   ├── effect.py
│   │       │   │   ├── fill.py
│   │       │   │   ├── geometry.py
│   │       │   │   ├── graphic.py
│   │       │   │   ├── image.py
│   │       │   │   ├── line.py
│   │       │   │   ├── picture.py
│   │       │   │   ├── properties.py
│   │       │   │   ├── relation.py
│   │       │   │   ├── spreadsheet_drawing.py
│   │       │   │   ├── text.py
│   │       │   │   └── xdr.py
│   │       │   ├── formatting/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── formatting.py
│   │       │   │   └── rule.py
│   │       │   ├── formula/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── tokenizer.py
│   │       │   │   └── translate.py
│   │       │   ├── packaging/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── core.py
│   │       │   │   ├── custom.py
│   │       │   │   ├── extended.py
│   │       │   │   ├── interface.py
│   │       │   │   ├── manifest.py
│   │       │   │   ├── relationship.py
│   │       │   │   └── workbook.py
│   │       │   ├── pivot/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── cache.py
│   │       │   │   ├── fields.py
│   │       │   │   ├── record.py
│   │       │   │   └── table.py
│   │       │   ├── reader/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── drawings.py
│   │       │   │   ├── excel.py
│   │       │   │   ├── strings.py
│   │       │   │   └── workbook.py
│   │       │   ├── styles/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── alignment.py
│   │       │   │   ├── borders.py
│   │       │   │   ├── builtins.py
│   │       │   │   ├── cell_style.py
│   │       │   │   ├── colors.py
│   │       │   │   ├── differential.py
│   │       │   │   ├── fills.py
│   │       │   │   ├── fonts.py
│   │       │   │   ├── named_styles.py
│   │       │   │   ├── numbers.py
│   │       │   │   ├── protection.py
│   │       │   │   ├── proxy.py
│   │       │   │   ├── styleable.py
│   │       │   │   ├── stylesheet.py
│   │       │   │   └── table.py
│   │       │   ├── utils/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── bound_dictionary.py
│   │       │   │   ├── cell.py
│   │       │   │   ├── dataframe.py
│   │       │   │   ├── datetime.py
│   │       │   │   ├── escape.py
│   │       │   │   ├── exceptions.py
│   │       │   │   ├── formulas.py
│   │       │   │   ├── indexed_list.py
│   │       │   │   ├── inference.py
│   │       │   │   ├── protection.py
│   │       │   │   └── units.py
│   │       │   ├── workbook/
│   │       │   │   ├── external_link/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── external.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _writer.py
│   │       │   │   ├── child.py
│   │       │   │   ├── defined_name.py
│   │       │   │   ├── external_reference.py
│   │       │   │   ├── function_group.py
│   │       │   │   ├── properties.py
│   │       │   │   ├── protection.py
│   │       │   │   ├── smart_tags.py
│   │       │   │   ├── views.py
│   │       │   │   ├── web.py
│   │       │   │   └── workbook.py
│   │       │   ├── worksheet/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _read_only.py
│   │       │   │   ├── _reader.py
│   │       │   │   ├── _write_only.py
│   │       │   │   ├── _writer.py
│   │       │   │   ├── cell_range.py
│   │       │   │   ├── cell_watch.py
│   │       │   │   ├── controls.py
│   │       │   │   ├── copier.py
│   │       │   │   ├── custom.py
│   │       │   │   ├── datavalidation.py
│   │       │   │   ├── dimensions.py
│   │       │   │   ├── drawing.py
│   │       │   │   ├── errors.py
│   │       │   │   ├── filters.py
│   │       │   │   ├── formula.py
│   │       │   │   ├── header_footer.py
│   │       │   │   ├── hyperlink.py
│   │       │   │   ├── merge.py
│   │       │   │   ├── ole.py
│   │       │   │   ├── page.py
│   │       │   │   ├── pagebreak.py
│   │       │   │   ├── picture.py
│   │       │   │   ├── print_settings.py
│   │       │   │   ├── properties.py
│   │       │   │   ├── protection.py
│   │       │   │   ├── related.py
│   │       │   │   ├── scenario.py
│   │       │   │   ├── smart_tag.py
│   │       │   │   ├── table.py
│   │       │   │   ├── views.py
│   │       │   │   └── worksheet.py
│   │       │   ├── writer/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── excel.py
│   │       │   │   └── theme.py
│   │       │   ├── xml/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── constants.py
│   │       │   │   └── functions.py
│   │       │   ├── __init__.py
│   │       │   └── _constants.py
│   │       ├── openpyxl-3.1.5.dist-info/
│   │       │   ├── top_level.txt
│   │       ├── ordered_set/
│   │       │   ├── __init__.py
│   │       ├── ordered_set-4.1.0.dist-info/
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
│   │       ├── pandas/
│   │       │   ├── _config/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── config.py
│   │       │   │   ├── dates.py
│   │       │   │   ├── display.py
│   │       │   │   └── localization.py
│   │       │   ├── _libs/
│   │       │   │   ├── tslibs/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── window/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── __init__.py
│   │       │   ├── _testing/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _hypothesis.py
│   │       │   │   ├── _io.py
│   │       │   │   ├── _warnings.py
│   │       │   │   ├── asserters.py
│   │       │   │   ├── compat.py
│   │       │   │   └── contexts.py
│   │       │   ├── api/
│   │       │   │   ├── executors/
│   │       │   │   │   └── __init__.py
│   │       │   │   ├── extensions/
│   │       │   │   │   └── __init__.py
│   │       │   │   ├── indexers/
│   │       │   │   │   └── __init__.py
│   │       │   │   ├── interchange/
│   │       │   │   │   └── __init__.py
│   │       │   │   ├── types/
│   │       │   │   │   └── __init__.py
│   │       │   │   ├── typing/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── aliases.py
│   │       │   │   ├── __init__.py
│   │       │   │   └── internals.py
│   │       │   ├── arrays/
│   │       │   │   └── __init__.py
│   │       │   ├── compat/
│   │       │   │   ├── numpy/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── function.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _constants.py
│   │       │   │   ├── _optional.py
│   │       │   │   ├── pickle_compat.py
│   │       │   │   └── pyarrow.py
│   │       │   ├── core/
│   │       │   │   ├── _numba/
│   │       │   │   │   ├── kernels/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── mean_.py
│   │       │   │   │   │   ├── min_max_.py
│   │       │   │   │   │   ├── shared.py
│   │       │   │   │   │   ├── sum_.py
│   │       │   │   │   │   └── var_.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── executor.py
│   │       │   │   │   └── extensions.py
│   │       │   │   ├── array_algos/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── datetimelike_accumulations.py
│   │       │   │   │   ├── masked_accumulations.py
│   │       │   │   │   ├── masked_reductions.py
│   │       │   │   │   ├── putmask.py
│   │       │   │   │   ├── quantile.py
│   │       │   │   │   ├── replace.py
│   │       │   │   │   ├── take.py
│   │       │   │   │   └── transforms.py
│   │       │   │   ├── arrays/
│   │       │   │   │   ├── arrow/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── _arrow_utils.py
│   │       │   │   │   │   ├── accessors.py
│   │       │   │   │   │   ├── array.py
│   │       │   │   │   │   └── extension_types.py
│   │       │   │   │   ├── sparse/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── accessor.py
│   │       │   │   │   │   ├── array.py
│   │       │   │   │   │   └── scipy_sparse.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _arrow_string_mixins.py
│   │       │   │   │   ├── _mixins.py
│   │       │   │   │   ├── _ranges.py
│   │       │   │   │   ├── _utils.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   ├── boolean.py
│   │       │   │   │   ├── categorical.py
│   │       │   │   │   ├── datetimelike.py
│   │       │   │   │   ├── datetimes.py
│   │       │   │   │   ├── floating.py
│   │       │   │   │   ├── integer.py
│   │       │   │   │   ├── interval.py
│   │       │   │   │   ├── masked.py
│   │       │   │   │   ├── numeric.py
│   │       │   │   │   ├── numpy_.py
│   │       │   │   │   ├── period.py
│   │       │   │   │   ├── string_.py
│   │       │   │   │   ├── string_arrow.py
│   │       │   │   │   └── timedeltas.py
│   │       │   │   ├── computation/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── align.py
│   │       │   │   │   ├── api.py
│   │       │   │   │   ├── check.py
│   │       │   │   │   ├── common.py
│   │       │   │   │   ├── engines.py
│   │       │   │   │   ├── eval.py
│   │       │   │   │   ├── expr.py
│   │       │   │   │   ├── expressions.py
│   │       │   │   │   ├── ops.py
│   │       │   │   │   ├── parsing.py
│   │       │   │   │   ├── pytables.py
│   │       │   │   │   └── scope.py
│   │       │   │   ├── dtypes/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── api.py
│   │       │   │   │   ├── astype.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   ├── cast.py
│   │       │   │   │   ├── common.py
│   │       │   │   │   ├── concat.py
│   │       │   │   │   ├── dtypes.py
│   │       │   │   │   ├── generic.py
│   │       │   │   │   ├── inference.py
│   │       │   │   │   └── missing.py
│   │       │   │   ├── groupby/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   ├── categorical.py
│   │       │   │   │   ├── generic.py
│   │       │   │   │   ├── groupby.py
│   │       │   │   │   ├── grouper.py
│   │       │   │   │   ├── indexing.py
│   │       │   │   │   ├── numba_.py
│   │       │   │   │   └── ops.py
│   │       │   │   ├── indexers/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── objects.py
│   │       │   │   │   └── utils.py
│   │       │   │   ├── indexes/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── accessors.py
│   │       │   │   │   ├── api.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   ├── category.py
│   │       │   │   │   ├── datetimelike.py
│   │       │   │   │   ├── datetimes.py
│   │       │   │   │   ├── extension.py
│   │       │   │   │   ├── frozen.py
│   │       │   │   │   ├── interval.py
│   │       │   │   │   ├── multi.py
│   │       │   │   │   ├── period.py
│   │       │   │   │   ├── range.py
│   │       │   │   │   └── timedeltas.py
│   │       │   │   ├── interchange/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── buffer.py
│   │       │   │   │   ├── column.py
│   │       │   │   │   ├── dataframe.py
│   │       │   │   │   ├── dataframe_protocol.py
│   │       │   │   │   ├── from_dataframe.py
│   │       │   │   │   └── utils.py
│   │       │   │   ├── internals/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── api.py
│   │       │   │   │   ├── blocks.py
│   │       │   │   │   ├── concat.py
│   │       │   │   │   ├── construction.py
│   │       │   │   │   ├── managers.py
│   │       │   │   │   └── ops.py
│   │       │   │   ├── methods/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── describe.py
│   │       │   │   │   ├── selectn.py
│   │       │   │   │   └── to_dict.py
│   │       │   │   ├── ops/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── array_ops.py
│   │       │   │   │   ├── common.py
│   │       │   │   │   ├── dispatch.py
│   │       │   │   │   ├── docstrings.py
│   │       │   │   │   ├── invalid.py
│   │       │   │   │   ├── mask_ops.py
│   │       │   │   │   └── missing.py
│   │       │   │   ├── reshape/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── api.py
│   │       │   │   │   ├── concat.py
│   │       │   │   │   ├── encoding.py
│   │       │   │   │   ├── melt.py
│   │       │   │   │   ├── merge.py
│   │       │   │   │   ├── pivot.py
│   │       │   │   │   ├── reshape.py
│   │       │   │   │   └── tile.py
│   │       │   │   ├── sparse/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── api.py
│   │       │   │   ├── strings/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── accessor.py
│   │       │   │   │   └── object_array.py
│   │       │   │   ├── tools/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── datetimes.py
│   │       │   │   │   ├── numeric.py
│   │       │   │   │   ├── timedeltas.py
│   │       │   │   │   └── times.py
│   │       │   │   ├── util/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── hashing.py
│   │       │   │   │   └── numba_.py
│   │       │   │   ├── window/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── common.py
│   │       │   │   │   ├── doc.py
│   │       │   │   │   ├── ewm.py
│   │       │   │   │   ├── expanding.py
│   │       │   │   │   ├── numba_.py
│   │       │   │   │   ├── online.py
│   │       │   │   │   └── rolling.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── accessor.py
│   │       │   │   ├── algorithms.py
│   │       │   │   ├── api.py
│   │       │   │   ├── apply.py
│   │       │   │   ├── arraylike.py
│   │       │   │   ├── base.py
│   │       │   │   ├── col.py
│   │       │   │   ├── common.py
│   │       │   │   ├── config_init.py
│   │       │   │   ├── construction.py
│   │       │   │   ├── flags.py
│   │       │   │   ├── frame.py
│   │       │   │   ├── generic.py
│   │       │   │   ├── indexing.py
│   │       │   │   ├── missing.py
│   │       │   │   ├── nanops.py
│   │       │   │   ├── resample.py
│   │       │   │   ├── roperator.py
│   │       │   │   ├── sample.py
│   │       │   │   ├── series.py
│   │       │   │   ├── shared_docs.py
│   │       │   │   └── sorting.py
│   │       │   ├── errors/
│   │       │   │   ├── __init__.py
│   │       │   │   └── cow.py
│   │       │   ├── io/
│   │       │   │   ├── clipboard/
│   │       │   │   │   └── __init__.py
│   │       │   │   ├── excel/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _base.py
│   │       │   │   │   ├── _calamine.py
│   │       │   │   │   ├── _odfreader.py
│   │       │   │   │   ├── _odswriter.py
│   │       │   │   │   ├── _openpyxl.py
│   │       │   │   │   ├── _pyxlsb.py
│   │       │   │   │   ├── _util.py
│   │       │   │   │   ├── _xlrd.py
│   │       │   │   │   └── _xlsxwriter.py
│   │       │   │   ├── formats/
│   │       │   │   │   ├── templates/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _color_data.py
│   │       │   │   │   ├── console.py
│   │       │   │   │   ├── css.py
│   │       │   │   │   ├── csvs.py
│   │       │   │   │   ├── excel.py
│   │       │   │   │   ├── format.py
│   │       │   │   │   ├── html.py
│   │       │   │   │   ├── info.py
│   │       │   │   │   ├── printing.py
│   │       │   │   │   ├── string.py
│   │       │   │   │   ├── style.py
│   │       │   │   │   ├── style_render.py
│   │       │   │   │   └── xml.py
│   │       │   │   ├── json/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _json.py
│   │       │   │   │   ├── _normalize.py
│   │       │   │   │   └── _table_schema.py
│   │       │   │   ├── parsers/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── arrow_parser_wrapper.py
│   │       │   │   │   ├── base_parser.py
│   │       │   │   │   ├── c_parser_wrapper.py
│   │       │   │   │   ├── python_parser.py
│   │       │   │   │   └── readers.py
│   │       │   │   ├── sas/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── sas7bdat.py
│   │       │   │   │   ├── sas_constants.py
│   │       │   │   │   ├── sas_xport.py
│   │       │   │   │   └── sasreader.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _util.py
│   │       │   │   ├── api.py
│   │       │   │   ├── clipboards.py
│   │       │   │   ├── common.py
│   │       │   │   ├── feather_format.py
│   │       │   │   ├── html.py
│   │       │   │   ├── iceberg.py
│   │       │   │   ├── orc.py
│   │       │   │   ├── parquet.py
│   │       │   │   ├── pickle.py
│   │       │   │   ├── pytables.py
│   │       │   │   ├── spss.py
│   │       │   │   ├── sql.py
│   │       │   │   ├── stata.py
│   │       │   │   └── xml.py
│   │       │   ├── plotting/
│   │       │   │   ├── _matplotlib/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── boxplot.py
│   │       │   │   │   ├── converter.py
│   │       │   │   │   ├── core.py
│   │       │   │   │   ├── groupby.py
│   │       │   │   │   ├── hist.py
│   │       │   │   │   ├── misc.py
│   │       │   │   │   ├── style.py
│   │       │   │   │   ├── timeseries.py
│   │       │   │   │   └── tools.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _core.py
│   │       │   │   └── _misc.py
│   │       │   ├── tests/
│   │       │   │   ├── api/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_api.py
│   │       │   │   │   └── test_types.py
│   │       │   │   ├── apply/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── common.py
│   │       │   │   │   ├── conftest.py
│   │       │   │   │   ├── test_frame_apply.py
│   │       │   │   │   ├── test_frame_apply_relabeling.py
│   │       │   │   │   ├── test_frame_transform.py
│   │       │   │   │   ├── test_invalid_arg.py
│   │       │   │   │   ├── test_numba.py
│   │       │   │   │   ├── test_series_apply.py
│   │       │   │   │   ├── test_series_apply_relabeling.py
│   │       │   │   │   ├── test_series_transform.py
│   │       │   │   │   └── test_str.py
│   │       │   │   ├── arithmetic/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── common.py
│   │       │   │   │   ├── conftest.py
│   │       │   │   │   ├── test_array_ops.py
│   │       │   │   │   ├── test_bool.py
│   │       │   │   │   ├── test_categorical.py
│   │       │   │   │   ├── test_datetime64.py
│   │       │   │   │   ├── test_interval.py
│   │       │   │   │   ├── test_numeric.py
│   │       │   │   │   ├── test_object.py
│   │       │   │   │   ├── test_period.py
│   │       │   │   │   ├── test_string.py
│   │       │   │   │   └── test_timedelta64.py
│   │       │   │   ├── arrays/
│   │       │   │   │   ├── boolean/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_arithmetic.py
│   │       │   │   │   │   ├── test_astype.py
│   │       │   │   │   │   ├── test_comparison.py
│   │       │   │   │   │   ├── test_construction.py
│   │       │   │   │   │   ├── test_function.py
│   │       │   │   │   │   ├── test_indexing.py
│   │       │   │   │   │   ├── test_logical.py
│   │       │   │   │   │   ├── test_ops.py
│   │       │   │   │   │   ├── test_reduction.py
│   │       │   │   │   │   └── test_repr.py
│   │       │   │   │   ├── categorical/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_algos.py
│   │       │   │   │   │   ├── test_analytics.py
│   │       │   │   │   │   ├── test_api.py
│   │       │   │   │   │   ├── test_astype.py
│   │       │   │   │   │   ├── test_constructors.py
│   │       │   │   │   │   ├── test_dtypes.py
│   │       │   │   │   │   ├── test_indexing.py
│   │       │   │   │   │   ├── test_map.py
│   │       │   │   │   │   ├── test_missing.py
│   │       │   │   │   │   ├── test_operators.py
│   │       │   │   │   │   ├── test_replace.py
│   │       │   │   │   │   ├── test_repr.py
│   │       │   │   │   │   ├── test_sorting.py
│   │       │   │   │   │   ├── test_subclass.py
│   │       │   │   │   │   ├── test_take.py
│   │       │   │   │   │   └── test_warnings.py
│   │       │   │   │   ├── datetimes/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_constructors.py
│   │       │   │   │   │   ├── test_cumulative.py
│   │       │   │   │   │   └── test_reductions.py
│   │       │   │   │   ├── floating/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── conftest.py
│   │       │   │   │   │   ├── test_arithmetic.py
│   │       │   │   │   │   ├── test_astype.py
│   │       │   │   │   │   ├── test_comparison.py
│   │       │   │   │   │   ├── test_concat.py
│   │       │   │   │   │   ├── test_construction.py
│   │       │   │   │   │   ├── test_contains.py
│   │       │   │   │   │   ├── test_function.py
│   │       │   │   │   │   ├── test_repr.py
│   │       │   │   │   │   └── test_to_numpy.py
│   │       │   │   │   ├── integer/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── conftest.py
│   │       │   │   │   │   ├── test_arithmetic.py
│   │       │   │   │   │   ├── test_comparison.py
│   │       │   │   │   │   ├── test_concat.py
│   │       │   │   │   │   ├── test_construction.py
│   │       │   │   │   │   ├── test_dtypes.py
│   │       │   │   │   │   ├── test_function.py
│   │       │   │   │   │   ├── test_indexing.py
│   │       │   │   │   │   ├── test_reduction.py
│   │       │   │   │   │   └── test_repr.py
│   │       │   │   │   ├── interval/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_astype.py
│   │       │   │   │   │   ├── test_formats.py
│   │       │   │   │   │   ├── test_interval.py
│   │       │   │   │   │   ├── test_interval_pyarrow.py
│   │       │   │   │   │   └── test_overlaps.py
│   │       │   │   │   ├── masked/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_arithmetic.py
│   │       │   │   │   │   ├── test_arrow_compat.py
│   │       │   │   │   │   ├── test_function.py
│   │       │   │   │   │   └── test_indexing.py
│   │       │   │   │   ├── numpy_/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_indexing.py
│   │       │   │   │   │   └── test_numpy.py
│   │       │   │   │   ├── period/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_arrow_compat.py
│   │       │   │   │   │   ├── test_astype.py
│   │       │   │   │   │   ├── test_constructors.py
│   │       │   │   │   │   └── test_reductions.py
│   │       │   │   │   ├── sparse/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_accessor.py
│   │       │   │   │   │   ├── test_arithmetics.py
│   │       │   │   │   │   ├── test_array.py
│   │       │   │   │   │   ├── test_astype.py
│   │       │   │   │   │   ├── test_combine_concat.py
│   │       │   │   │   │   ├── test_constructors.py
│   │       │   │   │   │   ├── test_dtype.py
│   │       │   │   │   │   ├── test_indexing.py
│   │       │   │   │   │   ├── test_libsparse.py
│   │       │   │   │   │   ├── test_reductions.py
│   │       │   │   │   │   └── test_unary.py
│   │       │   │   │   ├── string_/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_concat.py
│   │       │   │   │   │   ├── test_string.py
│   │       │   │   │   │   └── test_string_arrow.py
│   │       │   │   │   ├── timedeltas/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_constructors.py
│   │       │   │   │   │   ├── test_cumulative.py
│   │       │   │   │   │   └── test_reductions.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── masked_shared.py
│   │       │   │   │   ├── test_array.py
│   │       │   │   │   ├── test_datetimelike.py
│   │       │   │   │   ├── test_datetimes.py
│   │       │   │   │   ├── test_ndarray_backed.py
│   │       │   │   │   ├── test_period.py
│   │       │   │   │   └── test_timedeltas.py
│   │       │   │   ├── base/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── common.py
│   │       │   │   │   ├── test_constructors.py
│   │       │   │   │   ├── test_conversion.py
│   │       │   │   │   ├── test_fillna.py
│   │       │   │   │   ├── test_misc.py
│   │       │   │   │   ├── test_transpose.py
│   │       │   │   │   ├── test_unique.py
│   │       │   │   │   └── test_value_counts.py
│   │       │   │   ├── computation/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_compat.py
│   │       │   │   │   └── test_eval.py
│   │       │   │   ├── config/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_config.py
│   │       │   │   │   └── test_localization.py
│   │       │   │   ├── construction/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── test_extract_array.py
│   │       │   │   ├── copy_view/
│   │       │   │   │   ├── index/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_datetimeindex.py
│   │       │   │   │   │   ├── test_index.py
│   │       │   │   │   │   ├── test_intervalindex.py
│   │       │   │   │   │   ├── test_periodindex.py
│   │       │   │   │   │   └── test_timedeltaindex.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_array.py
│   │       │   │   │   ├── test_astype.py
│   │       │   │   │   ├── test_chained_assignment_deprecation.py
│   │       │   │   │   ├── test_clip.py
│   │       │   │   │   ├── test_constructors.py
│   │       │   │   │   ├── test_copy_deprecation.py
│   │       │   │   │   ├── test_core_functionalities.py
│   │       │   │   │   ├── test_functions.py
│   │       │   │   │   ├── test_indexing.py
│   │       │   │   │   ├── test_internals.py
│   │       │   │   │   ├── test_interp_fillna.py
│   │       │   │   │   ├── test_methods.py
│   │       │   │   │   ├── test_replace.py
│   │       │   │   │   ├── test_setitem.py
│   │       │   │   │   ├── test_util.py
│   │       │   │   │   └── util.py
│   │       │   │   ├── dtypes/
│   │       │   │   │   ├── cast/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_box_unbox.py
│   │       │   │   │   │   ├── test_can_hold_element.py
│   │       │   │   │   │   ├── test_construct_from_scalar.py
│   │       │   │   │   │   ├── test_construct_ndarray.py
│   │       │   │   │   │   ├── test_construct_object_arr.py
│   │       │   │   │   │   ├── test_dict_compat.py
│   │       │   │   │   │   ├── test_downcast.py
│   │       │   │   │   │   ├── test_find_common_type.py
│   │       │   │   │   │   ├── test_infer_datetimelike.py
│   │       │   │   │   │   ├── test_infer_dtype.py
│   │       │   │   │   │   └── test_promote.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_common.py
│   │       │   │   │   ├── test_concat.py
│   │       │   │   │   ├── test_dtypes.py
│   │       │   │   │   ├── test_generic.py
│   │       │   │   │   ├── test_inference.py
│   │       │   │   │   └── test_missing.py
│   │       │   │   ├── extension/
│   │       │   │   │   ├── array_with_attr/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── array.py
│   │       │   │   │   │   └── test_array_with_attr.py
│   │       │   │   │   ├── base/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── accumulate.py
│   │       │   │   │   │   ├── base.py
│   │       │   │   │   │   ├── casting.py
│   │       │   │   │   │   ├── constructors.py
│   │       │   │   │   │   ├── dim2.py
│   │       │   │   │   │   ├── dtype.py
│   │       │   │   │   │   ├── getitem.py
│   │       │   │   │   │   ├── groupby.py
│   │       │   │   │   │   ├── index.py
│   │       │   │   │   │   ├── interface.py
│   │       │   │   │   │   ├── io.py
│   │       │   │   │   │   ├── methods.py
│   │       │   │   │   │   ├── missing.py
│   │       │   │   │   │   ├── ops.py
│   │       │   │   │   │   ├── printing.py
│   │       │   │   │   │   ├── reduce.py
│   │       │   │   │   │   ├── reshaping.py
│   │       │   │   │   │   └── setitem.py
│   │       │   │   │   ├── date/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── array.py
│   │       │   │   │   ├── decimal/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── array.py
│   │       │   │   │   │   └── test_decimal.py
│   │       │   │   │   ├── json/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── array.py
│   │       │   │   │   │   └── test_json.py
│   │       │   │   │   ├── list/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── array.py
│   │       │   │   │   │   └── test_list.py
│   │       │   │   │   ├── uuid/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── test_uuid.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── conftest.py
│   │       │   │   │   ├── test_arrow.py
│   │       │   │   │   ├── test_categorical.py
│   │       │   │   │   ├── test_common.py
│   │       │   │   │   ├── test_datetime.py
│   │       │   │   │   ├── test_extension.py
│   │       │   │   │   ├── test_interval.py
│   │       │   │   │   ├── test_masked.py
│   │       │   │   │   ├── test_numpy.py
│   │       │   │   │   ├── test_period.py
│   │       │   │   │   ├── test_sparse.py
│   │       │   │   │   └── test_string.py
│   │       │   │   ├── frame/
│   │       │   │   │   ├── constructors/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_from_dict.py
│   │       │   │   │   │   └── test_from_records.py
│   │       │   │   │   ├── indexing/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_coercion.py
│   │       │   │   │   │   ├── test_delitem.py
│   │       │   │   │   │   ├── test_get.py
│   │       │   │   │   │   ├── test_get_value.py
│   │       │   │   │   │   ├── test_getitem.py
│   │       │   │   │   │   ├── test_indexing.py
│   │       │   │   │   │   ├── test_insert.py
│   │       │   │   │   │   ├── test_mask.py
│   │       │   │   │   │   ├── test_set_value.py
│   │       │   │   │   │   ├── test_setitem.py
│   │       │   │   │   │   ├── test_take.py
│   │       │   │   │   │   ├── test_where.py
│   │       │   │   │   │   └── test_xs.py
│   │       │   │   │   ├── methods/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_add_prefix_suffix.py
│   │       │   │   │   │   ├── test_align.py
│   │       │   │   │   │   ├── test_asfreq.py
│   │       │   │   │   │   ├── test_asof.py
│   │       │   │   │   │   ├── test_assign.py
│   │       │   │   │   │   ├── test_astype.py
│   │       │   │   │   │   ├── test_at_time.py
│   │       │   │   │   │   ├── test_between_time.py
│   │       │   │   │   │   ├── test_clip.py
│   │       │   │   │   │   ├── test_combine.py
│   │       │   │   │   │   ├── test_combine_first.py
│   │       │   │   │   │   ├── test_compare.py
│   │       │   │   │   │   ├── test_convert_dtypes.py
│   │       │   │   │   │   ├── test_copy.py
│   │       │   │   │   │   ├── test_count.py
│   │       │   │   │   │   ├── test_cov_corr.py
│   │       │   │   │   │   ├── test_describe.py
│   │       │   │   │   │   ├── test_diff.py
│   │       │   │   │   │   ├── test_dot.py
│   │       │   │   │   │   ├── test_drop.py
│   │       │   │   │   │   ├── test_drop_duplicates.py
│   │       │   │   │   │   ├── test_droplevel.py
│   │       │   │   │   │   ├── test_dropna.py
│   │       │   │   │   │   ├── test_dtypes.py
│   │       │   │   │   │   ├── test_duplicated.py
│   │       │   │   │   │   ├── test_equals.py
│   │       │   │   │   │   ├── test_explode.py
│   │       │   │   │   │   ├── test_fillna.py
│   │       │   │   │   │   ├── test_filter.py
│   │       │   │   │   │   ├── test_first_valid_index.py
│   │       │   │   │   │   ├── test_get_numeric_data.py
│   │       │   │   │   │   ├── test_head_tail.py
│   │       │   │   │   │   ├── test_infer_objects.py
│   │       │   │   │   │   ├── test_info.py
│   │       │   │   │   │   ├── test_interpolate.py
│   │       │   │   │   │   ├── test_is_homogeneous_dtype.py
│   │       │   │   │   │   ├── test_isetitem.py
│   │       │   │   │   │   ├── test_isin.py
│   │       │   │   │   │   ├── test_iterrows.py
│   │       │   │   │   │   ├── test_join.py
│   │       │   │   │   │   ├── test_map.py
│   │       │   │   │   │   ├── test_matmul.py
│   │       │   │   │   │   ├── test_nlargest.py
│   │       │   │   │   │   ├── test_pct_change.py
│   │       │   │   │   │   ├── test_pipe.py
│   │       │   │   │   │   ├── test_pop.py
│   │       │   │   │   │   ├── test_quantile.py
│   │       │   │   │   │   ├── test_rank.py
│   │       │   │   │   │   ├── test_reindex.py
│   │       │   │   │   │   ├── test_reindex_like.py
│   │       │   │   │   │   ├── test_rename.py
│   │       │   │   │   │   ├── test_rename_axis.py
│   │       │   │   │   │   ├── test_reorder_levels.py
│   │       │   │   │   │   ├── test_replace.py
│   │       │   │   │   │   ├── test_reset_index.py
│   │       │   │   │   │   ├── test_round.py
│   │       │   │   │   │   ├── test_sample.py
│   │       │   │   │   │   ├── test_select_dtypes.py
│   │       │   │   │   │   ├── test_set_axis.py
│   │       │   │   │   │   ├── test_set_index.py
│   │       │   │   │   │   ├── test_shift.py
│   │       │   │   │   │   ├── test_size.py
│   │       │   │   │   │   ├── test_sort_index.py
│   │       │   │   │   │   ├── test_sort_values.py
│   │       │   │   │   │   ├── test_swaplevel.py
│   │       │   │   │   │   ├── test_to_csv.py
│   │       │   │   │   │   ├── test_to_dict.py
│   │       │   │   │   │   ├── test_to_dict_of_blocks.py
│   │       │   │   │   │   ├── test_to_numpy.py
│   │       │   │   │   │   ├── test_to_period.py
│   │       │   │   │   │   ├── test_to_records.py
│   │       │   │   │   │   ├── test_to_timestamp.py
│   │       │   │   │   │   ├── test_transpose.py
│   │       │   │   │   │   ├── test_truncate.py
│   │       │   │   │   │   ├── test_tz_convert.py
│   │       │   │   │   │   ├── test_tz_localize.py
│   │       │   │   │   │   ├── test_update.py
│   │       │   │   │   │   ├── test_value_counts.py
│   │       │   │   │   │   └── test_values.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── common.py
│   │       │   │   │   ├── conftest.py
│   │       │   │   │   ├── test_alter_axes.py
│   │       │   │   │   ├── test_api.py
│   │       │   │   │   ├── test_arithmetic.py
│   │       │   │   │   ├── test_arrow_interface.py
│   │       │   │   │   ├── test_block_internals.py
│   │       │   │   │   ├── test_constructors.py
│   │       │   │   │   ├── test_cumulative.py
│   │       │   │   │   ├── test_iteration.py
│   │       │   │   │   ├── test_logical_ops.py
│   │       │   │   │   ├── test_nonunique_indexes.py
│   │       │   │   │   ├── test_npfuncs.py
│   │       │   │   │   ├── test_query_eval.py
│   │       │   │   │   ├── test_reductions.py
│   │       │   │   │   ├── test_repr.py
│   │       │   │   │   ├── test_stack_unstack.py
│   │       │   │   │   ├── test_subclass.py
│   │       │   │   │   ├── test_ufunc.py
│   │       │   │   │   ├── test_unary.py
│   │       │   │   │   └── test_validate.py
│   │       │   │   ├── generic/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_duplicate_labels.py
│   │       │   │   │   ├── test_finalize.py
│   │       │   │   │   ├── test_frame.py
│   │       │   │   │   ├── test_generic.py
│   │       │   │   │   ├── test_label_or_level_utils.py
│   │       │   │   │   ├── test_series.py
│   │       │   │   │   └── test_to_xarray.py
│   │       │   │   ├── groupby/
│   │       │   │   │   ├── aggregate/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_aggregate.py
│   │       │   │   │   │   ├── test_cython.py
│   │       │   │   │   │   ├── test_numba.py
│   │       │   │   │   │   └── test_other.py
│   │       │   │   │   ├── methods/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_describe.py
│   │       │   │   │   │   ├── test_groupby_shift_diff.py
│   │       │   │   │   │   ├── test_is_monotonic.py
│   │       │   │   │   │   ├── test_kurt.py
│   │       │   │   │   │   ├── test_nlargest_nsmallest.py
│   │       │   │   │   │   ├── test_nth.py
│   │       │   │   │   │   ├── test_quantile.py
│   │       │   │   │   │   ├── test_rank.py
│   │       │   │   │   │   ├── test_sample.py
│   │       │   │   │   │   ├── test_size.py
│   │       │   │   │   │   ├── test_skew.py
│   │       │   │   │   │   └── test_value_counts.py
│   │       │   │   │   ├── transform/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_numba.py
│   │       │   │   │   │   └── test_transform.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── conftest.py
│   │       │   │   │   ├── test_all_methods.py
│   │       │   │   │   ├── test_api.py
│   │       │   │   │   ├── test_apply.py
│   │       │   │   │   ├── test_bin_groupby.py
│   │       │   │   │   ├── test_categorical.py
│   │       │   │   │   ├── test_counting.py
│   │       │   │   │   ├── test_cumulative.py
│   │       │   │   │   ├── test_filters.py
│   │       │   │   │   ├── test_groupby.py
│   │       │   │   │   ├── test_groupby_dropna.py
│   │       │   │   │   ├── test_groupby_subclass.py
│   │       │   │   │   ├── test_grouping.py
│   │       │   │   │   ├── test_index_as_string.py
│   │       │   │   │   ├── test_indexing.py
│   │       │   │   │   ├── test_libgroupby.py
│   │       │   │   │   ├── test_missing.py
│   │       │   │   │   ├── test_numba.py
│   │       │   │   │   ├── test_numeric_only.py
│   │       │   │   │   ├── test_pipe.py
│   │       │   │   │   ├── test_raises.py
│   │       │   │   │   ├── test_reductions.py
│   │       │   │   │   └── test_timegrouper.py
│   │       │   │   ├── indexes/
│   │       │   │   │   ├── base_class/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_constructors.py
│   │       │   │   │   │   ├── test_formats.py
│   │       │   │   │   │   ├── test_indexing.py
│   │       │   │   │   │   ├── test_pickle.py
│   │       │   │   │   │   ├── test_reshape.py
│   │       │   │   │   │   ├── test_setops.py
│   │       │   │   │   │   └── test_where.py
│   │       │   │   │   ├── categorical/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_append.py
│   │       │   │   │   │   ├── test_astype.py
│   │       │   │   │   │   ├── test_category.py
│   │       │   │   │   │   ├── test_constructors.py
│   │       │   │   │   │   ├── test_equals.py
│   │       │   │   │   │   ├── test_fillna.py
│   │       │   │   │   │   ├── test_formats.py
│   │       │   │   │   │   ├── test_indexing.py
│   │       │   │   │   │   ├── test_map.py
│   │       │   │   │   │   ├── test_reindex.py
│   │       │   │   │   │   └── test_setops.py
│   │       │   │   │   ├── datetimelike_/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_drop_duplicates.py
│   │       │   │   │   │   ├── test_equals.py
│   │       │   │   │   │   ├── test_indexing.py
│   │       │   │   │   │   ├── test_is_monotonic.py
│   │       │   │   │   │   ├── test_nat.py
│   │       │   │   │   │   ├── test_sort_values.py
│   │       │   │   │   │   └── test_value_counts.py
│   │       │   │   │   ├── datetimes/
│   │       │   │   │   │   ├── methods/
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   ├── test_asof.py
│   │       │   │   │   │   │   ├── test_astype.py
│   │       │   │   │   │   │   ├── test_delete.py
│   │       │   │   │   │   │   ├── test_factorize.py
│   │       │   │   │   │   │   ├── test_fillna.py
│   │       │   │   │   │   │   ├── test_insert.py
│   │       │   │   │   │   │   ├── test_isocalendar.py
│   │       │   │   │   │   │   ├── test_map.py
│   │       │   │   │   │   │   ├── test_normalize.py
│   │       │   │   │   │   │   ├── test_repeat.py
│   │       │   │   │   │   │   ├── test_resolution.py
│   │       │   │   │   │   │   ├── test_round.py
│   │       │   │   │   │   │   ├── test_shift.py
│   │       │   │   │   │   │   ├── test_snap.py
│   │       │   │   │   │   │   ├── test_to_frame.py
│   │       │   │   │   │   │   ├── test_to_julian_date.py
│   │       │   │   │   │   │   ├── test_to_period.py
│   │       │   │   │   │   │   ├── test_to_pydatetime.py
│   │       │   │   │   │   │   ├── test_to_series.py
│   │       │   │   │   │   │   ├── test_tz_convert.py
│   │       │   │   │   │   │   ├── test_tz_localize.py
│   │       │   │   │   │   │   └── test_unique.py
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_arithmetic.py
│   │       │   │   │   │   ├── test_constructors.py
│   │       │   │   │   │   ├── test_date_range.py
│   │       │   │   │   │   ├── test_datetime.py
│   │       │   │   │   │   ├── test_formats.py
│   │       │   │   │   │   ├── test_freq_attr.py
│   │       │   │   │   │   ├── test_indexing.py
│   │       │   │   │   │   ├── test_iter.py
│   │       │   │   │   │   ├── test_join.py
│   │       │   │   │   │   ├── test_npfuncs.py
│   │       │   │   │   │   ├── test_ops.py
│   │       │   │   │   │   ├── test_partial_slicing.py
│   │       │   │   │   │   ├── test_pickle.py
│   │       │   │   │   │   ├── test_reindex.py
│   │       │   │   │   │   ├── test_scalar_compat.py
│   │       │   │   │   │   ├── test_setops.py
│   │       │   │   │   │   └── test_timezones.py
│   │       │   │   │   ├── interval/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_astype.py
│   │       │   │   │   │   ├── test_constructors.py
│   │       │   │   │   │   ├── test_equals.py
│   │       │   │   │   │   ├── test_formats.py
│   │       │   │   │   │   ├── test_indexing.py
│   │       │   │   │   │   ├── test_interval.py
│   │       │   │   │   │   ├── test_interval_range.py
│   │       │   │   │   │   ├── test_interval_tree.py
│   │       │   │   │   │   ├── test_join.py
│   │       │   │   │   │   ├── test_pickle.py
│   │       │   │   │   │   └── test_setops.py
│   │       │   │   │   ├── multi/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── conftest.py
│   │       │   │   │   │   ├── test_analytics.py
│   │       │   │   │   │   ├── test_astype.py
│   │       │   │   │   │   ├── test_compat.py
│   │       │   │   │   │   ├── test_constructors.py
│   │       │   │   │   │   ├── test_conversion.py
│   │       │   │   │   │   ├── test_copy.py
│   │       │   │   │   │   ├── test_drop.py
│   │       │   │   │   │   ├── test_duplicates.py
│   │       │   │   │   │   ├── test_equivalence.py
│   │       │   │   │   │   ├── test_formats.py
│   │       │   │   │   │   ├── test_get_level_values.py
│   │       │   │   │   │   ├── test_get_set.py
│   │       │   │   │   │   ├── test_indexing.py
│   │       │   │   │   │   ├── test_integrity.py
│   │       │   │   │   │   ├── test_isin.py
│   │       │   │   │   │   ├── test_join.py
│   │       │   │   │   │   ├── test_lexsort.py
│   │       │   │   │   │   ├── test_missing.py
│   │       │   │   │   │   ├── test_monotonic.py
│   │       │   │   │   │   ├── test_names.py
│   │       │   │   │   │   ├── test_partial_indexing.py
│   │       │   │   │   │   ├── test_pickle.py
│   │       │   │   │   │   ├── test_reindex.py
│   │       │   │   │   │   ├── test_reshape.py
│   │       │   │   │   │   ├── test_setops.py
│   │       │   │   │   │   ├── test_sorting.py
│   │       │   │   │   │   ├── test_take.py
│   │       │   │   │   │   └── test_util.py
│   │       │   │   │   ├── numeric/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_astype.py
│   │       │   │   │   │   ├── test_indexing.py
│   │       │   │   │   │   ├── test_join.py
│   │       │   │   │   │   ├── test_numeric.py
│   │       │   │   │   │   └── test_setops.py
│   │       │   │   │   ├── object/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_astype.py
│   │       │   │   │   │   └── test_indexing.py
│   │       │   │   │   ├── period/
│   │       │   │   │   │   ├── methods/
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   ├── test_asfreq.py
│   │       │   │   │   │   │   ├── test_astype.py
│   │       │   │   │   │   │   ├── test_factorize.py
│   │       │   │   │   │   │   ├── test_fillna.py
│   │       │   │   │   │   │   ├── test_insert.py
│   │       │   │   │   │   │   ├── test_is_full.py
│   │       │   │   │   │   │   ├── test_repeat.py
│   │       │   │   │   │   │   ├── test_shift.py
│   │       │   │   │   │   │   └── test_to_timestamp.py
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_constructors.py
│   │       │   │   │   │   ├── test_formats.py
│   │       │   │   │   │   ├── test_freq_attr.py
│   │       │   │   │   │   ├── test_indexing.py
│   │       │   │   │   │   ├── test_join.py
│   │       │   │   │   │   ├── test_monotonic.py
│   │       │   │   │   │   ├── test_partial_slicing.py
│   │       │   │   │   │   ├── test_period.py
│   │       │   │   │   │   ├── test_period_range.py
│   │       │   │   │   │   ├── test_pickle.py
│   │       │   │   │   │   ├── test_resolution.py
│   │       │   │   │   │   ├── test_scalar_compat.py
│   │       │   │   │   │   ├── test_searchsorted.py
│   │       │   │   │   │   ├── test_setops.py
│   │       │   │   │   │   └── test_tools.py
│   │       │   │   │   ├── ranges/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_constructors.py
│   │       │   │   │   │   ├── test_indexing.py
│   │       │   │   │   │   ├── test_join.py
│   │       │   │   │   │   ├── test_range.py
│   │       │   │   │   │   └── test_setops.py
│   │       │   │   │   ├── string/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_astype.py
│   │       │   │   │   │   └── test_indexing.py
│   │       │   │   │   ├── timedeltas/
│   │       │   │   │   │   ├── methods/
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   ├── test_astype.py
│   │       │   │   │   │   │   ├── test_factorize.py
│   │       │   │   │   │   │   ├── test_fillna.py
│   │       │   │   │   │   │   ├── test_insert.py
│   │       │   │   │   │   │   ├── test_repeat.py
│   │       │   │   │   │   │   └── test_shift.py
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_arithmetic.py
│   │       │   │   │   │   ├── test_constructors.py
│   │       │   │   │   │   ├── test_delete.py
│   │       │   │   │   │   ├── test_formats.py
│   │       │   │   │   │   ├── test_freq_attr.py
│   │       │   │   │   │   ├── test_indexing.py
│   │       │   │   │   │   ├── test_join.py
│   │       │   │   │   │   ├── test_ops.py
│   │       │   │   │   │   ├── test_pickle.py
│   │       │   │   │   │   ├── test_scalar_compat.py
│   │       │   │   │   │   ├── test_searchsorted.py
│   │       │   │   │   │   ├── test_setops.py
│   │       │   │   │   │   ├── test_timedelta.py
│   │       │   │   │   │   └── test_timedelta_range.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── conftest.py
│   │       │   │   │   ├── test_any_index.py
│   │       │   │   │   ├── test_base.py
│   │       │   │   │   ├── test_common.py
│   │       │   │   │   ├── test_datetimelike.py
│   │       │   │   │   ├── test_engines.py
│   │       │   │   │   ├── test_frozen.py
│   │       │   │   │   ├── test_index_new.py
│   │       │   │   │   ├── test_indexing.py
│   │       │   │   │   ├── test_numpy_compat.py
│   │       │   │   │   ├── test_old_base.py
│   │       │   │   │   ├── test_setops.py
│   │       │   │   │   └── test_subclass.py
│   │       │   │   ├── indexing/
│   │       │   │   │   ├── interval/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_interval.py
│   │       │   │   │   │   └── test_interval_new.py
│   │       │   │   │   ├── multiindex/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_chaining_and_caching.py
│   │       │   │   │   │   ├── test_datetime.py
│   │       │   │   │   │   ├── test_getitem.py
│   │       │   │   │   │   ├── test_iloc.py
│   │       │   │   │   │   ├── test_indexing_slow.py
│   │       │   │   │   │   ├── test_loc.py
│   │       │   │   │   │   ├── test_multiindex.py
│   │       │   │   │   │   ├── test_partial.py
│   │       │   │   │   │   ├── test_setitem.py
│   │       │   │   │   │   ├── test_slice.py
│   │       │   │   │   │   └── test_sorted.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── common.py
│   │       │   │   │   ├── test_at.py
│   │       │   │   │   ├── test_categorical.py
│   │       │   │   │   ├── test_chaining_and_caching.py
│   │       │   │   │   ├── test_check_indexer.py
│   │       │   │   │   ├── test_coercion.py
│   │       │   │   │   ├── test_datetime.py
│   │       │   │   │   ├── test_floats.py
│   │       │   │   │   ├── test_iat.py
│   │       │   │   │   ├── test_iloc.py
│   │       │   │   │   ├── test_indexers.py
│   │       │   │   │   ├── test_indexing.py
│   │       │   │   │   ├── test_loc.py
│   │       │   │   │   ├── test_na_indexing.py
│   │       │   │   │   ├── test_partial.py
│   │       │   │   │   └── test_scalar.py
│   │       │   │   ├── interchange/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_impl.py
│   │       │   │   │   ├── test_spec_conformance.py
│   │       │   │   │   └── test_utils.py
│   │       │   │   ├── internals/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_api.py
│   │       │   │   │   └── test_internals.py
│   │       │   │   ├── io/
│   │       │   │   │   ├── excel/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_odf.py
│   │       │   │   │   │   ├── test_odswriter.py
│   │       │   │   │   │   ├── test_openpyxl.py
│   │       │   │   │   │   ├── test_readers.py
│   │       │   │   │   │   ├── test_style.py
│   │       │   │   │   │   ├── test_writers.py
│   │       │   │   │   │   ├── test_xlrd.py
│   │       │   │   │   │   └── test_xlsxwriter.py
│   │       │   │   │   ├── formats/
│   │       │   │   │   │   ├── style/
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   ├── test_bar.py
│   │       │   │   │   │   │   ├── test_exceptions.py
│   │       │   │   │   │   │   ├── test_format.py
│   │       │   │   │   │   │   ├── test_highlight.py
│   │       │   │   │   │   │   ├── test_html.py
│   │       │   │   │   │   │   ├── test_matplotlib.py
│   │       │   │   │   │   │   ├── test_non_unique.py
│   │       │   │   │   │   │   ├── test_style.py
│   │       │   │   │   │   │   ├── test_to_latex.py
│   │       │   │   │   │   │   ├── test_to_string.py
│   │       │   │   │   │   │   ├── test_to_typst.py
│   │       │   │   │   │   │   └── test_tooltip.py
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_console.py
│   │       │   │   │   │   ├── test_css.py
│   │       │   │   │   │   ├── test_eng_formatting.py
│   │       │   │   │   │   ├── test_format.py
│   │       │   │   │   │   ├── test_ipython_compat.py
│   │       │   │   │   │   ├── test_printing.py
│   │       │   │   │   │   ├── test_to_csv.py
│   │       │   │   │   │   ├── test_to_excel.py
│   │       │   │   │   │   ├── test_to_html.py
│   │       │   │   │   │   ├── test_to_latex.py
│   │       │   │   │   │   ├── test_to_markdown.py
│   │       │   │   │   │   └── test_to_string.py
│   │       │   │   │   ├── json/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── conftest.py
│   │       │   │   │   │   ├── test_compression.py
│   │       │   │   │   │   ├── test_deprecated_kwargs.py
│   │       │   │   │   │   ├── test_json_table_schema.py
│   │       │   │   │   │   ├── test_json_table_schema_ext_dtype.py
│   │       │   │   │   │   ├── test_normalize.py
│   │       │   │   │   │   ├── test_pandas.py
│   │       │   │   │   │   ├── test_readlines.py
│   │       │   │   │   │   └── test_ujson.py
│   │       │   │   │   ├── parser/
│   │       │   │   │   │   ├── common/
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   ├── test_chunksize.py
│   │       │   │   │   │   │   ├── test_common_basic.py
│   │       │   │   │   │   │   ├── test_data_list.py
│   │       │   │   │   │   │   ├── test_decimal.py
│   │       │   │   │   │   │   ├── test_file_buffer_url.py
│   │       │   │   │   │   │   ├── test_float.py
│   │       │   │   │   │   │   ├── test_index.py
│   │       │   │   │   │   │   ├── test_inf.py
│   │       │   │   │   │   │   ├── test_ints.py
│   │       │   │   │   │   │   ├── test_iterator.py
│   │       │   │   │   │   │   └── test_read_errors.py
│   │       │   │   │   │   ├── dtypes/
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   ├── test_categorical.py
│   │       │   │   │   │   │   ├── test_dtypes_basic.py
│   │       │   │   │   │   │   └── test_empty.py
│   │       │   │   │   │   ├── usecols/
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   ├── test_parse_dates.py
│   │       │   │   │   │   │   ├── test_strings.py
│   │       │   │   │   │   │   └── test_usecols_basic.py
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── conftest.py
│   │       │   │   │   │   ├── test_c_parser_only.py
│   │       │   │   │   │   ├── test_comment.py
│   │       │   │   │   │   ├── test_compression.py
│   │       │   │   │   │   ├── test_concatenate_chunks.py
│   │       │   │   │   │   ├── test_converters.py
│   │       │   │   │   │   ├── test_dialect.py
│   │       │   │   │   │   ├── test_encoding.py
│   │       │   │   │   │   ├── test_header.py
│   │       │   │   │   │   ├── test_index_col.py
│   │       │   │   │   │   ├── test_mangle_dupes.py
│   │       │   │   │   │   ├── test_multi_thread.py
│   │       │   │   │   │   ├── test_na_values.py
│   │       │   │   │   │   ├── test_network.py
│   │       │   │   │   │   ├── test_parse_dates.py
│   │       │   │   │   │   ├── test_python_parser_only.py
│   │       │   │   │   │   ├── test_quoting.py
│   │       │   │   │   │   ├── test_read_fwf.py
│   │       │   │   │   │   ├── test_skiprows.py
│   │       │   │   │   │   ├── test_textreader.py
│   │       │   │   │   │   ├── test_unsupported.py
│   │       │   │   │   │   └── test_upcast.py
│   │       │   │   │   ├── pytables/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── common.py
│   │       │   │   │   │   ├── conftest.py
│   │       │   │   │   │   ├── test_append.py
│   │       │   │   │   │   ├── test_categorical.py
│   │       │   │   │   │   ├── test_compat.py
│   │       │   │   │   │   ├── test_complex.py
│   │       │   │   │   │   ├── test_errors.py
│   │       │   │   │   │   ├── test_file_handling.py
│   │       │   │   │   │   ├── test_keys.py
│   │       │   │   │   │   ├── test_put.py
│   │       │   │   │   │   ├── test_pytables_missing.py
│   │       │   │   │   │   ├── test_read.py
│   │       │   │   │   │   ├── test_retain_attributes.py
│   │       │   │   │   │   ├── test_round_trip.py
│   │       │   │   │   │   ├── test_select.py
│   │       │   │   │   │   ├── test_store.py
│   │       │   │   │   │   ├── test_subclass.py
│   │       │   │   │   │   ├── test_time_series.py
│   │       │   │   │   │   └── test_timezones.py
│   │       │   │   │   ├── sas/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_byteswap.py
│   │       │   │   │   │   ├── test_sas.py
│   │       │   │   │   │   ├── test_sas7bdat.py
│   │       │   │   │   │   └── test_xport.py
│   │       │   │   │   ├── xml/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── conftest.py
│   │       │   │   │   │   ├── test_to_xml.py
│   │       │   │   │   │   ├── test_xml.py
│   │       │   │   │   │   └── test_xml_dtypes.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── conftest.py
│   │       │   │   │   ├── generate_legacy_storage_files.py
│   │       │   │   │   ├── test_clipboard.py
│   │       │   │   │   ├── test_common.py
│   │       │   │   │   ├── test_compression.py
│   │       │   │   │   ├── test_feather.py
│   │       │   │   │   ├── test_fsspec.py
│   │       │   │   │   ├── test_gcs.py
│   │       │   │   │   ├── test_html.py
│   │       │   │   │   ├── test_http_headers.py
│   │       │   │   │   ├── test_iceberg.py
│   │       │   │   │   ├── test_orc.py
│   │       │   │   │   ├── test_parquet.py
│   │       │   │   │   ├── test_pickle.py
│   │       │   │   │   ├── test_s3.py
│   │       │   │   │   ├── test_spss.py
│   │       │   │   │   ├── test_sql.py
│   │       │   │   │   ├── test_stata.py
│   │       │   │   │   └── test_util.py
│   │       │   │   ├── libs/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_hashtable.py
│   │       │   │   │   ├── test_join.py
│   │       │   │   │   ├── test_lib.py
│   │       │   │   │   └── test_libalgos.py
│   │       │   │   ├── plotting/
│   │       │   │   │   ├── frame/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_frame.py
│   │       │   │   │   │   ├── test_frame_color.py
│   │       │   │   │   │   ├── test_frame_groupby.py
│   │       │   │   │   │   ├── test_frame_legend.py
│   │       │   │   │   │   ├── test_frame_subplots.py
│   │       │   │   │   │   └── test_hist_box_by.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── common.py
│   │       │   │   │   ├── conftest.py
│   │       │   │   │   ├── test_backend.py
│   │       │   │   │   ├── test_boxplot_method.py
│   │       │   │   │   ├── test_common.py
│   │       │   │   │   ├── test_converter.py
│   │       │   │   │   ├── test_datetimelike.py
│   │       │   │   │   ├── test_groupby.py
│   │       │   │   │   ├── test_hist_method.py
│   │       │   │   │   ├── test_misc.py
│   │       │   │   │   ├── test_series.py
│   │       │   │   │   └── test_style.py
│   │       │   │   ├── reductions/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_reductions.py
│   │       │   │   │   └── test_stat_reductions.py
│   │       │   │   ├── resample/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── conftest.py
│   │       │   │   │   ├── test_base.py
│   │       │   │   │   ├── test_datetime_index.py
│   │       │   │   │   ├── test_period_index.py
│   │       │   │   │   ├── test_resample_api.py
│   │       │   │   │   ├── test_resampler_grouper.py
│   │       │   │   │   ├── test_time_grouper.py
│   │       │   │   │   └── test_timedelta.py
│   │       │   │   ├── reshape/
│   │       │   │   │   ├── concat/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_append.py
│   │       │   │   │   │   ├── test_append_common.py
│   │       │   │   │   │   ├── test_categorical.py
│   │       │   │   │   │   ├── test_concat.py
│   │       │   │   │   │   ├── test_dataframe.py
│   │       │   │   │   │   ├── test_datetimes.py
│   │       │   │   │   │   ├── test_empty.py
│   │       │   │   │   │   ├── test_index.py
│   │       │   │   │   │   ├── test_invalid.py
│   │       │   │   │   │   ├── test_series.py
│   │       │   │   │   │   └── test_sort.py
│   │       │   │   │   ├── merge/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_join.py
│   │       │   │   │   │   ├── test_merge.py
│   │       │   │   │   │   ├── test_merge_antijoin.py
│   │       │   │   │   │   ├── test_merge_asof.py
│   │       │   │   │   │   ├── test_merge_cross.py
│   │       │   │   │   │   ├── test_merge_index_as_string.py
│   │       │   │   │   │   ├── test_merge_ordered.py
│   │       │   │   │   │   └── test_multi.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_crosstab.py
│   │       │   │   │   ├── test_cut.py
│   │       │   │   │   ├── test_from_dummies.py
│   │       │   │   │   ├── test_get_dummies.py
│   │       │   │   │   ├── test_melt.py
│   │       │   │   │   ├── test_pivot.py
│   │       │   │   │   ├── test_pivot_multilevel.py
│   │       │   │   │   ├── test_qcut.py
│   │       │   │   │   └── test_union_categoricals.py
│   │       │   │   ├── scalar/
│   │       │   │   │   ├── interval/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_arithmetic.py
│   │       │   │   │   │   ├── test_constructors.py
│   │       │   │   │   │   ├── test_contains.py
│   │       │   │   │   │   ├── test_formats.py
│   │       │   │   │   │   ├── test_interval.py
│   │       │   │   │   │   └── test_overlaps.py
│   │       │   │   │   ├── period/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_arithmetic.py
│   │       │   │   │   │   ├── test_asfreq.py
│   │       │   │   │   │   └── test_period.py
│   │       │   │   │   ├── timedelta/
│   │       │   │   │   │   ├── methods/
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   ├── test_as_unit.py
│   │       │   │   │   │   │   └── test_round.py
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_arithmetic.py
│   │       │   │   │   │   ├── test_constructors.py
│   │       │   │   │   │   ├── test_formats.py
│   │       │   │   │   │   └── test_timedelta.py
│   │       │   │   │   ├── timestamp/
│   │       │   │   │   │   ├── methods/
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   ├── test_as_unit.py
│   │       │   │   │   │   │   ├── test_normalize.py
│   │       │   │   │   │   │   ├── test_replace.py
│   │       │   │   │   │   │   ├── test_round.py
│   │       │   │   │   │   │   ├── test_timestamp_method.py
│   │       │   │   │   │   │   ├── test_to_julian_date.py
│   │       │   │   │   │   │   ├── test_to_pydatetime.py
│   │       │   │   │   │   │   ├── test_tz_convert.py
│   │       │   │   │   │   │   └── test_tz_localize.py
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_arithmetic.py
│   │       │   │   │   │   ├── test_comparisons.py
│   │       │   │   │   │   ├── test_constructors.py
│   │       │   │   │   │   ├── test_formats.py
│   │       │   │   │   │   ├── test_timestamp.py
│   │       │   │   │   │   └── test_timezones.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_na_scalar.py
│   │       │   │   │   └── test_nat.py
│   │       │   │   ├── series/
│   │       │   │   │   ├── accessors/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_cat_accessor.py
│   │       │   │   │   │   ├── test_dt_accessor.py
│   │       │   │   │   │   ├── test_list_accessor.py
│   │       │   │   │   │   ├── test_sparse_accessor.py
│   │       │   │   │   │   ├── test_str_accessor.py
│   │       │   │   │   │   └── test_struct_accessor.py
│   │       │   │   │   ├── indexing/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_datetime.py
│   │       │   │   │   │   ├── test_delitem.py
│   │       │   │   │   │   ├── test_get.py
│   │       │   │   │   │   ├── test_getitem.py
│   │       │   │   │   │   ├── test_indexing.py
│   │       │   │   │   │   ├── test_mask.py
│   │       │   │   │   │   ├── test_set_value.py
│   │       │   │   │   │   ├── test_setitem.py
│   │       │   │   │   │   ├── test_take.py
│   │       │   │   │   │   ├── test_where.py
│   │       │   │   │   │   └── test_xs.py
│   │       │   │   │   ├── methods/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_add_prefix_suffix.py
│   │       │   │   │   │   ├── test_align.py
│   │       │   │   │   │   ├── test_argsort.py
│   │       │   │   │   │   ├── test_asof.py
│   │       │   │   │   │   ├── test_astype.py
│   │       │   │   │   │   ├── test_autocorr.py
│   │       │   │   │   │   ├── test_between.py
│   │       │   │   │   │   ├── test_case_when.py
│   │       │   │   │   │   ├── test_clip.py
│   │       │   │   │   │   ├── test_combine.py
│   │       │   │   │   │   ├── test_combine_first.py
│   │       │   │   │   │   ├── test_compare.py
│   │       │   │   │   │   ├── test_convert_dtypes.py
│   │       │   │   │   │   ├── test_copy.py
│   │       │   │   │   │   ├── test_count.py
│   │       │   │   │   │   ├── test_cov_corr.py
│   │       │   │   │   │   ├── test_describe.py
│   │       │   │   │   │   ├── test_diff.py
│   │       │   │   │   │   ├── test_drop.py
│   │       │   │   │   │   ├── test_drop_duplicates.py
│   │       │   │   │   │   ├── test_dropna.py
│   │       │   │   │   │   ├── test_dtypes.py
│   │       │   │   │   │   ├── test_duplicated.py
│   │       │   │   │   │   ├── test_equals.py
│   │       │   │   │   │   ├── test_explode.py
│   │       │   │   │   │   ├── test_fillna.py
│   │       │   │   │   │   ├── test_get_numeric_data.py
│   │       │   │   │   │   ├── test_head_tail.py
│   │       │   │   │   │   ├── test_infer_objects.py
│   │       │   │   │   │   ├── test_info.py
│   │       │   │   │   │   ├── test_interpolate.py
│   │       │   │   │   │   ├── test_is_monotonic.py
│   │       │   │   │   │   ├── test_is_unique.py
│   │       │   │   │   │   ├── test_isin.py
│   │       │   │   │   │   ├── test_isna.py
│   │       │   │   │   │   ├── test_item.py
│   │       │   │   │   │   ├── test_map.py
│   │       │   │   │   │   ├── test_matmul.py
│   │       │   │   │   │   ├── test_nlargest.py
│   │       │   │   │   │   ├── test_nunique.py
│   │       │   │   │   │   ├── test_pct_change.py
│   │       │   │   │   │   ├── test_pop.py
│   │       │   │   │   │   ├── test_quantile.py
│   │       │   │   │   │   ├── test_rank.py
│   │       │   │   │   │   ├── test_reindex.py
│   │       │   │   │   │   ├── test_reindex_like.py
│   │       │   │   │   │   ├── test_rename.py
│   │       │   │   │   │   ├── test_rename_axis.py
│   │       │   │   │   │   ├── test_repeat.py
│   │       │   │   │   │   ├── test_replace.py
│   │       │   │   │   │   ├── test_reset_index.py
│   │       │   │   │   │   ├── test_round.py
│   │       │   │   │   │   ├── test_searchsorted.py
│   │       │   │   │   │   ├── test_set_name.py
│   │       │   │   │   │   ├── test_size.py
│   │       │   │   │   │   ├── test_sort_index.py
│   │       │   │   │   │   ├── test_sort_values.py
│   │       │   │   │   │   ├── test_to_csv.py
│   │       │   │   │   │   ├── test_to_dict.py
│   │       │   │   │   │   ├── test_to_frame.py
│   │       │   │   │   │   ├── test_to_numpy.py
│   │       │   │   │   │   ├── test_tolist.py
│   │       │   │   │   │   ├── test_truncate.py
│   │       │   │   │   │   ├── test_tz_localize.py
│   │       │   │   │   │   ├── test_unique.py
│   │       │   │   │   │   ├── test_unstack.py
│   │       │   │   │   │   ├── test_update.py
│   │       │   │   │   │   ├── test_value_counts.py
│   │       │   │   │   │   └── test_values.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_api.py
│   │       │   │   │   ├── test_arithmetic.py
│   │       │   │   │   ├── test_arrow_interface.py
│   │       │   │   │   ├── test_constructors.py
│   │       │   │   │   ├── test_cumulative.py
│   │       │   │   │   ├── test_formats.py
│   │       │   │   │   ├── test_iteration.py
│   │       │   │   │   ├── test_logical_ops.py
│   │       │   │   │   ├── test_missing.py
│   │       │   │   │   ├── test_npfuncs.py
│   │       │   │   │   ├── test_reductions.py
│   │       │   │   │   ├── test_subclass.py
│   │       │   │   │   ├── test_ufunc.py
│   │       │   │   │   ├── test_unary.py
│   │       │   │   │   └── test_validate.py
│   │       │   │   ├── strings/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── conftest.py
│   │       │   │   │   ├── test_api.py
│   │       │   │   │   ├── test_case_justify.py
│   │       │   │   │   ├── test_cat.py
│   │       │   │   │   ├── test_extract.py
│   │       │   │   │   ├── test_find_replace.py
│   │       │   │   │   ├── test_get_dummies.py
│   │       │   │   │   ├── test_split_partition.py
│   │       │   │   │   ├── test_string_array.py
│   │       │   │   │   └── test_strings.py
│   │       │   │   ├── tools/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_to_datetime.py
│   │       │   │   │   ├── test_to_numeric.py
│   │       │   │   │   ├── test_to_time.py
│   │       │   │   │   └── test_to_timedelta.py
│   │       │   │   ├── tseries/
│   │       │   │   │   ├── frequencies/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_freq_code.py
│   │       │   │   │   │   ├── test_frequencies.py
│   │       │   │   │   │   └── test_inference.py
│   │       │   │   │   ├── holiday/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── test_calendar.py
│   │       │   │   │   │   ├── test_federal.py
│   │       │   │   │   │   ├── test_holiday.py
│   │       │   │   │   │   └── test_observance.py
│   │       │   │   │   ├── offsets/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── common.py
│   │       │   │   │   │   ├── test_business_day.py
│   │       │   │   │   │   ├── test_business_halfyear.py
│   │       │   │   │   │   ├── test_business_hour.py
│   │       │   │   │   │   ├── test_business_month.py
│   │       │   │   │   │   ├── test_business_quarter.py
│   │       │   │   │   │   ├── test_business_year.py
│   │       │   │   │   │   ├── test_common.py
│   │       │   │   │   │   ├── test_custom_business_day.py
│   │       │   │   │   │   ├── test_custom_business_hour.py
│   │       │   │   │   │   ├── test_custom_business_month.py
│   │       │   │   │   │   ├── test_dst.py
│   │       │   │   │   │   ├── test_easter.py
│   │       │   │   │   │   ├── test_fiscal.py
│   │       │   │   │   │   ├── test_halfyear.py
│   │       │   │   │   │   ├── test_index.py
│   │       │   │   │   │   ├── test_month.py
│   │       │   │   │   │   ├── test_offsets.py
│   │       │   │   │   │   ├── test_offsets_properties.py
│   │       │   │   │   │   ├── test_quarter.py
│   │       │   │   │   │   ├── test_ticks.py
│   │       │   │   │   │   ├── test_week.py
│   │       │   │   │   │   └── test_year.py
│   │       │   │   │   └── __init__.py
│   │       │   │   ├── tslibs/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── test_api.py
│   │       │   │   │   ├── test_array_to_datetime.py
│   │       │   │   │   ├── test_ccalendar.py
│   │       │   │   │   ├── test_conversion.py
│   │       │   │   │   ├── test_fields.py
│   │       │   │   │   ├── test_libfrequencies.py
│   │       │   │   │   ├── test_liboffsets.py
│   │       │   │   │   ├── test_np_datetime.py
│   │       │   │   │   ├── test_npy_units.py
│   │       │   │   │   ├── test_parse_iso8601.py
│   │       │   │   │   ├── test_parsing.py
│   │       │   │   │   ├── test_period.py
│   │       │   │   │   ├── test_resolution.py
│   │       │   │   │   ├── test_strptime.py
│   │       │   │   │   ├── test_timedeltas.py
│   │       │   │   │   ├── test_timezones.py
│   │       │   │   │   ├── test_to_offset.py
│   │       │   │   │   └── test_tzconversion.py
│   │       │   │   ├── util/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── conftest.py
│   │       │   │   │   ├── test_assert_almost_equal.py
│   │       │   │   │   ├── test_assert_attr_equal.py
│   │       │   │   │   ├── test_assert_categorical_equal.py
│   │       │   │   │   ├── test_assert_extension_array_equal.py
│   │       │   │   │   ├── test_assert_frame_equal.py
│   │       │   │   │   ├── test_assert_index_equal.py
│   │       │   │   │   ├── test_assert_interval_array_equal.py
│   │       │   │   │   ├── test_assert_numpy_array_equal.py
│   │       │   │   │   ├── test_assert_produces_warning.py
│   │       │   │   │   ├── test_assert_series_equal.py
│   │       │   │   │   ├── test_deprecate.py
│   │       │   │   │   ├── test_deprecate_kwarg.py
│   │       │   │   │   ├── test_deprecate_nonkeyword_arguments.py
│   │       │   │   │   ├── test_doc.py
│   │       │   │   │   ├── test_hashing.py
│   │       │   │   │   ├── test_numba.py
│   │       │   │   │   ├── test_rewrite_warning.py
│   │       │   │   │   ├── test_shares_memory.py
│   │       │   │   │   ├── test_show_versions.py
│   │       │   │   │   ├── test_util.py
│   │       │   │   │   ├── test_validate_args.py
│   │       │   │   │   ├── test_validate_args_and_kwargs.py
│   │       │   │   │   ├── test_validate_inclusive.py
│   │       │   │   │   └── test_validate_kwargs.py
│   │       │   │   ├── window/
│   │       │   │   │   ├── moments/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── conftest.py
│   │       │   │   │   │   ├── test_moments_consistency_ewm.py
│   │       │   │   │   │   ├── test_moments_consistency_expanding.py
│   │       │   │   │   │   └── test_moments_consistency_rolling.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── conftest.py
│   │       │   │   │   ├── test_api.py
│   │       │   │   │   ├── test_apply.py
│   │       │   │   │   ├── test_base_indexer.py
│   │       │   │   │   ├── test_cython_aggregations.py
│   │       │   │   │   ├── test_dtypes.py
│   │       │   │   │   ├── test_ewm.py
│   │       │   │   │   ├── test_expanding.py
│   │       │   │   │   ├── test_groupby.py
│   │       │   │   │   ├── test_numba.py
│   │       │   │   │   ├── test_online.py
│   │       │   │   │   ├── test_pairwise.py
│   │       │   │   │   ├── test_rolling.py
│   │       │   │   │   ├── test_rolling_functions.py
│   │       │   │   │   ├── test_rolling_quantile.py
│   │       │   │   │   ├── test_rolling_skew_kurt.py
│   │       │   │   │   ├── test_timeseries_window.py
│   │       │   │   │   └── test_win_type.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── test_aggregation.py
│   │       │   │   ├── test_algos.py
│   │       │   │   ├── test_col.py
│   │       │   │   ├── test_common.py
│   │       │   │   ├── test_downstream.py
│   │       │   │   ├── test_errors.py
│   │       │   │   ├── test_expressions.py
│   │       │   │   ├── test_flags.py
│   │       │   │   ├── test_multilevel.py
│   │       │   │   ├── test_nanops.py
│   │       │   │   ├── test_optional_dependency.py
│   │       │   │   ├── test_register_accessor.py
│   │       │   │   ├── test_sorting.py
│   │       │   │   └── test_take.py
│   │       │   ├── tseries/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── api.py
│   │       │   │   ├── frequencies.py
│   │       │   │   ├── holiday.py
│   │       │   │   └── offsets.py
│   │       │   ├── util/
│   │       │   │   ├── version/
│   │       │   │   │   └── __init__.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _decorators.py
│   │       │   │   ├── _doctools.py
│   │       │   │   ├── _exceptions.py
│   │       │   │   ├── _print_versions.py
│   │       │   │   ├── _test_decorators.py
│   │       │   │   ├── _tester.py
│   │       │   │   └── _validators.py
│   │       │   ├── __init__.py
│   │       │   ├── _typing.py
│   │       │   ├── _version.py
│   │       │   ├── _version_meson.py
│   │       │   ├── conftest.py
│   │       │   └── testing.py
│   │       ├── pandas-3.0.3.dist-info/
│   │       │   ├── entry_points.txt
│   │       ├── pandas.libs/
│   │       ├── passlib/
│   │       │   ├── _data/
│   │       │   │   └── wordsets/
│   │       │   │       ├── bip39.txt
│   │       │   │       ├── eff_long.txt
│   │       │   │       ├── eff_prefixed.txt
│   │       │   │       └── eff_short.txt
│   │       │   ├── crypto/
│   │       │   │   ├── _blowfish/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _gen_files.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   └── unrolled.py
│   │       │   │   ├── scrypt/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _builtin.py
│   │       │   │   │   ├── _gen_files.py
│   │       │   │   │   └── _salsa.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _md4.py
│   │       │   │   ├── des.py
│   │       │   │   └── digest.py
│   │       │   ├── ext/
│   │       │   │   ├── django/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── models.py
│   │       │   │   │   └── utils.py
│   │       │   │   └── __init__.py
│   │       │   ├── handlers/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── argon2.py
│   │       │   │   ├── bcrypt.py
│   │       │   │   ├── cisco.py
│   │       │   │   ├── des_crypt.py
│   │       │   │   ├── digests.py
│   │       │   │   ├── django.py
│   │       │   │   ├── fshp.py
│   │       │   │   ├── ldap_digests.py
│   │       │   │   ├── md5_crypt.py
│   │       │   │   ├── misc.py
│   │       │   │   ├── mssql.py
│   │       │   │   ├── mysql.py
│   │       │   │   ├── oracle.py
│   │       │   │   ├── pbkdf2.py
│   │       │   │   ├── phpass.py
│   │       │   │   ├── postgres.py
│   │       │   │   ├── roundup.py
│   │       │   │   ├── scram.py
│   │       │   │   ├── scrypt.py
│   │       │   │   ├── sha1_crypt.py
│   │       │   │   ├── sha2_crypt.py
│   │       │   │   ├── sun_md5_crypt.py
│   │       │   │   └── windows.py
│   │       │   ├── tests/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── __main__.py
│   │       │   │   ├── _test_bad_register.py
│   │       │   │   ├── backports.py
│   │       │   │   ├── test_apache.py
│   │       │   │   ├── test_apps.py
│   │       │   │   ├── test_context.py
│   │       │   │   ├── test_context_deprecated.py
│   │       │   │   ├── test_crypto_builtin_md4.py
│   │       │   │   ├── test_crypto_des.py
│   │       │   │   ├── test_crypto_digest.py
│   │       │   │   ├── test_crypto_scrypt.py
│   │       │   │   ├── test_ext_django.py
│   │       │   │   ├── test_ext_django_source.py
│   │       │   │   ├── test_handlers.py
│   │       │   │   ├── test_handlers_argon2.py
│   │       │   │   ├── test_handlers_bcrypt.py
│   │       │   │   ├── test_handlers_cisco.py
│   │       │   │   ├── test_handlers_django.py
│   │       │   │   ├── test_handlers_pbkdf2.py
│   │       │   │   ├── test_handlers_scrypt.py
│   │       │   │   ├── test_hosts.py
│   │       │   │   ├── test_pwd.py
│   │       │   │   ├── test_registry.py
│   │       │   │   ├── test_totp.py
│   │       │   │   ├── test_utils.py
│   │       │   │   ├── test_utils_handlers.py
│   │       │   │   ├── test_utils_md4.py
│   │       │   │   ├── test_utils_pbkdf2.py
│   │       │   │   ├── test_win32.py
│   │       │   │   ├── tox_support.py
│   │       │   │   └── utils.py
│   │       │   ├── utils/
│   │       │   │   ├── compat/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── _ordered_dict.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── binary.py
│   │       │   │   ├── decor.py
│   │       │   │   ├── des.py
│   │       │   │   ├── handlers.py
│   │       │   │   ├── md4.py
│   │       │   │   └── pbkdf2.py
│   │       │   ├── __init__.py
│   │       │   ├── apache.py
│   │       │   ├── apps.py
│   │       │   ├── context.py
│   │       │   ├── exc.py
│   │       │   ├── hash.py
│   │       │   ├── hosts.py
│   │       │   ├── ifc.py
│   │       │   ├── pwd.py
│   │       │   ├── registry.py
│   │       │   ├── totp.py
│   │       │   └── win32.py
│   │       ├── passlib-1.7.4.dist-info/
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
│   │       │   │   ├── dependency_groups/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __main__.py
│   │       │   │   │   ├── _implementation.py
│   │       │   │   │   ├── _lint_dependency_groups.py
│   │       │   │   │   ├── _pip_wrapper.py
│   │       │   │   │   ├── _toml_compat.py
│   │       │   │   │   ├── LICENSE.txt
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
│   │       │   │   │   │   ├── _securetransport/
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   ├── bindings.py
│   │       │   │   │   │   │   └── low_level.py
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── _appengine_environ.py
│   │       │   │   │   │   ├── appengine.py
│   │       │   │   │   │   ├── ntlmpool.py
│   │       │   │   │   │   ├── pyopenssl.py
│   │       │   │   │   │   ├── securetransport.py
│   │       │   │   │   │   └── socks.py
│   │       │   │   │   ├── packages/
│   │       │   │   │   │   ├── backports/
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   ├── makefile.py
│   │       │   │   │   │   │   └── weakref_finalize.py
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── six.py
│   │       │   │   │   ├── util/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── connection.py
│   │       │   │   │   │   ├── proxy.py
│   │       │   │   │   │   ├── queue.py
│   │       │   │   │   │   ├── request.py
│   │       │   │   │   │   ├── response.py
│   │       │   │   │   │   ├── retry.py
│   │       │   │   │   │   ├── ssl_.py
│   │       │   │   │   │   ├── ssl_match_hostname.py
│   │       │   │   │   │   ├── ssltransport.py
│   │       │   │   │   │   ├── timeout.py
│   │       │   │   │   │   ├── url.py
│   │       │   │   │   │   └── wait.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _collections.py
│   │       │   │   │   ├── _version.py
│   │       │   │   │   ├── connection.py
│   │       │   │   │   ├── connectionpool.py
│   │       │   │   │   ├── exceptions.py
│   │       │   │   │   ├── fields.py
│   │       │   │   │   ├── filepost.py
│   │       │   │   │   ├── LICENSE.txt
│   │       │   │   │   ├── poolmanager.py
│   │       │   │   │   ├── request.py
│   │       │   │   │   └── response.py
│   │       │   │   ├── __init__.py
│   │       │   │   └── vendor.txt
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── __pip-runner__.py
│   │       ├── pip-26.0.1.dist-info/
│   │       │   ├── licenses/
│   │       │   │   ├── src/
│   │       │   │   │   └── pip/
│   │       │   │   │       └── _vendor/
│   │       │   │   │           ├── cachecontrol/
│   │       │   │   │           │   └── LICENSE.txt
│   │       │   │   │           ├── certifi/
│   │       │   │   │           ├── dependency_groups/
│   │       │   │   │           │   └── LICENSE.txt
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
│   │       ├── psutil/
│   │       │   ├── __init__.py
│   │       │   ├── _common.py
│   │       │   ├── _ntuples.py
│   │       │   ├── _psaix.py
│   │       │   ├── _psbsd.py
│   │       │   ├── _pslinux.py
│   │       │   ├── _psosx.py
│   │       │   ├── _psposix.py
│   │       │   ├── _pssunos.py
│   │       │   └── _pswindows.py
│   │       ├── psutil-7.2.2.dist-info/
│   │       │   ├── top_level.txt
│   │       ├── pyasn1/
│   │       │   ├── codec/
│   │       │   │   ├── ber/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── decoder.py
│   │       │   │   │   ├── encoder.py
│   │       │   │   │   └── eoo.py
│   │       │   │   ├── cer/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── decoder.py
│   │       │   │   │   └── encoder.py
│   │       │   │   ├── der/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── decoder.py
│   │       │   │   │   └── encoder.py
│   │       │   │   ├── native/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── decoder.py
│   │       │   │   │   └── encoder.py
│   │       │   │   ├── __init__.py
│   │       │   │   └── streaming.py
│   │       │   ├── compat/
│   │       │   │   ├── __init__.py
│   │       │   │   └── integer.py
│   │       │   ├── type/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── base.py
│   │       │   │   ├── char.py
│   │       │   │   ├── constraint.py
│   │       │   │   ├── error.py
│   │       │   │   ├── namedtype.py
│   │       │   │   ├── namedval.py
│   │       │   │   ├── opentype.py
│   │       │   │   ├── tag.py
│   │       │   │   ├── tagmap.py
│   │       │   │   ├── univ.py
│   │       │   │   └── useful.py
│   │       │   ├── __init__.py
│   │       │   ├── debug.py
│   │       │   └── error.py
│   │       ├── pyasn1-0.6.3.dist-info/
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
│   │       ├── pydantic_settings/
│   │       │   ├── sources/
│   │       │   │   ├── providers/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── aws.py
│   │       │   │   │   ├── azure.py
│   │       │   │   │   ├── cli.py
│   │       │   │   │   ├── dotenv.py
│   │       │   │   │   ├── env.py
│   │       │   │   │   ├── gcp.py
│   │       │   │   │   ├── json.py
│   │       │   │   │   ├── nested_secrets.py
│   │       │   │   │   ├── pyproject.py
│   │       │   │   │   ├── secrets.py
│   │       │   │   │   ├── toml.py
│   │       │   │   │   └── yaml.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── base.py
│   │       │   │   ├── types.py
│   │       │   │   └── utils.py
│   │       │   ├── __init__.py
│   │       │   ├── exceptions.py
│   │       │   ├── main.py
│   │       │   ├── utils.py
│   │       │   └── version.py
│   │       ├── pydantic_settings-2.14.1.dist-info/
│   │       │   ├── licenses/
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
│   │       ├── pyjwt-2.12.1.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
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
│   │       ├── python_dateutil-2.9.0.post0.dist-info/
│   │       │   ├── top_level.txt
│   │       ├── python_docx-1.2.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── python_dotenv-1.2.2.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       │   ├── top_level.txt
│   │       ├── python_engineio-4.13.2.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── python_jose-3.5.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── python_multipart/
│   │       │   ├── __init__.py
│   │       │   ├── decoders.py
│   │       │   ├── exceptions.py
│   │       │   ├── multipart.py
│   │       ├── python_multipart-0.0.29.dist-info/
│   │       │   ├── licenses/
│   │       │   │   └── LICENSE.txt
│   │       ├── python_socketio-5.16.2.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── pythonwin/
│   │       │   ├── pywin/
│   │       │   │   ├── debugger/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── configui.py
│   │       │   │   │   ├── dbgcon.py
│   │       │   │   │   ├── dbgpyapp.py
│   │       │   │   │   ├── debugger.py
│   │       │   │   │   └── fail.py
│   │       │   │   ├── Demos/
│   │       │   │   │   ├── app/
│   │       │   │   │   │   ├── basictimerapp.py
│   │       │   │   │   │   ├── customprint.py
│   │       │   │   │   │   ├── demoutils.py
│   │       │   │   │   │   ├── dlgappdemo.py
│   │       │   │   │   │   ├── dojobapp.py
│   │       │   │   │   │   └── helloapp.py
│   │       │   │   │   ├── ocx/
│   │       │   │   │   │   ├── demoutils.py
│   │       │   │   │   │   ├── flash.py
│   │       │   │   │   │   ├── msoffice.py
│   │       │   │   │   │   ├── ocxserialtest.py
│   │       │   │   │   │   ├── ocxtest.py
│   │       │   │   │   │   └── webbrowser.py
│   │       │   │   │   ├── cmdserver.py
│   │       │   │   │   ├── createwin.py
│   │       │   │   │   ├── demoutils.py
│   │       │   │   │   ├── dibdemo.py
│   │       │   │   │   ├── dlgtest.py
│   │       │   │   │   ├── dyndlg.py
│   │       │   │   │   ├── fontdemo.py
│   │       │   │   │   ├── guidemo.py
│   │       │   │   │   ├── hiertest.py
│   │       │   │   │   ├── menutest.py
│   │       │   │   │   ├── objdoc.py
│   │       │   │   │   ├── openGLDemo.py
│   │       │   │   │   ├── progressbar.py
│   │       │   │   │   ├── sliderdemo.py
│   │       │   │   │   ├── splittst.py
│   │       │   │   │   ├── threadedgui.py
│   │       │   │   │   └── toolbar.py
│   │       │   │   ├── dialogs/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── ideoptions.py
│   │       │   │   │   ├── list.py
│   │       │   │   │   ├── login.py
│   │       │   │   │   └── status.py
│   │       │   │   ├── docking/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── DockingBar.py
│   │       │   │   ├── framework/
│   │       │   │   │   ├── editor/
│   │       │   │   │   │   ├── color/
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   └── coloreditor.py
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── configui.py
│   │       │   │   │   │   ├── document.py
│   │       │   │   │   │   ├── editor.py
│   │       │   │   │   │   ├── frame.py
│   │       │   │   │   │   ├── ModuleBrowser.py
│   │       │   │   │   │   ├── template.py
│   │       │   │   │   │   └── vss.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── app.py
│   │       │   │   │   ├── bitmap.py
│   │       │   │   │   ├── cmdline.py
│   │       │   │   │   ├── dbgcommands.py
│   │       │   │   │   ├── dlgappcore.py
│   │       │   │   │   ├── help.py
│   │       │   │   │   ├── interact.py
│   │       │   │   │   ├── intpyapp.py
│   │       │   │   │   ├── intpydde.py
│   │       │   │   │   ├── scriptutils.py
│   │       │   │   │   ├── sgrepmdi.py
│   │       │   │   │   ├── startup.py
│   │       │   │   │   ├── stdin.py
│   │       │   │   │   ├── toolmenu.py
│   │       │   │   │   ├── window.py
│   │       │   │   │   └── winout.py
│   │       │   │   ├── idle/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── AutoExpand.py
│   │       │   │   │   ├── AutoIndent.py
│   │       │   │   │   ├── CallTips.py
│   │       │   │   │   ├── FormatParagraph.py
│   │       │   │   │   ├── IdleHistory.py
│   │       │   │   │   └── PyParse.py
│   │       │   │   ├── mfc/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── activex.py
│   │       │   │   │   ├── afxres.py
│   │       │   │   │   ├── dialog.py
│   │       │   │   │   ├── docview.py
│   │       │   │   │   ├── object.py
│   │       │   │   │   ├── thread.py
│   │       │   │   │   └── window.py
│   │       │   │   ├── scintilla/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── bindings.py
│   │       │   │   │   ├── config.py
│   │       │   │   │   ├── configui.py
│   │       │   │   │   ├── control.py
│   │       │   │   │   ├── document.py
│   │       │   │   │   ├── find.py
│   │       │   │   │   ├── formatter.py
│   │       │   │   │   ├── IDLEenvironment.py
│   │       │   │   │   ├── keycodes.py
│   │       │   │   │   ├── scintillacon.py
│   │       │   │   │   └── view.py
│   │       │   │   ├── tools/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── browseProjects.py
│   │       │   │   │   ├── browser.py
│   │       │   │   │   ├── hierlist.py
│   │       │   │   │   ├── regedit.py
│   │       │   │   │   ├── regpy.py
│   │       │   │   │   └── TraceCollector.py
│   │       │   │   ├── __init__.py
│   │       │   ├── license.txt
│   │       ├── pytz/
│   │       │   ├── zoneinfo/
│   │       │   │   ├── Africa/
│   │       │   │   ├── America/
│   │       │   │   │   ├── Argentina/
│   │       │   │   │   ├── Indiana/
│   │       │   │   │   ├── Kentucky/
│   │       │   │   │   ├── North_Dakota/
│   │       │   │   ├── Antarctica/
│   │       │   │   ├── Arctic/
│   │       │   │   ├── Asia/
│   │       │   │   ├── Atlantic/
│   │       │   │   ├── Australia/
│   │       │   │   ├── Brazil/
│   │       │   │   ├── Canada/
│   │       │   │   ├── Chile/
│   │       │   │   ├── Etc/
│   │       │   │   ├── Europe/
│   │       │   │   ├── Indian/
│   │       │   │   ├── Mexico/
│   │       │   │   ├── Pacific/
│   │       │   │   ├── US/
│   │       │   ├── __init__.py
│   │       │   ├── exceptions.py
│   │       │   ├── lazy.py
│   │       │   ├── reference.py
│   │       │   ├── tzfile.py
│   │       │   └── tzinfo.py
│   │       ├── pytz-2026.2.dist-info/
│   │       │   ├── LICENSE.txt
│   │       │   ├── top_level.txt
│   │       ├── pywin32-311.dist-info/
│   │       │   ├── entry_points.txt
│   │       │   ├── top_level.txt
│   │       ├── pywin32_system32/
│   │       ├── pyyaml-6.0.3.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── top_level.txt
│   │       ├── redis/
│   │       │   ├── _parsers/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── base.py
│   │       │   │   ├── commands.py
│   │       │   │   ├── encoders.py
│   │       │   │   ├── helpers.py
│   │       │   │   ├── hiredis.py
│   │       │   │   ├── resp2.py
│   │       │   │   ├── resp3.py
│   │       │   │   └── socket.py
│   │       │   ├── asyncio/
│   │       │   │   ├── http/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── http_client.py
│   │       │   │   ├── multidb/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── client.py
│   │       │   │   │   ├── command_executor.py
│   │       │   │   │   ├── config.py
│   │       │   │   │   ├── database.py
│   │       │   │   │   ├── event.py
│   │       │   │   │   ├── failover.py
│   │       │   │   │   ├── failure_detector.py
│   │       │   │   │   └── healthcheck.py
│   │       │   │   ├── observability/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── recorder.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── client.py
│   │       │   │   ├── cluster.py
│   │       │   │   ├── connection.py
│   │       │   │   ├── lock.py
│   │       │   │   ├── retry.py
│   │       │   │   ├── sentinel.py
│   │       │   │   └── utils.py
│   │       │   ├── auth/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── err.py
│   │       │   │   ├── idp.py
│   │       │   │   ├── token.py
│   │       │   │   └── token_manager.py
│   │       │   ├── commands/
│   │       │   │   ├── bf/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── commands.py
│   │       │   │   │   └── info.py
│   │       │   │   ├── json/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _util.py
│   │       │   │   │   ├── commands.py
│   │       │   │   │   ├── decoders.py
│   │       │   │   │   └── path.py
│   │       │   │   ├── search/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _util.py
│   │       │   │   │   ├── aggregation.py
│   │       │   │   │   ├── commands.py
│   │       │   │   │   ├── dialect.py
│   │       │   │   │   ├── document.py
│   │       │   │   │   ├── field.py
│   │       │   │   │   ├── hybrid_query.py
│   │       │   │   │   ├── hybrid_result.py
│   │       │   │   │   ├── index_definition.py
│   │       │   │   │   ├── profile_information.py
│   │       │   │   │   ├── query.py
│   │       │   │   │   ├── querystring.py
│   │       │   │   │   ├── reducers.py
│   │       │   │   │   ├── result.py
│   │       │   │   │   └── suggestion.py
│   │       │   │   ├── timeseries/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── commands.py
│   │       │   │   │   ├── info.py
│   │       │   │   │   └── utils.py
│   │       │   │   ├── vectorset/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── commands.py
│   │       │   │   │   └── utils.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── cluster.py
│   │       │   │   ├── core.py
│   │       │   │   ├── helpers.py
│   │       │   │   ├── policies.py
│   │       │   │   ├── redismodules.py
│   │       │   │   └── sentinel.py
│   │       │   ├── http/
│   │       │   │   ├── __init__.py
│   │       │   │   └── http_client.py
│   │       │   ├── multidb/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── circuit.py
│   │       │   │   ├── client.py
│   │       │   │   ├── command_executor.py
│   │       │   │   ├── config.py
│   │       │   │   ├── database.py
│   │       │   │   ├── event.py
│   │       │   │   ├── exception.py
│   │       │   │   ├── failover.py
│   │       │   │   └── failure_detector.py
│   │       │   ├── observability/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── attributes.py
│   │       │   │   ├── config.py
│   │       │   │   ├── metrics.py
│   │       │   │   ├── providers.py
│   │       │   │   ├── recorder.py
│   │       │   │   └── registry.py
│   │       │   ├── __init__.py
│   │       │   ├── background.py
│   │       │   ├── backoff.py
│   │       │   ├── cache.py
│   │       │   ├── client.py
│   │       │   ├── cluster.py
│   │       │   ├── connection.py
│   │       │   ├── crc.py
│   │       │   ├── credentials.py
│   │       │   ├── data_structure.py
│   │       │   ├── driver_info.py
│   │       │   ├── event.py
│   │       │   ├── exceptions.py
│   │       │   ├── lock.py
│   │       │   ├── maint_notifications.py
│   │       │   ├── ocsp.py
│   │       │   ├── retry.py
│   │       │   ├── sentinel.py
│   │       │   ├── typing.py
│   │       │   └── utils.py
│   │       ├── redis-7.4.0.dist-info/
│   │       │   ├── licenses/
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
│   │       ├── rsa/
│   │       │   ├── __init__.py
│   │       │   ├── asn1.py
│   │       │   ├── cli.py
│   │       │   ├── common.py
│   │       │   ├── core.py
│   │       │   ├── key.py
│   │       │   ├── parallel.py
│   │       │   ├── pem.py
│   │       │   ├── pkcs1.py
│   │       │   ├── pkcs1_v2.py
│   │       │   ├── prime.py
│   │       │   ├── randnum.py
│   │       │   ├── transform.py
│   │       │   └── util.py
│   │       ├── rsa-4.9.1.dist-info/
│   │       │   ├── entry_points.txt
│   │       ├── sasl2/
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
│   │       ├── simple_websocket/
│   │       │   ├── __init__.py
│   │       │   ├── aiows.py
│   │       │   ├── asgi.py
│   │       │   ├── errors.py
│   │       │   └── ws.py
│   │       ├── simple_websocket-1.1.0.dist-info/
│   │       │   ├── top_level.txt
│   │       ├── six-1.17.0.dist-info/
│   │       │   ├── top_level.txt
│   │       ├── sniffio/
│   │       │   ├── _tests/
│   │       │   │   ├── __init__.py
│   │       │   │   └── test_sniffio.py
│   │       │   ├── __init__.py
│   │       │   ├── _impl.py
│   │       │   ├── _version.py
│   │       ├── sniffio-1.3.1.dist-info/
│   │       │   ├── top_level.txt
│   │       ├── socketio/
│   │       │   ├── __init__.py
│   │       │   ├── admin.py
│   │       │   ├── asgi.py
│   │       │   ├── async_admin.py
│   │       │   ├── async_aiopika_manager.py
│   │       │   ├── async_client.py
│   │       │   ├── async_manager.py
│   │       │   ├── async_namespace.py
│   │       │   ├── async_pubsub_manager.py
│   │       │   ├── async_redis_manager.py
│   │       │   ├── async_server.py
│   │       │   ├── async_simple_client.py
│   │       │   ├── base_client.py
│   │       │   ├── base_manager.py
│   │       │   ├── base_namespace.py
│   │       │   ├── base_server.py
│   │       │   ├── client.py
│   │       │   ├── exceptions.py
│   │       │   ├── kafka_manager.py
│   │       │   ├── kombu_manager.py
│   │       │   ├── manager.py
│   │       │   ├── middleware.py
│   │       │   ├── msgpack_packet.py
│   │       │   ├── namespace.py
│   │       │   ├── packet.py
│   │       │   ├── pubsub_manager.py
│   │       │   ├── redis_manager.py
│   │       │   ├── server.py
│   │       │   ├── simple_client.py
│   │       │   ├── tornado.py
│   │       │   └── zmq_manager.py
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
│   │       ├── tqdm/
│   │       │   ├── contrib/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── bells.py
│   │       │   │   ├── concurrent.py
│   │       │   │   ├── discord.py
│   │       │   │   ├── itertools.py
│   │       │   │   ├── logging.py
│   │       │   │   ├── slack.py
│   │       │   │   ├── telegram.py
│   │       │   │   └── utils_worker.py
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── _main.py
│   │       │   ├── _monitor.py
│   │       │   ├── _tqdm.py
│   │       │   ├── _tqdm_gui.py
│   │       │   ├── _tqdm_notebook.py
│   │       │   ├── _tqdm_pandas.py
│   │       │   ├── _utils.py
│   │       │   ├── asyncio.py
│   │       │   ├── auto.py
│   │       │   ├── autonotebook.py
│   │       │   ├── cli.py
│   │       │   ├── dask.py
│   │       │   ├── gui.py
│   │       │   ├── keras.py
│   │       │   ├── notebook.py
│   │       │   ├── rich.py
│   │       │   ├── std.py
│   │       │   ├── tk.py
│   │       │   ├── utils.py
│   │       │   └── version.py
│   │       ├── tqdm-4.67.3.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       │   ├── top_level.txt
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
│   │       ├── tzdata/
│   │       │   ├── zoneinfo/
│   │       │   │   ├── Africa/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── America/
│   │       │   │   │   ├── Argentina/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   ├── Indiana/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   ├── Kentucky/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   ├── North_Dakota/
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── Antarctica/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── Arctic/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── Asia/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── Atlantic/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── Australia/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── Brazil/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── Canada/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── Chile/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── Etc/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── Europe/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── Indian/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── Mexico/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── Pacific/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── US/
│   │       │   │   │   ├── __init__.py
│   │       │   │   ├── __init__.py
│   │       │   ├── __init__.py
│   │       ├── tzdata-2026.2.dist-info/
│   │       │   ├── licenses/
│   │       │   │   ├── licenses/
│   │       │   ├── top_level.txt
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
│   │       ├── waitress/
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── adjustments.py
│   │       │   ├── buffers.py
│   │       │   ├── channel.py
│   │       │   ├── compat.py
│   │       │   ├── parser.py
│   │       │   ├── proxy_headers.py
│   │       │   ├── receiver.py
│   │       │   ├── rfc7230.py
│   │       │   ├── runner.py
│   │       │   ├── server.py
│   │       │   ├── task.py
│   │       │   ├── trigger.py
│   │       │   ├── utilities.py
│   │       │   └── wasyncore.py
│   │       ├── waitress-3.0.2.dist-info/
│   │       │   ├── entry_points.txt
│   │       │   ├── LICENSE.txt
│   │       │   ├── top_level.txt
│   │       ├── watchfiles/
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── cli.py
│   │       │   ├── filters.py
│   │       │   ├── main.py
│   │       │   ├── run.py
│   │       │   └── version.py
│   │       ├── watchfiles-1.2.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── sboms/
│   │       │   │   └── watchfiles_rust_notify.cyclonedx.json
│   │       │   ├── entry_points.txt
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
│   │       ├── websockets/
│   │       │   ├── asyncio/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── async_timeout.py
│   │       │   │   ├── client.py
│   │       │   │   ├── compatibility.py
│   │       │   │   ├── connection.py
│   │       │   │   ├── messages.py
│   │       │   │   ├── router.py
│   │       │   │   └── server.py
│   │       │   ├── extensions/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── base.py
│   │       │   │   └── permessage_deflate.py
│   │       │   ├── legacy/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── auth.py
│   │       │   │   ├── client.py
│   │       │   │   ├── exceptions.py
│   │       │   │   ├── framing.py
│   │       │   │   ├── handshake.py
│   │       │   │   ├── http.py
│   │       │   │   ├── protocol.py
│   │       │   │   └── server.py
│   │       │   ├── sync/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── client.py
│   │       │   │   ├── connection.py
│   │       │   │   ├── messages.py
│   │       │   │   ├── router.py
│   │       │   │   ├── server.py
│   │       │   │   └── utils.py
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── auth.py
│   │       │   ├── cli.py
│   │       │   ├── client.py
│   │       │   ├── connection.py
│   │       │   ├── datastructures.py
│   │       │   ├── exceptions.py
│   │       │   ├── frames.py
│   │       │   ├── headers.py
│   │       │   ├── http.py
│   │       │   ├── http11.py
│   │       │   ├── imports.py
│   │       │   ├── protocol.py
│   │       │   ├── proxy.py
│   │       │   ├── server.py
│   │       │   ├── streams.py
│   │       │   ├── typing.py
│   │       │   ├── uri.py
│   │       │   ├── utils.py
│   │       │   └── version.py
│   │       ├── websockets-16.0.dist-info/
│   │       │   ├── licenses/
│   │       │   ├── entry_points.txt
│   │       │   ├── top_level.txt
│   │       ├── werkzeug/
│   │       │   ├── datastructures/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── accept.py
│   │       │   │   ├── auth.py
│   │       │   │   ├── cache_control.py
│   │       │   │   ├── csp.py
│   │       │   │   ├── etag.py
│   │       │   │   ├── file_storage.py
│   │       │   │   ├── headers.py
│   │       │   │   ├── mixins.py
│   │       │   │   ├── range.py
│   │       │   │   └── structures.py
│   │       │   ├── debug/
│   │       │   │   ├── shared/
│   │       │   │   │   ├── debugger.js
│   │       │   │   │   ├── ICON_LICENSE.md
│   │       │   │   │   └── style.css
│   │       │   │   ├── __init__.py
│   │       │   │   ├── console.py
│   │       │   │   ├── repr.py
│   │       │   │   └── tbtools.py
│   │       │   ├── middleware/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── dispatcher.py
│   │       │   │   ├── http_proxy.py
│   │       │   │   ├── lint.py
│   │       │   │   ├── profiler.py
│   │       │   │   ├── proxy_fix.py
│   │       │   │   └── shared_data.py
│   │       │   ├── routing/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── converters.py
│   │       │   │   ├── exceptions.py
│   │       │   │   ├── map.py
│   │       │   │   ├── matcher.py
│   │       │   │   └── rules.py
│   │       │   ├── sansio/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── http.py
│   │       │   │   ├── multipart.py
│   │       │   │   ├── request.py
│   │       │   │   ├── response.py
│   │       │   │   └── utils.py
│   │       │   ├── wrappers/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── request.py
│   │       │   │   └── response.py
│   │       │   ├── __init__.py
│   │       │   ├── _internal.py
│   │       │   ├── _reloader.py
│   │       │   ├── exceptions.py
│   │       │   ├── formparser.py
│   │       │   ├── http.py
│   │       │   ├── local.py
│   │       │   ├── security.py
│   │       │   ├── serving.py
│   │       │   ├── test.py
│   │       │   ├── testapp.py
│   │       │   ├── urls.py
│   │       │   ├── user_agent.py
│   │       │   ├── utils.py
│   │       │   └── wsgi.py
│   │       ├── werkzeug-3.1.8.dist-info/
│   │       │   ├── licenses/
│   │       │   │   └── LICENSE.txt
│   │       ├── win32/
│   │       │   ├── Demos/
│   │       │   │   ├── c_extension/
│   │       │   │   │   └── setup.py
│   │       │   │   ├── dde/
│   │       │   │   │   ├── ddeclient.py
│   │       │   │   │   └── ddeserver.py
│   │       │   │   ├── images/
│   │       │   │   ├── pipes/
│   │       │   │   │   ├── cat.py
│   │       │   │   │   └── runproc.py
│   │       │   │   ├── security/
│   │       │   │   │   ├── sspi/
│   │       │   │   │   │   ├── fetch_url.py
│   │       │   │   │   │   ├── simple_auth.py
│   │       │   │   │   │   ├── socket_server.py
│   │       │   │   │   │   └── validate_password.py
│   │       │   │   │   ├── account_rights.py
│   │       │   │   │   ├── explicit_entries.py
│   │       │   │   │   ├── get_policy_info.py
│   │       │   │   │   ├── GetTokenInformation.py
│   │       │   │   │   ├── list_rights.py
│   │       │   │   │   ├── localized_names.py
│   │       │   │   │   ├── lsaregevent.py
│   │       │   │   │   ├── lsastore.py
│   │       │   │   │   ├── query_information.py
│   │       │   │   │   ├── regsave_sa.py
│   │       │   │   │   ├── regsecurity.py
│   │       │   │   │   ├── sa_inherit.py
│   │       │   │   │   ├── security_enums.py
│   │       │   │   │   ├── set_file_audit.py
│   │       │   │   │   ├── set_file_owner.py
│   │       │   │   │   ├── set_policy_info.py
│   │       │   │   │   ├── setkernelobjectsecurity.py
│   │       │   │   │   ├── setnamedsecurityinfo.py
│   │       │   │   │   ├── setsecurityinfo.py
│   │       │   │   │   └── setuserobjectsecurity.py
│   │       │   │   ├── service/
│   │       │   │   │   ├── nativePipeTestService.py
│   │       │   │   │   ├── pipeTestService.py
│   │       │   │   │   ├── pipeTestServiceClient.py
│   │       │   │   │   └── serviceEvents.py
│   │       │   │   ├── win32wnet/
│   │       │   │   │   ├── testwnet.py
│   │       │   │   │   └── winnetwk.py
│   │       │   │   ├── BackupRead_BackupWrite.py
│   │       │   │   ├── BackupSeek_streamheaders.py
│   │       │   │   ├── CopyFileEx.py
│   │       │   │   ├── CreateFileTransacted_MiniVersion.py
│   │       │   │   ├── desktopmanager.py
│   │       │   │   ├── eventLogDemo.py
│   │       │   │   ├── EvtFormatMessage.py
│   │       │   │   ├── EvtSubscribe_pull.py
│   │       │   │   ├── EvtSubscribe_push.py
│   │       │   │   ├── FileSecurityTest.py
│   │       │   │   ├── getfilever.py
│   │       │   │   ├── GetSaveFileName.py
│   │       │   │   ├── mmapfile_demo.py
│   │       │   │   ├── NetValidatePasswordPolicy.py
│   │       │   │   ├── OpenEncryptedFileRaw.py
│   │       │   │   ├── print_desktop.py
│   │       │   │   ├── rastest.py
│   │       │   │   ├── RegCreateKeyTransacted.py
│   │       │   │   ├── RegRestoreKey.py
│   │       │   │   ├── SystemParametersInfo.py
│   │       │   │   ├── timer_demo.py
│   │       │   │   ├── win32clipboard_bitmapdemo.py
│   │       │   │   ├── win32clipboardDemo.py
│   │       │   │   ├── win32comport_demo.py
│   │       │   │   ├── win32console_demo.py
│   │       │   │   ├── win32cred_demo.py
│   │       │   │   ├── win32fileDemo.py
│   │       │   │   ├── win32gui_demo.py
│   │       │   │   ├── win32gui_devicenotify.py
│   │       │   │   ├── win32gui_dialog.py
│   │       │   │   ├── win32gui_menu.py
│   │       │   │   ├── win32gui_taskbar.py
│   │       │   │   ├── win32netdemo.py
│   │       │   │   ├── win32rcparser_demo.py
│   │       │   │   ├── win32servicedemo.py
│   │       │   │   ├── win32ts_logoff_disconnected.py
│   │       │   │   └── winprocess.py
│   │       │   ├── include/
│   │       │   ├── lib/
│   │       │   │   ├── _win32verstamp_pywin32ctypes.py
│   │       │   │   ├── afxres.py
│   │       │   │   ├── commctrl.py
│   │       │   │   ├── mmsystem.py
│   │       │   │   ├── netbios.py
│   │       │   │   ├── ntsecuritycon.py
│   │       │   │   ├── pywin32_bootstrap.py
│   │       │   │   ├── pywin32_testutil.py
│   │       │   │   ├── pywintypes.py
│   │       │   │   ├── rasutil.py
│   │       │   │   ├── regcheck.py
│   │       │   │   ├── regutil.py
│   │       │   │   ├── sspi.py
│   │       │   │   ├── sspicon.py
│   │       │   │   ├── win2kras.py
│   │       │   │   ├── win32con.py
│   │       │   │   ├── win32cryptcon.py
│   │       │   │   ├── win32evtlogutil.py
│   │       │   │   ├── win32gui_struct.py
│   │       │   │   ├── win32inetcon.py
│   │       │   │   ├── win32netcon.py
│   │       │   │   ├── win32pdhquery.py
│   │       │   │   ├── win32pdhutil.py
│   │       │   │   ├── win32rcparser.py
│   │       │   │   ├── win32serviceutil.py
│   │       │   │   ├── win32timezone.py
│   │       │   │   ├── win32traceutil.py
│   │       │   │   ├── win32verstamp.py
│   │       │   │   ├── winerror.py
│   │       │   │   ├── winioctlcon.py
│   │       │   │   ├── winnt.py
│   │       │   │   ├── winperf.py
│   │       │   │   └── winxptheme.py
│   │       │   ├── libs/
│   │       │   ├── scripts/
│   │       │   │   ├── VersionStamp/
│   │       │   │   │   ├── BrandProject.py
│   │       │   │   │   ├── bulkstamp.py
│   │       │   │   │   └── vssutil.py
│   │       │   │   ├── backupEventLog.py
│   │       │   │   ├── ControlService.py
│   │       │   │   ├── h2py.py
│   │       │   │   ├── killProcName.py
│   │       │   │   ├── pywin32_postinstall.py
│   │       │   │   ├── pywin32_testall.py
│   │       │   │   ├── rasutil.py
│   │       │   │   ├── regsetup.py
│   │       │   │   └── setup_d.py
│   │       │   ├── test/
│   │       │   │   ├── win32rcparser/
│   │       │   │   ├── handles.py
│   │       │   │   ├── test_clipboard.py
│   │       │   │   ├── test_exceptions.py
│   │       │   │   ├── test_odbc.py
│   │       │   │   ├── test_pywintypes.py
│   │       │   │   ├── test_security.py
│   │       │   │   ├── test_sspi.py
│   │       │   │   ├── test_win32api.py
│   │       │   │   ├── test_win32clipboard.py
│   │       │   │   ├── test_win32cred.py
│   │       │   │   ├── test_win32crypt.py
│   │       │   │   ├── test_win32event.py
│   │       │   │   ├── test_win32file.py
│   │       │   │   ├── test_win32gui.py
│   │       │   │   ├── test_win32guistruct.py
│   │       │   │   ├── test_win32inet.py
│   │       │   │   ├── test_win32net.py
│   │       │   │   ├── test_win32pipe.py
│   │       │   │   ├── test_win32print.py
│   │       │   │   ├── test_win32profile.py
│   │       │   │   ├── test_win32rcparser.py
│   │       │   │   ├── test_win32timezone.py
│   │       │   │   ├── test_win32trace.py
│   │       │   │   ├── test_win32ts.py
│   │       │   │   ├── test_win32wnet.py
│   │       │   │   └── testall.py
│   │       │   ├── license.txt
│   │       │   └── winxpgui.py
│   │       ├── win32com/
│   │       │   ├── client/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── build.py
│   │       │   │   ├── CLSIDToClass.py
│   │       │   │   ├── combrowse.py
│   │       │   │   ├── connect.py
│   │       │   │   ├── dynamic.py
│   │       │   │   ├── gencache.py
│   │       │   │   ├── genpy.py
│   │       │   │   ├── makepy.py
│   │       │   │   ├── selecttlb.py
│   │       │   │   ├── tlbrowse.py
│   │       │   │   └── util.py
│   │       │   ├── demos/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── connect.py
│   │       │   │   ├── dump_clipboard.py
│   │       │   │   ├── eventsApartmentThreaded.py
│   │       │   │   ├── eventsFreeThreaded.py
│   │       │   │   ├── excelAddin.py
│   │       │   │   ├── excelRTDServer.py
│   │       │   │   ├── iebutton.py
│   │       │   │   ├── ietoolbar.py
│   │       │   │   ├── outlookAddin.py
│   │       │   │   └── trybag.py
│   │       │   ├── HTML/
│   │       │   │   ├── image/
│   │       │   │   ├── COM_Records.html
│   │       │   │   ├── docindex.html
│   │       │   │   ├── GeneratedSupport.html
│   │       │   │   ├── index.html
│   │       │   │   ├── misc.html
│   │       │   │   ├── package.html
│   │       │   │   ├── PythonCOM.html
│   │       │   │   ├── QuickStartClientCom.html
│   │       │   │   ├── QuickStartServerCom.html
│   │       │   │   └── variant.html
│   │       │   ├── include/
│   │       │   ├── libs/
│   │       │   ├── makegw/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── makegw.py
│   │       │   │   ├── makegwenum.py
│   │       │   │   └── makegwparse.py
│   │       │   ├── server/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── connect.py
│   │       │   │   ├── dispatcher.py
│   │       │   │   ├── exception.py
│   │       │   │   ├── factory.py
│   │       │   │   ├── localserver.py
│   │       │   │   ├── policy.py
│   │       │   │   ├── register.py
│   │       │   │   └── util.py
│   │       │   ├── servers/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── dictionary.py
│   │       │   │   ├── interp.py
│   │       │   │   ├── perfmon.py
│   │       │   │   ├── PythonTools.py
│   │       │   │   └── test_pycomtest.py
│   │       │   ├── test/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── daodump.py
│   │       │   │   ├── errorSemantics.py
│   │       │   │   ├── GenTestScripts.py
│   │       │   │   ├── pippo_server.py
│   │       │   │   ├── policySemantics.py
│   │       │   │   ├── readme.txt
│   │       │   │   ├── testAccess.py
│   │       │   │   ├── testADOEvents.py
│   │       │   │   ├── testall.py
│   │       │   │   ├── testArrays.py
│   │       │   │   ├── testAXScript.py
│   │       │   │   ├── testClipboard.py
│   │       │   │   ├── testCollections.py
│   │       │   │   ├── testConversionErrors.py
│   │       │   │   ├── testDates.py
│   │       │   │   ├── testDCOM.py
│   │       │   │   ├── testDictionary.py
│   │       │   │   ├── testDynamic.py
│   │       │   │   ├── testExchange.py
│   │       │   │   ├── testExplorer.py
│   │       │   │   ├── testGatewayAddresses.py
│   │       │   │   ├── testGIT.py
│   │       │   │   ├── testIterators.py
│   │       │   │   ├── testmakepy.py
│   │       │   │   ├── testMarshal.py
│   │       │   │   ├── testMSOffice.py
│   │       │   │   ├── testMSOfficeEvents.py
│   │       │   │   ├── testPersist.py
│   │       │   │   ├── testPippo.py
│   │       │   │   ├── testPyComTest.py
│   │       │   │   ├── testPyScriptlet.js
│   │       │   │   ├── testROT.py
│   │       │   │   ├── testServers.py
│   │       │   │   ├── testShell.py
│   │       │   │   ├── testStorage.py
│   │       │   │   ├── testStreams.py
│   │       │   │   ├── testvb.py
│   │       │   │   ├── testvbscript_regexp.py
│   │       │   │   ├── testWMI.py
│   │       │   │   ├── testxslt.js
│   │       │   │   ├── testxslt.py
│   │       │   │   └── util.py
│   │       │   ├── __init__.py
│   │       │   ├── License.txt
│   │       │   ├── olectl.py
│   │       │   ├── readme.html
│   │       │   ├── storagecon.py
│   │       │   ├── universal.py
│   │       │   └── util.py
│   │       ├── win32comext/
│   │       │   ├── adsi/
│   │       │   │   ├── demos/
│   │       │   │   │   ├── objectPicker.py
│   │       │   │   │   ├── scp.py
│   │       │   │   │   ├── search.py
│   │       │   │   │   └── test.py
│   │       │   │   ├── __init__.py
│   │       │   │   └── adsicon.py
│   │       │   ├── authorization/
│   │       │   │   ├── demos/
│   │       │   │   │   ├── EditSecurity.py
│   │       │   │   │   └── EditServiceSecurity.py
│   │       │   │   ├── __init__.py
│   │       │   ├── axcontrol/
│   │       │   │   ├── __init__.py
│   │       │   ├── axdebug/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── adb.py
│   │       │   │   ├── codecontainer.py
│   │       │   │   ├── contexts.py
│   │       │   │   ├── debugger.py
│   │       │   │   ├── documents.py
│   │       │   │   ├── dump.py
│   │       │   │   ├── expressions.py
│   │       │   │   ├── gateways.py
│   │       │   │   ├── stackframe.py
│   │       │   │   └── util.py
│   │       │   ├── axscript/
│   │       │   │   ├── client/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── debug.py
│   │       │   │   │   ├── error.py
│   │       │   │   │   ├── framework.py
│   │       │   │   │   ├── pydumper.py
│   │       │   │   │   ├── pyscript.py
│   │       │   │   │   ├── pyscript_rexec.py
│   │       │   │   │   └── scriptdispatch.py
│   │       │   │   ├── Demos/
│   │       │   │   │   └── client/
│   │       │   │   │       ├── asp/
│   │       │   │   │       │   ├── interrupt/
│   │       │   │   │       │   │   ├── test.html
│   │       │   │   │       │   │   └── test1.html
│   │       │   │   │       ├── ie/
│   │       │   │   │       └── wsh/
│   │       │   │   ├── server/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── axsite.py
│   │       │   │   ├── test/
│   │       │   │   │   ├── leakTest.py
│   │       │   │   │   ├── testHost.py
│   │       │   │   │   └── testHost4Dbg.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── asputil.py
│   │       │   ├── bits/
│   │       │   │   ├── test/
│   │       │   │   │   ├── show_all_jobs.py
│   │       │   │   │   └── test_bits.py
│   │       │   │   ├── __init__.py
│   │       │   ├── directsound/
│   │       │   │   ├── test/
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── ds_record.py
│   │       │   │   │   └── ds_test.py
│   │       │   │   ├── __init__.py
│   │       │   ├── ifilter/
│   │       │   │   ├── demo/
│   │       │   │   │   └── filterDemo.py
│   │       │   │   ├── __init__.py
│   │       │   │   └── ifiltercon.py
│   │       │   ├── internet/
│   │       │   │   ├── __init__.py
│   │       │   │   ├── inetcon.py
│   │       │   ├── mapi/
│   │       │   │   ├── demos/
│   │       │   │   │   └── mapisend.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── emsabtags.py
│   │       │   │   ├── mapitags.py
│   │       │   │   └── mapiutil.py
│   │       │   ├── propsys/
│   │       │   │   ├── test/
│   │       │   │   │   └── testpropsys.py
│   │       │   │   ├── __init__.py
│   │       │   │   └── pscon.py
│   │       │   ├── shell/
│   │       │   │   ├── demos/
│   │       │   │   │   ├── servers/
│   │       │   │   │   │   ├── column_provider.py
│   │       │   │   │   │   ├── context_menu.py
│   │       │   │   │   │   ├── copy_hook.py
│   │       │   │   │   │   ├── empty_volume_cache.py
│   │       │   │   │   │   ├── folder_view.py
│   │       │   │   │   │   ├── icon_handler.py
│   │       │   │   │   │   └── shell_view.py
│   │       │   │   │   ├── browse_for_folder.py
│   │       │   │   │   ├── create_link.py
│   │       │   │   │   ├── dump_link.py
│   │       │   │   │   ├── explorer_browser.py
│   │       │   │   │   ├── IActiveDesktop.py
│   │       │   │   │   ├── IFileOperationProgressSink.py
│   │       │   │   │   ├── IShellLinkDataList.py
│   │       │   │   │   ├── ITransferAdviseSink.py
│   │       │   │   │   ├── IUniformResourceLocator.py
│   │       │   │   │   ├── shellexecuteex.py
│   │       │   │   │   ├── viewstate.py
│   │       │   │   │   └── walk_shell_folders.py
│   │       │   │   ├── test/
│   │       │   │   │   ├── testShellFolder.py
│   │       │   │   │   ├── testShellItem.py
│   │       │   │   │   └── testSHFileOperation.py
│   │       │   │   ├── __init__.py
│   │       │   │   └── shellcon.py
│   │       │   └── taskscheduler/
│   │       │       ├── test/
│   │       │       │   ├── test_addtask.py
│   │       │       │   ├── test_addtask_1.py
│   │       │       │   ├── test_addtask_2.py
│   │       │       │   └── test_localsystem.py
│   │       │       ├── __init__.py
│   │       ├── wrapt/
│   │       │   ├── __init__.py
│   │       │   ├── __wrapt__.py
│   │       │   ├── arguments.py
│   │       │   ├── decorators.py
│   │       │   ├── importer.py
│   │       │   ├── patches.py
│   │       │   ├── proxies.py
│   │       │   ├── weakrefs.py
│   │       │   └── wrappers.py
│   │       ├── wrapt-2.1.2.dist-info/
│   │       │   ├── licenses/
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
│   │       ├── yaml/
│   │       │   ├── __init__.py
│   │       │   ├── composer.py
│   │       │   ├── constructor.py
│   │       │   ├── cyaml.py
│   │       │   ├── dumper.py
│   │       │   ├── emitter.py
│   │       │   ├── error.py
│   │       │   ├── events.py
│   │       │   ├── loader.py
│   │       │   ├── nodes.py
│   │       │   ├── parser.py
│   │       │   ├── reader.py
│   │       │   ├── representer.py
│   │       │   ├── resolver.py
│   │       │   ├── scanner.py
│   │       │   ├── serializer.py
│   │       │   └── tokens.py
│   │       ├── py.py
│   │       ├── pythoncom.py
│   │       ├── pywin32.version.txt
│   │       ├── six.py
│   │       ├── socks.py
│   │       ├── sockshandler.py
│   │       ├── typing_extensions.py
│   ├── Scripts/
│   │   ├── activate.bat
│   │   ├── Activate.ps1
│   │   ├── deactivate.bat
│   │   ├── pywin32_postinstall.py
│   │   ├── pywin32_testall.py
│   ├── .gitignore
├── Backend/
│   ├── Autorizar/
│   │   ├── codigo/
│   │   │   ├── __init__.py
│   │   │   ├── autorizar_adapter.py
│   │   │   ├── autorizar_codigo.md
│   │   │   └── process_autorizar.py
│   │   ├── configuracoes/
│   │   │   ├── autorizar_configuracoes.md
│   │   │   └── config_local.json
│   │   ├── documentacao/
│   │   │   ├── autorizar_documentacao.md
│   │   │   └── manual_operacional.md
│   │   ├── executaveis/
│   │   │   ├── autorizar_executaveis.md
│   │   │   ├── iniciar_rpa.bat
│   │   │   └── rodar_autorizar.bat
│   │   ├── relatorios/
│   │   ├── autorizar_rpa.md
│   │   └── main_autorizar.py
│   ├── CollectABA/
│   │   ├── codigo/
│   │   │   ├── __init__.py
│   │   │   ├── codigo_collectaba.md
│   │   │   ├── collectaba_adapter.py
│   │   │   ├── collectaba_engine.py
│   │   │   └── collectaba_service.py
│   │   ├── configuracoes/
│   │   │   └── configuracoes_collectaba.md
│   │   ├── documentacao/
│   │   │   └── documentacao_collectaba.md
│   │   ├── executaveis/
│   │   │   ├── executaveis_collectaba.md
│   │   │   ├── iniciar_rpa.bat
│   │   │   └── rodar_collectaba.bat
│   │   ├── __init__.py
│   │   ├── collectaba_rpa.md
│   │   └── main_collectaba.py
│   ├── Consolidacao/
│   │   ├── codigo/
│   │   │   ├── __init__.py
│   │   │   ├── codigo_consolidacao.md
│   │   │   ├── consolidacao_adapter.py
│   │   │   ├── process_consolidacao.py
│   │   │   └── rpa_consolidacao.py
│   │   ├── configuracoes/
│   │   │   ├── config_consolidacao.py
│   │   │   ├── config_local.json
│   │   │   └── configuracoes_consolidacao.md
│   │   ├── documentacao/
│   │   │   ├── documentacao_consolidacao.md
│   │   │   └── manual_operacional.md
│   │   ├── executaveis/
│   │   │   ├── executaveis_consolidacao.md
│   │   │   ├── iniciar_rpa.bat
│   │   │   └── rodar_consolidacao.bat
│   │   ├── __init__.py
│   │   ├── consolidacao_rpa.md
│   │   └── main_consolidacao.py
│   ├── Contrato/
│   │   ├── codigo/
│   │   │   ├── __init__.py
│   │   │   ├── codigo_contrato.md
│   │   │   └── contratos_adapter.py
│   │   ├── configuracoes/
│   │   │   ├── config_local.json
│   │   │   └── configuracoes_contrato.md
│   │   ├── documentacao/
│   │   │   ├── documentacao_contrato.md
│   │   │   └── manual_operacional.md
│   │   ├── executaveis/
│   │   │   ├── executaveis_contrato.md
│   │   │   ├── iniciar_rpa.bat
│   │   │   └── rodar_contrato.bat
│   │   ├── __init__.py
│   │   ├── contrato_rpa.md
│   │   └── main_contrato.py
│   ├── Emissao/
│   │   ├── codigo/
│   │   │   ├── __init__.py
│   │   │   ├── codigo_emissao.md
│   │   │   ├── emissao_adapter.py
│   │   │   └── process_guias_emissao.py
│   │   ├── configuracoes/
│   │   │   ├── config_local.json
│   │   │   └── configuracoes_emissao.md
│   │   ├── documentacao/
│   │   │   ├── analise_emissao_guias.md
│   │   │   ├── documentacao_emissao.md
│   │   │   └── manual_operacional.md
│   │   ├── executaveis/
│   │   │   ├── executaveis_emissao.md
│   │   │   ├── iniciar_rpa.bat
│   │   │   └── rodar_emissao.bat
│   │   ├── __init__.py
│   │   ├── emissao_rpa.md
│   │   └── main_emissao.py
│   ├── Global/
│   │   ├── base_rpa/
│   │   │   ├── __init__.py
│   │   │   ├── base_rpa.py
│   │   │   ├── base_rpa_global.md
│   │   │   └── logger_isolado.py
│   │   ├── documentacao/
│   │   │   ├── DOCUMENTACAO_COMPLETA_RPA.md
│   │   │   └── documentacao_global.md
│   │   ├── infraestrutura/
│   │   │   ├── chrome_driver/
│   │   │   │   ├── chrome_driver_global.md
│   │   │   ├── migrations/
│   │   │   │   ├── migration_agenda_semanal.sql
│   │   │   │   ├── migration_paciente_documentos.sql
│   │   │   │   ├── migrations_docs.md
│   │   │   │   └── schema_pacientes.sql
│   │   │   ├── .env
│   │   │   ├── __init__.py
│   │   │   ├── api_controle.py
│   │   │   ├── Desligar_Sistema.bat
│   │   │   ├── healthcheck.py
│   │   │   ├── infraestrutura_global.md
│   │   │   ├── log_tailer.py
│   │   │   ├── orchestrator.py
│   │   │   ├── process_manager.py
│   │   │   ├── real_time_handler.py
│   │   │   ├── requirements.txt
│   │   │   ├── set_global_parameters.py
│   │   │   ├── set_log_system.py
│   │   │   ├── terapias.json
│   │   │   └── UNIQ_PRO_LAUNCHER.py
│   │   ├── servicos/
│   │   │   ├── __init__.py
│   │   │   ├── agenda_service.py
│   │   │   ├── auth_service.py
│   │   │   ├── configuracoes_service.py
│   │   │   ├── database.py
│   │   │   ├── documentos_service.py
│   │   │   ├── driver.py
│   │   │   ├── driver_manager.py
│   │   │   ├── email_service.py
│   │   │   ├── limpeza_service.py
│   │   │   ├── pacientes_service.py
│   │   │   ├── profissionais_service.py
│   │   │   ├── screenshot_service.py
│   │   │   ├── servicos_global.md
│   │   │   └── support_functions.py
│   │   ├── __init__.py
│   │   └── global_recursos_compartilhados.md
│   ├── Lancamento/
│   │   ├── codigo/
│   │   │   ├── __init__.py
│   │   │   ├── adapter_lancamento_agenda.py
│   │   │   ├── codigo_lancamento.md
│   │   │   ├── lancamento_adapter.py
│   │   │   ├── process_orders_lancamento.py
│   │   │   └── send_report_lancamento.py
│   │   ├── configuracoes/
│   │   │   ├── config_local.json
│   │   │   └── configuracoes_lancamento.md
│   │   ├── documentacao/
│   │   │   ├── documentacao_lancamento.md
│   │   │   └── manual_operacional.md
│   │   ├── executaveis/
│   │   │   ├── executaveis_lancamento.md
│   │   │   ├── iniciar_rpa.bat
│   │   │   └── rodar_lancamento.bat
│   │   ├── reports/
│   │   │   └── reports_lancamento.md
│   │   ├── __init__.py
│   │   ├── lancamento_rpa.md
│   │   └── main_lancamento.py
│   ├── reports/
│   │   └── reports_nome.md
│   └── backend_uniq_rpa.md
├── Configuracao/
│   ├── configuracao_rpa.md
│   └── Configurar_Windows.bat
├── core/
│   ├── governanca/
│   │   ├── criar_novo_rpa.py
│   │   ├── governanca_core.md
│   │   ├── guardiao_execucao.py
│   │   ├── leitor_documentacao.py
│   │   └── validador_regras.py
│   └── core_nome.md
├── docs/
│   ├── PLAN-collectaba-text-selector.md
│   ├── PLAN-parallel-rpa-monitor.md
│   └── projeto_saas_blueprint.md
├── Frontend/
│   ├── Autorizar/
│   │   ├── assets/
│   │   │   └── assets_autorizar.md
│   │   ├── documentacao/
│   │   │   └── documentacao_autorizar.md
│   │   ├── templates/
│   │   │   ├── aba_token_pendente.html
│   │   │   └── templates_autorizar.md
│   │   └── frontend_autorizar_painel.md
│   ├── CollectABA/
│   │   ├── assets/
│   │   │   └── assets_collectaba.md
│   │   ├── documentacao/
│   │   │   └── documentacao_frontend_collectaba.md
│   │   ├── templates/
│   │   │   ├── collectaba.html
│   │   │   └── templates_collectaba.md
│   │   └── frontend_collectaba_painel.md
│   ├── Consolidacao/
│   │   ├── assets/
│   │   │   └── assets_consolidacao.md
│   │   ├── documentacao/
│   │   │   └── documentacao_frontend_consolidacao.md
│   │   ├── templates/
│   │   │   └── templates_consolidacao.md
│   │   └── frontend_consolidacao_painel.md
│   ├── Contrato/
│   │   ├── assets/
│   │   │   └── assets_contrato.md
│   │   ├── documentacao/
│   │   │   └── documentacao_frontend_contrato.md
│   │   ├── templates/
│   │   │   └── templates_contrato.md
│   │   └── frontend_contrato_painel.md
│   ├── Emissao/
│   │   ├── assets/
│   │   │   └── assets_emissao.md
│   │   ├── documentacao/
│   │   │   └── documentacao_frontend_emissao.md
│   │   ├── templates/
│   │   │   └── templates_emissao.md
│   │   └── frontend_emissao_painel.md
│   ├── Global/
│   │   ├── assets/
│   │   │   ├── js/
│   │   │   │   └── monitor_ws.js
│   │   │   ├── agenda_v3.js
│   │   │   ├── assets_global.md
│   │   ├── documentacao/
│   │   │   └── documentacao_frontend_global.md
│   │   ├── templates/
│   │   │   ├── monitor/
│   │   │   │   └── monitor.html
│   │   │   ├── _theme_head.html
│   │   │   ├── admin_configuracoes.html
│   │   │   ├── admin_profissionais.html
│   │   │   ├── admin_usuarios.html
│   │   │   ├── agenda.html
│   │   │   ├── autorizar.html
│   │   │   ├── collectaba.html
│   │   │   ├── consolidacao.html
│   │   │   ├── contratos.html
│   │   │   ├── erro.html
│   │   │   ├── index.html
│   │   │   ├── lancamento.html
│   │   │   ├── login.html
│   │   │   ├── pacientes.html
│   │   │   ├── sucesso.html
│   │   │   ├── templates_global.md
│   │   │   └── tokens.html
│   │   ├── app_uniq.py
│   │   └── frontend_global_painel.md
│   ├── Lancamento/
│   │   ├── assets/
│   │   │   └── assets_lancamento.md
│   │   ├── documentacao/
│   │   │   └── documentacao_frontend_lancamento.md
│   │   ├── templates/
│   │   │   └── templates_lancamento.md
│   │   └── frontend_lancamento_painel.md
│   └── frontend_uniq_rpa.md
├── scratch/
├── .cursorrules
├── .gitignore
├── arquivos_intocaveis_rpa.md
├── INICIAR_SISTEMA_VISUAL.bat
├── projeto_uniq_rpa.md
└── README.md
```

| 2026-08-05 | Correção CollectABA Modal Race Condition | Adicionado WebDriverWait explícito para ion-modal fechar antes da próxima iteração do ciclo de textos, garantindo que o Angular registre múltiplos evolutivos para o mesmo paciente sequencialmente sem sobrepor a mesma textarea. | Resolvido |

---
## [ATUALIZACAO] Agosto 2026: Consolidação de Histórico e Painéis de Interface Dinâmica

* **Integração Universal de Histórico**: Todas as interfaces (`lancamento.html`, `agenda.html`, `autorizar.html`, `consolidacao.html`) adotam o padrão de Tabs introduzido no Evolutivo ("Controle" vs "Histórico"). Os relatórios renderizam JSON dinamicamente via JS na tela do usuário.
* **API Global de Histórico**: Endpoint `/api/v2/rpa/historico/<nome_rpa>` padronizado e gerencia o consumo. O banco (`tb_historico_rpa`) passou a usar coluna JSON (`relatorio`) com métricas absolutas e tempos exatos de execução.
* **Consolidação Temporal**: A etapa de consolidação salva permanentemente cópias da planilha cruzada de períodos fechados no backend (`dados/saida/historico/Consolidacao_{mes}_{id}.xlsx`). O Frontend busca essas pendências históricas convertidas sob demanda para CSV instantaneamente.
* **Limpeza e Clean Code**: Limpeza profunda de resíduos de desenvolvimento efetuada nas raízes. Nativos Python para migração foram excluídos, restando as pastas oficiais ditadas pela Governança (`/codigo`, `/dados`, `/logs`, `/infra`).

