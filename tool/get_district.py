import json

data_path = r'D:\python_project\doc_gen\template\raw_address.json'

with open(data_path, 'r', encoding='utf-8') as f:
    data = json.loads(f.read())

district = []
for item in data['data']:
    for item1 in item['level2s']:
        district.append(item1['name'])

save_path = r'D:\python_project\doc_gen\data\district.json'
with open(save_path, 'w', encoding='utf-8') as f:
    f.write(json.dumps(district, indent=4))
    print(len(district))