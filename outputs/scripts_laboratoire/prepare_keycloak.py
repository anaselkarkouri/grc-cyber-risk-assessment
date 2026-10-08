from pathlib import Path
from datetime import datetime, timezone
import urllib.request, json, zipfile, hashlib, subprocess, secrets, os
ROOT=Path(__file__).resolve().parents[2]
DEST=ROOT/'work/grc_laboratoire/T01_acces_mfa'
DEST.mkdir(parents=True,exist_ok=True)
who=subprocess.check_output(['whoami.exe'],text=True).strip()
subprocess.run(['icacls.exe',str(DEST),'/inheritance:r','/grant:r',who+':(OI)(CI)F','*S-1-5-18:(OI)(CI)F','*S-1-5-32-544:(OI)(CI)F'],check=True,capture_output=True)
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'GRC-Lab-Local'}),timeout=90) as r:return json.load(r)
release=get('https://api.github.com/repos/keycloak/keycloak/releases/tags/26.8.0')
asset=next(x for x in release['assets'] if x['name']==f"keycloak-{release['tag_name']}.zip")
jdk={'version':{'semver':'25.0.4.1+1'}}
packages=[('keycloak',asset['browser_download_url'],'7ed1de3fda2598369262613bf682aab7e233d80a38c405e91588f7a7454370a1'),('jdk','https://github.com/adoptium/temurin25-binaries/releases/download/jdk-25.0.4.1%2B1/OpenJDK25U-jdk_x64_windows_hotspot_25.0.4.1_1.zip','00c847d804f4a78e9f04f2683faf14fed898535b177b7fc704486cb0284e9283')]
manifest=[]
for name,url,digest in packages:
    p=DEST/(name+'.zip')
    if not p.exists():
        print('Telechargement '+name,flush=True)
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'GRC-Lab-Local'}),timeout=120) as r, p.open('wb') as f:
            while block:=r.read(1024*1024):f.write(block)
    observed=hashlib.sha256(p.read_bytes()).hexdigest()
    if digest and observed!=digest: raise ValueError('Empreinte differente pour '+name)
    with zipfile.ZipFile(p) as z:
        folder=DEST/z.namelist()[0].split('/')[0]
        if not folder.exists():z.extractall(DEST)
    manifest.append({'composant':name,'url':url,'sha256_attendu':digest,'sha256_observe':observed,'verifie':bool(digest),'dossier':str(folder),'taille':p.stat().st_size})
data={'date_utc':datetime.now(timezone.utc).isoformat(),'keycloak_version':release['tag_name'],'jdk_version':jdk['version']['semver'],'composants':manifest}
(DEST/'versions.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
passwords={'bootstrap':secrets.token_urlsafe(28),'LAB-ADMIN':secrets.token_urlsafe(28),'LAB-LECTEUR':secrets.token_urlsafe(28)}
# Ce fichier est local, soumis aux ACL privees du dossier ; il ne sera jamais livre.
if not (DEST/'secrets_locaux.json').exists():(DEST/'secrets_locaux.json').write_text(json.dumps(passwords),encoding='utf-8')
print(json.dumps(data),flush=True)
