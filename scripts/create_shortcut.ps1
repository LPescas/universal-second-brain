$WshShell = New-Object -comObject WScript.Shell
$DesktopPath = [Environment]::GetFolderPath("Desktop")
$Shortcut = $WshShell.CreateShortcut("$DesktopPath\Second Brain Dashboard.lnk")
$Shortcut.TargetPath = "powershell.exe"
$Shortcut.Arguments = "-WindowStyle Hidden -ExecutionPolicy Bypass -File `"C:\Users\USER\.second_brain\frontend\start_dashboard.ps1`""
$Shortcut.IconLocation = "shell32.dll,15"
$Shortcut.Description = "Inicia o monitor visual do ecossistema Second Brain"
$Shortcut.Save()
Write-Host "Atalho criado na Area de Trabalho com sucesso!"
