import json
import pandas as pd

company_data = {}
excel_paths = [
    r'D:\python_project\doc_gen\excel_data\4.000 DOANH NGHIEP HN.xls',
]

for excel_path in excel_paths:
    company_excel = pd.read_excel(excel_path, sheet_name='Sheet1', engine='xlrd', header=0)
    tmp = company_excel['Ten tat (T.Anh)'].dropna().tolist()
    for item in tmp:
        if type(item) == str:
            company_data[item.strip()] = 1

company = list(company_data.keys())
save_path = r'D:\python_project\doc_gen\data\eng_company.json'
with open(save_path, 'w', encoding='utf-8') as f:
    f.write(json.dumps(company, indent=4))
    print(len(company))
