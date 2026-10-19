# Contexto do Projeto: SecondBrain_Aurelio (Atualizado 2026-09-24)

## Visao Geral
Agente de IA local Aurelio — Jarvis pessoal integrado ao Second Brain.

## Caminho
C:\Projetos\SecondBrain_Aurelio

## Stack Tecnica
- Python stdlib puro (sem dependencias externas)
- Ollama local (HTTP direto via urllib)
- SQLite (aurelio.db)
- Modelos: qwen2.5 (principal), mistral, llama3 (fallback)
- Embedding: nomic-embed-text (local)

## Arquitetura de Modulos
- core/orchestrator.py  -> Pipeline principal (IMUTAVEL, 7 passos)
- agent/agent.py        -> Identidade, prompts formato 3 partes, proativo
- memory/memory.py      -> Busca hibrida, embeddings, chunking, batch
- database/db.py        -> SQLite CRUD, controle crescimento (max 1000)
- models/model_manager.py -> Ollama multi-modelo + fallback automatico
- interface/ui.py       -> Chat terminal, loader animado, comandos CLI
- main.py               -> Entrada CLI com --status, --reprocessar, --ingerir

## Regras de Governanca
- Nada bypassa o orchestrator.pipeline_principal()
- Modo restrito: apenas Second Brain | Modo expandido: + conhecimento externo
- Resposta sempre em 3 partes: Acao Direta + Contexto + Sugestao
- Logs em logs/app.log (arquivo + stdout)

## Status de Implementacao
COMPLETO - Todos testes passaram em 2026-09-24
