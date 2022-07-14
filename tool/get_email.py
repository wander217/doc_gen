import json
import pandas as pd

company_data = {}
excel_paths = [
    r'D:\python_project\doc_gen\excel_data\TTV.VN FREE - 370.000 DOANH NGHIEP TOAN QUOC P1 .xls',
    r'D:\python_project\doc_gen\excel_data\TTV.VN FREE - 370.000 DOANH NGHIEP TOAN QUOC P2.xls'
]

for excel_path in excel_paths:
    company_excel = pd.read_excel(excel_path, sheet_name='Sheet1', engine='xlrd', header=2)
    tmp = company_excel['EMAIL'].dropna().tolist()
    for item in tmp:
        if type(item) == str:
            company_data[item.strip()] = 1

company = list(company_data.keys())
save_path = r'D:\python_project\doc_gen\data\email.json'
with open(save_path, 'w', encoding='utf-8') as f:
    f.write(json.dumps(company, indent=4))
    print(len(company))
