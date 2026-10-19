# ⚡ Scripts Operacionais e Motores de Automação

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

## 🎯 1. Propósito do Diretório
Scripts utilitários para sincronização de repositórios, coleta de métricas, consolidação e governança.

---

## 📦 2. Mapeamento de Artefatos Principais

| Artefato | Finalidade / Papel |
| :--- | :--- |
| `repo_sync_engine.py` | Motor de auto-sincronização com proteção Cold Snapshot. |
| `schedule_auto_sync.ps1` | Gerenciador da tarefa agendada no Windows. |
| `build_installed_assets_catalog.py` | Gerador do catálogo unificado de ativos. |
| `generate_ai_guides.py` | Gerador automatizado dos manuais AI_GUIDE.md. |
| `usage_metrics.py` | Módulo de injeção e cálculo de métricas de uso da IA. |
| `health_check.py` | Rotina de verificação de integridade e diagnósticos. |

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
