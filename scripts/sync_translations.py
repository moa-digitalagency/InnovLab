import json
import os

def sync_translations():
    lang_dir = 'lang'
    fr_file = os.path.join(lang_dir, 'fr.json')

    with open(fr_file, 'r', encoding='utf-8') as f:
        fr_data = json.load(f)

    for filename in os.listdir(lang_dir):
        if filename.endswith('.json') and filename != 'fr.json':
            filepath = os.path.join(lang_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                target_data = json.load(f)

            updated = False
            for key, value in fr_data.items():
                if key not in target_data:
                    target_data[key] = value
                    updated = True
                elif isinstance(value, dict) and isinstance(target_data.get(key), dict):
                    # For nested dictionaries
                    for subkey, subvalue in value.items():
                        if subkey not in target_data[key]:
                            target_data[key][subkey] = subvalue
                            updated = True

            if updated:
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(target_data, f, ensure_ascii=False, indent=4)
                print(f"Updated {filename}")
            else:
                print(f"No missing keys in {filename}")

if __name__ == "__main__":
    sync_translations()
