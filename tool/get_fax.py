import json
import pandas as pd
import re

fax_data = {}
excel_paths = [
    r'D:\python_project\doc_gen\excel_data\TTV.VN FREE - 370.000 DOANH NGHIEP TOAN QUOC P1 .xls',
    r'D:\python_project\doc_gen\excel_data\TTV.VN FREE - 370.000 DOANH NGHIEP TOAN QUOC P2.xls'
]
pattern = r'[0-9]{8}'

for excel_path in excel_paths:
    fax_excel = pd.read_excel(excel_path, sheet_name='Sheet1', engine='xlrd', header=2)
    tmp = fax_excel['TEL/FAX'].dropna().tolist()
    for item in tmp:
        if type(item) != str:
            item = str(item)
        find_item = re.findall(pattern, item)
        for item1 in find_item:
            fax_data[item1.strip()] = 1

phone = list(fax_data.keys())
save_path = r'D:\python_project\doc_gen\data\fax.json'
with open(save_path, 'w', encoding='utf-8') as f:
    f.write(json.dumps(phone, indent=4))
    print(len(phone))
