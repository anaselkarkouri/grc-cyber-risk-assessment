from pathlib import Path
import json, subprocess, os, urllib.request, time
import ssl
ROOT=Path(__file__).resolve().parents[2]
D=ROOT/'work/grc_laboratoire/T01_acces_mfa'
v=json.loads((D/'versions.json').read_text())
keycloak=Path(v['composants'][0]['dossier']); jdk=Path(v['composants'][1]['dossier'])
s=json.loads((D/'secrets_locaux.json').read_text())
env=dict(os.environ,JAVA_HOME=str(jdk),KC_BOOTSTRAP_ADMIN_USERNAME='LAB-RECOVERY',KC_BOOTSTRAP_ADMIN_PASSWORD=s['bootstrap'],JAVA_OPTS_APPEND='-Xms128m -Xmx512m')
cert=D/'localhost.pem'; key=D/'localhost-key.pem'
if not cert.exists():
 subprocess.run([r'C:\Program Files\Git\usr\bin\openssl.exe','req','-x509','-newkey','rsa:2048','-noenc','-keyout',str(key),'-out',str(cert),'-days','30','-subj','/CN=127.0.0.1','-addext','subjectAltName=IP:127.0.0.1,DNS:localhost'],check=True,capture_output=True)
command=['cmd.exe','/c',str(keycloak/'bin/kc.bat'),'start-dev','--http-enabled=false','--http-host=127.0.0.1','--https-port=18443','--https-certificate-file='+str(cert),'--https-certificate-key-file='+str(key),'--http-management-host=127.0.0.1','--http-management-port=19000']
with (D/'keycloak_console.log').open('ab') as f:
    p=subprocess.Popen(command,env=env,cwd=keycloak,stdout=f,stderr=f,creationflags=subprocess.CREATE_NO_WINDOW)
(D/'processus.json').write_text(json.dumps({'pid':p.pid,'command':command,'ecoute':'127.0.0.1:18443','mode':'start-dev avec TLS local','versions':v},indent=2),encoding='utf-8')
for _ in range(60):
    try:
        with urllib.request.urlopen('https://127.0.0.1:18443/realms/master',timeout=2,context=ssl.create_default_context(cafile=str(cert))) as r:
            if r.status==200:print('Keycloak disponible sur loopback');break
    except Exception:time.sleep(1)
else:raise RuntimeError('Demarrage non confirme ; consulter keycloak_console.log')
