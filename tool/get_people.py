import json

data = [
    'Kinh', 'Chứt', 'Mường', 'Thổ',
    'Ba na', 'Brâu', 'Bru Vân Kiều',
    'Chơ Ro', 'Co', 'Cờ Ho', 'Cơ Tu',
    'Giẻ Triêng', 'Hrê', 'Kháng', 'Khmer',
    'Khơ Mú', 'Mạ', 'Mảng', 'Mnông',
    'Ơ Đu', 'Rơ Măm', 'Tà Ôi', 'Xinh Mun',
    'Sơ Đăng', 'X\'Tiêng', 'Bố Y', 'Giáy',
    'Lào', 'Nự', 'Nùng', 'Sán Chay', 'Tày',
    'Thái', 'Cờ Lao', 'La Chí', 'La Ha',
    'Pu Péo', 'Dao', 'Hmong', 'Pà Thẻn',
    'Chăm', 'Chu Ru', 'Ê Đê', 'Gia Rai',
    'Raglay', 'Hoa', 'Ngái', 'Sán Dìu',
    'Cống', 'Hà Nhì', 'La Hủ', 'Lô Lô',
    'Phù Lá', 'Si Ha'
]

save_path = r'D:\python_project\doc_gen\data\people.json'
with open(save_path, 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=4))
    print(len(data))