import json
import os

data = []
data_path = r'D:\python_project\doc_gen\gen_by_type\ho_kinh_doanh\image_result'
for root in os.listdir(data_path):
    for folder in os.listdir(os.path.join(data_path, root)):
        with open(os.path.join(data_path, root, folder, 'link.txt'), 'r', encoding='utf-8') as f:
            link_data = json.loads(f.read())
        data.append({
            "file_name": "{}__{}".format(root, folder),
            'target': link_data
        })

save_path = r'D:\python_project\doc_gen\gen_by_type\ho_kinh_doanh\link.json'
with open(save_path, 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=4))
    print(len(data))
