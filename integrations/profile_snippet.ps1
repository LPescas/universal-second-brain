# Second Brain — PowerShell Profile Snippet v2.0
# Sourced automatically via $PROFILE injection.
# DO NOT EDIT MANUALLY — regenerate via brain-upgrade

$BRAIN_ROOT = "C:\Users\USER\.second_brain"
$BRAIN_SCRIPTS = "$BRAIN_ROOT\scripts"
$BRAIN_PROJECTS = "$BRAIN_ROOT\projects"
$BRAIN_INTEGRATIONS = "$BRAIN_ROOT\integrations"

# --- CORE BRAIN COMMANDS ---

function brain-learn {
    param([string]$Note)
    $date = Get-Date -Format "yyyy-MM-dd HH:mm"
    $entry = "`n### $date | USER | MANUAL`n- $Note`n"
    Add-Content -Path "$BRAIN_ROOT\learning_log.md" -Value $entry
    Write-Host "[OK] Learning registered." -ForegroundColor Green
}

function brain-index {
    Get-Content "$BRAIN_ROOT\MASTER_INDEX.yaml"
}

function brain-sync {
    & powershell -ExecutionPolicy Bypass -File "$BRAIN_SCRIPTS\consolidate.ps1"
}

function brain-clean {
    & powershell -ExecutionPolicy Bypass -File "$BRAIN_SCRIPTS\cleanup.ps1"
}

function brain-detect {
    # Run pattern detection engine (learn_detector.py)
    python "$BRAIN_SCRIPTS\learn_detector.py"
}

function brain-consolidate {
    # Run autonomous consolidation (auto_consolidate.py)
    python "$BRAIN_SCRIPTS\auto_consolidate.py"
}

function brain-project {
    param([string]$ProjectName)
    $path = "$BRAIN_PROJECTS\${ProjectName}_context.md"
    if (Test-Path $path) {
        Get-Content $path
    }
    else {
        Write-Host "[FAIL] Project '$ProjectName' not found. Available:" -ForegroundColor Red
        Get-ChildItem "$BRAIN_PROJECTS\" -Name
    }
}

function brain-rules {
    # Show active enforcement rules
    Get-Content "$BRAIN_ROOT\active_behavior_rules.yaml"
}

function brain-cursor {
    Copy-Item "$BRAIN_INTEGRATIONS\cursorrules_template.md" -Destination ".\.cursorrules" -Force
    Write-Host "[OK] .cursorrules deployed to $(Get-Location)" -ForegroundColor Green
}

function brain-add-project {
    param(
        [Parameter(Mandatory=$true)][string]$Name,
        [Parameter(Mandatory=$true)][string]$ProjectPath,
        [string]$Description = "No description provided."
    )
    $date = Get-Date -Format "yyyy-MM-dd"
    $safeName = $Name.ToLower() -replace '\s+', '_'
    $filePath = "$BRAIN_PROJECTS\${safeName}_context.md"
    $content = @"
# Contexto do Projeto: $Name

> Carregamento sob demanda. Criado em $date.

---

## Visao Geral
$Description

## Caminho
$ProjectPath

## Stack Tecnica
_A ser preenchido_

---

## Historico
| Data       | Descricao                                     |
|------------|-----------------------------------------------|
| $date      | Contexto inicial criado via brain-add-project |
"@
    Set-Content -Path $filePath -Value $content -Encoding UTF8
    Write-Host "[OK] Project '$Name' added: $filePath" -ForegroundColor Green
    Write-Host "[WARN] Update MASTER_INDEX.yaml to add routing entry." -ForegroundColor Yellow
}

# --- CLAUDE CODE WRAPPER ---
# Overrides 'claude' to inject Second Brain context via --append-system-prompt-file
# CLAUDE.md global (~/.claude/CLAUDE.md) is already auto-loaded by Claude Code.
# This wrapper adds active_behavior_rules as additional enforcement.

function brain-claude {
    param(
        [Parameter(ValueFromRemainingArguments=$true)]
        [string[]]$Args
    )
    $rulesFile = "$BRAIN_ROOT\active_behavior_rules.yaml"
    if (Test-Path $rulesFile) {
        & claude --append-system-prompt-file "$rulesFile" @Args
    }
    else {
        & claude @Args
    }
}

# Alias: 'bc' as shorthand for brain-claude
Set-Alias bc brain-claude

# --- CODEX BRIDGE ---
# When Codex CLI is installed, this alias intercepts it and injects Second Brain context.

function brain-codex {
    param(
        [Parameter(ValueFromRemainingArguments=$true)]
        [string[]]$CodexArgs
    )
    python "$BRAIN_SCRIPTS\codex_bridge.py" @CodexArgs
}

# Make 'codex' an alias for the bridge (transparent when codex is installed)
if (-not (Get-Command codex -ErrorAction SilentlyContinue) -or (Get-Command codex).Source -notmatch 'codex.bridge') {
    function codex {
        param([Parameter(ValueFromRemainingArguments=$true)][string[]]$A)
        brain-codex @A
    }
}

# --- WEEKLY AUTO-CONSOLIDATION SCHEDULER ---
# Register a Windows Task to run auto_consolidate.py every Sunday at 03:00
function brain-schedule {
    $taskName = "SecondBrain_AutoConsolidate"
    $existing = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
    if ($existing) {
        Write-Host "[OK] Task '$taskName' already scheduled." -ForegroundColor DarkGreen
        return
    }
    $action = New-ScheduledTaskAction `
        -Execute "python" `
        -Argument "`"$BRAIN_SCRIPTS\auto_consolidate.py`""
    $trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At "03:00"
    $settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Hours 1)
    Register-ScheduledTask `
        -TaskName $taskName `
        -Action $action `
        -Trigger $trigger `
        -Settings $settings `
        -Description "Second Brain weekly auto-consolidation" | Out-Null
    Write-Host "[OK] Scheduled: '$taskName' every Sunday at 03:00" -ForegroundColor Green
}

Write-Host "[BRAIN] Second Brain v2.0 loaded." -ForegroundColor Cyan
Write-Host "  Core    : brain-learn, brain-index, brain-rules, brain-sync, brain-clean" -ForegroundColor DarkGray
Write-Host "  Learning: brain-detect, brain-consolidate, brain-schedule" -ForegroundColor DarkGray
Write-Host "  Project : brain-project, brain-cursor, brain-add-project" -ForegroundColor DarkGray
Write-Host "  Agents  : brain-claude (bc), brain-codex, codex (bridged)" -ForegroundColor DarkGray
