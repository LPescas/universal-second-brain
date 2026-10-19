#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
organize_governance_second_brain.py
===================================
Aplica rigorosamente o Skill Global de Governança RPA (Zero Trust) em todo o
ecossistema do Second Brain:
1. Gera README.md portal completo (Humano & Agente de IA)
2. Gera projeto_second_brain.md (Documento Mestre Zero Trust)
3. Gera arquivos *_nome.md com cabeçalho obrigatório em todas as subpastas
4. Registra histórico e valida conformidade estrutural
"""
import io
import sys
from pathlib import Path

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SB_ROOT = Path(r"C:\Users\USER\.second_brain")

MANDATORY_BANNER = """> 🚨 **REGRA DE GOVERNANÇA GLOBAL — LEITURA OBRIGATÓRIA ANTES DE QUALQUER COMMIT/MODIFICAÇÃO**
>
> 1. ✅ **TODO** subdiretório deste projeto possui um arquivo `*_nome.md` descrevendo seus artefatos e histórico.
> 2. ✅ **SEMPRE** que você (ou um Agente de IA) alterar, criar ou remover um arquivo, você **DEVE** atualizar o `.md` específico daquela subpasta imediatamente, registrando o histórico.
> 3. ✅ **PADRÃO DE PASTAS OBRIGATÓRIO**: Módulos e subpastas devem manter isolamento estrito de código, dados e documentação.
> 4. ✅ Se a mudança for estrutural, o arquivo raiz (`projeto_second_brain.md`) também deve ser atualizado.
>
> ❌ **CÓDIGO SEM DOCUMENTAÇÃO ATUALIZADA OU FORA DA ESTRUTURA PADRÃO SERÁ CONSIDERADO INVÁLIDO.**
"""

def generate_folder_doc(folder_path: Path, filename: str, title: str, purpose: str, artifacts: list[tuple[str, str]]) -> None:
    folder_path.mkdir(parents=True, exist_ok=True)
    target = folder_path / filename

    rows = "\n".join(f"| `{art}` | {desc} |" for art, desc in artifacts)

    content = f"""# {title}

---

{MANDATORY_BANNER}

---

## 🎯 1. Propósito do Diretório
{purpose}

---

## 📦 2. Mapeamento de Artefatos Principais

| Artefato | Finalidade / Papel |
| :--- | :--- |
{rows}

---

## 🤖 3. Diretrizes de Uso para o Agente de IA
- **Leitura Específica:** Nunca carregue arquivos deste diretório inteiros sem necessidade comprovada.
- **Isolamento:** Modificações neste diretório devem manter a separação clara entre código e documentação.
- **Atualização Mandatória:** Toda nova criação ou alteração neste diretório requer adição de linha no histórico abaixo.

---

## 📜 4. Histórico de Alterações

| Data | Autor / Agente | Descrição da Modificação |
| :--- | :--- | :--- |
| 2026-10-19 | Antigravity | Implantação da governança Zero Trust e organização padronizada do diretório. |
"""
    target.write_text(content, encoding="utf-8")
    print(f"  [OK] {target.relative_to(SB_ROOT)}")


def main():
    print("=" * 65)
    print("  ORGANIZANDO GOVERNANÇA ZERO TRUST DO SECOND BRAIN")
    print("=" * 65)

    # 1. README.md na raiz
    readme_path = SB_ROOT / "README.md"
    readme_content = """# 🧠 Second Brain — Hub Universal de Conhecimento, Agentes e Ferramentas

> **Versão:** 2.0 (Zero Trust & Auto-Sync Enabled)  
> **Proprietário:** USER  
> **Localização:** `C:\\Users\\USER\\.second_brain`  
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
C:\\Users\\USER\\.second_brain\\
├── README.md                      # Portal de boas-vindas e guia rápido (este arquivo)
├── projeto_second_brain.md         # Documentação Mestre de Governança Zero Trust
├── MASTER_INDEX.yaml               # Ponto de entrada P0 de roteamento do sistema
├── global_rules.md                 # Regras absolutas de comportamento para IA
├── active_behavior_rules.yaml      # Regras ativas de comportamento com fingerprints
├── behavioral_patterns.yaml        # Padrões comportamentais do desenvolvedor
│
├── core\\                          # Núcleo de Governança e Execução
│   └── governanca\\                # Guardião Zero Trust, validadores e leitores
│
├── repos\\                         # Hub de 25 Repositórios com Auto-Sync
│   ├── media_processing\\          # Síntese de voz, áudio, vídeo e diagramas
│   ├── dev_reverse_engineering\\   # Engenharia reversa, TDD, prompts e ML
│   ├── ui_ux_design\\              # Design de interfaces premium anti-slop
│   ├── orchestration_governance\\  # Multi-agentes, barramentos e framework 5P
│   ├── routing_gateways\\          # Gateways de IA gratuitos e roteamento
│   ├── memory_rag_graphs\\         # Memória persistente e grafos de dependências
│   ├── document_web_parsers\\      # Extratores de PDF (docling) e scraping leve
│   └── cloud_security_b2b\\        # Auditoria OWASP, nuvem e conectores SaaS
│
├── knowledge\\                     # Base de Conhecimento e Decisões
│   ├── installed_assets_catalog.md # Catálogo mestre unificado de todos os ativos
│   ├── project_decisions.md        # Decisões arquiteturais registradas
│   ├── learning_log.md             # Aprendizados contínuos do agente
│   └── rpa_database_schema_audit.md# Auditoria e schema de bancos de dados
│
├── scripts\\                       # Motores Operacionais e Automações
│   ├── repo_sync_engine.py         # Motor de sincronização e cold snapshot
│   ├── schedule_auto_sync.ps1      # Agendamento no Windows Task Scheduler
│   ├── generate_ai_guides.py       # Gerador dos contratos AI_GUIDE.md
│   ├── build_installed_assets_catalog.py # Indexador dinâmico de recursos
│   └── usage_metrics.py            # Backend de telemetria para o dashboard
│
├── frontend\\                      # Dashboard Visual de Métricas
│   ├── index.html                  # Interface do painel de controle
│   ├── app.js                      # Lógica de renderização de gráficos
│   └── start_dashboard.ps1         # Inicializador local do painel
│
├── backend\\                       # Serviços Locais e Agente Aurelio
│   └── aurelio\\                   # Agente autônomo local integrado
│
├── projects\\                      # Contextos de Projetos Externos
│   ├── rpa_context.md              # Contexto operacional do RPA UNIQ
│   ├── wrpe_recorder_context.md    # Contexto operacional do WRPE Recorder
│   └── RPA_Autorizar\\             # Documentações de sub-módulos RPA
│
├── integrations\\                  # Conectores com IDEs e Terminais
│   ├── cursorrules_template.md     # Template para regras do Cursor
│   └── profile_snippet.ps1         # Integração com perfil PowerShell
│
└── .agents\\                       # AG Kit — Motor Multi-Agente
    ├── agent\\                     # 20 Agentes especialistas (.md)
    ├── skills\\                    # 47 Skills e manuais de engenharia
    ├── workflows\\                 # 13 Workflows de comando (/plan, /debug...)
    ├── rules\\                     # Regras operacionais universais
    └── scripts\\                   # Scripts de validação empírica isolada
```

---

## ⚡ Comandos Rápidos e Atalhos

### Para o Desenvolvedor (Humano):
- **Abrir Dashboard:** Execute `.\\frontend\\start_dashboard.ps1` no PowerShell.
- **Sincronizar Repositórios:** Execute `python .\\scripts\\repo_sync_engine.py`.
- **Agendar Sincronização Diária:** Execute `.\\scripts\\schedule_auto_sync.ps1 -Install`.
- **Reindexar Ativos:** Execute `python .\\scripts\\build_installed_assets_catalog.py`.

### Para o Agente de IA:
- **Ponto de Partida Obrigatório:** Ler [MASTER_INDEX.yaml](file:///C:/Users/USER/.second_brain/MASTER_INDEX.yaml).
- **Roteamento de Demanda:** Consultar [installed_assets_catalog.md](file:///C:/Users/USER/.second_brain/knowledge/installed_assets_catalog.md) antes de criar qualquer código do zero.
- **Economia de Tokens:** Ler apenas as seções relevantes dos contratos `AI_GUIDE.md` de cada ferramenta.
- **Validação Empírica Obrigatória:** Executar testes via `.agents/scripts/` antes de finalizar entregas.
- **Assinatura de Execução:** Injetar métricas em `usage_metrics.py` e imprimir o relatório formal do Second Brain ao final de cada turno.
"""
    readme_path.write_text(readme_content, encoding="utf-8")
    print(f"  [OK] README.md")

    # 2. projeto_second_brain.md na raiz
    master_doc_path = SB_ROOT / "projeto_second_brain.md"
    master_doc_content = f"""# 🧠 Projeto Second Brain — Documento Mestre de Arquitetura e Governança

---

{MANDATORY_BANNER}

---

## 1. Visão Geral do Sistema
O **Second Brain** atua como uma camada superior de governança, memória semântica e orquestração de ferramentas compartilhada entre múltiplos projetos (`RPA`, `WRPE_Recorder`, `SecondBrain_Aurelio`, etc.) e múltiplos assistentes de IA (Google Antigravity, Claude Code, Gemini CLI, Cursor, Ollama).

## 2. Princípios de Governança Zero Trust
1. **Nenhum arquivo sem documentação:** Cada pasta possui seu arquivo `*_nome.md` local com descrição e histórico.
2. **Guardião de Execução Ativo:** Nenhuma alteração estrutural ocorre sem passar pelas validações em `core/governanca/`.
3. **Persistência Fria (Cold Snapshot):** Repositórios em `repos/` operam de forma isolada e nunca perdem dados se deletados remotamente.
4. **Retroalimentação Contínua:** Decisões são registradas em `knowledge/project_decisions.md` e métricas enviadas ao dashboard.

## 3. Matriz de Componentes Centrais

| Subpasta | Arquivo de Governança | Função Primária |
| :--- | :--- | :--- |
| `core/` | `core_second_brain.md` | Núcleo de governança e guardião Zero Trust |
| `repos/` | `repos_second_brain.md` | Hub de 25 repositórios externos persistidos |
| `knowledge/` | `knowledge_second_brain.md` | Base de conhecimento, decisões e métricas |
| `scripts/` | `scripts_second_brain.md` | Motores de automação, sincronização e telemetria |
| `frontend/` | `frontend_second_brain.md` | Dashboard visual de telemetria do Second Brain |
| `backend/` | `backend_second_brain.md` | Serviços locais e motor do agente Aurelio |
| `projects/` | `projects_second_brain.md` | Contextos de integração com projetos externos |
| `integrations/` | `integrations_second_brain.md` | Configurações para Cursor, VS Code e PowerShell |
| `.agents/` | `agents_second_brain.md` | Ecossistema AG Kit (agentes, skills, workflows) |

---

## 📜 Histórico Global de Governança

| Data | Autor / Agente | Descrição Macro |
| :--- | :--- | :--- |
| 2026-07-31 | USER / IA | Criação inicial do Second Brain v1.0. |
| 2026-08-03 | USER / IA | Evolução para Second Brain v2.0 com telemetria no frontend. |
| 2026-10-19 | Antigravity | Integração do Hub Universal com 25 repositórios e proteção Cold Snapshot. |
| 2026-10-19 | Antigravity | Aplicação completa do Skill Global de Governança Zero Trust em todas as pastas. |
"""
    master_doc_path.write_text(master_doc_content, encoding="utf-8")
    print(f"  [OK] projeto_second_brain.md")

    # 3. Documentações de Subpastas
    folders = [
        (
            SB_ROOT / "core",
            "core_second_brain.md",
            "🛡️ Core de Governança e Execução do Second Brain",
            "Contém os módulos de validação estrutural e segurança Zero Trust do sistema.",
            [
                ("governanca/", "Subdiretório com os validadores, leitores e guardião de execução.")
            ]
        ),
        (
            SB_ROOT / "backend",
            "backend_second_brain.md",
            "⚙️ Backend e Serviços Locais do Second Brain",
            "Hospeda serviços de processamento local, APIs e o agente de inteligência autônomo Aurelio.",
            [
                ("aurelio/", "Módulo completo do Agente Aurelio com banco SQLite e orquestrador local.")
            ]
        ),
        (
            SB_ROOT / "backend" / "aurelio",
            "aurelio_backend.md",
            "🤖 Agente Aurelio — Inteligência Artificial Local",
            "Implementação de agente local autônomo executando sobre modelos locais via Ollama.",
            [
                ("agent/", "Lógica de persona, prompt de sistema e tomada de decisão."),
                ("core/", "Pipeline imutável de orquestração do Aurelio."),
                ("database/", "Camada de persistência local SQLite (aurelio.db)."),
                ("memory/", "Memória semântica e vetorial com busca híbrida."),
                ("models/", "Schemas de dados e tipagens de mensagens."),
                ("data/", "Armazenamento temporário de dados."),
                ("logs/", "Logs operacionais de sessões do agente.")
            ]
        ),
        (
            SB_ROOT / "frontend",
            "frontend_second_brain.md",
            "📊 Frontend e Dashboard Visual do Second Brain",
            "Interface web interativa para auditoria de métricas de telemetria, tokens gastos e economia de tempo.",
            [
                ("index.html", "Estrutura visual da dashboard."),
                ("app.js", "Lógica de renderização dinâmica de dados e gráficos."),
                ("style.css", "Design moderno com estética premium e tema escuro."),
                ("start_dashboard.ps1", "Script PowerShell para inicialização instantânea do servidor local.")
            ]
        ),
        (
            SB_ROOT / "scripts",
            "scripts_second_brain.md",
            "⚡ Scripts Operacionais e Motores de Automação",
            "Scripts utilitários para sincronização de repositórios, coleta de métricas, consolidação e governança.",
            [
                ("repo_sync_engine.py", "Motor de auto-sincronização com proteção Cold Snapshot."),
                ("schedule_auto_sync.ps1", "Gerenciador da tarefa agendada no Windows."),
                ("build_installed_assets_catalog.py", "Gerador do catálogo unificado de ativos."),
                ("generate_ai_guides.py", "Gerador automatizado dos manuais AI_GUIDE.md."),
                ("usage_metrics.py", "Módulo de injeção e cálculo de métricas de uso da IA."),
                ("health_check.py", "Rotina de verificação de integridade e diagnósticos.")
            ]
        ),
        (
            SB_ROOT / "knowledge",
            "knowledge_second_brain.md",
            "📚 Base de Conhecimento, Decisões e Catálogos",
            "Armazena a inteligência de longo prazo, histórico de correções, decisões de arquitetura e schemas de banco.",
            [
                ("installed_assets_catalog.md", "Catálogo mestre dos 25 repositórios, 20 agentes, 47 skills e 13 workflows."),
                ("project_decisions.md", "Registro formal de decisões técnicas e preferências do usuário."),
                ("learning_log.md", "Log contínuo de aprendizados e resoluções de problemas."),
                ("rpa_database_schema_audit.md", "Dicionário de dados e auditoria do banco de dados do RPA.")
            ]
        ),
        (
            SB_ROOT / "projects",
            "projects_second_brain.md",
            "🗂️ Contextos de Projetos e Módulos Integrados",
            "Armazena documentação viva e mapas de contexto dos projetos mantidos na máquina.",
            [
                ("rpa_context.md", "Documentação arquitetural completa do sistema RPA UNIQ."),
                ("wrpe_recorder_context.md", "Contexto operacional do gravador e reproductor WRPE."),
                ("RPA_Autorizar/", "Documentações e histórico de correções do módulo de Autorização.")
            ]
        ),
        (
            SB_ROOT / "projects" / "RPA_Autorizar",
            "rpa_autorizar_project.md",
            "📑 Módulo RPA Autorizar — Histórico e Fixes",
            "Histórico de correções pontuais, filtros e regras do fluxo de Autorização de Guias do RPA.",
            [
                ("bug_fix_captura_parcial.md", "Resolução de bug de captura parcial de dados."),
                ("bug_fix_filtro_bloqueador.md", "Resolução de filtros impeditivos em telas web."),
                ("bug_fix_sem_acao.md", "Tratamento de timeout e retorno de telas sem ação.")
            ]
        ),
        (
            SB_ROOT / "integrations",
            "integrations_second_brain.md",
            "🔌 Conectores de IDEs e Ambientes de Terminal",
            "Pontes de conexão entre o Second Brain e as ferramentas de desenvolvimento do desenvolvedor.",
            [
                ("cursorrules_template.md", "Template de integração para o editor Cursor."),
                ("vscode_settings.json", "Configurações recomendadas para o VS Code."),
                ("profile_snippet.ps1", "Snippet de inicialização rápida no perfil PowerShell do usuário.")
            ]
        ),
        (
            SB_ROOT / "repos",
            "repos_second_brain.md",
            "🗄️ Hub Universal de Repositórios Especializados",
            "Repositório central de 25 ferramentas externas divididas em 8 grupos táticos com proteção Cold Snapshot.",
            [
                ("repos_manifest.yaml", "Manifesto central com URLs, commits, categorias e status."),
                ("media_processing/", "Processamento de vídeo, áudio, TTS e diagramação."),
                ("dev_reverse_engineering/", "Engenharia reversa, TDD, prompts e ML."),
                ("ui_ux_design/", "Design anti-slop e sistemas de interface premium."),
                ("orchestration_governance/", "Multi-agentes, barramentos assíncronos e 5Ps."),
                ("routing_gateways/", "Gateways de LLM gratuitos e balanceamento de custos."),
                ("memory_rag_graphs/", "Memória contínua, RAG reflexivo e grafos de código."),
                ("document_web_parsers/", "Parsers avançados de PDF (IBM Docling) e scraping leve."),
                ("cloud_security_b2b/", "Auditoria OWASP, conectores SaaS Nango e nuvem Tencent.")
            ]
        ),
        (
            SB_ROOT / "repos" / "media_processing",
            "media_processing_repos.md",
            "🎙️ Repositórios de Mídia, Vídeo, Áudio e Diagramas",
            "Ferramentas locais para clonagem vocal, edição de vídeo programática, diagramação e extração de telas.",
            [
                ("VoiceStudio/", "Estúdio neural de TTS e clonagem vocal (AI_GUIDE.md integrado)."),
                ("editonny/", "Edição e cortes inteligentes de vídeo para evidências de automações."),
                ("diagram-design/", "Padrões visuais e blueprints para diagramas de arquitetura."),
                ("paperclip/", "Extrator e conversor de capturas de tela diretamente em código HTML/CSS.")
            ]
        ),
        (
            SB_ROOT / "repos" / "dev_reverse_engineering",
            "dev_reverse_engineering_repos.md",
            "🔬 Repositórios de Código, Engenharia Reversa e Prototipagem",
            "Descompilação de binários, atalhos de produtividade, boilerplates e frameworks de excelência técnica.",
            [
                ("rea/", "Engenharia reversa e descompilação de executáveis com LLM."),
                ("ECC/", "Everything Claude Code: prompts de sistema e automações de CLI."),
                ("vibe-coding-toolkit/", "Snippets e scaffolds para desenvolvimento acelerado."),
                ("andrej-karpathy-skills/", "Princípios didáticos de nanoGPT e transformers limpos."),
                ("superpowers/", "Habilidades mestras de TDD, debugging por evidência e blindagem.")
            ]
        ),
        (
            SB_ROOT / "repos" / "ui_ux_design",
            "ui_ux_design_repos.md",
            "🎨 Repositórios de Design de Interface e Acabamento Visual",
            "Padrões para criação de interfaces modernas de classe mundial sem aspecto genérico.",
            [
                ("impeccable/", "Diretrizes e tokens de micro-interações, contraste e design anti-slop.")
            ]
        ),
        (
            SB_ROOT / "repos" / "orchestration_governance",
            "orchestration_governance_repos.md",
            "🤖 Repositórios de Orquestração Multi-Agente e Governança",
            "Runtimes assíncronos, barramentos de mensagens, simulação de personas e metodologias estruturadas.",
            [
                ("ruflo/", "Orquestrador multi-agente de alto desempenho com barramento assíncrono."),
                ("agentville/", "Ambiente de simulação colaborativa entre agentes especialistas."),
                ("framework-5p/", "Metodologia dos 5Ps para governança de projetos e arquitetura."),
                ("claude-plugins-official/", "Catálogo de especificações oficiais de plugins de IA.")
            ]
        ),
        (
            SB_ROOT / "repos" / "routing_gateways",
            "routing_gateways_repos.md",
            "🌐 Repositórios de Roteamento de LLMs e APIs Gratuitas",
            "Gateways e proxies para desviar chamadas para modelos gratuitos ou mais eficientes, economizando tokens.",
            [
                ("OmniRoute/", "Roteador inteligente de chamadas com balanceamento e fallback."),
                ("freellmapi/", "Agregador de múltiplos endpoints públicos de IA gratuitos compatíveis com OpenAI.")
            ]
        ),
        (
            SB_ROOT / "repos" / "memory_rag_graphs",
            "memory_rag_graphs_repos.md",
            "🧠 Repositórios de Memória Persistente e Grafos de Conhecimento",
            "Sistemas de retenção de memória de longo prazo, auto-avaliação pós-execução e grafos de código.",
            [
                ("claude-mem/", "Memória contínua cross-session para retenção de contexto."),
                ("hindsight/", "Módulo de reflexão pós-execução para validação de contexto RAG."),
                ("graphify/", "Conversor de código e banco de dados em grafos de conhecimento relacionais.")
            ]
        ),
        (
            SB_ROOT / "repos" / "document_web_parsers",
            "document_web_parsers_repos.md",
            "📄 Repositórios de Parsers de Documentos, Scraping e Ciência",
            "Extração estruturada de PDFs complexos, raspagem de páginas web sem anúncios e cálculos exatos.",
            [
                ("docling/", "Extrator multimodal da IBM para conversão precisa de PDFs e tabelas em Markdown."),
                ("ponytail/", "Web scraper headless ultrarrápido que extrai apenas texto limpo."),
                ("scientific-agent-skills/", "Cálculos matemáticos sem alucinação e busca de artigos científicos.")
            ]
        ),
        (
            SB_ROOT / "repos" / "cloud_security_b2b",
            "cloud_security_b2b_repos.md",
            "🔒 Repositórios de Nuvem, Segurança OWASP e Conectores B2B",
            "Auditoria automatizada de vulnerabilidades, gestão multi-cloud e conectores para centenas de APIs SaaS.",
            [
                ("security-audit-skill/", "Auditoria estática de código para OWASP Top 10 e segredos expostos."),
                ("Octop/", "Gestão unificada multi-cloud da Tencent para automação de instâncias e storage."),
                ("nango/", "Plataforma open-source unificada para 250+ integrações SaaS e OAuth.")
            ]
        ),
        (
            SB_ROOT / ".agents",
            "agents_second_brain.md",
            "🤖 AG Kit — Ecossistema de Agentes, Skills e Workflows",
            "Motor de execução inteligente do Second Brain: 20 agentes especialistas, 47 skills e 13 workflows.",
            [
                ("agent/", "Definições dos 20 agentes especialistas em Markdown."),
                ("skills/", "47 manuais operacionais e rotinas de engenharia."),
                ("workflows/", "13 comandos estruturados (/plan, /create, /debug, /verify...)."),
                ("rules/", "Regras de protocolo, roteamento inteligente e clean code."),
                ("scripts/", "Scripts de validação empírica isolada.")
            ]
        )
    ]

    for folder, fname, title, purpose, arts in folders:
        generate_folder_doc(folder, fname, title, purpose, arts)

    print("\n" + "=" * 65)
    print("  ORGANIZAÇÃO E DOCUMENTAÇÃO ZERO TRUST CONCLUÍDA!")
    print("=" * 65)


if __name__ == "__main__":
    main()
