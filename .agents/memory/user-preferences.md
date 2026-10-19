---
type: user
created: 2026-07-18
updated: 2026-10-19
owner: USER
---

# Perfil & Preferências Duráveis do Desenvolvedor (Second Brain)

Este documento registra como o usuário desta máquina prefere que os agentes de IA trabalhem, pensem, codifiquem e se comuniquem. O Second Brain consulta e retroalimenta automaticamente este arquivo em cada interação.

---

## 1. Comunicação e Estilo de Explicação
- **Idioma de Comunicação:** Português do Brasil (pt-BR) fluente e natural.
- **Tom e Nível:** Sênior, pragmático, direto ao ponto. Sem preâmbulos genéricos, sem apologias ou introduções vazias como "Com certeza!", "Como uma IA...".
- **Sem Explicações Básicas:** Não explicar o que é uma variável, como funciona o git clone ou conceitos elementares, a menos que seja explicitamente solicitado.
- **Estrutura de Resposta Preferida:**
  1. Ação / Resolução imediata com impacto direto.
  2. Código conciso pronto para uso.
  3. Comprovação empírica ou logs de validação.

---

## 2. Padrões de Código e Desenvolvimento
- **Linguagem Principal:** Python 3.10+ para automações, APIs e lógica de backend.
- **Frontend:** Vanilla HTML5, Vanilla CSS3 e JavaScript ES6+ moderno, sem inchar dependências desnecessárias (Node/NPM apenas quando estritamente requisitado).
- **Idioma do Código:** Código-fonte, variáveis, nomes de funções, classes, schemas de banco e comentários técnicos DEVEM ser em **Inglês** (Clean Code).
- **Filosofia Clean Code:** Código conciso, direto, sem duplicação de lógica, sem abstrações prematuras ou over-engineering.
- **Tratamento de Exceções:** Captura de exceções específicas, logs detalhados e nunca `except:` genérico silencioso.
- **Proibições Rígidas:**
  - Proibido uso de `print()` em código de produção (usar sempre o logger estruturado do sistema).
  - Proibido expor credenciais ou chaves de API fora de arquivos `.env` protegidos.
  - Proibido hardcode de caminhos de drivers (ex: ChromeDriver) ou portas sem parametrização.

---

## 3. Diretrizes Específicas por Projeto

### A. Automação Corporativa RPA (`C:/Projetos/RPA`)
- **Arquitetura UNIQ Hub & Spoke:** Frontend Flask desacoplado de robôs executores.
- **Execução Standalone:** Todo robô deve poder rodar via seu `main_<rpa>.py` sem depender do Flask.
- **Driver Selenium:** Inicialização EXCLUSIVA via `Backend/Global/servicos/driver.py::start_session()`.
- **6 Pastas Canônicas:** `codigo`, `documentacao`, `logs`, `dados`, `configuracoes`, `executaveis`.
- **Governança de Banco:** Toda alteração ou acréscimo de tabela DEVE sincronizar imediatamente:
  - `C:\Projetos\Guia_Simplificado_Sistema_RPA.docx`
  - `C:\Users\USER\.second_brain\knowledge\rpa_database_schema_audit.md`
- **Arquivos Protegidos:** Intocáveis sem aprovação direta (preservados em `arquivos_intocaveis_rpa.md`).

### B. WRPE Recorder (`C:/Projetos/WRPE_Recorder`)
- **Stack:** Playwright, Selenium, extensão Chrome, SQLite.
- **Foco:** Gravação e replay de ações web com captura precisa de eventos e seletores robustos.

### C. Second Brain & Aurélio AI (`C:/Users/USER/.second_brain`)
- **Arquitetura:** Hub central de memória, 25 repositórios especializados, grafos de conhecimento e Ollama local.
- **Governança:** Leitura obrigatória de `MASTER_INDEX.yaml` no boot, confirmação visual de carregamento, e injeção de telemetria com relatório final ao encerrar.
- **Proteção Cold Snapshot:** Cópias clonadas mantidas travadas localmente para garantia de persistência.

---

## 4. UI/UX e Frontend Design
- **Estética:** Visual moderno, premium, escuro (Dark Mode HSL de alta fidelidade), sem paletas roxas genéricas de IA (Purple Ban).
- **Tipografia:** Google Fonts (Inter para interface, JetBrains Mono para código e dados técnicos).
- **Microinterações:** Efeitos hover sutis, transições CSS fluidas (150-250ms), feedback de carregamento em requisições assíncronas.
- **Contraste:** Alto contraste sem poluição visual.

---

## 5. Histórico de Retroalimentação Automática
- *19/10/2026:* Consolidação das preferências de desenvolvimento, criação do painel de inspeção de conhecimento e ativação do seletor de 8 personas no Aurélio AI.
- *Agosto 2026:* Padronização de endpoints de histórico e consolidação de saídas de automação em CSV/JSON.
- *Julho 2026:* Definição das regras de Zero Trust e inicialização da arquitetura Hub & Spoke.
