# 🧠 Second Brain — Hub Universal de Conhecimento, Agentes e Ferramentas

> **Versão:** 2.0 (Zero Trust & Auto-Sync Enabled)  
> **Proprietário:** USER  
> **Localização:** `C:\Users\USER\.second_brain`  
> **Compatibilidade:** Universal (Claude Code, Gemini CLI, Google Antigravity, GLM, Ollama, OpenAI, VS Code, Cursor)

---

## 🎯 O que é o Second Brain?

O **Second Brain** é o centro nervoso e operacional unificado da sua máquina. Ele centraliza:
1. **Regras Globais e Governança:** Diretrizes absolutas de execução para qualquer agente de IA.
2. **Hub de 25 Repositórios Especializados:** Ferramentas locais de alta performance (mídia, descompilação, parsers, RAG, design) com proteção **Cold Snapshot** e sincronização automática.
3. **Catálogo de Ativos Multi-Agente:** 20 agentes especialistas, 47 skills operacionais e 13 workflows de automação prontos para execução imediata.
4. **Memória Contínua:** Retenção perpétua de preferências, decisões técnicas e histórico de aprendizado cross-session.
5. **Dashboard de Métricas em Tempo Real:** Interface visual com telemetria de tokens, arquivos poupados e tempo economizado.

---

## 🗺️ Mapa de Diretórios e Recursos

```text
C:\Users\USER\.second_brain\
├── README.md                      # Portal de boas-vindas e guia rápido (este arquivo)
├── projeto_second_brain.md         # Documentação Mestre de Governança Zero Trust
├── MASTER_INDEX.yaml               # Ponto de entrada P0 de roteamento do sistema
├── global_rules.md                 # Regras absolutas de comportamento para IA
├── active_behavior_rules.yaml      # Regras ativas de comportamento com fingerprints
├── behavioral_patterns.yaml        # Padrões comportamentais do desenvolvedor
│
├── core\                          # Núcleo de Governança e Execução
│   └── governanca\                # Guardião Zero Trust, validadores e leitores
│
├── repos\                         # Hub de 25 Repositórios com Auto-Sync
│   ├── media_processing\          # Síntese de voz, áudio, vídeo e diagramas
│   ├── dev_reverse_engineering\   # Engenharia reversa, TDD, prompts e ML
│   ├── ui_ux_design\              # Design de interfaces premium anti-slop
│   ├── orchestration_governance\  # Multi-agentes, barramentos e framework 5P
│   ├── routing_gateways\          # Gateways de IA gratuitos e roteamento
│   ├── memory_rag_graphs\         # Memória persistente e grafos de dependências
│   ├── document_web_parsers\      # Extratores de PDF (docling) e scraping leve
│   └── cloud_security_b2b\        # Auditoria OWASP, nuvem e conectores SaaS
│
├── knowledge\                     # Base de Conhecimento e Decisões
│   ├── installed_assets_catalog.md # Catálogo mestre unificado de todos os ativos
│   ├── project_decisions.md        # Decisões arquiteturais registradas
│   ├── learning_log.md             # Aprendizados contínuos do agente
│   └── rpa_database_schema_audit.md# Auditoria e schema de bancos de dados
│
├── scripts\                       # Motores Operacionais e Automações
│   ├── repo_sync_engine.py         # Motor de sincronização e cold snapshot
│   ├── schedule_auto_sync.ps1      # Agendamento no Windows Task Scheduler
│   ├── generate_ai_guides.py       # Gerador dos contratos AI_GUIDE.md
│   ├── build_installed_assets_catalog.py # Indexador dinâmico de recursos
│   └── usage_metrics.py            # Backend de telemetria para o dashboard
│
├── frontend\                      # Dashboard Visual de Métricas
│   ├── index.html                  # Interface do painel de controle
│   ├── app.js                      # Lógica de renderização de gráficos
│   └── start_dashboard.ps1         # Inicializador local do painel
│
├── backend\                       # Serviços Locais e Agente Aurelio
│   └── aurelio\                   # Agente autônomo local integrado
│
├── projects\                      # Contextos de Projetos Externos
│   ├── rpa_context.md              # Contexto operacional do RPA UNIQ
│   ├── wrpe_recorder_context.md    # Contexto operacional do WRPE Recorder
│   └── RPA_Autorizar\             # Documentações de sub-módulos RPA
│
├── integrations\                  # Conectores com IDEs e Terminais
│   ├── cursorrules_template.md     # Template para regras do Cursor
│   └── profile_snippet.ps1         # Integração com perfil PowerShell
│
└── .agents\                       # AG Kit — Motor Multi-Agente
    ├── agent\                     # 20 Agentes especialistas (.md)
    ├── skills\                    # 47 Skills e manuais de engenharia
    ├── workflows\                 # 13 Workflows de comando (/plan, /debug...)
    ├── rules\                     # Regras operacionais universais
    └── scripts\                   # Scripts de validação empírica isolada
```

---

## ⚡ Comandos Rápidos e Atalhos

### Para o Desenvolvedor (Humano):
- **Abrir Dashboard:** Execute `.\frontend\start_dashboard.ps1` no PowerShell.
- **Sincronizar Repositórios:** Execute `python .\scripts\repo_sync_engine.py`.
- **Agendar Sincronização Diária:** Execute `.\scripts\schedule_auto_sync.ps1 -Install`.
- **Reindexar Ativos:** Execute `python .\scripts\build_installed_assets_catalog.py`.

### Para o Agente de IA:
- **Ponto de Partida Obrigatório:** Ler [MASTER_INDEX.yaml](file:///C:/Users/USER/.second_brain/MASTER_INDEX.yaml).
- **Roteamento de Demanda:** Consultar [installed_assets_catalog.md](file:///C:/Users/USER/.second_brain/knowledge/installed_assets_catalog.md) antes de criar qualquer código do zero.
- **Economia de Tokens:** Ler apenas as seções relevantes dos contratos `AI_GUIDE.md` de cada ferramenta.
- **Validação Empírica Obrigatória:** Executar testes via `.agents/scripts/` antes de finalizar entregas.
- **Assinatura de Execução:** Injetar métricas em `usage_metrics.py` e imprimir o relatório formal do Second Brain ao final de cada turno.
