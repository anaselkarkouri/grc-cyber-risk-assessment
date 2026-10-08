from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2];LAB=ROOT/'work/grc_laboratoire';sys.path.insert(0,str(LAB/'python_deps'))
import paramiko
W=LAB/'T02_journalisation_siem/gestionnaire';c=paramiko.SSHClient();c.load_host_keys(str(W/'known_hosts'));c.set_missing_host_key_policy(paramiko.RejectPolicy())
c.connect('127.0.0.1',port=22022,username='labgrc',key_filename=str(W/'ssh_privee'),timeout=20,allow_agent=False,look_for_keys=False)
cmd="date -u; ps -eo pid,comm,args | grep -E '[a]pt-get|[d]pkg'; curl -4 -I --max-time 7 https://archive.ubuntu.com/ubuntu/dists/noble/InRelease; curl -4 -I --max-time 7 http://archive.ubuntu.com/ubuntu/dists/noble/InRelease; sudo tail -n 12 /var/log/cloud-init-output.log"
if len(sys.argv)>1 and sys.argv[1]=='etat':
 cmd="date -u; df -h /; free -m; dpkg-query -W -f='${Status} ${Version}\\n' wazuh-manager; ps -eo pid,ppid,comm,pcpu,pmem,etime | sort -k 4 -nr | head -n 16; sudo systemctl is-active wazuh-manager; sudo tail -n 8 /var/log/cloud-init-output.log"
if len(sys.argv)>1 and sys.argv[1]=='https':
 cmd="sudo sed -i 's|http://archive.ubuntu.com|https://archive.ubuntu.com|g;s|http://security.ubuntu.com|https://security.ubuntu.com|g' /etc/apt/sources.list.d/ubuntu.sources; printf '%s\\n' 'Acquire::ForceIPv4 \"true\";' 'Acquire::http::Timeout \"15\";' 'Acquire::https::Timeout \"15\";' 'Acquire::Retries \"1\";' | sudo tee /etc/apt/apt.conf.d/99grc-lab-network >/dev/null; sudo cat /etc/apt/apt.conf.d/99grc-lab-network"
if len(sys.argv)>1 and sys.argv[1]=='installer':
 cmd="set -e; sudo apt-get -o Dir::Etc::sourcelist=/etc/apt/sources.list.d/wazuh.list -o Dir::Etc::sourceparts=- update; sudo DEBIAN_FRONTEND=noninteractive apt-get install -y wazuh-manager; sudo test -f /var/ossec/etc/ossec.conf.initial || sudo cp /var/ossec/etc/ossec.conf /var/ossec/etc/ossec.conf.initial; sudo sed -i 's/<logall_json>no<\\/logall_json>/<logall_json>yes<\\/logall_json>/' /var/ossec/etc/ossec.conf; sudo systemctl enable --now wazuh-manager; sudo systemctl restart wazuh-manager; dpkg-query -W wazuh-manager"
if len(sys.argv)>1 and sys.argv[1]=='annuler_update':
 cmd="sudo python3 - <<'PY'\nimport pathlib,os,signal\nfor p in pathlib.Path('/proc').iterdir():\n if not p.name.isdigit():continue\n try:a=(p/'cmdline').read_bytes().decode().strip('\\x00').split('\\x00')\n except OSError:continue\n if a==['apt-get','update']:\n  os.kill(int(p.name),signal.SIGINT);print('Interruption du seul apt-get update : PID '+p.name)\nPY"
_,out,err=c.exec_command(cmd,timeout=900);text=out.read().decode('utf-8',errors='replace');errors=err.read().decode('utf-8',errors='replace');code=out.channel.recv_exit_status();c.close()
(W/('diagnostic_'+(sys.argv[1] if len(sys.argv)>1 else 'reseau')+'.txt')).write_text(text+'\n'+errors,encoding='utf-8');sys.stdout.reconfigure(encoding='utf-8');print(text[-4500:]);print(errors[-1500:]);print('Code distant : '+str(code))
