param([int]$AncienProcessus=0)
$ErrorActionPreference='Stop'
if($AncienProcessus -gt 0){
 $old=Get-CimInstance Win32_Process -Filter "ProcessId=$AncienProcessus"
 if($old -and $old.Name -eq 'powershell.exe' -and $old.CommandLine -like '*grc_laboratoire*inventaire_eleve.ps1*'){Stop-Process -Id $AncienProcessus -Force}
}
$lab=Join-Path (Split-Path (Split-Path $PSScriptRoot -Parent) -Parent) 'work\grc_laboratoire'
$dest=Join-Path $lab 'inventaire'
New-Item -ItemType Directory -Path $dest -Force | Out-Null
$r=[ordered]@{date_utc=[DateTime]::UtcNow.ToString('o'); elevated=([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)}
function Save-Progress { $r | ConvertTo-Json -Depth 8 | Set-Content -Encoding utf8 -LiteralPath (Join-Path $dest 'inventaire_eleve.json') }
Save-Progress
try {
 $dir='C:\Program Files (x86)\ossec-agent'
 [xml]$cfg=Get-Content -Raw -LiteralPath (Join-Path $dir 'ossec.conf')
 $r.servers=@($cfg.ossec_config.client.server | ForEach-Object { [ordered]@{address=$_.address;port=$_.port;protocol=$_.protocol} })
 $r.channels=@($cfg.ossec_config.localfile | ForEach-Object { [ordered]@{location=$_.location;log_format=$_.log_format;query=$_.query} })
 $r.version=(Get-Item -LiteralPath (Join-Path $dir 'wazuh-agent.exe')).VersionInfo.FileVersion
 $r.acl_config=(Get-Acl -LiteralPath (Join-Path $dir 'ossec.conf')).Sddl
 $r.acl_logs=(Get-Acl -LiteralPath (Join-Path $dir 'ossec.log')).Sddl
 Save-Progress
 # Uniquement etat de connexion, jamais client.keys, mot de passe ou contenu de journaux tiers.
 $logFile=Join-Path $dir 'ossec.log'
 $stream=[IO.File]::Open($logFile,[IO.FileMode]::Open,[IO.FileAccess]::Read,[IO.FileShare]::ReadWrite)
 try {
  $r.log_length=$stream.Length
  [void]$stream.Seek([Math]::Max(0,$stream.Length-65536),[IO.SeekOrigin]::Begin)
  $reader=New-Object IO.StreamReader($stream)
  $tail=$reader.ReadToEnd()
  $r.connection_lines=@($tail -split "`n" | Where-Object {$_ -match 'Connected to|Unable to connect|Trying to connect|Closing connection|Version detected'} | Select-Object -Last 12)
 } finally {$stream.Dispose()}
 Save-Progress
 $r.security_log=Get-WinEvent -ListLog Security | Select-Object LogName,IsEnabled,RecordCount,MaximumSizeInBytes,LogMode
 $r.security_latest=Get-WinEvent -LogName Security -MaxEvents 1 | Select-Object Id,TimeCreated,RecordId
 $r.audit_policy=(& auditpol.exe /get /subcategory:'{0CCE9215-69AE-11D9-BED3-505054503030}' 2>&1 | Out-String)
} catch { $r.error=$_.Exception.Message }
$r.finished_utc=[DateTime]::UtcNow.ToString('o')
$r | ConvertTo-Json -Depth 8 | Set-Content -Encoding utf8 -LiteralPath (Join-Path $dest 'inventaire_eleve.json')
