import json

save_path = r'D:\python_project\doc_gen\data\day.json'
data = [
    'Thứ hai',
    'Thứ ba',
    'Thứ tư',
    'Thứ năm',
    'Thứ sáu',
    'Thứ bảy',
    'Chủ nhật'
]
with open(save_path, 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=4))
