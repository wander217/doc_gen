import json
import os
import random
from faker import Faker
from vietnam_number import n2w
from vn_fullname_generator import generator


def data_gen():
    date = Faker().date_object()
    format_string = 'ngày {} tháng {} năm {}'.format(date.day, date.month, date.year)
    return format_string


def amount_list_2_number(amount_list: list):
    amount = 0
    for item in amount_list:
        amount = amount * 1000 + int(item)
    return amount


def get_amount_character(amount_list: list):
    amount = amount_list_2_number(amount_list)
    new_text = n2w(str(amount)).capitalize()
    new_text = " ".join(new_text.split(" ")[:-2])
    return new_text


def amount_list_2_text(amount_list):
    norm_amount_list = []
    for i, amount in enumerate(amount_list):
        if i == 0:
            norm_amount_list.append(amount)
            continue
        tmp = str(amount)
        tmp = ''.join(['0' for _ in range(3 - len(tmp))]) + tmp
        norm_amount_list.append(tmp)
    return '.'.join(norm_amount_list)


def data_generator(city_path: str,
                   vi_name_path: str,
                   foreign_name_path: str,
                   acronym_name_path: str,
                   address_path: str,
                   phone_path: str,
                   fax_path: str,
                   email_path: str,
                   website_path: str,
                   save_path: str,
                   business_type_template: str,
                   business_path:str):
    data = {
        "paragraph": {},
        "table": {}
    }
    # processing city data
    with open(city_path, 'r', encoding='utf-8') as f:
        city_data = json.loads(f.read())
    city_type_dict = random.choice(list(city_data.keys()))
    data['paragraph']['city_name'] = random.choice(city_data[city_type_dict]).upper()
    # ending processing city data

    # processing contract data
    contract_code = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    data['paragraph']['contract_code'] = contract_code
    # ending processing contract data

    # processing first date
    data['paragraph']['first_date'] = "Đăng ký lần đầu, " + data_gen()
    # ending processing first date

    # processing change date
    change_date = ["Đăng ký lần thứ {}, ".format(random.randint(0, 100)) + data_gen()]
    data['paragraph']['change_date'] = random.choice(change_date)
    # ending processing change date

    # processing vietnamese name data
    with open(vi_name_path, 'r', encoding='utf-8') as f:
        vi_name_data = json.loads(f.read())
    data['paragraph']['vietnamese_name'] = random.choice(vi_name_data)
    # ending processing vietnamese name data

    # processing foreign name data
    with open(foreign_name_path, 'r', encoding='utf-8') as f:
        foreign_name_data = json.loads(f.read())
    data['paragraph']['foreign_name'] = random.choice(foreign_name_data)
    # ending processing foreign name data

    # processing acronym name data
    with open(acronym_name_path, 'r', encoding='utf-8') as f:
        acronym_name_data = json.loads(f.read())
    data['paragraph']['acronym_name'] = random.choice(acronym_name_data)
    # ending processing acronym name data

    # processing address data
    with open(address_path, 'r', encoding='utf-8') as f:
        address_data = json.loads(f.read())
    data['paragraph']['company_address'] = random.choice(address_data)
    # ending processing address data

    # processing phone data
    with open(phone_path, 'r', encoding='utf-8') as f:
        phone_data = json.loads(f.read())
    data['paragraph']['phone'] = random.choice(phone_data)
    # ending processing phone data

    # processing fax data
    with open(fax_path, 'r', encoding='utf-8') as f:
        fax_data = json.loads(f.read())
    data['paragraph']['fax'] = random.choice(fax_data)
    # ending processing fax data

    # processing email data
    with open(email_path, 'r', encoding='utf-8') as f:
        email_data = json.loads(f.read())
    data['paragraph']['email'] = random.choice(email_data)
    # ending processing email data

    # processing website data
    with open(website_path, 'r', encoding='utf-8') as f:
        website_data = json.loads(f.read())
    data['paragraph']['website'] = random.choice(website_data)
    # ending processing website data

    # processing capital amount data
    capital_amount = [str(random.randint(1, 999)) if i == 0 else str(random.randint(0, 999))
                      for i in range(random.randint(2, 3))] + ['000']
    data['paragraph']['capital_amount'] = amount_list_2_text(capital_amount) + " đồng"
    # ending processing capital amount data

    # processing capital amount character data
    data['paragraph']['capital_character_amount'] = get_amount_character(capital_amount) + " đồng"
    # ending processing capital amount character data

    # processing capital amount character data
    capital_value = [str(random.randint(1, 999)) if i == 0 else str(random.randint(0, 999))
                     for i in range(1)] + ['000']
    data['paragraph']['capital_value'] = amount_list_2_text(capital_value) + " đồng"
    # ending processing capital amount character data

    # processing total capital data
    total_capital = amount_list_2_number(capital_amount) / amount_list_2_number(capital_value)
    data['paragraph']['total_capital'] = str(int(total_capital))
    # ending processing total capital data

    # processing sale capital data
    data['paragraph']['sale_capital'] = str(random.randint(100, 9999))
    # ending processing sale capital data

    # processing legal capital data
    legal_value = [str(random.randint(1, 999)) if i == 0 else str(random.randint(0, 999))
                   for i in range(3, 5)] + ['000']
    data['paragraph']['legal_capital'] = amount_list_2_text(legal_value) + " đồng"
    # ending processing legal capital data

    # processing owner fullname data
    gender = random.randint(0, 1)
    data['paragraph']['own_fullname'] = generator.generate(gender).upper()
    # ending processing owner fullname data

    # processing owner sex data
    data['paragraph']['own_sex'] = "Nam" if gender == 1 else "Nữ"
    # ending processing owner sex data

    # processing table business type
    data['table']['bt'] = {
        "link": business_type_template,
        'target': []
    }
    with open(business_path, 'r', encoding='utf-8') as f:
        business_data = json.loads(f.read())
    for i in range(random.randint(1, 10)):
        selected_business = random.choice(business_data)
        data['table']['bt']['target'].append({
            "bt_id": str(i + 1),
            "bt_name": selected_business['name'],
            "bt_code": selected_business['code'],
        })
    # ending processing table business type

    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    city_path = r'D:\python_project\doc_gen\data\city.json'
    vi_name_path = r'D:\python_project\doc_gen\data\vi_company_name.json'
    eng_name_path = r'D:\python_project\doc_gen\data\eng_company_name.json'
    short_name_path = r'D:\python_project\doc_gen\data\short_company_name.json'
    address_path = r'D:\python_project\doc_gen\data\address.json'
    phone_path = r'D:\python_project\doc_gen\data\phone.json'
    fax_path = r'D:\python_project\doc_gen\data\fax.json'
    email_path = r'D:\python_project\doc_gen\data\email.json'
    website_path = r'D:\python_project\doc_gen\data\website.json'
    save_path = r'D:\python_project\doc_gen\gen_by_type\cong_ty_co_phan\json_data'
    business_type_template = r'D:\python_project\doc_gen\template\table\business_type.docx'
    business_path = r'D:\python_project\doc_gen\data\job.json'
    data_number = 1
    for i in range(data_number):
        save_path = os.path.join(save_path, '{}.json'.format(i))
        data_generator(city_path=city_path,
                       vi_name_path=vi_name_path,
                       foreign_name_path=eng_name_path,
                       acronym_name_path=short_name_path,
                       address_path=address_path,
                       phone_path=phone_path,
                       email_path=email_path,
                       fax_path=fax_path,
                       website_path=website_path,
                       save_path=save_path,
                       business_type_template=business_type_template,
                       business_path=business_path)
