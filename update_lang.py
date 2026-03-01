import json
import glob

files = glob.glob('lang/*.json')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if 'hero' in data and 'title' in data['hero']:
        title = data['hero']['title']
        # replace <br/> tags
        title = title.replace('<br/> ', '').replace(' <br/>', '').replace('<br/>', ' ')
        data['hero']['title'] = title

    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
