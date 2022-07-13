import json
import unicodedata

city_path = r'D:\python_project\doc_gen\data\raw_address.json'
with open(city_path, 'r', encoding='utf-8') as f:
    data = json.loads(f.read())

city = {
    "thanh_pho": [],
    "tinh": []
}

key = unicodedata.normalize("NFC", "Thành phố")
for item in data['data']:
    item_name = unicodedata.normalize("NFC", item['name'])
    if "Thành phố" in item_name:
        city['thanh_pho'].append(item_name)
    else:
        city['tinh'].append(item_name)

save_path = r'D:\python_project\doc_gen\data\city.json'

with open(save_path, 'w', encoding='utf-8') as f:
    f.write(json.dumps(city))

print(city)