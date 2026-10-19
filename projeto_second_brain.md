# 🧠 Projeto Second Brain — Documento Mestre de Arquitetura e Governança

---

> 🚨 **REGRA DE GOVERNANÇA GLOBAL — LEITURA OBRIGATÓRIA ANTES DE QUALQUER COMMIT/MODIFICAÇÃO**
>
> 1. ✅ **TODO** subdiretório deste projeto possui um arquivo `*_nome.md` descrevendo seus artefatos e histórico.
> 2. ✅ **SEMPRE** que você (ou um Agente de IA) alterar, criar ou remover um arquivo, você **DEVE** atualizar o `.md` específico daquela subpasta imediatamente, registrando o histórico.
> 3. ✅ **PADRÃO DE PASTAS OBRIGATÓRIO**: Módulos e subpastas devem manter isolamento estrito de código, dados e documentação.
> 4. ✅ Se a mudança for estrutural, o arquivo raiz (`projeto_second_brain.md`) também deve ser atualizado.
>
> ❌ **CÓDIGO SEM DOCUMENTAÇÃO ATUALIZADA OU FORA DA ESTRUTURA PADRÃO SERÁ CONSIDERADO INVÁLIDO.**


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
