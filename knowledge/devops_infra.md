# DevOps & Infraestrutura — Base de Conhecimento

> Carregamento sob demanda. Triggers: deploy, docker, ci, server, infra.

---

## Ambiente Atual
- OS: Windows
- Shell: PowerShell
- IDE: VSCode (primário), Cursor (secundário)
- Agentes de IA: Antigravity, Cursor AI, Claude

## Patterns
- `.env` centralizado por projeto (nunca hardcoded)
- `.bat` para automações Windows
- `.command` para automações macOS (se necessário)
- requirements.txt para dependências Python
- venv isolado por projeto

## Deployment
- Projetos RPA rodam localmente (não cloud)
- ChromeDriver auto-sync via driver_manager.py
- Inicialização via `INICIAR_SISTEMA_VISUAL.bat`

---

## 📜 Histórico
| Data       | Descrição                                    |
|------------|----------------------------------------------|
| 2026-07-31 | Criação inicial                              |
