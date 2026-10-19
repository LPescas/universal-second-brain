<#
.SYNOPSIS
    Second Brain - Full Setup Script (PowerShell)
.DESCRIPTION
    Creates the complete Second Brain structure, deploys integrations,
    and configures CLI aliases. Run once after initial file creation.
.NOTES
    Path: C:\Users\USER\.second_brain\scripts\setup.ps1
    Run as: powershell -ExecutionPolicy Bypass -File setup.ps1
#>

$ErrorActionPreference = "Stop"
$BRAIN_ROOT = "C:\Users\USER\.second_brain"
$PROJECTS_ROOT = "C:\Projetos"

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  SECOND BRAIN - Setup Automatico" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# --- 1. Verify structure ---
Write-Host "[1/6] Verificando estrutura de diretorios..." -ForegroundColor Yellow

$requiredDirs = @(
    "$BRAIN_ROOT",
    "$BRAIN_ROOT\knowledge",
    "$BRAIN_ROOT\projects",
    "$BRAIN_ROOT\scripts",
    "$BRAIN_ROOT\integrations"
)

foreach ($dir in $requiredDirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Host "  [OK] Created: $dir" -ForegroundColor Green
    }
    else {
        Write-Host "  [OK] Exists: $dir" -ForegroundColor DarkGreen
    }
}

# --- 2. Verify core files ---
Write-Host "[2/6] Verificando arquivos core..." -ForegroundColor Yellow

$coreFiles = @(
    "$BRAIN_ROOT\MASTER_INDEX.yaml",
    "$BRAIN_ROOT\global_rules.md",
    "$BRAIN_ROOT\behavioral_patterns.yaml",
    "$BRAIN_ROOT\learning_log.md"
)

foreach ($file in $coreFiles) {
    if (Test-Path $file) {
        Write-Host "  [OK] $($file | Split-Path -Leaf)" -ForegroundColor DarkGreen
    }
    else {
        Write-Host "  [FAIL] MISSING: $($file | Split-Path -Leaf)" -ForegroundColor Red
    }
}

# --- 3. Deploy .cursorrules to all projects ---
Write-Host "[3/6] Deploying .cursorrules para projetos existentes..." -ForegroundColor Yellow

$cursorTemplate = "$BRAIN_ROOT\integrations\cursorrules_template.md"
if (Test-Path $cursorTemplate) {
    if (Test-Path $PROJECTS_ROOT) {
        $rootProjects = Get-ChildItem -Path $PROJECTS_ROOT -Directory -Depth 0
        foreach ($proj in $rootProjects) {
            $targetCursor = Join-Path $proj.FullName ".cursorrules"
            Copy-Item $cursorTemplate -Destination $targetCursor -Force
            Write-Host "  [OK] .cursorrules -> $($proj.Name)" -ForegroundColor Green
        }
    }
}

# --- 4. Update PowerShell profile ---
Write-Host "[4/6] Configurando PowerShell Profile..." -ForegroundColor Yellow

$profilePath = $PROFILE
$profileDir = Split-Path $profilePath -Parent
$snippetPath = "$BRAIN_ROOT\integrations\profile_snippet.ps1"
$marker = "# --- SECOND BRAIN INTEGRATION ---"

if (-not (Test-Path $profileDir)) {
    New-Item -ItemType Directory -Path $profileDir -Force | Out-Null
}

if (-not (Test-Path $profilePath)) {
    New-Item -ItemType File -Path $profilePath -Force | Out-Null
    Write-Host "  [OK] Created PowerShell profile: $profilePath" -ForegroundColor Green
}

$profileContent = Get-Content $profilePath -Raw -ErrorAction SilentlyContinue
if ($profileContent -and $profileContent.Contains($marker)) {
    Write-Host "  [OK] Second Brain already in profile" -ForegroundColor DarkGreen
}
else {
    $injection = "`n`n$marker`n. `"$snippetPath`"`n"
    Add-Content -Path $profilePath -Value $injection
    Write-Host "  [OK] Second Brain injected into PowerShell profile" -ForegroundColor Green
}

# --- 5. Merge VSCode settings ---
Write-Host "[5/6] Mesclando configuracoes VSCode..." -ForegroundColor Yellow

$vscodeSettingsDir = "$env:APPDATA\Code\User"
$vscodeSettingsPath = "$vscodeSettingsDir\settings.json"
$brainSettingsPath = "$BRAIN_ROOT\integrations\vscode_settings.json"

if (Test-Path $vscodeSettingsPath) {
    $existingContent = Get-Content $vscodeSettingsPath -Raw -ErrorAction SilentlyContinue
    if ($existingContent -and $existingContent.Contains("gemini.secondBrain")) {
        Write-Host "  [OK] VSCode settings already configured" -ForegroundColor DarkGreen
    }
    else {
        # Create backup
        $backupPath = "$vscodeSettingsPath.bak.$(Get-Date -Format 'yyyyMMddHHmmss')"
        Copy-Item $vscodeSettingsPath -Destination $backupPath
        Write-Host "  [BACKUP] $backupPath" -ForegroundColor DarkYellow

        try {
            $existing = Get-Content $vscodeSettingsPath -Raw | ConvertFrom-Json
            $brainSettings = Get-Content $brainSettingsPath -Raw | ConvertFrom-Json

            foreach ($prop in $brainSettings.PSObject.Properties) {
                if ($prop.Name -notlike "//*") {
                    $existing | Add-Member -MemberType NoteProperty -Name $prop.Name -Value $prop.Value -Force
                }
            }

            $existing | ConvertTo-Json -Depth 10 | Set-Content $vscodeSettingsPath
            Write-Host "  [OK] VSCode settings merged" -ForegroundColor Green
        }
        catch {
            Write-Host "  [WARN] Could not auto-merge VSCode settings. Manual merge needed." -ForegroundColor Yellow
            Write-Host "  Reference: $brainSettingsPath" -ForegroundColor Yellow
        }
    }
}
else {
    Write-Host "  [WARN] VSCode settings.json not found at $vscodeSettingsPath" -ForegroundColor Yellow
}

# --- 6. Scan and index projects ---
Write-Host "[6/6] Escaneando projetos em $PROJECTS_ROOT..." -ForegroundColor Yellow

if (Test-Path $PROJECTS_ROOT) {
    $allProjects = Get-ChildItem -Path $PROJECTS_ROOT -Directory -Depth 0
    foreach ($proj in $allProjects) {
        $safeName = $proj.Name.ToLower() -replace '\s+','_'
        $contextFile = "$BRAIN_ROOT\projects\${safeName}_context.md"
        if (Test-Path $contextFile) {
            Write-Host "  [OK] $($proj.Name) -> indexed" -ForegroundColor DarkGreen
        }
        else {
            Write-Host "  [WARN] $($proj.Name) -> NOT INDEXED (run brain-add-project)" -ForegroundColor Yellow
        }
    }
}

# --- Summary ---
Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  SETUP COMPLETO!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Hub: $BRAIN_ROOT" -ForegroundColor White
Write-Host "  Recarregue o terminal para usar os aliases:" -ForegroundColor White
Write-Host "    brain-learn   - registrar aprendizado" -ForegroundColor DarkGray
Write-Host "    brain-index   - ver master index" -ForegroundColor DarkGray
Write-Host "    brain-sync    - consolidar aprendizados" -ForegroundColor DarkGray
Write-Host "    brain-clean   - limpeza do learning log" -ForegroundColor DarkGray
Write-Host "    brain-project - ver contexto de projeto" -ForegroundColor DarkGray
Write-Host "    brain-cursor  - deploy .cursorrules no dir atual" -ForegroundColor DarkGray
Write-Host ""
