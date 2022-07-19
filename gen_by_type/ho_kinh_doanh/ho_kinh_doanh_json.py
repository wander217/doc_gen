import json
import os
import random
from faker import Faker
from vietnam_number import n2w
from vn_fullname_generator import generator
from tqdm import tqdm
from asset import JSON_DATA_PATH


def data_gen():
    date = Faker().date_object()
    format_string = 'ngày {} tháng {} năm {}'.format(date.day, date.month, date.year)
    return format_string


def date_gen():
    date = Faker().date_object()
    format_type = ["{}/{}/{}", "{}-{}-{}"]
    selection_format = random.choice(format_type)
    format_string = selection_format.format(date.day, date.month, date.year)
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


def data_generator(district_path: str,
                   vi_name_path: str,
                   address_path: str,
                   phone_path: str,
                   fax_path: str,
                   email_path: str,
                   website_path: str,
                   business_path: str,
                   business_annotation: str,
                   ethnicity_path: str,
                   idcard_code_path: str,
                   idcard_place_path: str,
                   persistance_residence_path: str,
                   living_place_path: str,
                   save_path: str,
                   **kwargs):
    data = {
        "paragraph": {},
        "table": {}
    }
    # processing city data
    with open(district_path, 'r', encoding='utf-8') as f:
        district_data = json.loads(f.read())
    data['paragraph']['district_name'] = random.choice(district_data).upper()
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

    # processing business type
    with open(business_path, 'r', encoding='utf-8') as f:
        business_data = json.loads(f.read())
    data['paragraph']['business_type'] = ";".join([
        random.choice(business_data)['name']
        for _ in range(random.randint(1, 4))
    ])
    with open(business_annotation, 'r', encoding='utf-8') as f:
        business_annotation_data = json.loads(f.read())
    data['paragraph']['business_annotation'] = random.choice(business_annotation_data)
    # ending processing business type

    # processing business capital data
    capital_amount = [str(random.randint(1, 999)) if i == 0 else str(random.randint(0, 999))
                      for i in range(random.randint(2, 3))] + ['000']
    data['paragraph']['business_capital'] = amount_list_2_text(capital_amount) + "đ"
    data['paragraph']['business_character_capital'] = get_amount_character(capital_amount)
    # ending processing business capital data

    # processing owner fullname data
    gender = random.randint(0, 1)
    data['paragraph']['own_fullname'] = generator.generate(gender).upper()
    # ending processing owner fullname data

    # processing owner sex data
    data['paragraph']['own_sex'] = "Nam" if gender == 1 else "Nữ"
    # ending processing owner sex data

    # processing owner birthday data
    data['paragraph']['own_birthday'] = date_gen()
    # ending processing owner birthday data

    # processing owner ethnicity data
    with open(ethnicity_path, 'r', encoding='utf-8') as f:
        ethnicity_data = json.loads(f.read())
    data['paragraph']['own_ethnicity'] = random.choice(ethnicity_data)
    # ending processing owner ethnicity data

    # processing owner type data
    own_type = ["Cá nhân", "Các thành viên hộ gia đình"]
    data['paragraph']['own_type'] = own_type[0]
    # ending processing owner type data

    # processing owner national data
    data['paragraph']['own_national'] = 'Việt Nam'
    # ending processing owner national data

    # processing owner idcard type data
    idcard_type = ['Chứng minh thư nhân dân', 'Hộ chiếu', 'Căn cước công dân']
    data['paragraph']['own_idcard_type'] = random.choice(idcard_type)
    # ending processing owner idcard type data

    # processing owner idcard code data
    with open(idcard_code_path, 'r', encoding='utf-8') as f:
        idcard_code = json.loads(f.read())
    data['paragraph']['own_idcard_code'] = random.choice(idcard_code)
    # ending processing owner idcard code data

    # processing owner idcard place data
    with open(idcard_place_path, 'r', encoding='utf-8') as f:
        idcard_place = json.loads(f.read())
    data['paragraph']['own_idcard_place'] = random.choice(idcard_place)
    # ending processing owner idcard place data

    # processing owner idcard date data
    data['paragraph']['own_idcard_date'] = date_gen()
    # ending processing owner idcard date data

    # processing owner persistance residence data
    with open(persistance_residence_path, 'r', encoding='utf-8') as f:
        persistance_residence = json.loads(f.read())
    data['paragraph']['own_persistance_residence'] = random.choice(persistance_residence)
    # ending processing owner persistance residence data

    # processing owner living place data
    with open(living_place_path, 'r', encoding='utf-8') as f:
        living_place = json.loads(f.read())
    data['paragraph']['own_living_place'] = random.choice(living_place)
    # ending processing owner living place data

    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    save_path = r'D:\python_project\doc_gen\gen_by_type\ho_kinh_doanh\json_data\1'
    data_number = 100
    for i in tqdm(range(data_number)):
        item_save_path = os.path.join(save_path, '{}.json'.format(i))
        data_generator(**JSON_DATA_PATH, save_path=item_save_path)
