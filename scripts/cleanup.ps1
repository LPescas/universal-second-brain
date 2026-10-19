<#
.SYNOPSIS
    Second Brain - Cleanup and Self-Maintenance Script
.DESCRIPTION
    Performs health checks, validates structure integrity,
    and reports Second Brain statistics.
.NOTES
    Run via: brain-clean (or powershell -File cleanup.ps1)
#>

$ErrorActionPreference = "Stop"
$BRAIN_ROOT = "C:\Users\USER\.second_brain"

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  SECOND BRAIN - Limpeza e Manutencao" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

$issues = 0

# --- 1. Structure Integrity ---
Write-Host "[1/5] Verificando integridade estrutural..." -ForegroundColor Yellow

$requiredFiles = @(
    @{Path="$BRAIN_ROOT\MASTER_INDEX.yaml"; Name="MASTER_INDEX.yaml"},
    @{Path="$BRAIN_ROOT\global_rules.md"; Name="global_rules.md"},
    @{Path="$BRAIN_ROOT\behavioral_patterns.yaml"; Name="behavioral_patterns.yaml"},
    @{Path="$BRAIN_ROOT\learning_log.md"; Name="learning_log.md"}
)

foreach ($file in $requiredFiles) {
    if (Test-Path $file.Path) {
        $size = [math]::Round((Get-Item $file.Path).Length / 1KB, 1)
        Write-Host "  [OK] $($file.Name) ($size KB)" -ForegroundColor DarkGreen
    }
    else {
        Write-Host "  [FAIL] MISSING: $($file.Name)" -ForegroundColor Red
        $issues++
    }
}

# --- 2. MASTER_INDEX size check ---
Write-Host "[2/5] Verificando MASTER_INDEX.yaml (max 100 linhas)..." -ForegroundColor Yellow

$indexPath = "$BRAIN_ROOT\MASTER_INDEX.yaml"
if (Test-Path $indexPath) {
    $lineCount = (Get-Content $indexPath).Count
    if ($lineCount -le 100) {
        Write-Host "  [OK] $lineCount linhas (dentro do limite)" -ForegroundColor DarkGreen
    }
    else {
        Write-Host "  [WARN] $lineCount linhas (EXCEDE o limite de 100!)" -ForegroundColor Red
        $issues++
    }
}

# --- 3. Learning log size check ---
Write-Host "[3/5] Verificando learning_log.md..." -ForegroundColor Yellow

$logPath = "$BRAIN_ROOT\learning_log.md"
if (Test-Path $logPath) {
    $logLines = (Get-Content $logPath).Count
    $logSizeVal = [math]::Round((Get-Item $logPath).Length / 1KB, 1)

    if ($logLines -gt 200) {
        Write-Host "  [WARN] $logLines linhas - recomendado consolidar via brain-sync" -ForegroundColor Yellow
        $issues++
    }
    else {
        Write-Host "  [OK] $logLines linhas ($logSizeVal KB)" -ForegroundColor DarkGreen
    }
}

# --- 4. Project context freshness ---
Write-Host "[4/5] Verificando frescor dos contextos de projeto..." -ForegroundColor Yellow

$projectsDir = "$BRAIN_ROOT\projects"
if (Test-Path $projectsDir) {
    $contextFiles = Get-ChildItem $projectsDir -Filter "*_context.md"
    $now = Get-Date

    foreach ($ctx in $contextFiles) {
        $age = ($now - $ctx.LastWriteTime).Days
        $projectName = $ctx.BaseName -replace '_context$', ''

        if ($age -gt 30) {
            Write-Host "  [WARN] $projectName - $age dias sem atualizacao" -ForegroundColor Yellow
            $issues++
        }
        else {
            Write-Host "  [OK] $projectName - atualizado ha $age dia(s)" -ForegroundColor DarkGreen
        }
    }
}

# --- 5. Orphan .cursorrules check ---
Write-Host "[5/5] Verificando .cursorrules nos projetos..." -ForegroundColor Yellow

$projectsRoot = "C:\Projetos"
if (Test-Path $projectsRoot) {
    $projectDirs = Get-ChildItem -Path $projectsRoot -Directory -Depth 0
    foreach ($proj in $projectDirs) {
        $cursorFile = Join-Path $proj.FullName ".cursorrules"
        if (Test-Path $cursorFile) {
            Write-Host "  [OK] $($proj.Name) - .cursorrules presente" -ForegroundColor DarkGreen
        }
        else {
            Write-Host "  [WARN] $($proj.Name) - sem .cursorrules (use brain-cursor)" -ForegroundColor Yellow
            $issues++
        }
    }
}

# --- Summary ---
Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  RELATORIO DE SAUDE" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Calculate total size
$totalSize = 0
Get-ChildItem $BRAIN_ROOT -Recurse -File | ForEach-Object { $totalSize += $_.Length }
$totalSizeKB = [math]::Round($totalSize / 1KB, 1)

$knowledgeCount = (Get-ChildItem "$BRAIN_ROOT\knowledge" -Filter "*.md" -ErrorAction SilentlyContinue).Count
$projectCount = (Get-ChildItem "$BRAIN_ROOT\projects" -Filter "*.md" -ErrorAction SilentlyContinue).Count

Write-Host "  Total size: $totalSizeKB KB" -ForegroundColor White
Write-Host "  Knowledge bases: $knowledgeCount" -ForegroundColor White
Write-Host "  Projetos indexados: $projectCount" -ForegroundColor White

if ($issues -eq 0) {
    Write-Host "  Problemas: 0" -ForegroundColor Green
    Write-Host ""
    Write-Host "  Second Brain esta saudavel!" -ForegroundColor Green
}
else {
    Write-Host "  Problemas: $issues" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "  $issues problema(s) detectado(s). Revise acima." -ForegroundColor Yellow
}
Write-Host ""
