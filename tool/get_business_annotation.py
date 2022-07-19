import json

data = [
    'Hộ gia đình chỉ được kinh doanh khi có đủ điều kiện theo quy định của Pháp luật',
    'Chỉ được kinh doanh sau khi thực hiện các điều kiện quy định',
    'Ngành nghề kinh doanh có điều kiện, hộ kinh doanh chỉ hoạt động khi có đủ điều kiện theo quy định của pháp luật',
    'Phải thực hiện đúng quy định của pháp luật về đất đai, xây dựng, phòng cháy chữa cháy, bảo vệ môi trường, các quy định của pháp luật hiện hành và điều kiện kinh doanh đối với ngành nghề kinh doanh có điều kiện',
    'Chỉ được kinh doanh khi có giấy chứng nhận cơ sở đủ điều kiện an toàn thực phẩm',
    'Chỉ được phép kinh doanh khi có giấy phép hoạt động khám bệnh, chữa bệnh;Kinh doanh không lấn chiếm lòng đường',
]

save_path = r'D:\python_project\doc_gen\data\business_annotation.json'
with open(save_path, 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=4))
    print(len(data))
