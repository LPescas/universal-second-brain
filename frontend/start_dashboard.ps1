# Start Second Brain Dashboard (Background Service)
$Port = 8765
$Root = (Resolve-Path "$PSScriptRoot\..").Path
$Url  = "http://localhost:$Port/frontend/index.html"

# 1. Export fresh metrics and hub/graph data quietly
$MetricsScript = "$Root\scripts\usage_metrics.py"
if (Test-Path $MetricsScript) {
    python $MetricsScript --export 2>&1 | Out-Null
}
$ExportHubScript = "$Root\scripts\export_frontend_hub_data.py"
if (Test-Path $ExportHubScript) {
    python $ExportHubScript 2>&1 | Out-Null
}

# 2. Check if server is already running on this port
$PortInUse = (Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue)

if (-not $PortInUse) {
    # 3. Start server in a background process (persistent minimized window)
    Start-Process -FilePath "python" -ArgumentList "scripts\server.py $Port" -WorkingDirectory $Root -WindowStyle Minimized
    
    # Wait a second for binding
    Start-Sleep -Seconds 1
}

# 4. Open browser
Start-Process $Url
