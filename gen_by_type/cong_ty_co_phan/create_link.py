import json
import os


def create_link(pages: list):
    count = 0
    is_ignore = False
    for page in pages:
        for target in page:
            if is_ignore:
                target['link'] = count
                count += 1
                is_ignore = False
                continue
            if "SỞ KẾ HOẠCH VÀ ĐẦU TƯ" == target['text']:
                target['link'] = count + 1
                is_ignore = True
            elif "PHÒNG ĐĂNG KÝ KINH DOANH" == target['text']:
                target['link'] = count
                is_ignore = False
            elif "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM" == target['text']:
                target['link'] = count
                is_ignore = False
            elif "Độc lập - Tự do - Hạnh phúc" == target['text']:
                target['link'] = count
                is_ignore = False
            elif "GIẤY CHỨNG NHẬN ĐĂNG KÝ DOANH NGHIỆP" == target['text']:
                target['link'] = count
                is_ignore = True
            elif "Mã số doanh nghiệp" in target['text']:
                target['link'] = count
                is_ignore = False
            elif "Đăng ký lần đầu" in target['text']:
                target['link'] = count
                is_ignore = False
            elif "Đăng ký lần thứ" in target['text']:
                target['link'] = count
                is_ignore = False
            elif "1. Tên công ty" in target['text']:
                target['link'] = count
                is_ignore = False
            elif 'Tên công ty viết bằng tiếng Việt' in target['text']:
                target['link'] = count
                is_ignore = False
            count += 1
    return pages


if __name__ == "__main__":
    data_path = r'/gen_by_type/cong_ty_co_phan/image_result/cong_ty_co_phan_1'
    pages = []
    for file in os.listdir(data_path):
        if file.endswith("json"):
            with open(os.path.join(data_path, file), 'r', encoding='utf-8') as f:
                data = json.loads(f.read())
                pages.append(data)
    for item in create_link(pages)[0]:
        print(item)
