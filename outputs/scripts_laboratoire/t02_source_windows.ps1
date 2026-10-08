<# Lecture locale assainie. Un evenement n'est produit qu'avec les deux commutateurs explicites.
 Ne modifie jamais ossec.conf, client.keys, la politique d'audit ni une VM existante. #>
param([switch]$Evenement,[switch]$GestionnaireLaboratoireConfirme,[ValidatePattern('^LAB-GRC-EVT[0-9]*$')][string]$Compte='LAB-GRC-EVT')
$ErrorActionPreference='Stop'
$lab=Join-Path (Split-Path (Split-Path $PSScriptRoot -Parent) -Parent) 'work\grc_laboratoire'
$out=Join-Path $lab ('T02_journalisation_siem\'+[DateTime]::UtcNow.ToString('yyyyMMddTHHmmssZ'))
New-Item -ItemType Directory -Path $out -Force | Out-Null
$elevated=([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if(-not $elevated){throw 'Ouvrir PowerShell en administrateur pour lire Security et creer exclusivement le compte de test.'}
& (Join-Path $PSScriptRoot 'inventaire_eleve.ps1')
Copy-Item -LiteralPath (Join-Path $lab 'inventaire\inventaire_eleve.json') -Destination (Join-Path $out 'T02-P01_source.json')
if(-not $Evenement){Write-Output 'Inventaire seulement. Aucun compte ni evenement cree.';return}
if(-not $GestionnaireLaboratoireConfirme){throw 'Verifier que la destination Wazuh relevee est bien un laboratoire personnel avant de produire un evenement.'}
$account=$Compte
if(Get-LocalUser -Name $account -ErrorAction SilentlyContinue){throw 'Compte deja existant : conserver ses donnees et choisir explicitement un nouveau nom dans une copie du script.'}
$bytes=New-Object byte[] 36
[Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bytes)
$password=[Convert]::ToBase64String($bytes)+'!aA7'
$secure=ConvertTo-SecureString $password -AsPlainText -Force
New-LocalUser -Name $account -Password $secure -Description 'Compte artificiel T02 GRC cree par script local' -AccountExpires ((Get-Date).AddDays(1)) | Out-Null
Add-Type -TypeDefinition @'
using System;
using System.Runtime.InteropServices;
public class GRCLogon {
 [DllImport("advapi32.dll", SetLastError=true, CharSet=CharSet.Unicode)]
 public static extern bool LogonUser(string u,string d,string p,int t,int v,out IntPtr h);
 [DllImport("kernel32.dll")] public static extern bool CloseHandle(IntPtr h);
}
'@
$start=Get-Date
$handle=[IntPtr]::Zero
try {
 $ok=[GRCLogon]::LogonUser($account,'.',($password+'incorrect'),2,0,[ref]$handle)
 $nativeError=[Runtime.InteropServices.Marshal]::GetLastWin32Error()
 if($ok){[GRCLogon]::CloseHandle($handle)|Out-Null;throw 'Connexion incorrecte acceptee : anomalie a examiner.'}
 Start-Sleep -Seconds 3
 $events=Get-WinEvent -FilterHashtable @{LogName='Security';Id=4625;StartTime=$start} -ErrorAction SilentlyContinue
 $proof=@()
 foreach($ev in $events){
  [xml]$xml=$ev.ToXml()
  $data=@{};foreach($field in $xml.Event.EventData.Data){$data[$field.Name]=$field.'#text'}
  if($data.TargetUserName -eq $account){
   $proof+=[ordered]@{event_id=$ev.Id;record_id=$ev.RecordId;date_utc=$ev.TimeCreated.ToUniversalTime().ToString('o');host=$xml.Event.System.Computer;provider=$xml.Event.System.Provider.Name;target_account=$account;status=$data.Status;substatus=$data.SubStatus;logon_type=$data.LogonType;process_name=$data.ProcessName}
  }
 }
 [ordered]@{date_utc=[DateTime]::UtcNow.ToString('o');account=$account;resultat_api=$ok;erreur_win32=$nativeError;events=@($proof);limite='Champs selectionnes ; reception Wazuh et alerte restent a rechercher avec meme compte, record_id, host et heure.'} | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 -LiteralPath (Join-Path $out 'T02-P02_evenement_local.json')
 if($proof.Count -eq 0){Write-Output 'Aucun 4625 trouve : verifier audit et delai, sans conclure a une collecte SIEM.'}
} finally {
 Disable-LocalUser -Name $account
 $password=$null;$secure=$null
}
Write-Output ('Preuves locales : '+$out)
