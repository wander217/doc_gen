import json
import pandas as pd
import re

phone_data = {}
excel_paths = [
    r'D:\python_project\doc_gen\excel_data\TTV.VN FREE - 370.000 DOANH NGHIEP TOAN QUOC P1 .xls',
    r'D:\python_project\doc_gen\excel_data\TTV.VN FREE - 370.000 DOANH NGHIEP TOAN QUOC P2.xls'
]
pattern = r'[0-9]{9}'
pattern1 = r'[0-9]{10}'

for excel_path in excel_paths:
    company_excel = pd.read_excel(excel_path, sheet_name='Sheet1', engine='xlrd', header=2)
    tmp = company_excel['DI DONG'].dropna().tolist()
    for item in tmp:
        if type(item) == str:
            find_item = re.findall(pattern, item)
            for item1 in find_item:
                if item1[0] != '0':
                    item1 = '0' + item1
                phone_data[item1.strip()] = 1
            find_item = re.findall(pattern1, item)
            for item1 in find_item:
                phone_data[item1.strip()] = 1

phone = list(phone_data.keys())
save_path = r'D:\python_project\doc_gen\data\phone.json'
with open(save_path, 'w', encoding='utf-8') as f:
    f.write(json.dumps(phone, indent=4))
    print(len(phone))
