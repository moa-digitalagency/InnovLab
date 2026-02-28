import json
import os

langs = ['fr', 'en', 'es', 'pt', 'it', 'de', 'ar', 'zh', 'ja', 'ko']
base_lang = 'fr'

def get_keys(d, prefix=''):
    keys = []
    for k, v in d.items():
        full_key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            keys.extend(get_keys(v, full_key))
        else:
            keys.append(full_key)
    return keys

try:
    with open(f'lang/{base_lang}.json', 'r', encoding='utf-8') as f:
        base_keys = set(get_keys(json.load(f)))

    print(f"✅ Langue de base ({base_lang}) chargée : {len(base_keys)} clés trouvées.\n")

    all_good = True
    for lang in langs:
        if lang == base_lang: continue
        path = f'lang/{lang}.json'
        if not os.path.exists(path):
            print(f"❌ Fichier manquant : {path}")
            all_good = False
            continue

        with open(path, 'r', encoding='utf-8') as f:
            try:
                lang_keys = set(get_keys(json.load(f)))
                missing = base_keys - lang_keys
                if missing:
                    print(f"❌ {lang}.json : Il manque {len(missing)} clés -> {list(missing)[:5]}...")
                    all_good = False
                else:
                    print(f"✅ {lang}.json : Intégrité vérifiée à 100%.")
            except json.JSONDecodeError:
                print(f"❌ {lang}.json : JSON invalide !")
                all_good = False

    if all_good:
        print("\n🚀 SUCCÈS TOTAL : Toutes les langues sont parfaitement synchronisées !")
except Exception as e:
    print(f"Erreur : {e}")
