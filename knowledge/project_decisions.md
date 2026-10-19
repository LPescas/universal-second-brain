# 🗂️ Registro de Decisões e Questões Essenciais (Project Decisions)

> **Objetivo:** Este arquivo funciona como a memória de longo prazo para todas as perguntas arquiteturais, de design e segurança já respondidas pelo usuário. 
> **Regra:** ANTES de fazer qualquer "Pergunta Essencial" ao usuário durante a fase de planejamento (Planner), o agente DEVE consultar este arquivo. Se a resposta já existir aqui, aplique-a silenciosamente sem gastar tokens com novas perguntas.

---

## 🏛️ Arquitetura (Architecture)

### [Second Brain] Captura de Duração de Processo
**Pergunta original:** Como capturar o tempo que a IA ficou processando para exibir "Média de tempo de uso com SB"?
**Resposta do Usuário:** A IA deve enviar o tempo estimado em segundos/minutos toda vez que finalizar a tarefa. Não usar cálculo automático por diferença de chamadas.
**Data:** 2026-08-03

### [Second Brain] Formato Visual de Eficiência
**Pergunta original:** Qual formato visual para o indicador de eficiência? (100k tokens/minuto vs nota 8.5/10)
**Resposta do Usuário:** Usar formato `100k tokens / minuto` (throughput real, não nota abstrata).
**Data:** 2026-08-03

### [Second Brain] Cálculo Base "Sem Second Brain"
**Pergunta original:** Como calcular matematicamente o gasto estimado sem o Second Brain?
**Resposta do Usuário:** Pesquisar a média real de gastos de agentes de IA sem sistema de memória persistente e usar como base de comparação. Não inventar números — basear em dados reais ou estimativas fundamentadas.
**Data:** 2026-08-03

### [Second Brain] Métricas do Dashboard — Modelo de Dados
**Pergunta original:** As métricas devem mostrar "tokens economizados" ou "tokens gastos"?
**Resposta do Usuário:** Tokens GASTOS (reais). Não é possível saber com precisão quanto seria gasto sem SB, então o dashboard deve mostrar gastos reais por processo. O "Antes vs Depois" usa uma média estimada baseada em pesquisa de mercado para comparação.
**Data:** 2026-08-03

### [Second Brain] Hub Universal de Repositórios, Cold Snapshot e Agnosticismo de IA
**Pergunta original / Diretriz:** Como estruturar os 25 repositórios externos e assets existentes no Second Brain para uso multi-agente?
**Decisão do Usuário / Arquitetura:**
1. Todos os 25 repositórios devem ser clonados localmente em `repos/` categorizados por grupo e mantidos em modo Cold Snapshot resiliente (não perde a funcionalidade se o repo for deletado/privatizado no GitHub).
2. Auto-sincronização automática e silenciosa via engine sem solicitação manual do usuário.
3. Compatibilidade universal estrita: qualquer agente (Claude Code, Gemini, GLM, Ollama, Antigravity, etc.) deve conseguir acionar e entender os recursos via `AI_GUIDE.md` padronizado.
4. Redução de tokens e retroalimentação mandatórias no fluxo do Second Brain.
**Data:** 2026-10-19

---

## 🎨 Design e Frontend (UI/UX)

### [Second Brain Dashboard] Gráfico de Timeline
**Pergunta original:** O gráfico principal deve ser por dia (calendário) ou por sessão?
**Resposta do Usuário:** Por sessão — mostrar as últimas 30 sessões, não os últimos 30 dias do calendário.
**Data:** 2026-08-03

---

## 🔒 Segurança (Security)

---

## ⚙️ Regras de Negócio e Comportamento (Business/Behavior)

### [Second Brain] Métricas Nunca Devem Mentir
**Pergunta original:** Podemos usar estimativas para métricas do dashboard?
**Resposta do Usuário:** "NAO PODE MENTIR NOS NUMEROS POIS ISSO É UM PROJETO TOTALMENTE IMPORTANTE E NAO PODE CONTER ERROS." Dados devem ser reais e verificáveis. O único campo estimado permitido é o "Sem Second Brain" do comparativo Antes/Depois, que deve ser baseado em pesquisa real.
**Data:** 2026-08-03

### [Second Brain] Hub Universal de 25 Repositórios com Proteção Cold Snapshot Implementado Fisicamente
**Pergunta original:** Pode iniciar a implementação física e verifique se está tudo funcionando corretamente?
**Resposta do Usuário:** Autorização para execução física de todos os 25 repositórios, engine de auto-sync, manuais AI_GUIDE.md e catálogo integrado.
**Decisão Arquitetural Consolidada:** Os 25 repositórios foram clonados localmente na raiz categorizada `C:\Users\USER\.second_brain\repos\`. Todos possuem seus manuais `AI_GUIDE.md` para compatibilidade universal com qualquer modelo de IA. O motor `repo_sync_engine.py` mantém proteção Cold Snapshot (nenhum arquivo local é deletado se o repo remoto se tornar privado ou for excluído). O catálogo mestre em `knowledge/installed_assets_catalog.md` e o `MASTER_INDEX.yaml` foram atualizados e validados com 100% de sucesso empírico via script em `.agents/scripts/test_physical_implementation.py`.
**Data:** 2026-10-19

### [Second Brain] Repositório Git Público e Visualizador do Grafo de Conhecimento no Frontend
**Pergunta original / Diretriz:** Agora organize um repositorio no meu git explicando todo esse processo para qualquer usuario colocar esse second brain na sua maquina, explique quais repositorios foram colocados nesse projeto, atualizações e tudo mais pode deixar publico, coloque ele em ingles e explique como utilizar e como no frontend voce consegue verificar e utilizar muitos desses repositorios e verificar eles funcionando de forma visual no frontend direto da sua maquina, como a pagina de grafos e etc.
**Resposta do Usuário:** Publicação completa em repositório Git, documentação global em inglês, mapeamento dos 25 repositórios e visualização interativa do ecossistema no Frontend.
**Decisão Arquitetural Consolidada:** 
1. **Git Repository & Submódulos**: Inicializado o repositório Git em `C:\Users\USER\.second_brain\`, licença MIT (`LICENSE`), `.gitignore` cobrindo bytecodes, arquivos de banco SQLite e logs de sessão. Todos os 25 repositórios do Hub foram mapeados em `.gitmodules` com seus links upstream oficiais, permitindo navegação limpa no GitHub e compatibilidade total com Git.
2. **Documentação Universal em Inglês**: Elaborado o `README.md` abrangente em inglês detalhando a arquitetura Hub & Spoke, catálogo dos 25 repositórios divididos em 8 categorias, guia de instalação rápida em 5 passos, motor de auto-sync em background e protocolo de consumo semântico por agentes de IA. A documentação nativa em português foi preservada em `README_PT.md`.
3. **Frontend Grafo Interativo 60fps**: Desenvolvido motor de física force-directed no HTML5 Canvas (`#graph-canvas`) para navegação em tempo real por nós e arestas do Second Brain (Core, Categorias, 25 Ferramentas e Projetos), com recursos de arrastar nós, centralização dinâmica, pausa física e painel inspetor de detalhes técnicos.
4. **Hub de Ferramentas & Modal AI_GUIDE**: Criada a aba de exploração de ferramentas com filtros de categoria por pills, busca em tempo real e visualizador modal para inspeção direta dos contratos `AI_GUIDE.md`.
5. **Automação & Validação Empírica**: Criado o script `scripts/export_frontend_hub_data.py` (integrado ao launcher `start_dashboard.ps1`) para gerar os datasets `repos_data.json` e `graph_data.json`. Aprovados 100% dos testes em `.agents/scripts/test_git_and_frontend_hub.py` (3/3), `test_second_brain_governance.py` (5/5) e `test_physical_implementation.py` (7/7).
**Data:** 2026-10-19


