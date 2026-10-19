# schedule_auto_sync.ps1 -- Registro de Tarefa Agendada para Sincronização Silenciosa do Second Brain
# ==================================================================================================
param(
    [switch]$Install,
    [switch]$Uninstall,
    [switch]$RunNow,
    [switch]$Status
)

$TaskName = "SecondBrain_AutoSync_Hub"
$ScriptPath = "C:\Users\USER\.second_brain\scripts\repo_sync_engine.py"
$PythonExe = "python.exe"

if ($RunNow) {
    Write-Host "[Second Brain] Disparando sincronização imediata..." -ForegroundColor Cyan
    & python -c "import sys; sys.stdout.reconfigure(encoding='utf-8'); exec(open(r'$ScriptPath', encoding='utf-8').read())"
    exit $LASTEXITCODE
}

if ($Status) {
    Write-Host "[Second Brain] Verificando status da tarefa agendada '$TaskName'..." -ForegroundColor Cyan
    $task = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
    if ($task) {
        Write-Host "  [OK] Tarefa Agendada '$TaskName' estÃ¡ INSTALADA." -ForegroundColor Green
        Write-Host "  Estado: $($task.State)"
    } else {
        Write-Host "  [AVISO] Tarefa Agendada '$TaskName' nÃ£o encontrada no Windows Task Scheduler." -ForegroundColor Yellow
    }
    exit 0
}

if ($Uninstall) {
    Write-Host "[Second Brain] Removendo tarefa agendada '$TaskName'..." -ForegroundColor Yellow
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
    Write-Host "  [OK] Tarefa removida com sucesso." -ForegroundColor Green
    exit 0
}

if ($Install) {
    Write-Host "[Second Brain] Configurando tarefa agendada diÃ¡ria '$TaskName'..." -ForegroundColor Cyan
    
    $action = New-ScheduledTaskAction -Execute "python.exe" -Argument "-c `"import sys; sys.stdout.reconfigure(encoding='utf-8'); exec(open(r'$ScriptPath', encoding='utf-8').read())`"" -WorkingDirectory "C:\Users\USER\.second_brain"
    $trigger = New-ScheduledTaskTrigger -Daily -At "03:00AM"
    $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -RunOnlyIfNetworkAvailable

    try {
        Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Description "Auto-Sincronizacao Silenciosa de Repositorios do Second Brain com Protecao Cold Snapshot" -ErrorAction Stop | Out-Null
        Write-Host "  [OK] Tarefa Agendada '$TaskName' registrada com sucesso para execuÃ§Ã£o diÃ¡ria Ã s 03:00!" -ForegroundColor Green
    } catch {
        Write-Host "  [AVISO] Registro no Task Scheduler requer privilÃ©gios de Administrador ou polÃ­tica local. Erro: $_" -ForegroundColor Yellow
        Write-Host "  Como alternativa, a sincronizaÃ§Ã£o pode ser chamada sob demanda via 'brain-sync' ou 'python repo_sync_engine.py'." -ForegroundColor Gray
    }
    exit 0
}

Write-Host "Uso:"
Write-Host "  .\schedule_auto_sync.ps1 -Install   # Instala no Task Scheduler"
Write-Host "  .\schedule_auto_sync.ps1 -Uninstall # Remove do Task Scheduler"
Write-Host "  .\schedule_auto_sync.ps1 -RunNow    # Executa agora"
Write-Host "  .\schedule_auto_sync.ps1 -Status    # Consulta status"
