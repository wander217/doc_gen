import json
import cv2 as cv
import numpy as np

data_path = r'D:\python_project\doc_gen\gen_by_type\ho_kinh_doanh\image_result\1\ho_kinh_doanh_3\0.json'
image_path = r'D:\python_project\doc_gen\gen_by_type\ho_kinh_doanh\image_result\1\ho_kinh_doanh_3\0.png'

image = cv.imread(image_path)
with open(data_path, 'r', encoding='utf-8') as f:
    data = json.loads(f.read())

for item in data:
    cv.polylines(image, [np.array(item['bbox']).astype(np.int32)], True, (255, 0, 0), 2)
cv.imshow("abc", image)
cv.waitKey(0)
