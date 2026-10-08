from pathlib import Path
import sys,json
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[2];LAB=ROOT/'work/grc_laboratoire';sys.path.insert(0,str(LAB/'python_deps'))
import paramiko
W=LAB/'T02_journalisation_siem/gestionnaire';out=Path(json.loads((W.parent/'derniere_preuve.json').read_text())['path'])
c=paramiko.SSHClient();c.load_host_keys(str(W/'known_hosts'));c.set_missing_host_key_policy(paramiko.RejectPolicy());c.connect('127.0.0.1',port=22022,username='labgrc',key_filename=str(W/'ssh_privee'),timeout=15,allow_agent=False,look_for_keys=False)
cmd="date --utc --iso-8601=seconds; id -nG; if test -r /var/ossec/logs/archives/archives.json; then printf 'lecture_sans_sudo=permise\\n'; else printf 'lecture_sans_sudo=refusee\\n'; fi; sudo grep -nE '^monitord\\.(rotate_log|keep_log_days|compress)' /var/ossec/etc/internal_options.conf /var/ossec/etc/local_internal_options.conf; sudo find /etc/cron.d /etc/cron.daily /etc/logrotate.d -maxdepth 1 -iname '*wazuh*' -print"
_,o,e=c.exec_command(cmd,timeout=15);result={'date_collecte_utc':datetime.now(timezone.utc).isoformat(),'commande':cmd,'stdout':o.read().decode('utf-8',errors='replace'),'stderr':e.read().decode('utf-8',errors='replace'),'code':o.channel.recv_exit_status(),'limite':'Lecture de configuration et de droits uniquement ; aucun historique de 90 jours ni résistance à un administrateur démontrés.'};c.close()
(out/'T02-P05b_parametres_retention.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');sys.stdout.reconfigure(encoding='utf-8');print(json.dumps(result,ensure_ascii=False))
