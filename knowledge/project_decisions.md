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

### [Second Brain] Implantação do Skill Global de Governança RPA (Zero Trust) em todo o Ecossistema
**Pergunta original:** Agora utilize todos os recursos do second brain, e o governancia de skill global para organizar o projeto .second_brain de maneira limpa para o agente de ia e o usuario ter todos os recursos, pastas, codigos e etc organizados na sua maquina.
**Resposta do Usuário:** Solicitação de aplicação total da governança, documentação e organização limpa.
**Decisão Arquitetural Consolidada:** Foi estabelecida uma camada de governança Zero Trust estrutural completa para o próprio Second Brain: (1) Criação do `README.md` como portal visual para o usuário humano e atalhos para agentes; (2) Criação do `projeto_second_brain.md` como documento mestre de arquitetura; (3) Módulo `core/governanca/` com o Guardião de Execução (`guardiao_execucao.py`), Validador (`validador_regras.py`) e Leitor (`leitor_documentacao.py`); (4) Documentação Zero Trust obrigatória (`*_nome.md`) em 100% das subpastas e categorias; (5) Teste empírico automatizado em `.agents/scripts/test_second_brain_governance.py` aprovado com 5/5 testes verdes.
**Data:** 2026-10-19


