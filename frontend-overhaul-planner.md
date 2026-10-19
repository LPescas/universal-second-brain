# 📋 PLANNER: Repaginação e Evolução do Frontend do Second Brain v2.0

> **Status:** Proposto / Pronto para Execução  
> **Autor:** `project-planner` (AG Kit Multi-Agent Framework)  
> **Data:** 2026-10-19  
> **Alvo:** `C:\Users\USER\.second_brain\frontend\` e ecossistema integrado  

---

## 🎯 1. Visão Geral e Objetivos do Projeto

O objetivo desta atualização é transformar o frontend do Second Brain em uma **Central de Observabilidade e Operação Unificada**, onde o usuário e os agentes de IA interagem visualmente com todo o conhecimento, projetos e ferramentas locais da máquina.

### Pilares Fundamentais:
1. **Telemetria de Uso 100% Real**: Exibição honesta de tokens gastos por dia (gráfico temporal diário), tempo médio de resposta/duração por interação e censo dinâmico de recursos (47 skills, 20 agentes, 13 workflows, 25 ferramentas).
2. **Grafo de Projetos Locais do Usuário**: Uma aba visual interativa (Canvas 60fps) mapeando todos os projetos na máquina (`C:\Projetos\RPA`, `C:\Projetos\WRPE_Recorder`, `SecondBrain_Aurelio`, etc.), suas rotas, componentes, banco de dados e telas, permitindo que a IA e o usuário localizem qualquer código sem escanear diretórios às cegas e sem gastar tokens.
3. **Aurélio AI Desktop (Ollama Integrado)**: Interface de chat operacional conectada ao backend nativo do Aurélio, com suporte a modelos Ollama de baixo consumo de RAM e alta capacidade de raciocínio (`qwen2.5-coder:7b`, `hermes3:8b`, `qwen2.5:3b`), prestando consultoria em arquitetura, melhorias e indicação exata de skills e ferramentas para cada tarefa.
4. **Governança Zero Trust & Eficiência de Tokens**: Continuidade da proteção por cabeçalhos obrigatórios, validação empírica em `.agents/scripts/` e contratos semânticos `AI_GUIDE.md`.

---

## 🏗️ 2. Arquitetura da Solução e Componentes

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   FRONTEND SECOND BRAIN (Web UI)                       │
├───────────────────┬───────────────────┬────────────────────────────────┤
│ 📊 Dashboard Real │ 🕸️ Grafo Projetos │ 🤖 Aurélio AI (Ollama Local)  │
│ - Tokens por dia  │ - RPA             │ - Chat Jarvis (3 partes)       │
│ - Tempo resposta  │ - WRPE_Recorder   │ - Recomendador de Skills       │
│ - Censo de Skills │ - SecondBrain     │ - Seletor de Modelo Ollama     │
│ - Eficiência RAG  │ - Inspeção Telas  │ - Modo Restrito / Expandido    │
└─────────┬─────────┴─────────┬─────────┴───────────────┬────────────────┘
          │                   │                         │
          ▼                   ▼                         ▼
┌───────────────────┐ ┌───────────────────┐ ┌───────────────────────────┐
│ scripts/          │ │ scripts/          │ │ scripts/server.py         │
│ usage_metrics.py  │ │ map_projects.py   │ │ + backend/aurelio/        │
│ (agregação diária)│ │ (topologia grafo) │ │ (pipeline_principal Ollama)│
└───────────────────┘ └───────────────────┘ └───────────────────────────┘
```

---

## 🧩 3. Detalhamento dos 4 Módulos de Atualização

### Módulo 1: Telemetria Real Diária e Censo Dinâmico de Recursos
- **Arquivo backend/script**: `scripts/usage_metrics.py`
  - Adicionar função `compute_daily_timeline(entries)`: agrupa e soma o consumo real de tokens por data de calendário (`YYYY-MM-DD`), calculando total do dia, total de interações e tempo médio de resposta do dia.
  - Adicionar função `get_system_census()`: varredura em tempo real que calcula:
    - Total de Skills em `.agents/skills/` e globais.
    - Total de Agentes especialistas em `.agents/agent/`.
    - Total de Workflows operacionais em `.agents/workflows/`.
    - Total de Ferramentas externas em `repos/`.
    - Total de Projetos monitorados em `projects/`.
- **Exportador**: `scripts/export_frontend_hub_data.py`
  - Incluir os dados diários e o censo no `frontend/telemetry_data.json` e `scripts/metrics_export.json`.
- **UI do Dashboard**:
  - Novo card de métrica: **"Tokens Utilizados Hoje / Por Dia"**.
  - Novo card de métrica: **"Tempo Médio de Duração / Resposta"** (em segundos/minutos).
  - Novo card de métrica: **"Recursos & Skills Ativas"** (contagem dinâmica com link de navegação).
  - Gráfico de barras da timeline alternável: **Por Sessão** vs **Por Dia Calendário**.

### Módulo 2: Aba do Grafo de Projetos Interligados do Usuário
- **Identificação da Aba**: `#section-user-projects-graph` (ou expansão da aba de Grafos com seletor de visão: *Hub de Ferramentas* vs *Projetos da Máquina*).
- **Mapeamento de Topologia dos Projetos**:
  - `C:\Projetos\RPA`:
    - Módulos: Faturamento TISS, Digitação de Guias SP/SADT, Emissão, Lançamento de Rascunhos, Autorização, Consolidadores, CollectAba.
    - Infra: Flask server, Selenium WebDriver, Banco SQLite (`tb_agenda_profissionais`, `tb_usuarios`), Telas HTML (`lancamento.html`, `monitor.html`).
  - `C:\Projetos\WRPE_Recorder`:
    - Módulos: Gravação de ações de usuário, Playwright recorder, Extensão Chrome, Replay engine, SQLite store.
  - `C:\Projetos\SecondBrain_Aurelio`:
    - Módulos: Agente Jarvis, Pipeline de 7 etapas, Memória híbrida (BM25 + embeddings), SQLite `aurelio.db`, Integração Ollama.
  - `C:\Projetos\AutomationTest_122844`:
    - Módulos: Scripts de automação Selenium, suites de teste de regressão.
  - `C:\Users\USER\.second_brain`:
    - Módulos: Core de Governança Zero Trust, Guardião de Execução, Hub dos 25 repositórios, Memória contínua.
- **Painel Inspetor de Projeto (Inspector)**:
  - Ao clicar no nó de um projeto ou submódulo:
    - Caminho absoluto na máquina (link direto para abrir/inspecionar).
    - Descrição da finalidade e regras de negócio.
    - Lista de arquivos intocáveis / arquivos protegidos.
    - Páginas web / endpoints associados.
    - **Benefício de IA**: Permite que o agente consulte apenas esse nó contextual antes de executar tarefas, sem ler pastas inteiras no disco, garantindo zero alucinações e mínimo gasto de tokens.

### Módulo 3: Aba Aurélio AI — Consultor Desktop Local via Ollama
- **Arquivo backend**: `scripts/server.py` e `backend/aurelio/agent/agent.py`
  - Conexão do endpoint `POST /api/chat` diretamente ao `orchestrator.pipeline_principal()`.
  - Endpoint `GET /api/aurelio/status`: verifica se o daemon do Ollama está rodando (`http://localhost:11434/api/tags`), lista os modelos instalados e o modelo ativo.
  - Endpoint `POST /api/aurelio/model`: permite trocar o modelo em tempo de execução via UI.
- **Seleção e Benchmark de Modelos Ollama (Desktop Eficiente)**:
  - 🥇 **Opção 1 (Recomendado - Melhor Raciocínio & Código): `qwen2.5-coder:7b` ou `qwen2.5:7b`**
    - Consumo de RAM: ~4.7 GB VRAM/RAM.
    - Pontos Fortes: Compreensão impecável de arquitetura, gera código limpo, suporte nativo perfeito a Português BR.
  - 🥈 **Opção 2 (Ultra-Leve & Rápido): `qwen2.5:3b` ou `llama3.2:3b`**
    - Consumo de RAM: ~2.0 a 2.5 GB.
    - Pontos Fortes: Latência quase zero, ideal para computadores com menos RAM livre ou sem placa de vídeo dedicada.
  - 🥉 **Opção 3 (Especialista em Agentes & Instruções): `hermes3:8b`**
    - Consumo de RAM: ~5.0 GB.
    - Pontos Fortes: Execução rigorosa de prompts de sistema e chamadas a ferramentas.
- **Interface Gráfica do Aurélio na Web**:
  - Chat moderno com histórico contínuo (carregado do banco `aurelio.db`).
  - Badge de status de conexão com o Ollama em tempo real (Online 🟢 / Offline 🔴).
  - Seletor de modelo Ollama no cabeçalho do chat.
  - Toggle entre **Modo Restrito** (somente base Second Brain) e **Modo Expandido** (Second Brain + conhecimento geral).
  - **Cards de Sugestão de Skills & Ferramentas**:
    - Quando o usuário pergunta como fazer algo, o Aurélio identifica no Second Brain e sugere pills clicáveis: *"Use a skill `@frontend-design`"* ou *"Use a ferramenta `repos/media_processing/VoiceStudio`"*.

### Módulo 4: Repaginação e Design System Integrado
- **Arquivos**: `frontend/index.html`, `frontend/style.css`, `frontend/app.js`
  - Menu lateral organizado com ícones claros e contadores (Dashboard, Projetos, Histórico, Saúde, Conhecimento, Evolução, Hub Repositórios, Grafo Projetos & Core, Aurélio AI).
  - Design Dark Mode refinado com paleta Slate/Cyan/Emerald/Violet.
  - Transições suaves e carregamento reativo via fetch assíncrono com debounce e cache bypass.

---

## 🗓️ 4. Fases de Execução Passo a Passo (4-Phase Plan)

### Fase 1: Backend de Métricas & Topologia de Projetos (Tempo estimado: 15 min)
- [ ] Atualizar `scripts/usage_metrics.py` com agregação por dia calendário e métricas de tempo de resposta.
- [ ] Criar gerador de topologia de projetos `scripts/map_user_projects_graph.py` que lê os contextos de `projects/` e `MASTER_INDEX.yaml`.
- [ ] Atualizar `scripts/export_frontend_hub_data.py` para exportar `projects_graph_data.json` e `telemetry_daily.json`.

### Fase 2: Backend do Servidor & Integração Ollama Aurélio (Tempo estimado: 20 min)
- [ ] Atualizar `scripts/server.py` com rotas `/api/aurelio/status`, `/api/aurelio/model` e `/api/chat`.
- [ ] Atualizar `backend/aurelio/agent/agent.py` para enriquecer as respostas com recomendações dinâmicas de skills e repositórios do Hub.
- [ ] Validar conexão do Aurélio com modelos Ollama locais (`qwen2.5`, `hermes3`, etc.).

### Fase 3: Frontend — UI, Gráficos, Grafo de Projetos e Chat Aurélio (Tempo estimado: 35 min)
- [ ] Atualizar `frontend/index.html` com os novos cards de KPIs diários e a interface completa do Aurélio AI.
- [ ] Adicionar seletor de visualização no Grafo (Hub de Repositórios vs Projetos da Máquina) no Canvas.
- [ ] Implementar a lógica de chat do Aurélio no `frontend/app.js` (envio assíncrono, renderização em 3 partes, pills de skills sugeridas).
- [ ] Estilizar novos componentes no `frontend/style.css`.

### Fase 4: Validação Empírica, Testes e Auto-Alimentação (Tempo estimado: 15 min)
- [ ] Criar script de teste empírico `.agents/scripts/test_frontend_overhaul.py`.
- [ ] Executar bateria completa de testes de governança e implementação.
- [ ] Testar no navegador via `frontend/start_dashboard.ps1`.
- [ ] Atualizar `knowledge/learning_log.md` e `knowledge/project_decisions.md`.
- [ ] Commit Git das alterações.

---

## 🔒 5. Conformidade com Governança e Regras do Second Brain

- **Zero Trust Guardian**: Nenhuma pasta será criada sem seu respectivo arquivo de documentação `*_nome.md` com cabeçalho de governança.
- **Nomenclatura Limpa**: Todos os arquivos de script respeitarão a convenção `snake_case` sem caracteres acentuados.
- **Validação Isolada Mandatória**: Nenhuma entrega será finalizada sem execução empírica comprovada por script em `.agents/scripts/`.
