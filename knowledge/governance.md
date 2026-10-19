# Governança — Base de Conhecimento

> Carregamento sob demanda. Triggers: governance, zero-trust, compliance, audit, documentation.

---

## Sistema Zero-Trust UNIQ

### Regras Fundamentais
1. **Documentação obrigatória**: Todo subdir tem `*_nome.md`
2. **Header de governança**: Todo `.md` de pasta deve ter o header de governança global
3. **Código sem doc = inválido**: Nenhuma mudança sem atualizar o `.md` correspondente
4. **Mudança estrutural**: Atualizar o `projeto_*.md` raiz

### Header de Governança (Template)
```markdown
> 🚨 **REGRA DE GOVERNANÇA GLOBAL — LEITURA OBRIGATÓRIA ANTES DE QUALQUER COMMIT/MODIFICAÇÃO**
>
> 1. ✅ **TODO** subdiretório deste projeto possui um arquivo `*_nome.md` descrevendo seus artefatos e histórico.
> 2. ✅ **SEMPRE** que você (ou um Agente de IA) alterar, criar ou remover um arquivo, você **DEVE** atualizar o `.md` específico daquela subpasta imediatamente, registrando o histórico.
> 3. ✅ Se a mudança for estrutural, este arquivo raiz (`projeto_*.md`) também deve ser atualizado.
>
> ❌ **CÓDIGO SEM DOCUMENTAÇÃO ATUALIZADA SERÁ CONSIDERADO INVÁLIDO.**
```

### Guardião de Execução
- Intercepta boot do sistema
- Valida: pastas obrigatórias, entry points, docs, naming
- Localização: `core/governanca/`
- Scripts: `guardiao_execucao.py`, `validador_regras.py`, `leitor_documentacao.py`

### Skill Global
- `C:\Users\USER\.gemini\config\skills\rpa_governance\SKILL.md`
- Ativa automaticamente em qualquer projeto RPA
- Contém templates e scripts de bootstrapping

---

## 📜 Histórico
| Data       | Descrição                                    |
|------------|----------------------------------------------|
| 2026-07-31 | Criação inicial a partir do sistema UNIQ     |
