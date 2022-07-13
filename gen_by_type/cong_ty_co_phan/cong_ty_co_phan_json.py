import json
import os
import random


def data_generator(city_path: str,
                   save_path: str):
    data = {
        "paragraph": {},
        "table": []
    }
    # processing city data
    with open(city_path, 'r', encoding='utf-8') as f:
        city_data = json.loads(f.read())
    data['paragraph']['city_name'] = random.choice(city_data)
    # ending processing city data

    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    city_path = r'D:\python_project\doc_gen\data\city.json'
    save_path = r'D:\python_project\doc_gen\gen_by_type\cong_ty_co_phan\json_data'
    data_number = 1
    for i in range(data_number):
        save_path = os.path.join(save_path, '{}.json'.format(i))
        data_generator(city_path, save_path)
