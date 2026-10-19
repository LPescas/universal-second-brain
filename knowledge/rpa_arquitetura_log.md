
## 2026-08-27: Implementação do Histórico UI
- Criado modelo de abas com script autônomo (Python inject HTML).
- Endpoint de historico (/api/v2/rpa/historico/<nome>) adicionado à api_controle.py.
- O motor do banco usa JSON puro para flexibilidade.

## 2026-08-27: Update Histórico Consolidacao (Downloads Permanentes)
- Backup isolado timestamped (Consolidacao_YYYY-MM_{timestamp}.xlsx) no adapter.
- Criado historico_path salvo no DB e rotas de download no pi_controle.py convertendo JSON -> CSV live.
