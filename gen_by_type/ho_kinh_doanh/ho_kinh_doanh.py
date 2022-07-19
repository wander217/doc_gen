import json
import os
from docx import Document
from tqdm import tqdm

from tool.get_bounding_box import get_bounding_box
from tool.pdf2image import convert2image
from tool.table_gen import processing_table_data
from python_docx_replace.docx_replace import docx_replace
from docx2pdf import convert

if __name__ == "__main__":
    data_path = r'D:\python_project\doc_gen\gen_by_type\ho_kinh_doanh\json_data\1'
    for i, item in enumerate(os.listdir(data_path)):
        with open(os.path.join(data_path, item), 'r', encoding='utf-8') as f:
            document_data = json.loads(f.read())
        template_path: str = r'D:\python_project\doc_gen\gen_by_type\ho_kinh_doanh\template\ho_kinh_doanh_4.docx'
        document: Document = Document(docx=template_path)
        docx_replace(document, **document_data['paragraph'])
        for tbl_key, tbl_data in document_data['table'].items():
            processing_table_data(tbl_key, tbl_data, document)
        doc_save_path = r'D:\python_project\doc_gen\gen_by_type\ho_kinh_doanh\doc_result\4\save_doc_{}.docx'.format(i)
        document.save(doc_save_path)
        pdf_save_path = r'D:\python_project\doc_gen\gen_by_type\ho_kinh_doanh\pdf_result\4\ho_kinh_doanh_{}.pdf'.format(i)
        convert(doc_save_path, pdf_save_path)

    pdf_path = r'D:\python_project\doc_gen\gen_by_type\ho_kinh_doanh\pdf_result\4'
    image_save_path = r'D:\python_project\doc_gen\gen_by_type\ho_kinh_doanh\image_result\4'
    for file in tqdm(os.listdir(pdf_path)):
        file_name = file.split(".")[0]
        convert2image(os.path.join(pdf_path, file),
                      os.path.join(image_save_path, file_name))

    for file in tqdm(os.listdir(pdf_path)):
        file_name = file.split(".")[0]
        get_bounding_box(os.path.join(pdf_path, file),
                         os.path.join(image_save_path, file_name))