# Arquitetura RPA — Base de Conhecimento

> Carregamento sob demanda. Triggers: rpa, automation, selenium, driver, orchestrator.

---

## Padrão "The UNIQ Way"
1. **Hub & Spoke Modular**: Frontend Flask separado de Backend RPA
2. **Scripts Salva-Vidas**: Todo módulo opera standalone via `main_<rpa>.py`
3. **Zero-Trust Documentation**: Todo subdir tem `*_nome.md`
4. **6 Pastas Obrigatórias**: codigo, documentacao, logs, dados, configuracoes, executaveis
5. **Isolamento de Estado**: Credenciais apenas em `.env` central

## Selenium/Driver
- Init via `Backend/Global/servicos/driver.py::start_session()` — NUNCA init bruto
- ChromeDriver auto-sync via `driver_manager.py`
- Sem ChromeDriver hardcoded

## Orchestrator
- `Backend/Global/infraestrutura/orchestrator.py` coordena todos os módulos
- Rotas Flask mapeiam para templates HTML
- Cada módulo pode rodar independente do Flask (via main_*.py)

## Logging
- Format: `[ID] [RPA] [ETAPA] [TIPO] Mensagem`
- `print()` = PROIBIDO
- Logs locais: `<modulo>/logs/`
- Logs web: `Backend/Global/logs/`

## Guardião de Execução
- `core/governanca/guardiao_execucao.py` — valida estrutura no boot
- `core/governanca/validador_regras.py` — compliance check
- `core/governanca/leitor_documentacao.py` — valida presença de docs

---

## 📜 Histórico
| Data       | Descrição                                    |
|------------|----------------------------------------------|
| 2026-07-31 | Criação inicial a partir da arquitetura UNIQ |

---
## [ATUALIZACAO] Agosto 2026: Consolidação de Histórico e Painéis de Interface Dinâmica

* **Integração Universal de Histórico**: Todas as interfaces (`lancamento.html`, `agenda.html`, `autorizar.html`, `consolidacao.html`) adotam o padrão de Tabs introduzido no Evolutivo ("Controle" vs "Histórico"). Os relatórios renderizam JSON dinamicamente via JS na tela do usuário.
* **API Global de Histórico**: Endpoint `/api/v2/rpa/historico/<nome_rpa>` padronizado e gerencia o consumo. O banco (`tb_historico_rpa`) passou a usar coluna JSON (`relatorio`) com métricas absolutas e tempos exatos de execução.
* **Consolidação Temporal**: A etapa de consolidação salva permanentemente cópias da planilha cruzada de períodos fechados no backend (`dados/saida/historico/Consolidacao_{mes}_{id}.xlsx`). O Frontend busca essas pendências históricas convertidas sob demanda para CSV instantaneamente.
* **Limpeza e Clean Code**: Limpeza profunda de resíduos de desenvolvimento efetuada nas raízes. Nativos Python para migração foram excluídos, restando as pastas oficiais ditadas pela Governança (`/codigo`, `/dados`, `/logs`, `/infra`).

