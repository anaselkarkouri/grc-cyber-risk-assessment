from pathlib import Path
import sys,hashlib,json,subprocess,io,time
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[2]; LAB=ROOT/'work/grc_laboratoire'
sys.path.insert(0,str(LAB/'python_deps'))
import requests,pycdlib,paramiko
sys.stdout.reconfigure(encoding='utf-8')
W=LAB/'T02_journalisation_siem/gestionnaire'; W.mkdir(parents=True,exist_ok=True)
VB=r'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe'; NAME='GRC-Wazuh-T02-20261007'
def run(*a):
 p=subprocess.run([VB,*a],capture_output=True,text=True,encoding='utf-8',errors='replace')
 if p.returncode:raise RuntimeError(p.stderr[-1500:])
 return p.stdout
if NAME in run('list','vms'):
 info=run('showvminfo',NAME,'--machinereadable')
 cfg=json.loads(next(line.split('=',1)[1] for line in info.splitlines() if line.startswith('CfgFile=')))
 if not Path(cfg).resolve().is_relative_to((W/'VM').resolve()):raise RuntimeError('VM de même nom enregistrée dans une autre racine : utiliser les scripts originaux de cette mission ou choisir explicitement un nouveau nom, port et réseau.')
base='https://cloud-images.ubuntu.com/noble/20260926/'
filename='noble-server-cloudimg-amd64.vmdk'
s=requests.Session(); sums=s.get(base+'SHA256SUMS',timeout=60);sums.raise_for_status();(W/'SHA256SUMS').write_text(sums.text)
expected=next(l.split()[0] for l in sums.text.splitlines() if l.split()[-1].lstrip('*')==filename)
disk=W/filename
if not disk.exists():
 with s.get(base+filename,stream=True,timeout=60) as r:
  r.raise_for_status()
  with disk.open('wb') as f:
   for chunk in r.iter_content(1024*1024):f.write(chunk)
actual=hashlib.file_digest(disk.open('rb'),'sha256').hexdigest()
if actual!=expected:raise RuntimeError('SHA256 image Ubuntu incorrect')
print('Image Ubuntu vérifiée SHA256.',flush=True)
keyfile=W/'ssh_privee';
if not keyfile.exists():paramiko.RSAKey.generate(3072).write_private_key_file(str(keyfile))
key=paramiko.RSAKey.from_private_key_file(str(keyfile)); public=key.get_name()+' '+key.get_base64()+' grc-lab'
userdata='''#cloud-config
hostname: grc-wazuh-t02
manage_etc_hosts: true
ssh_pwauth: false
disable_root: true
users:
  - name: labgrc
    groups: [sudo]
    shell: /bin/bash
    sudo: ALL=(ALL) NOPASSWD:ALL
    lock_passwd: true
    ssh_authorized_keys:
      - '''+public+'''
package_update: true
packages: [curl, gnupg, apt-transport-https]
write_files:
  - path: /etc/apt/apt.conf.d/99grc-lab-network
    permissions: '0644'
    content: |
      Acquire::ForceIPv4 "true";
      Acquire::http::Timeout "15";
      Acquire::https::Timeout "15";
      Acquire::Retries "1";
  - path: /usr/local/sbin/grc-install-wazuh
    permissions: '0755'
    content: |
      #!/bin/bash
      set -eu
      curl -fsSL https://packages.wazuh.com/key/GPG-KEY-WAZUH | gpg --dearmor -o /usr/share/keyrings/wazuh.gpg
      chmod 644 /usr/share/keyrings/wazuh.gpg
      printf '%s\\n' 'deb [signed-by=/usr/share/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main' > /etc/apt/sources.list.d/wazuh.list
      apt-get update
      DEBIAN_FRONTEND=noninteractive apt-get install -y wazuh-manager
      cp /var/ossec/etc/ossec.conf /var/ossec/etc/ossec.conf.initial
      sed -i 's/<logall_json>no<\/logall_json>/<logall_json>yes<\/logall_json>/' /var/ossec/etc/ossec.conf
      systemctl enable --now wazuh-manager
      systemctl restart wazuh-manager
      dpkg-query -W wazuh-manager > /home/labgrc/installation-terminee
runcmd:
  - [bash, /usr/local/sbin/grc-install-wazuh]
'''
network='''version: 2
ethernets:
  nat:
    match: {macaddress: "08:00:27:a1:b2:c4"}
    dhcp4: true
  lab:
    match: {macaddress: "08:00:27:a1:b2:c3"}
    addresses: [192.168.56.10/24]
    dhcp4: false
'''
iso=pycdlib.PyCdlib();iso.new(interchange_level=3,vol_ident='CIDATA',joliet=3,rock_ridge='1.09')
for name,data in [('user-data',userdata),('meta-data','instance-id: grc-wazuh-20261007\nlocal-hostname: grc-wazuh-t02\n'),('network-config',network)]:
 b=data.encode();iso.add_fp(io.BytesIO(b),len(b),iso_path='/'+name.upper().replace('-','_')+';1',rr_name=name,joliet_path='/'+name)
iso.write(str(W/'seed.iso'));iso.close()
if NAME not in run('list','vms'):
 run('createvm','--name',NAME,'--ostype','Ubuntu_64','--basefolder',str(W/'VM'),'--register')
 run('modifyvm',NAME,'--memory','2048','--cpus','2','--firmware','efi','--hpet','on','--nic1','nat','--macaddress1','080027A1B2C4','--natpf1','ssh,tcp,127.0.0.1,22022,,22','--nic2','hostonly','--hostonlyadapter2','VirtualBox Host-Only Ethernet Adapter','--macaddress2','080027A1B2C3','--audio-enabled','off','--clipboard-mode','disabled','--drag-and-drop','disabled')
 run('clonemedium','disk',str(disk),str(W/'manager.vdi'),'--format','VDI')
 run('modifymedium','disk',str(W/'manager.vdi'),'--resize','20480')
 run('storagectl',NAME,'--name','SATA','--add','sata','--controller','IntelAhci','--portcount','2')
 run('storageattach',NAME,'--storagectl','SATA','--port','0','--device','0','--type','hdd','--medium',str(W/'manager.vdi'))
 run('storageattach',NAME,'--storagectl','SATA','--port','1','--device','0','--type','dvddrive','--medium',str(W/'seed.iso'))
proof={'date_utc':datetime.now(timezone.utc).isoformat(),'vm':NAME,'image_url':base+filename,'sha256_attendu':expected,'sha256_observe':actual,'comparaison':actual==expected,'source_checksum':base+'SHA256SUMS','limite_verification':'SHA256 reçu par HTTPS officiel ; signature GPG du manifeste non vérifiée.','memoire_mio':2048,'cpu':2,'disque_mio':20480,'ip_hostonly':'192.168.56.10','ssh_nat':'127.0.0.1:22022','portee':'Gestionnaire et fichiers alerts/archives JSON uniquement ; pas de dashboard ni indexer, laboratoire personnel.'}
(W/'preparation_assainie.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2),encoding='utf-8')
if 'VMState="poweroff"' in run('showvminfo',NAME,'--machinereadable'):run('startvm',NAME,'--type','headless')
print('Nouvelle VM dédiée démarrée : '+NAME,flush=True)
