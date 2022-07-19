import json
import pandas as pd

idcard_code_data = {}
excel_paths = [
    r'D:\python_project\doc_gen\template\6_DS 15.700 GIAM DOC TAI HA NOI.xls'
]

for excel_path in excel_paths:
    company_excel = pd.read_excel(excel_path, sheet_name='2300 CTY MOI THANH LAP HN 2010', engine='xlrd', header=1)
    tmp = company_excel['Số CMTND/Hộ chiếu'].dropna().tolist()
    for item in tmp:
        if type(item) == str:
            idcard_code_data[item.strip()] = 1

idcard_code = list(idcard_code_data.keys())
save_path = r'D:\python_project\doc_gen\data\idcard_code.json'
with open(save_path, 'w', encoding='utf-8') as f:
    f.write(json.dumps(idcard_code, indent=4))
    print(len(idcard_code))

