from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'MANIFEST_PUBLIC.json').read_text(encoding='utf-8'))
for item in manifest['files']:
    p=root/item['path']
    assert p.is_file(),item['path']
    assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],item['path']
print(f"{len(manifest['files'])} fichiers vérifiés")
