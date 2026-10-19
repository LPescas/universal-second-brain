# Padrões Python — Base de Conhecimento

> Carregamento sob demanda. Triggers: python, flask, fastapi, async, typing.

---

## Padrões do Usuário (Validados)
- Type hints obrigatórios (strict)
- `print()` proibido → sempre logger
- Snake_case para tudo
- Sem acentos em nomes de arquivo
- Google-style docstrings
- Imports absolutos
- Max 120 chars/linha
- Tratamento de erro específico (sem bare except)
- Entry points: `main_<module>.py` na raiz do módulo

## Flask Patterns (Projetos UNIQ)
- Servidor Web em `app_uniq.py`
- Rotas organizadas por orchestrator
- Templates HTML com Jinja2
- Serviços compartilhados em `Global/`

## Estrutura de Módulos
```
modulo/
├── main_<modulo>.py        # Entry point (sys.path manipulation)
├── codigo/                 # Toda lógica Python
│   ├── <modulo>_adapter.py # Interface com sistemas externos
│   ├── process_<x>.py      # Processamento de dados
│   └── helpers/
├── configuracoes/          # .env, params
├── dados/                  # I/O runtime
├── documentacao/           # Docs
├── executaveis/            # .bat scripts
└── logs/                   # Log output
```

---

## 📜 Histórico
| Data       | Descrição                                    |
|------------|----------------------------------------------|
| 2026-07-31 | Criação inicial a partir dos projetos UNIQ   |
