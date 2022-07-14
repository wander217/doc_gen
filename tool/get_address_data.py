import json

import pandas as pd

address_data = {}
excel_paths = [
    r'D:\python_project\doc_gen\excel_data\TTV.VN FREE - 370.000 DOANH NGHIEP TOAN QUOC P1 .xls',
    r'D:\python_project\doc_gen\excel_data\TTV.VN FREE - 370.000 DOANH NGHIEP TOAN QUOC P2.xls'
]

for excel_path in excel_paths:
    address_excel = pd.read_excel(excel_path, sheet_name='Sheet1', engine='xlrd', header=2)
    tmp = address_excel['DIA CHI'].dropna().tolist()
    tmp1 = address_excel['TINH THANH'].dropna().tolist()
    for address, city in zip(tmp, tmp1):
        if type(address) == str:
            address_data[address.strip() + " " + city] = 1

address = list(address_data.keys())
save_path = r'D:\python_project\doc_gen\data\address.json'
with open(save_path, 'w', encoding='utf-8') as f:
    f.write(json.dumps(address, indent=4))
