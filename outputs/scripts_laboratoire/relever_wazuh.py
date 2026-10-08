from pathlib import Path
import sys,json,hashlib
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[2];LAB=ROOT/'work/grc_laboratoire';sys.path.insert(0,str(LAB/'python_deps'))
import paramiko
W=LAB/'T02_journalisation_siem/gestionnaire'
c=paramiko.SSHClient();c.load_host_keys(str(W/'known_hosts'));c.set_missing_host_key_policy(paramiko.RejectPolicy())
c.connect('127.0.0.1',port=22022,username='labgrc',key_filename=str(W/'ssh_privee'),timeout=30,banner_timeout=30,allow_agent=False,look_for_keys=False)
out=ROOT/'outputs/Portfolio_GRC_Anas/Annexes_laboratoire/preuves'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ');out.mkdir(exist_ok=False)
def command(s):
 _,o,e=c.exec_command(s,timeout=30);result=o.read().decode('utf-8',errors='replace');err=e.read().decode('utf-8',errors='replace');return {'commande':s,'code':o.channel.recv_exit_status(),'stdout':result,'stderr':err}
def write(name,d):
 (out/name).write_text(json.dumps({'date_collecte_utc':datetime.now(timezone.utc).isoformat(),**d},ensure_ascii=False,indent=2),encoding='utf-8')
write('T02-P01_gestionnaire.json',{'sources':command('date --utc --iso-8601=seconds; uname -r; cat /etc/os-release; dpkg-query -W wazuh-manager; sudo systemctl is-active wazuh-manager; sudo /var/ossec/bin/agent_control -l; ip -brief address'),'preparation':json.loads((W/'preparation_assainie.json').read_text(encoding='utf-8'))})
code="""import json,pathlib
for origin in ['archives','alerts']:
 p=pathlib.Path('/var/ossec/logs')/origin/(origin+'.json');found=[]
 if p.exists():
  with p.open('rb') as f:
   for raw in f:
    try:line=raw.decode('utf-8');encoding='utf-8'
    except UnicodeDecodeError:line=raw.decode('cp1252',errors='replace');encoding='cp1252 avec remplacement si nécessaire'
    try:d=json.loads(line)
    except ValueError:continue
    w=d.get('data',{}).get('win',{});e=w.get('eventdata',{});s=w.get('system',{})
    if str(s.get('eventID'))=='4625' and str(e.get('targetUserName','')).startswith('LAB-GRC-EVT'):
     found.append({'decodage_ligne':encoding,'timestamp_wazuh':d.get('timestamp'),'agent':d.get('agent'),'manager':d.get('manager'),'rule':d.get('rule'),'location':d.get('location'),'decoder':d.get('decoder'),'source':{k:s.get(k) for k in ['providerName','eventID','eventRecordID','systemTime','computer','channel']},'eventdata':{k:e.get(k) for k in ['targetUserName','status','subStatus','logonType','processName']}})
 print(json.dumps({'origine':str(p),'taille_source':p.stat().st_size if p.exists() else None,'evenements_assainis':found},ensure_ascii=False))
"""
result=command("sudo python3 - <<'PY'\n"+code+"\nPY")
if result['code']!=0:raise RuntimeError(result['stderr'])
records=[json.loads(line) for line in result['stdout'].splitlines()]
for name,d in zip(['T02-P03_reception.json','T02-P04_alerte.json'],records):write(name,{'commande':'sudo python3, lecture ligne par ligne et sélection compte LAB-GRC-EVT*, ID 4625 ; champs autorisés uniquement','resultat':d,'limite':'Événements des autres comptes exclus ; sortie brute entière jamais exportée.'})
write('T02-P05_droits_conservation.json',{'lecture':command("sudo stat -c '%n %U:%G %a %s octets' /var/ossec/logs /var/ossec/logs/alerts /var/ossec/logs/archives /var/ossec/logs/alerts/alerts.json /var/ossec/logs/archives/archives.json; sudo grep -E '<(logall|logall_json|jsonout_output|alerts_log|log_alert_level)>' /var/ossec/etc/ossec.conf; sudo find /var/ossec/logs/alerts /var/ossec/logs/archives -maxdepth 3 -type f -printf '%TY-%Tm-%Td %p\\n' | head -n 12"),'limites':['Aucun historique de 90 jours sur ce nouveau gestionnaire.','Droits POSIX et SSH à clé examinés ; sudo root permet de modifier les traces.','Aucun stockage immuable, séparation complète des opérateurs ou test de récupérabilité à 90 jours.','Pas d’indexer ni de dashboard dans ce montage minimal.']})
c.close();(LAB/'T02_journalisation_siem/derniere_preuve.json').write_text(json.dumps({'path':str(out)}),encoding='utf-8');print(json.dumps({'preuves':str(out),'receptions':len(records[0]['evenements_assainis']),'alertes':len(records[1]['evenements_assainis'])}))
