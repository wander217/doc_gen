import json
import os
import unicodedata

import numpy as np


def create_link(_pages: list):
    key = [
        'ủy ban nhân dân',
        'phòng tài chính - kế hoạch',
        'cộng hòa xã hội chủ nghĩa việt nam',
        'độc lập - tự do - hạnh phúc',
        'giấy chứng nhận đăng ký hộ kinh doanh',
        'số',
        'đăng ký lần đầu',
        'đăng ký lần thứ',
        '1. tên hộ kinh doanh',
        '2. địa chỉ trụ sở hộ kinh doanh:',
        'điện thoại:',
        'fax:',
        'email:',
        'website:',
        '3. ngành, nghề kinh doanh',
        '4. vốn kinh doanh',
        '5. chủ thể thành lập hộ kinh doanh',
        '6. thông tin về chủ hộ kinh doanh',
        'sinh ngày',
        'dân tộc',
        'quốc tịch',
        'loại giấy tờ pháp lý của cá nhân',
        'số giấy tờ pháp lý của cá nhân',
        'ngày cấp',
        'nơi cấp',
        'địa chỉ thường trú',
        'địa chỉ liên lạc',
        '7. danh sách thành viên hộ gia đình đăng ký thành lập hộ kinh doanh',
        'stt',
        'tên',
        'quốc',
        'địa chỉ liên lạc',
        'địa chỉ thường trú',
        'số giấy tờ pháp lý',
        'ghi chú',
        'trưởng phòng',
        'ký, ghi rõ họ tên và đóng dấu'
    ]

    text_boxes = []
    for page in _pages:
        for target in page:
            text_boxes.append(target)

    ignore = np.zeros((len(text_boxes),), dtype=np.int32).tolist()
    groups = []
    pointer = 1
    for i, _ in enumerate(text_boxes):
        if ignore[i] == 1:
            continue
        group = []
        for j in range(i, len(text_boxes)):
            text1 = unicodedata.normalize('NFC', key[pointer])
            text2 = unicodedata.normalize('NFC', text_boxes[j]['text'].lower())
            if pointer >= len(key):
                break
            elif text1 not in text2:
                group.append(text_boxes[j])
                ignore[j] = 1
            else:
                pointer += 1
                break
        groups.append(group)
    count = 0
    for group in groups:
        for i, item in enumerate(group):
            if i == len(group) - 1:
                item['link'] = count
            else:
                item['link'] = count + 1
            count += 1
    results = []
    for group in groups:
        for item in group:
            results.append(item)
    return results


if __name__ == "__main__":
    data_path = r'D:\python_project\doc_gen\gen_by_type\ho_kinh_doanh\image_result\4'
    for folder in os.listdir(data_path):
        pages = []
        for file in os.listdir(os.path.join(data_path, folder)):
            if file.endswith("json"):
                with open(os.path.join(data_path, folder, file), 'r', encoding='utf-8') as f:
                    tmp = f.read()
                    if len(tmp) == 0:
                        continue
                    data = json.loads(tmp)
                    pages.append(data)
        links = create_link(pages)
        pages.clear()
        # print(links)
        # raise Exception("abc")
        with open(os.path.join(data_path, folder, 'link.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(links, indent=4))
