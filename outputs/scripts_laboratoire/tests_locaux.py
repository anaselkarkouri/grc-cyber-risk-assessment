"""T04 et T03 : executions locales, exclusivement dans un nouveau dossier date."""
from pathlib import Path
from datetime import datetime, timezone
import subprocess, json, hashlib, shutil, time, zipfile

ROOT = Path(__file__).resolve().parents[2]
LAB = ROOT / 'work/grc_laboratoire'
ANN = ROOT / 'outputs/Portfolio_GRC_Anas/Annexes_laboratoire'
STAMP = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
RUN = LAB / ('execution_' + STAMP)
PROOF = ANN / 'preuves' / STAMP
RUN.mkdir(parents=True, exist_ok=False)
PROOF.mkdir(parents=True, exist_ok=False)

def now(): return datetime.now(timezone.utc).isoformat()
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name, obj):
    (PROOF / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')
def cmd(args, cwd=None):
    p = subprocess.run(args, cwd=cwd, capture_output=True, encoding='utf-8', errors='replace')
    return {'date_utc':now(), 'commande':args, 'code':p.returncode, 'stdout':p.stdout, 'stderr':p.stderr}
def acl(p): return cmd(['icacls.exe', str(p)])

# Aucun fichier de reference n'est modifie avant cette copie.
ref = LAB / ('reference_avant_retest_' + STAMP)
shutil.copytree(ROOT/'outputs/Portfolio_GRC_Anas', ref/'Portfolio_GRC_Anas')
# La reproduction publique conserve les cas et preuves, sans CV personnel.
save('REFERENCE_MANIFEST.json', [{'path':str(p.relative_to(ref)), 'sha256':sha(p)} for p in ref.rglob('*') if p.is_file()])

git = r'C:\Program Files\Git\cmd\git.exe'
repo = RUN/'T04_secrets_git/depot_demo'
repo.mkdir(parents=True)
glog=[]
def g(*a, ok=(0,)):
    r=cmd([git,*a], repo); glog.append(r)
    if r['code'] not in ok: raise RuntimeError(r)
    return r['stdout'].strip()
g('init','--initial-branch=main')
g('config','user.name','LAB-GRC')
g('config','user.email','lab-grc@example.invalid')
g('config','commit.gpgsign','false')
g('config','core.autocrlf','false')
cfg=repo/'configuration.txt'
cfg.write_text('usage=donnees-artificielles\nmarqueur=SECRET-DEMO-NON-UTILISABLE\n',encoding='utf-8')
initial=cfg.read_text(encoding='utf-8')
g('add','configuration.txt'); g('commit','-m','T04 marqueur inoffensif initial')
c1=g('rev-parse','HEAD')
cfg.write_text('usage=donnees-artificielles\nmarqueur=retire-de-la-version-courante\n',encoding='utf-8')
g('add','configuration.txt'); g('commit','-m','T04 retrait du marqueur courant')
c2=g('rev-parse','HEAD')
current=g('show','HEAD:configuration.txt'); old=g('show',c1+':configuration.txt')
g('grep','-n','SECRET-DEMO-NON-UTILISABLE','HEAD',ok=(1,))
g('grep','-n','SECRET-DEMO-NON-UTILISABLE',c1)
g('log','--format=fuller','--date=iso-strict'); g('remote','-v'); g('status','--porcelain')
save('T04-P01_perimetre_droits.json', {'date_utc':now(),'repo':str(repo),'version':cmd([git,'--version']),'droits':[acl(repo),acl(repo/'.git')], 'distant':False})
save('T04-P02_premier_commit.json', {'commit':c1,'contenu':initial,'marqueur_inutilisable':True})
save('T04-P03_historique.json', {'date_utc':now(),'commit_initial':c1,'commit_courant':c2,'courant':current,'ancien':old,'commandes':glog,'courant_sans_marqueur':'SECRET-DEMO-NON-UTILISABLE' not in current,'ancien_avec_marqueur':'SECRET-DEMO-NON-UTILISABLE' in old})
assert 'SECRET-DEMO-NON-UTILISABLE' not in current and 'SECRET-DEMO-NON-UTILISABLE' in old
save('T04-P04_conclusion.json', {'statut':'reussi','perimetre':'un fichier, deux commits, ACL NTFS locales','limites':['aucune cle utilisable','aucune rotation','aucun role GitHub','aucune recherche exhaustive de secrets']})

t3=RUN/'T03_sauvegarde_restauration'; src=t3/'source'; dst=t3/'restaure'
src.mkdir(parents=True); dst.mkdir()
items=[{'id':'LAB-001','titre':'Acces fictif','etat':'ouvert','texte':'Ticket artificiel numero un.'}, {'id':'LAB-002','titre':'Restauration de controle','etat':'en cours','texte':'Donnees artificielles avec accents : integrite, recuperation.'}, {'id':'LAB-003','titre':'Verification terminée','etat':'clos','texte':'Aucun client reel, aucune donnee personnelle.'}]
expected=[]
for item in items:
    p=src/(item['id']+'.json'); p.write_text(json.dumps(item,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    expected.append({'fichier':p.name,'contenu':item,'taille':p.stat().st_size,'sha256':sha(p)})
save('T03-P01_attendus.json', {'date_utc':now(),'source':str(src),'fichiers':expected})
archive=t3/'sauvegarde_tickets.zip'; start=now(); b=time.perf_counter()
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for p in sorted(src.iterdir()): z.write(p,p.name)
btime=time.perf_counter()-b; bend=now()
save('T03-P02_copie.json', {'debut_utc':start,'fin_utc':bend,'duree_secondes':btime,'mecanisme':'Python zipfile ZIP_DEFLATED, archive locale de fichiers','archive':str(archive),'taille':archive.stat().st_size,'sha256':sha(archive),'fichiers':zipfile.ZipFile(archive).namelist(),'droits':acl(archive)})
rstart=now(); age=time.time()-archive.stat().st_mtime; b=time.perf_counter()
with zipfile.ZipFile(archive) as z:
    for info in z.infolist():
        target=(dst/info.filename).resolve()
        if not target.is_relative_to(dst.resolve()): raise ValueError('Chemin ZIP hors laboratoire')
    z.extractall(dst)
rtime=time.perf_counter()-b; rend=now(); result=[]
for e in expected:
    p=dst/e['fichier']; actual=json.loads(p.read_text(encoding='utf-8'))
    result.append({'fichier':p.name,'taille_attendue':e['taille'],'taille_observee':p.stat().st_size,'sha256_attendu':e['sha256'],'sha256_observe':sha(p),'contenu_observe':actual,'egalite_contenu':actual==e['contenu'],'egalite_taille':p.stat().st_size==e['taille'],'egalite_sha256':sha(p)==e['sha256']})
save('T03-P03_comparaison.json', {'date_utc':now(),'restauration':str(dst),'fichiers':result,'droits_source':acl(src),'droits_restauration':acl(dst)})
assert all(x['egalite_contenu'] and x['egalite_taille'] and x['egalite_sha256'] for x in result)
save('T03-P04_chronologie.json', {'debut_utc':rstart,'fin_utc':rend,'duree_restauration_secondes':rtime,'age_copie_secondes':age,'statut':'reussi','limites':['copie sur le meme volume et sous le meme utilisateur','pas de stockage immuable ni de copie hors site','ni application ni base SaaS restauree','RTO huit heures et RPO 24 heures non prouves'],'python':cmd([__import__('sys').executable,'--version'])})
shutil.copy2(archive,PROOF/'T03_copie_artificielle.zip')
save('MANIFEST_PREUVES.json', [{'fichier':p.name,'taille':p.stat().st_size,'sha256':sha(p)} for p in sorted(PROOF.iterdir()) if p.is_file()])
(LAB/'derniere_execution_locale.json').write_text(json.dumps({'run':str(RUN),'preuves':str(PROOF),'reference':str(ref),'date_utc':now()},indent=2),encoding='utf-8')
print(json.dumps({'T04':'reussi','T03':'reussi','restauration_secondes':rtime,'preuves':str(PROOF),'reference':str(ref)}))
