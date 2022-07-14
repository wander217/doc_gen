import json

data_path = r'D:\python_project\doc_gen\excel_data\job_id.json'

with open(data_path, 'r', encoding='utf-8') as f:
    data = json.loads(f.read())

new_data = []
for item in data:
    if item['C6']:
        new_data.append({
            "name": item['C7'],
            "code": item['C6']
        })
    elif item['C5']:
        new_data.append({
            "name": item['C7'],
            "code": item['C5']
        })
    elif item['C4']:
        new_data.append({
            "name": item['C7'],
            "code": item['C4']
        })
    elif item['C3']:
        new_data.append({
            "name": item['C7'],
            "code": item['C3']
        })

save_path = r'D:\python_project\doc_gen\data\job.json'
with open(save_path, 'w', encoding='utf-8') as f:
    f.write(json.dumps(new_data, indent=4))
