import json
import glob

files = glob.glob('lang/*.json')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"{file}: {data.get('hero', {}).get('title', '')}")
