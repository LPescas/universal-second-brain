# setup_repos_structure.ps1 — Fase 1: Criação da estrutura de diretórios do Hub
$base = "C:\Users\USER\.second_brain\repos"

$categories = @(
    "media_processing",
    "dev_reverse_engineering",
    "ui_ux_design",
    "orchestration_governance",
    "routing_gateways",
    "memory_rag_graphs",
    "document_web_parsers",
    "cloud_security_b2b"
)

foreach ($cat in $categories) {
    $path = Join-Path $base $cat
    New-Item -ItemType Directory -Path $path -Force | Out-Null
    Write-Host "[OK] Created: $path"
}

Write-Host ""
Write-Host "[DONE] Estrutura de categorias criada com sucesso!"
Get-ChildItem $base | Format-Table Name, Mode -AutoSize
