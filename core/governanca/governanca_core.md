# Governança e Compliance do Second Brain

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

Esta subpasta contém o **Guardião de Execução**, módulo desenvolvido para atuar como uma barreira de proteção (Zero Trust) contra modificações acidentais, desalinhadas ou induzidas (por AIs e desenvolvedores) que firam as regras de governança do Second Brain.

## 🎯 Objetivo

Garantir o cumprimento estrito das diretrizes documentadas no `MASTER_INDEX.yaml`, `global_rules.md`, `projeto_second_brain.md` e em todos os arquivos `.md` distribuídos pelas subpastas do ecossistema.

## 🧱 Componentes de Governança

- `guardiao_execucao.py`: Orquestrador principal de validação pré-execução.
- `leitor_documentacao.py`: Força a leitura do documento principal e valida a presença de `.md` local em todas as pastas.
- `validador_regras.py`: Cérebro das validações estruturais: arquivos críticos, convenções de nomenclatura e conformidade Zero Trust.

---

## 📜 Histórico Global de Alterações

| Data | Autor/Agente | Descrição Macro da Mudança |
| :--- | :--- | :--- |
| 2026-10-19 | Antigravity | Implantação do Core de Governança Zero Trust e compliance no Second Brain. |
| 2026-10-19 | Antigravity | Padronização de documentação em todas as subpastas e repositórios. |
