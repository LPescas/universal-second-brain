<#
.SYNOPSIS
    Second Brain — Consolidation Script
.DESCRIPTION
    Processes learning_log.md, presents pending learnings for validation,
    and promotes validated patterns to behavioral_patterns.yaml.
    Also prunes consolidated entries from the log.
.NOTES
    Run via: brain-sync (or powershell -File consolidate.ps1)
#>

$ErrorActionPreference = "Stop"
$BRAIN_ROOT = "C:\Users\USER\.second_brain"
$LOG_FILE = "$BRAIN_ROOT\learning_log.md"
$PATTERNS_FILE = "$BRAIN_ROOT\behavioral_patterns.yaml"

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  🧠 SECOND BRAIN — Consolidação" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

if (-not (Test-Path $LOG_FILE)) {
    Write-Host "❌ learning_log.md not found" -ForegroundColor Red
    exit 1
}

# --- 1. Read learning log ---
Write-Host "[1/4] Lendo learning_log.md..." -ForegroundColor Yellow
$logContent = Get-Content $LOG_FILE -Raw

# Extract entries from "Active Learnings" section
$activeSection = [regex]::Match($logContent, '## Active Learnings.*?(?=## Consolidated|$)', [System.Text.RegularExpressions.RegexOptions]::Singleline)

if (-not $activeSection.Success -or $activeSection.Value.Trim().Length -lt 50) {
    Write-Host "✔ Nenhum aprendizado pendente para consolidar." -ForegroundColor DarkGreen
    exit 0
}

# --- 2. Display pending entries ---
Write-Host "[2/4] Aprendizados pendentes de validação:" -ForegroundColor Yellow
Write-Host ""
Write-Host $activeSection.Value -ForegroundColor White
Write-Host ""

# --- 3. Prompt for validation ---
Write-Host "[3/4] Validação interativa" -ForegroundColor Yellow
$response = Read-Host "Deseja promover TODOS os padrões acima para behavioral_patterns.yaml? (s/n/selecionar)"

if ($response -eq "s" -or $response -eq "S") {
    # Promote all
    $date = Get-Date -Format "yyyy-MM-dd"
    $promotionEntry = "`n# Consolidated from learning_log on $date`n$($activeSection.Value)`n"

    # Append to patterns file as comment block
    Add-Content -Path $PATTERNS_FILE -Value $promotionEntry
    Write-Host "✅ Todos os padrões promovidos para behavioral_patterns.yaml" -ForegroundColor Green

    # Clear active section and move to consolidated
    $consolidatedEntry = "`n### $date | CONSOLIDATION | AUTO`n- Batch consolidation: all active learnings promoted`n"
    $newLogContent = $logContent -replace '## Active Learnings.*?(?=## Consolidated)', "## Active Learnings (Pending Validation)`n`n_Nenhum aprendizado pendente._`n`n## Consolidated"
    # Add to consolidated section
    $newLogContent = $newLogContent -replace '## Consolidated Patterns \(Validated by User\)', "## Consolidated Patterns (Validated by User)`n$consolidatedEntry"

    # Update consolidation history
    $historyEntry = "| $date | batch | all | $(($activeSection.Value -split "`n" | Where-Object { $_ -match '^\s*-' }).Count) |"
    $newLogContent = $newLogContent -replace '\| _none_ \| _none_ \| _none_ \| _none_ \|', $historyEntry

    Set-Content -Path $LOG_FILE -Value $newLogContent
    Write-Host "✅ learning_log.md atualizado" -ForegroundColor Green

} elseif ($response -eq "n" -or $response -eq "N") {
    Write-Host "⏭ Consolidação cancelada. Nenhuma mudança feita." -ForegroundColor Yellow
} else {
    Write-Host "⚠️ Seleção individual ainda não implementada. Use 's' ou 'n'." -ForegroundColor Yellow
}

# --- 4. Summary ---
Write-Host ""
Write-Host "[4/4] Resumo:" -ForegroundColor Yellow
$logSize = (Get-Item $LOG_FILE).Length
$patternsSize = (Get-Item $PATTERNS_FILE).Length
Write-Host "  📄 learning_log.md: $([math]::Round($logSize/1KB, 1)) KB" -ForegroundColor White
Write-Host "  📄 behavioral_patterns.yaml: $([math]::Round($patternsSize/1KB, 1)) KB" -ForegroundColor White
Write-Host ""
