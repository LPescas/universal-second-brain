# 🧠 Plano de Expansão e Unificação do Second Brain: Hub Universal de Ferramentas, Repositórios e Agentes

> **Slug:** `second-brain-expansion.md`  
> **Status:** ✅ CONCLUÍDO E VALIDADO EMPIRICAMENTE (100% dos Testes Passaram)  
> **Responsável:** `@project-planner` + `@orchestrator`  
> **Compatibilidade Alvo:** Universal (Claude Code, Gemini CLI, Google Antigravity, GLM, Ollama, OpenAI, Cursor, VS Code)  
> **Localização de Instalação:** `C:\Users\USER\.second_brain\repos\` e `C:\Users\USER\.second_brain\.agents\`

---

## 🎯 1. Objetivo Geral

Estruturar, catalogar, baixar localmente e integrar **25 repositórios especializados** e todos os **plugins, skills, workflows e agentes existentes** dentro do **Second Brain**, criando um ecossistema agnóstico de modelo de IA que:
1. **Reduza drasticamente o consumo de tokens** através de guias semânticos diretos (`AI_GUIDE.md`), evitando reescrita de ferramentas ou pesquisas repetitivas.
2. **Promova retroalimentação automática** contínua para memória de longo prazo.
3. **Garanta persistência e resiliência fria (Cold Snapshot)**: cada repositório operará localmente, mantendo sua funcionalidade mesmo se for excluído ou tornado privado no GitHub.
4. **Implemente atualização automática em segundo plano (Auto-Sync Engine)** sem requerer intervenção manual do usuário.
5. **Permita que qualquer agente de qualquer fornecedor (Claude, Gemini, GLM, Ollama, etc.)** acesse, compreenda e utilize as capacidades imediatamente.

---

## 🗂️ 2. Taxonomia e Agrupamento dos 25 Repositórios

Os 25 repositórios serão alocados na raiz de repositórios do Second Brain (`C:\Users\USER\.second_brain\repos\<categoria>\<repo_name>`), divididos nos 8 grupos estratégicos a seguir:

```
C:\Users\USER\.second_brain\repos\
├── media_processing\          # Imagem, Vídeo, Áudio e Diagramação
│   ├── VoiceStudio\           # Síntese TTS, clonagem vocal e estúdio de áudio
│   ├── editonny\              # Edição automatizada de vídeo e imagem com IA
│   ├── diagram-design\        # Padronização e blueprints de diagramas visuais/ASCII
│   └── paperclip\             # Extração visual, conversor de design/telas para código
│
├── dev_reverse_engineering\   # Código, Engenharia Reversa e Prototipagem
│   ├── rea\                   # Engenharia reversa, análise de binários e descompilação com LLM
│   ├── ECC\                   # Everything Claude Code - coletânea de prompts e ferramentas CLI
│   ├── vibe-coding-toolkit\   # Boilerplates ultra-rápidos e snippets de prototipagem ágil
│   ├── andrej-karpathy-skills # Princípios de Deep Learning, nanoGPT e boas práticas de ML
│   └── superpowers\           # Habilidades mestras (TDD rigoroso, debugging sistemático)
│
├── ui_ux_design\              # Design de Interfaces e Qualidade Visual
│   └── impeccable\            # Princípios anti-slop, micro-interações e design refinado
│
├── orchestration_governance\  # Orquestração Multi-Agente e Metodologias
│   ├── ruflo\                 # Runtime de orquestração multi-agente de alta velocidade
│   ├── agentville\            # Simulação e colaboração de agentes especializados
│   ├── framework-5p\          # Metodologia dos 5Ps para estruturação de projetos e negócios
│   └── claude-plugins-official# Catálogo oficial de extensões e plugins de agentes
│
├── routing_gateways\          # Roteamento de Modelos e APIs Gratuitas
│   ├── OmniRoute\             # Roteador inteligente de LLMs com fallback e custo zero
│   └── freellmapi\            # Gateway agregador de provedores de IA gratuitos
│
├── memory_rag_graphs\         # Memória Persistente e Grafos de Conhecimento
│   ├── claude-mem\            # Memória contínua cross-session para agentes de IA
│   ├── hindsight\             # Avaliação reflexiva de contexto RAG e memória adaptativa
│   └── graphify\              # Conversão de código e documentos em Grafos de Conhecimento
│
├── document_web_parsers\      # Ingestão de Documentos, Scraping e Ciência
│   ├── docling\               # Extrator e parser multimodal de PDF, Word e tabelas
│   ├── ponytail\              # Scraper web headless ultrarrápido sem overhead
│   └── scientific-agent-skills# Habilidades para pesquisa, cálculo e artigos científicos
│
└── cloud_security_b2b\        # Nuvem, Segurança e Conectores B2B
    ├── security-audit-skill\  # Auditoria de vulnerabilidades e postura OWASP/Cloudflare
    ├── Octop\                 # Gestão e automação multi-cloud unificada da Tencent
    └── nango\                 # Conector unificado para centenas de integrações SaaS (OAuth)
```

---

## 🔄 3. Arquitetura do Motor de Auto-Atualização e Resiliência (Auto-Sync Engine)

### 3.1 Mecanismo de Sincronização (`repo_sync_engine.py`)
- **Localização:** `C:\Users\USER\.second_brain\scripts\repo_sync_engine.py`
- **Manifesto de Controle:** `C:\Users\USER\.second_brain\repos\repos_manifest.yaml`
- **Comportamento:**
  1. Itera por todos os repositórios listados no manifesto.
  2. Executa `git remote update` e `git pull --ff-only`.
  3. **Tolerância a Falhas e Cold Storage:** Se o repositório remoto retornar erro 404 (deletado) ou 403 (privatizado), o script não apaga nem danifica a pasta local; ele marca o status no manifesto como `COLD_SNAPSHOT_LOCKED` e emite alerta no log.
  4. Registra histórico de atualizações em `C:\Users\USER\.second_brain\scripts\repo_sync_history.json`.
  5. Atualiza a data de última sincronização e o hash do commit no manifesto.

### 3.2 Agendamento Automático Silencioso
- Configuração de tarefa agendada no Windows (Task Scheduler) ou script disparado em background via rotina de manutenção do Second Brain sem solicitar confirmação manual ao usuário.

---

## 📄 4. Padrão Universal de Documentação (`AI_GUIDE.md`)

Cada repositório baixado e cada asset existente receberá na raiz da sua respectiva pasta um arquivo `AI_GUIDE.md` contendo um contrato padronizado legível por humanos e qualquer modelo de IA:

```markdown
---
name: [Nome da Ferramenta/Repo]
category: [media | dev | reverse_eng | ui_ux | orchestration | routing | memory | parsers | security]
universal_compatibility: [claude, gemini, glm, ollama, antigravity, openai, cursor]
tokens_efficiency: [Alto | Médio] - [Breve justificativa de economia de tokens]
triggers: [palavra1, palavra2, comando, intenção]
---

# 📖 Guia de Uso: [Nome da Ferramenta]

## 1. O que é e para que serve
Resumo claro e direto de 2 a 3 frases explicando o propósito central.

## 2. Como isso ajuda nos seus projetos (Benefícios Práticos)
- Evita reconstruir lógica do zero.
- Como aplicar no projeto RPA, WRPE_Recorder ou novos desenvolvimentos.

## 3. Como o Agente de IA deve Executar (Qualquer Modelo)
- **Modo CLI / Terminal:** Comandos diretos.
- **Modo Script Python / Wrapper:** Código pronto de chamada.
- **Entrada e Saída esperadas:** Formato de dados.

## 4. Como Economizar Tokens e Retroalimentar o Second Brain
- Diretrizes para consumir apenas os outputs estruturados e registrar aprendizados no Second Brain.
```

---

## 🗃️ 5. Auditoria e Padronização dos Recursos Já Instalados

O Second Brain já conta com um rico conjunto de recursos que serão unificados sob o mesmo padrão:
1. **40+ Skills em `.agents/skills/`** (`clean-code`, `systematic-debugging`, `tdd-workflow`, `frontend-design`, `powershell-windows`, etc.):
   - Verificação de metadados YAML.
   - Criação do catálogo mestre indexado em `C:\Users\USER\.second_brain\knowledge\installed_assets_catalog.md`.
2. **20 Agentes Especialistas em `.agents/agent/`** (`backend-specialist`, `frontend-specialist`, `debugger`, `orchestrator`, `project-planner`, etc.):
   - Mapeamento das regras de acionamento cruzado com os novos repositórios.
3. **Workflows em `.agents/workflows/`** (`/plan`, `/create`, `/orchestrate`, `/debug`, `/verify`):
   - Inclusão dos novos fluxos de sincronização e chamadas aos repositórios.
4. **Scripts Operacionais em `scripts/`**:
   - Integração das métricas e consolidadores com o novo `repo_sync_engine.py`.

---

## 🗺️ 6. Integração com as Regras Gerais e `MASTER_INDEX.yaml`

1. **Atualização do `MASTER_INDEX.yaml`**:
   - Adicionar chave `repositories_hub` apontando para o manifesto e as categorias.
   - Atualizar a seção `intent_routing` para que solicitações como "fazer engenharia reversa", "extrair texto de PDF complexo", "gerar diagrama", "rotear LLM barato", "sintetizar voz" apontem automaticamente para as ferramentas locais correspondentes.
2. **Atualização das Regras Globais (`global_rules.md`)**:
   - Estabelecer a regra de **Consulta Prévia Mandatória ao Hub**: qualquer agente antes de criar uma biblioteca ou sugerir uma solução deve consultar se já existe uma ferramenta instalada no Second Brain para a tarefa.

---

## 📋 7. Cronograma e Fases de Execução (Task Breakdown)

### Fase 1: Fundação, Manifesto e Motor de Sincronização
- [x] **Tarefa 1.1:** Criar a árvore de pastas em `C:\Users\USER\.second_brain\repos\` com as 8 categorias.
- [x] **Tarefa 1.2:** Criar o arquivo `C:\Users\USER\.second_brain\repos\repos_manifest.yaml` contendo as URLs dos 25 repositórios, pastas de destino, status e comandos de atualização.
- [x] **Tarefa 1.3:** Desenvolver o script `C:\Users\USER\.second_brain\scripts\repo_sync_engine.py` com suporte a clone resiliente, auto-pull e proteção cold snapshot contra deleções remotas.
- [x] **Tarefa 1.4:** Criar rotina agendada/background de sincronização periódica silenciosa (`schedule_auto_sync.ps1`).

### Fase 2: Download e Persistência Fria dos 25 Repositórios
- [x] **Tarefa 2.1 (Mídia & Diagramas):** Baixar e congelar `VoiceStudio`, `editonny`, `diagram-design`, `paperclip`.
- [x] **Tarefa 2.2 (Código & Engenharia Reversa):** Baixar e congelar `rea`, `ECC`, `vibe-coding-toolkit`, `andrej-karpathy-skills`, `superpowers`.
- [x] **Tarefa 2.3 (UI/UX):** Baixar e congelar `impeccable`.
- [x] **Tarefa 2.4 (Orquestração & Governança):** Baixar e congelar `ruflo`, `agentville`, `framework-5p`, `claude-plugins-official`.
- [x] **Tarefa 2.5 (Roteamento & Gateways):** Baixar e congelar `OmniRoute`, `freellmapi`.
- [x] **Tarefa 2.6 (Memória, Grafos & RAG):** Baixar e congelar `claude-mem`, `hindsight`, `graphify`.
- [x] **Tarefa 2.7 (Parsers, Scraping & Ciência):** Baixar e congelar `docling`, `ponytail`, `scientific-agent-skills`.
- [x] **Tarefa 2.8 (Cloud, Segurança & Integrações):** Baixar e congelar `security-audit-skill`, `Octop`, `nango`.

### Fase 3: Geração dos Manuais Universais (`AI_GUIDE.md`)
- [x] **Tarefa 3.1:** Gerar os 25 arquivos `AI_GUIDE.md` nos diretórios de cada repositório baixado, com instruções claras em português para usuário e prompts padronizados para agentes.
- [x] **Tarefa 3.2:** Validar conformidade para uso com Claude Code, Gemini CLI, Antigravity, Ollama, GLM e OpenAI.

### Fase 4: Auditoria e Catalogação dos Assets Existentes
- [x] **Tarefa 4.1:** Varrer e indexar as 47 skills, 20 agentes e 13 workflows já instalados em `.agents/`.
- [x] **Tarefa 4.2:** Criar `C:\Users\USER\.second_brain\knowledge\installed_assets_catalog.md` unificando todos os recursos nativos e recém-instalados.

### Fase 5: Conexão com Regras Centrais e `MASTER_INDEX.yaml`
- [x] **Tarefa 5.1:** Atualizar `MASTER_INDEX.yaml` com as novas rotas de intenção e índice de repositórios (`repositories_hub`).
- [x] **Tarefa 5.2:** Atualizar `global_rules.md` com a diretriz de economia de tokens por reuso do hub (Regra 12).

### Fase 6: Validação Empírica e Testes
- [x] **Tarefa 6.1:** Executar teste de sincronização do `repo_sync_engine.py` e simular cenário offline/repositório protegido.
- [x] **Tarefa 6.2:** Testar um wrapper de chamada (status, validação de arquivos e integridade de git).
- [x] **Tarefa 6.3:** Gerar relatório consolidado de auditoria no dashboard de métricas (`test_physical_implementation.py`).

---

## 🔒 Critérios de Conclusão (Done When)

1. Todos os 25 repositórios clonados e persistidos localmente em suas devidas pastas categorizadas.
2. Script `repo_sync_engine.py` funcional e testado com fallback cold snapshot.
3. Cada repositório possuindo seu `AI_GUIDE.md` completo, legível por qualquer modelo de IA.
4. Assets legados catalogados e integrados no catálogo mestre.
5. `MASTER_INDEX.yaml` e regras globais devidamente atualizados e roteando requisições para o hub.
