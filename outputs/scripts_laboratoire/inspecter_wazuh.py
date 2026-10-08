from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[2];LAB=ROOT/'work/grc_laboratoire';sys.path.insert(0,str(LAB/'python_deps'))
import paramiko
W=LAB/'T02_journalisation_siem/gestionnaire'
c=paramiko.SSHClient();c.load_host_keys(str(W/'known_hosts')) if (W/'known_hosts').exists() else None
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('127.0.0.1',port=22022,username='labgrc',key_filename=str(W/'ssh_privee'),timeout=60,banner_timeout=60,auth_timeout=60,allow_agent=False,look_for_keys=False)
c.save_host_keys(str(W/'known_hosts'))
cmd='cloud-init status; test ! -f installation-terminee || cat installation-terminee; sudo tail -n 15 /var/log/cloud-init-output.log; sudo systemctl is-active wazuh-manager; sudo timeout 3 /var/ossec/bin/agent_control -l'
_,out,err=c.exec_command(cmd,timeout=30);print(out.read().decode('utf-8',errors='replace'));print(err.read().decode('utf-8',errors='replace'));c.close()
