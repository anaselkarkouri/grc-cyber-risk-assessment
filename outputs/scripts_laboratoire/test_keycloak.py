"""Test du veritable Keycloak par HTTP. Aucun token, secret TOTP ou mot de passe dans les preuves."""
from pathlib import Path
from datetime import datetime, timezone
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'python_deps'))
import json, requests, time, secrets, hashlib, base64, hmac, struct, subprocess, os
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[2]; D=ROOT/'work/grc_laboratoire/T01_acces_mfa'
BASE='https://127.0.0.1:18443'; REALM='grc-lab'
os.environ['REQUESTS_CA_BUNDLE']=str(D/'localhost.pem')
P=ROOT/'outputs/Portfolio_GRC_Anas/Annexes_laboratoire/preuves'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
P.mkdir(parents=True,exist_ok=False)
S=json.loads((D/'secrets_locaux.json').read_text()); V=json.loads((D/'versions.json').read_text())
def save(name,data):
 (P/name).write_text(json.dumps({'date_utc':datetime.now(timezone.utc).isoformat(),**data},ensure_ascii=False,indent=2),encoding='utf-8')
def otp(secret):
 b32=secret.replace(' ','').upper();key=base64.b32decode(b32+'='*((-len(b32))%8)); n=int(time.time())//30
 digest=hmac.new(key,struct.pack('>Q',n),hashlib.sha1).digest(); o=digest[-1]&15
 return f'{(struct.unpack(">I",digest[o:o+4])[0]&0x7fffffff)%1000000:06d}'
boot=requests.post(BASE+'/realms/master/protocol/openid-connect/token',data={'grant_type':'password','client_id':'admin-cli','username':'LAB-RECOVERY','password':S['bootstrap']},timeout=10)
boot.raise_for_status(); H={'Authorization':'Bearer '+boot.json()['access_token']}
def api(method,path,data=None):
 r=requests.request(method,BASE+'/admin/'+path,headers=H,json=data,timeout=10)
 if r.status_code>=400:raise RuntimeError(f'API {method} {path}: {r.status_code} {r.text[:200]}')
 return r
if requests.get(BASE+'/admin/realms/'+REALM,headers=H).status_code==404:
 api('POST','realms',{'realm':REALM,'enabled':True,'sslRequired':'none','registrationAllowed':False,'resetPasswordAllowed':False,'rememberMe':False,'otpPolicyType':'totp','otpPolicyAlgorithm':'HmacSHA1','otpPolicyDigits':6,'otpPolicyPeriod':30,'otpPolicyLookAheadWindow':1,'eventsEnabled':True,'eventsExpiration':86400,'adminEventsEnabled':True,'adminEventsDetailsEnabled':False,'accessTokenLifespan':60,'ssoSessionIdleTimeout':300,'ssoSessionMaxLifespan':1800})
r=api('GET','realms/'+REALM+'/authentication/required-actions').json()
action=next(x for x in r if x['alias']=='CONFIGURE_TOTP'); action['enabled']=True;action['defaultAction']=True
api('PUT','realms/'+REALM+'/authentication/required-actions/CONFIGURE_TOTP',action)
clients=api('GET','realms/'+REALM+'/clients').json()
if not any(x['clientId']=='grc-evidence' for x in clients):
 api('POST','realms/'+REALM+'/clients',{'clientId':'grc-evidence','enabled':True,'publicClient':True,'standardFlowEnabled':True,'directAccessGrantsEnabled':False,'redirectUris':['http://127.0.0.1:18081/callback'],'attributes':{'pkce.code.challenge.method':'S256'}})
clients=api('GET','realms/'+REALM+'/clients').json(); mc=next(x['id'] for x in clients if x['clientId']=='realm-management')
ids={}
for user in ['LAB-ADMIN','LAB-LECTEUR']:
 users=api('GET','realms/'+REALM+'/users?username='+user+'&exact=true').json()
 if not users:
  api('POST','realms/'+REALM+'/users',{'username':user,'enabled':True,'firstName':'Laboratoire','lastName':user,'email':user.lower()+'@example.invalid','requiredActions':['CONFIGURE_TOTP'],'credentials':[{'type':'password','value':S[user],'temporary':False}]})
 users=api('GET','realms/'+REALM+'/users?username='+user+'&exact=true').json(); ids[user]=users[0]['id']
 roles=['realm-admin'] if user=='LAB-ADMIN' else ['query-users','view-users']
 mappings=[api('GET',f'realms/{REALM}/clients/{mc}/roles/{role}').json() for role in roles]
 api('POST',f'realms/{REALM}/users/{ids[user]}/role-mappings/clients/{mc}',mappings)

flow=api('GET',f'realms/{REALM}/authentication/flows/browser/executions').json()
save('T01-P01_regles_roles.json',{'service':BASE,'realm':REALM,'versions':V,'java_version':subprocess.run([str(Path(V['composants'][1]['dossier'])/'bin/java.exe'),'-version'],capture_output=True,text=True).stderr,'comptes':{'LAB-ADMIN':['realm-management/realm-admin'],'LAB-LECTEUR':['realm-management/query-users','realm-management/view-users']},'actions_obligatoires':{'CONFIGURE_TOTP':{'enabled':action['enabled'],'defaultAction':action['defaultAction']}},'flux_navigateur':[{k:e.get(k) for k in ['displayName','providerId','requirement','authenticationFlow']} for e in flow],'direct_access_grants_client':False,'resetPasswordAllowed':False,'registrationAllowed':False,'limite_bootstrap':'LAB-RECOVERY du realm master, exception de mise en place locale, hors comptes de test'})

def login(user, enroll=False, stop_at_otp=False, wrong=False):
 sess=requests.Session(); verifier=secrets.token_urlsafe(48)
 challenge=base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).decode().rstrip('=')
 params={'client_id':'grc-evidence','redirect_uri':'http://127.0.0.1:18081/callback','response_type':'code','scope':'openid','state':secrets.token_urlsafe(16),'nonce':secrets.token_urlsafe(16),'code_challenge':challenge,'code_challenge_method':'S256','prompt':'login'}
 page=sess.get(BASE+f'/realms/{REALM}/protocol/openid-connect/auth',params=params,timeout=10)
 soup=BeautifulSoup(page.text,'html.parser'); form=soup.find('form',id='kc-form-login')
 assert form, 'Formulaire mot de passe absent'
 data={i.get('name'):i.get('value','') for i in form.find_all('input') if i.get('name') and i.get('type')=='hidden'}
 data.update(username=user,password=S[user])
 page=sess.post(form['action'],data=data,allow_redirects=False,timeout=10)
 trace={'compte':user,'nouvelle_session_http':True,'mot_de_passe_http':page.status_code,'token_apres_mot_de_passe':False}
 for _ in range(8):
  if page.status_code not in (302,303):break
  location=page.headers['Location']
  assert location.startswith(BASE), 'Authentification terminee sans OTP ou redirection externe inattendue'
  page=sess.get(location,allow_redirects=False,timeout=10)
 soup=BeautifulSoup(page.text,'html.parser')
 enroll_form=soup.find('form',id='kc-totp-settings-form'); otp_form=soup.find('form',id='kc-otp-login-form')
 if enroll_form:
  manual=soup.find('a',id='mode-manual')
  if manual:
   page=sess.get(manual['href'],timeout=10);soup=BeautifulSoup(page.text,'html.parser');enroll_form=soup.find('form',id='kc-totp-settings-form')
  secret_field=soup.find('input',{'name':'totpSecret'})
  assert secret_field, 'Secret TOTP fourni par Keycloak absent'
  visible=soup.find(id='kc-totp-secret-key')
  if not visible:
   (D/'diagnostic_page.html').write_text(page.text,encoding='utf-8');raise RuntimeError('Cle manuelle OTP non trouvee')
  secret=visible.get_text(strip=True); S[user+'_totp']=secret
  (D/'secrets_locaux.json').write_text(json.dumps(S),encoding='utf-8')
  data={i.get('name'):i.get('value','') for i in enroll_form.find_all('input') if i.get('name') and i.get('type')=='hidden'}
  data.update(totp=otp(secret),userLabel='LAB-TOTP',**{'save':'Save'})
  page=sess.post(enroll_form['action'],data=data,allow_redirects=False,timeout=10)
  trace['enrolement_keycloak']=True
 elif otp_form:
  trace['challenge_otp_apres_mot_de_passe']=True
  if stop_at_otp:return trace,None
  data={i.get('name'):i.get('value','') for i in otp_form.find_all('input') if i.get('name') and i.get('type')=='hidden'}
  code=otp(S[user+'_totp']); data['otp']=('000000' if code!='000000' else '999999') if wrong else code
  page=sess.post(otp_form['action'],data=data,allow_redirects=False,timeout=10)
  if wrong:
   trace['mauvais_otp_http']=page.status_code;trace['mauvais_otp_refuse']=BeautifulSoup(page.text,'html.parser').find('form',id='kc-otp-login-form') is not None
   return trace,None
 else:
  (D/'diagnostic_page.html').write_text(page.text,encoding='utf-8')
  raise RuntimeError('Ni enrolement ni challenge OTP ; diagnostic prive en laboratoire')
 # Suivre uniquement les redirections internes ; le callback contient un code ephemere jamais exporte.
 for _ in range(8):
  if page.status_code in (302,303):
   location=page.headers['Location']
   if location.startswith('http://127.0.0.1:18081/callback'):break
   page=sess.get(location,allow_redirects=False,timeout=10)
  else:
   (D/'diagnostic_page.html').write_text(page.text,encoding='utf-8');raise RuntimeError('Redirection OIDC absente apres OTP')
 from urllib.parse import urlparse,parse_qs
 q=parse_qs(urlparse(location).query)
 assert q['state'][0]==params['state']
 code=q['code'][0]
 token=sess.post(BASE+f'/realms/{REALM}/protocol/openid-connect/token',data={'grant_type':'authorization_code','client_id':'grc-evidence','redirect_uri':params['redirect_uri'],'code':code,'code_verifier':verifier},timeout=10)
 token.raise_for_status();trace['otp_valide_token_http']=token.status_code
 result=token.json();result['_http_session']=sess;result['_auth_params']=params
 return trace,result

traces=[]
for user in ids:
 trace,tok=login(user,enroll=True);traces.append(trace)
trace,_=login('LAB-ADMIN',stop_at_otp=True);traces.append(trace);assert trace.get('challenge_otp_apres_mot_de_passe')
trace,_=login('LAB-ADMIN',wrong=True);traces.append(trace);assert trace['mauvais_otp_refuse']
# Eviter le rejet du rejeu d'un OTP deja employe pendant l'enrolement.
time.sleep(31-int(time.time())%30)
reader_trace,rtok=login('LAB-LECTEUR');admin_trace,atok=login('LAB-ADMIN');traces.extend([reader_trace,admin_trace])
RH={'Authorization':'Bearer '+rtok['access_token']};AH={'Authorization':'Bearer '+atok['access_token']}
allowed=requests.get(BASE+f'/admin/realms/{REALM}/users',headers=RH,timeout=10)
denied=requests.put(BASE+f'/admin/realms/{REALM}',headers=RH,json={'displayName':'GRC LAB'},timeout=10)
admin=requests.put(BASE+f'/admin/realms/{REALM}',headers=AH,json={'displayName':'GRC LAB'},timeout=10)
save('T01-P02_autorisations.json',{'lecteur_lecture_utilisateurs':allowed.status_code,'lecteur_modification_realm':denied.status_code,'admin_modification_realm':admin.status_code,'resultats_attendus':[200,403,204],'etendue':'API administrative native Keycloak, droits serveur controles'})
assert (allowed.status_code,denied.status_code,admin.status_code)==(200,403,204)
save('T01-P03_mfa.json',{'observations':traces,'facteur':'TOTP RFC 6238, service Keycloak, 6 chiffres/30 secondes SHA1','secrets_exportes':False,'limite':'TOTP genere par automatisation sur ce meme poste ; pas de preuve de possession d un telephone distinct ni de resistance au phishing'})
alternatives=[]
for client in ['grc-evidence','admin-cli']:
 grant=requests.post(BASE+f'/realms/{REALM}/protocol/openid-connect/token',data={'grant_type':'password','client_id':client,'username':'LAB-ADMIN','password':S['LAB-ADMIN']},timeout=10)
 alternatives.append({'client':client,'mot_de_passe_seul_http':grant.status_code,'error':grant.json().get('error'),'token_delivre':'access_token' in grant.json()})
 assert grant.status_code==400 and 'access_token' not in grant.json()
save('T01_chemins_alternatifs.json',{'tests':alternatives,'limite':'Deux clients examines seulement ; ne remplace pas un inventaire de tous les flux et clients en production.'})
before=api('GET',f'realms/{REALM}/users/{ids["LAB-ADMIN"]}/sessions').json()
logout=api('POST',f'realms/{REALM}/users/{ids["LAB-ADMIN"]}/logout')
after=api('GET',f'realms/{REALM}/users/{ids["LAB-ADMIN"]}/sessions').json()
refresh=requests.post(BASE+f'/realms/{REALM}/protocol/openid-connect/token',data={'grant_type':'refresh_token','client_id':'grc-evidence','refresh_token':atok['refresh_token']},timeout=10)
introspect=requests.post(BASE+f'/realms/{REALM}/protocol/openid-connect/token/introspect',data={'token':atok['access_token']},timeout=10)
params=dict(atok['_auth_params'],prompt='none')
silent=atok['_http_session'].get(BASE+f'/realms/{REALM}/protocol/openid-connect/auth',params=params,allow_redirects=False,timeout=10)
from urllib.parse import urlparse,parse_qs
silent_error=parse_qs(urlparse(silent.headers.get('Location','')).query).get('error',['non_observe'])[0]
old_access=requests.get(BASE+f'/admin/realms/{REALM}/users',headers=AH,timeout=10)
save('T01-P04_revocation_recuperation.json',{'sessions_avant':len(before),'revoke_http':logout.status_code,'sessions_apres':len(after),'refresh_apres_revocation_http':refresh.status_code,'refresh_erreur':refresh.json().get('error'),'sso_silencieux_apres_revocation_http':silent.status_code,'sso_erreur':silent_error,'api_ancien_access_token_http':old_access.status_code,'recuperation':'Pas de mail ni codes de recuperation actives ; LAB-RECOVERY master peut reinitialiser apres controle local. Exception bootstrap locale privee, pas une procedure organisationnelle validee.','exception':'bootstrap master utilise pour configurer et revoquer ; politique OTP testee sur LAB-ADMIN et LAB-LECTEUR seulement','limite_jeton':'JWT deja emis peut rester valable jusqu a expiration selon la ressource ; duree configuree 60 secondes. Revocation des sessions, SSO et refresh testee ; pas de revocation immediate universelle dans des applications tierces.'})
assert before and not after and refresh.status_code==400 and refresh.json().get('error')=='invalid_grant'
assert silent_error=='login_required'
events=api('GET',f'realms/{REALM}/events?max=100').json()
save('T01_evenements_assainis.json',{'evenements':[{'time':e.get('time'),'type':e.get('type'),'error':e.get('error'),'clientId':e.get('clientId'),'realmId':REALM} for e in events]})
save('T01_statut.json',{'statut':'reussi','perimetre':'deux comptes Keycloak, API roles, MFA TOTP et session/refresh','preuves':[x.name for x in P.iterdir()]})
(D/'derniere_preuve.json').write_text(json.dumps({'path':str(P)}),encoding='utf-8')
print(json.dumps({'T01':'reussi','preuves':str(P)}))
