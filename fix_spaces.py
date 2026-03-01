import json
import glob
import re

files = glob.glob('lang/*.json')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if 'hero' in data and 'title' in data['hero']:
        title = data['hero']['title']

        # Add a space before and after the span tag if there's no space and it's not CJK text
        # Specifically fixing issues like "Costruireil <span...", "tecnologico</span>dell'Africa"
        if file.endswith('it.json'):
            title = title.replace('Costruireil', 'Costruire il')
            title = title.replace('</span>dell\'Africa', '</span> dell\'Africa')
        elif file.endswith('pt.json'):
            title = title.replace('Construindoo', 'Construindo o')
            title = title.replace('</span>da África', '</span> da África')
        elif file.endswith('de.json'):
            title = title.replace('Aufbauder', 'Aufbau der')
            title = title.replace('</span>Afrikas', '</span> Afrikas')
        elif file.endswith('ar.json'):
            title = title.replace('بناء<span', 'بناء <span')
            title = title.replace('</span>في أفريقيا', '</span> في أفريقيا')
        elif file.endswith('zh.json'):
            # It already has space "建设 非洲的" maybe too much
            pass

        data['hero']['title'] = title

    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
