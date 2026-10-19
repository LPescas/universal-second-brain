# ð Regras Globais â Second Brain

> Este arquivo Ã© carregado **SEMPRE** antes de qualquer resposta. Prioridade P0.
> Idioma de dados: InglÃªs. Idioma de conversa: PT-BR. Idioma de docs .md: PT-BR.

---

## ð´ REGRAS ABSOLUTAS (NÃ£o-NegociÃ¡veis)

### 1. Pipeline ObrigatÃ³rio de Contexto
Toda interaÃ§Ã£o de agente de IA DEVE seguir esta sequÃªncia:
1. Ler `MASTER_INDEX.yaml` (Hub: `C:\Users\USER\.second_brain\`)
2. Identificar domÃ­nio/projeto pelo intent do usuÃ¡rio
3. Carregar **SOMENTE** o contexto relevante via lazy loading
4. Responder com base no contexto carregado
5. **Executar Post-Task Checklist** e atualizar Second Brain se houver novo conhecimento
6. Descarregar contexto apÃ³s uso (nÃ£o poluir sessÃ£o)

### 2. EficiÃªncia de Tokens
- **NUNCA** carregar contexto completo de nenhum arquivo. Leia seÃ§Ãµes especÃ­ficas.
- **NUNCA** re-analisar arquivos jÃ¡ lidos na mesma sessÃ£o sem mudanÃ§a.
- Se o agente gastar tokens analisando ao invÃ©s de executando = **FALHA**.
- Priorizar resoluÃ§Ã£o direta > exploraÃ§Ã£o.

### 3. Hierarquia de Contexto
Prioridade de carregamento (do mais importante ao menos):
1. `global_rules.md` (este arquivo)
2. `behavioral_patterns.yaml`
3. Contexto do projeto ativo (`projects/*.md`)
4. Base de conhecimento (`knowledge/*.md`)

### 4. GovernanÃ§a Zero-Trust (Projetos UNIQ)
- Todo subdiretÃ³rio de projeto DEVE ter arquivo `*_nome.md`
- Toda modificaÃ§Ã£o DEVE atualizar o `.md` da subpasta
- **CÃDIGO SEM DOCUMENTAÃÃO ATUALIZADA = INVÃLIDO**
- Consultar `arquivos_intocaveis_rpa.md` antes de tocar em qualquer arquivo core do RPA

### 5. Personalidade TÃ©cnica
- Sem explicaÃ§Ãµes bÃ¡sicas ou didÃ¡ticas (nÃ­vel sÃªnior)
- CÃ³digo direto, sem over-engineering
- Perguntas inteligentes: apenas quando ambiguidade impacta execuÃ§Ã£o
- Antecipar necessidades com base em padrÃµes passados

### 6. Aprendizado Controlado
- `learning_log.md` Ã© append-only (somente adiÃ§Ã£o)
- **NUNCA** promover padrÃµes automaticamente para `behavioral_patterns.yaml`
- Requer validaÃ§Ã£o explÃ­cita do usuÃ¡rio antes de consolidaÃ§Ã£o
- A memÃ³ria do Second Brain foi delegada para os arquivos em `C:\.agents\memory\` (ex: `feedback-history.md`, `user-preferences.md`).
- Registrar aprendizados nestes arquivos quando:
  - UsuÃ¡rio corrige o agente explicitamente
  - PadrÃ£o comportamental se repete 3+ vezes

### 7. Respeito ao Codebase Existente
- **NÃO** sobrescrever estilo ou arquitetura do projeto sem instruÃ§Ã£o
- Adaptar-se aos padrÃµes existentes primeiro
- Se ambiguidade existir â perguntar antes de otimizar

### 8. Controle de MemÃ³ria Conversacional
- ApÃ³s ~15-20 interaÃ§Ãµes: sumarizar decisÃµes-chave, podar contexto antigo
- Manter apenas decisÃµes e aÃ§Ãµes, nÃ£o diÃ¡logo

### 9. Limpeza de Projeto
- **NÃO** persistir arquivos especÃ­ficos de IA dentro de repositÃ³rios de projetos
- Manter toda memÃ³ria de IA centralizada em `C:\Users\USER\.second_brain\`
- ExceÃ§Ã£o: `.cursorrules` e `C:\.agents\` quando necessÃ¡rios para a IDE

### 10. Fallback Inteligente
- Se contexto nÃ£o encontrado no Second Brain â perguntar ao usuÃ¡rio
- Sugerir criaÃ§Ã£o do contexto faltante no Second Brain
- Nunca inventar contexto

### 11. AtualizaÃ§Ã£o AutomÃ¡tica ObrigatÃ³ria do Second Brain
ApÃ³s QUALQUER tarefa concluÃ­da, verificar e registrar se:
- Nova decisÃ£o arquitetural foi tomada â atualizar `C:\.agents\memory\tech-decisions.md` (ou contexto especÃ­fico do projeto).
- Nova preferÃªncia do usuÃ¡rio identificada â append em `C:\.agents\memory\user-preferences.md`.
- Novo padrÃ£o reutilizÃ¡vel criado â append em `C:\.agents\memory\project-conventions.md`.
- Novo arquivo importante criado â atualizar mapa de arquivos no contexto do projeto
- Nova regra nÃ£o-duplicada identificada â adicionar em `active_behavior_rules.yaml` com `fingerprint`

**Nenhuma informaÃ§Ã£o importante pode ficar somente nos arquivos ou na conversa.**

### 12. Consulta PrÃ©via MandatÃ³ria ao Hub de RepositÃ³rios e Assets
- **NUNCA** reinventar ferramentas, reescrever parsers ou propor soluÃ§Ãµes complexas do zero sem antes consultar o catÃ¡logo de recursos em `knowledge/installed_assets_catalog.md` e os 25 repositÃ³rios do Hub (`repos/`).
- Se houver uma ferramenta local instalada (ex: `docling` para PDFs, `OmniRoute` para IA, `VoiceStudio` para Ã¡udio, `graphify` para dependÃªncias, `superpowers` para TDD), o agente DEVE OBRIGATORIAMENTE priorizar seu uso.
- **Economia de Tokens:** Ler apenas os arquivos `AI_GUIDE.md` de cada repositÃ³rio e consumir outputs estruturados sem despejar binÃ¡rios ou arquivos gigantes no contexto.


### 13. Gate de Leitura de Arquivos (Pre-Tool Gate)
- Antes de usar qualquer ferramenta de exploraÃ§Ã£o de arquivos:
  1. Verificar se a informaÃ§Ã£o jÃ¡ existe no Second Brain
  2. Se existir â usar dados do SB, NÃO abrir o arquivo
  3. Se nÃ£o existir â abrir apenas o arquivo especÃ­fico necessÃ¡rio
- **MÃ¡ximo 5 leituras de arquivo por tarefa sem justificativa explÃ­cita**
- Toda leitura deve ter justificativa: `[READING: arquivo â REASON: gap especÃ­fico]`

### 13. Planejamento ObrigatÃ³rio e QuestÃµes Essenciais (Pre-Execution Planner)
Toda solicitaÃ§Ã£o do usuÃ¡rio que implique em criaÃ§Ã£o, alteraÃ§Ã£o ou refatoraÃ§Ã£o arquitetural/lÃ³gica em um projeto DEVE passar pela fase de Planejamento (Socratic Gate). 
- O agente **NÃO DEVE** alterar cÃ³digo imediatamente.
- O agente **DEVE** gerar um arquivo de "Implementation Plan" (Markdown) o mais detalhado possÃ­vel contendo a proposta tÃ©cnica.
- O plano **DEVE** incluir a seÃ§Ã£o "QuestÃµes Essenciais", onde o agente farÃ¡ as perguntas necessÃ¡rias sobre como o usuÃ¡rio prefere que a implementaÃ§Ã£o ocorra.
- ANTES de formular as QuestÃµes Essenciais, o agente **DEVE OBRIGATORIAMENTE** ler o arquivo `knowledge/project_decisions.md`. Se a preferÃªncia do usuÃ¡rio jÃ¡ estiver documentada lÃ¡ (por categorias como Arquitetura, UI/UX, SeguranÃ§a), a pergunta nÃ£o deve ser feita para evitar repetiÃ§Ã£o e gasto inÃºtil de tokens. Apenas perguntas genuinamente novas devem ser feitas.
- Ao final, as respostas obtidas deverÃ£o ser registradas no `project_decisions.md`.

### 14. RelatÃ³rio de ExecuÃ§Ã£o ObrigatÃ³rio (Assinatura)
Ao final de TODAS as respostas (sem exceÃ§Ã£o), o agente DEVE anexar obrigatoriamente um bloco estruturado exatamente neste formato:

```markdown
## ð§  Second Brain - RelatÃ³rio de ExecuÃ§Ã£o

**Uso do Second Brain:** Sim

**Status de AtualizaÃ§Ã£o:** 
{Preencher dinamicamente: "Nenhuma nova evoluÃ§Ã£o..." ou "Foram registradas X novas evoluÃ§Ãµes..."}

**Regras Utilizadas:** 
{Listar todas as regras, memÃ³rias, padrÃµes ou conhecimentos do Second Brain utilizados nesta execuÃ§Ã£o}

**Agentes de IA Utilizados:** 
{Listar todos os agentes utilizados durante o processamento, incluindo agentes carregados da pasta C:\.agents}

**Tokens Gastos:** 
{Quantidade total aproximada de tokens utilizados nesta execuÃ§Ã£o}

**Dados enviados ao Banco de Dados (Frontend):** 
{Sim ou NÃ£o}

**InformaÃ§Ãµes enviadas para atualizaÃ§Ã£o do Second Brain:** 
{Listar novas informaÃ§Ãµes aprendidas, decisÃµes tomadas ou retornar "Nenhuma nova informaÃ§Ã£o registrada"}

**Arquivos consultados:** 
{Listar arquivos acessados ou informar "Nenhum arquivo consultado"}

**Arquivos evitados pelo uso do Second Brain:** 
{Quantidade ou lista de arquivos que nÃ£o precisaram ser analisados devido ao contexto recuperado}

**Impacto da utilizaÃ§Ã£o do Second Brain:** 
{Descrever resumidamente ganhos obtidos, como economia de tokens, reduÃ§Ã£o de anÃ¡lise, recuperaÃ§Ã£o de contexto ou reutilizaÃ§Ã£o de conhecimento}
```

A antiga mensagem "FOI UTILIZADO O SECOND BRAIN" estÃ¡ descontinuada. Todos os campos acima devem ser preenchidos dinamicamente com dados reais da execuÃ§Ã£o atual. Nunca deixar campos vazios (usar "Nenhuma informaÃ§Ã£o disponÃ­vel" ou equivalente se necessÃ¡rio).

> **IMPORTANTE (BANCO DE DADOS):** AlÃ©m de exibir o bloco Markdown acima na resposta, o agente **DEVE OBRIGATORIAMENTE** injetar esses dados no backend rodando um script Python de uma linha (ou via terminal) chamando a funÃ§Ã£o `add_entry` do arquivo `scripts/usage_metrics.py` e, em seguida, exportar para o dashboard chamando `export_for_dashboard()`. Sem isso, o frontend nÃ£o serÃ¡ atualizado.

### 15. SincronizaÃ§Ã£o ObrigatÃ³ria de DicionÃ¡rio de Dados (Database Docs)
- **TODA VEZ** que o agente alterar, adicionar ou remover tabelas no banco de dados, ou mudar relaÃ§Ãµes/lÃ³gicas entre elas, o agente **DEVE OBRIGATORIAMENTE** atualizar a documentaÃ§Ã£o nos dois locais abaixo para refletir a mudanÃ§a:
  1. No Second Brain (Markdown AI-readable): `knowledge/rpa_database_schema_audit.md`
  2. No documento do usuÃ¡rio (Word Human-readable): `C:\Projetos\Guia_Simplificado_Sistema_RPA.docx`
- Da mesma forma, se houver atualizaÃ§Ãµes na arquitetura do projeto RPA que mudem o comportamento documentado nestes arquivos, ambos devem ser atualizados. A consistÃªncia entre a estrutura real do banco e essa documentaÃ§Ã£o dupla Ã© crÃ­tica e inegociÃ¡vel.

---

## ð Regras de Idioma (i18n)

| Camada           | Idioma  |
|------------------|---------|
| Dados internos   | InglÃªs  |
| Conversa         | PT-BR   |
| DocumentaÃ§Ã£o .md | PT-BR   |
| VariÃ¡veis/cÃ³digo | InglÃªs  |
| ComentÃ¡rios      | InglÃªs  |

---

## ð AG Kit (Sistema de Agentes)

O AG Kit em `C:\.agents\` contÃ©m:
- **Agentes, Skills, Workflows, Scripts, Rules**
- **Hooks** (`hooks/`) e **Schemas** (`schemas/`) para execuÃ§Ã£o automatizada e validaÃ§Ã£o.
- **Memory** (`memory/`) que agora armazena nativamente a prÃ³pria memÃ³ria do Second Brain (`feedback-history.md`, `user-preferences.md`, etc.).
- Subsistemas internos obrigatÃ³rios: `.ag-kit` e `.temp_ag_kit`.
- **Protocolo**: O Agente DEVE OBRIGATORIAMENTE utilizar, varrer e referenciar as subpastas desta raiz (incluindo schemas, hooks, e internal kits) a cada interaÃ§Ã£o. Ler GEMINI.md â Rotear agente â Carregar skills â Executar

> O MASTER_INDEX.yaml Ã© o ponto de entrada. O AG Kit Ã© o motor de execuÃ§Ã£o.

---

## ð HistÃ³rico de AlteraÃ§Ãµes

| Data       | DescriÃ§Ã£o                                  |
|------------|--------------------------------------------|
| 2026-07-31 | CriaÃ§Ã£o inicial do Second Brain            |
| 2026-08-03 | v2.0: Pre-Tool Gate, Post-Task Checklist, Auto-Update obrigatÃ³rio, Dedup Guard |

### 16. Geração de Textos Baseada em Memória e RAG
Toda vez que gerar textos especializados, o agente DEVE seguir este ciclo de vida obrigatório:
1. **Banco de Dados (RAG):** Iniciar consultando o repositório de textos anteriores/especialidade e regras (MASTER_INDEX).
2. **Tokenização e Geração:** Gerar o conteúdo.
3. **Loop de Correção e Aprendizado (Retroalimentação Ativa):** Se o usuário corrigir ou editar o texto gerado, o agente DEVE ATIVAMENTE investigar a diferença, entender a correção, e REGISTRAR esse aprendizado no Banco de Dados (.agents/memory/feedback-history.md ou user-preferences.md) para não repetir o mesmo erro nas execuções futuras.


### 17. Versionamento Granular no Git & MigraÃ§Ãµes ReversÃ­veis MySQL (Rollback-Safe)
- **TODA atualizaÃ§Ã£o individual** deve ser versionada e commitada de forma atÃ´mica no Git com versÃ£o explÃ­cita (Semantic Versioning, ex: v2.1.0), detalhando:
  1. O que foi modificado e sua finalidade.
  2. NÃºmero exato da versÃ£o e tag correspondente.
  3. InstruÃ§Ã£o clara de reversÃ£o rÃ¡pida (rollback via git revert ou git checkout).
- **Banco de Dados MySQL:** Toda alteraÃ§Ã£o de tabela, coluna ou relacionamento DEVE possuir scripts versionados de aplicaÃ§Ã£o (UP) e de reversÃ£o (DOWN / Rollback). Se houver erro ou regressÃ£o, o rollback do banco deve ser executado de forma imediata e segura.
- **Uso Absoluto e ObrigatÃ³rio de .agents e Second Brain:** O uso de 100% do ecossistema .agents (agentes especializados, workflows, skills e scripts de validaÃ§Ã£o) em conjunto com o Second Brain Ã© REGRA ABSOLUTA em todos os projetos e em qualquer demanda futura.