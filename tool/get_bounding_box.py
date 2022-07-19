import copy
import json
import os.path
import fitz
from tqdm import tqdm


def get_bounding_box(data_path: str, save_path: str):
    lines = []
    doc = fitz.Document(data_path)
    count = 0
    for page in doc:
        texts = page.get_text("words", sort=False)

        new_line = []
        for text in texts:
            if text[-1] != 0:
                new_line.append(text[:5])
            else:
                if len(new_line) != 0:
                    lines.append(copy.deepcopy(new_line))
                new_line.clear()
                new_line.append(text[:5])
        if len(new_line) != 0:
            lines.append(copy.deepcopy(new_line))

        # print("-" * 55)
        # for text1 in lines:
        #     for text2 in text1:
        #         print(text2)
        # print("-" * 55)
        MAX = 10000000

        line_data = []
        for line in lines:
            tmp = []
            for item in line:
                tmp.append(item)
            x_min, y_min, x_max, y_max = MAX, MAX, 0, 0
            gather_text = []
            for item in tmp:
                x1, y1, x2, y2, t = item
                x_min = min([x_min, x1])
                x_max = max([x_max, x2])
                y_min = min([y_min, y1])
                y_max = max([y_max, y2])
                gather_text.append(t)
            line_data.append({
                "text": " ".join(gather_text),
                "bbox": [[x_min, y_min],
                         [x_max, y_min],
                         [x_max, y_max],
                         [x_min, y_max]]
            })
        # for line in line_data:
        #     print(line)
        with open(os.path.join(save_path, "{}.json".format(count)), 'w', encoding='utf-8') as f:
            f.write(json.dumps(line_data, indent=4))
        count += 1
        lines.clear()


if __name__ == "__main__":
    data_path = r'D:\python_project\doc_gen\gen_by_type\cong_ty_co_phan\pdf_result'
    save_path = r'D:\python_project\doc_gen\gen_by_type\cong_ty_co_phan\image_result'
    for file in tqdm(os.listdir(data_path)):
        file_name = file.split(".")[0]
        get_bounding_box(os.path.join(data_path, file),
                         os.path.join(save_path, file_name))
