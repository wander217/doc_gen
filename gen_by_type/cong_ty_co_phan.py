import docx
from docx import Document
from python_docx_replace.docx_replace import docx_replace
from python_docx_replace.docx_replace import RunTextChanger, MaxRetriesReached
import copy

paragraph_datas = {
    "city_name": "THÀNH PHỐ HÀ NỘI",
    "contract_code": "S1232322",
    "first_date": "Đăng ký lần đầu, Thứ 6 ngày 8 tháng 7 năm 2022",
    "change_date": "Đăng ký lần thứ 2, Thứ 6 ngày 8 tháng 7 năm 2022",
    "vietnamese_name": "Công ty cổ phần ABC",
    "foreign_name": "Công ty ABC",
    "acronym_name": "ABC company",
    "phone": "0328296433",
    "fax": "328296433",
    "email": "abc@gmail.com.vn",
    "website": "abc.com.vn",
    "capital_amount": "1000 đồng",
    "capital_value": "100 đồng",
    "total_capital": "100 đồng",
    "own_fullname": "nguyễn văn A",
    "own_sex": "nam",
    "own_position": "abcde",
    "own_birthday": "21/07/1999",
    "own_ethnicity": "Kinh",
    "own_nation": "Việt Nam",
    "own_type": "Chứng minh thư nhân dân",
    "own_idcard_code": "0123456788",
    "own_idcard_date": "12/03/2010",
    "own_idcard_place": "Công an Hà Nội",
    "own_idcard_rp": "Số 1, đường A, phố B, khu C, Thành phố D",
    "own_idcard_lv": "Số 1, đường A, phố B, khu C, Thành phố D",
}

table_datas = {
    "bt": [
        {"bt_id": "0", "bt_name": "Abc", "bt_code": "123"},
        {"bt_id": "1", "bt_name": "Def", "bt_code": "345"},
    ]
}


def get_table_from_keyword(keyword, document):
    for table in document.tables:
        for row in table.rows:
            for col in row.cells:
                for paragraph in col.paragraphs:
                    if keyword in paragraph.text:
                        return table


def _simple_replace(p, key, value):
    """Try to replace a key in the paragraph runs, simpler alternative"""
    for run in p.runs:
        if key in run.text:
            run.text = run.text.replace(f"${{{key}}}", value)


def _complex_replace(p, key, value):
    """Complex alternative, which check all broken items inside the runs"""
    max_retries_replace_a_key = 100  # to avoid infinite loop, this value is set

    changer = RunTextChanger(p, key, value)
    changer.replace()

    current = 1
    while key in p.text:  # if the key appears more than once in the paragraph, it will replaced all
        current += 1
        if current > max_retries_replace_a_key:
            raise MaxRetriesReached(max_retries_replace_a_key, key)
        changer = RunTextChanger(p, key, value)
        changer.replace()


def processing_table_data(key, value, document):
    table = get_table_from_keyword(key, document)
    first_row = table.rows[1]
    for i, row_data in enumerate(value):
        temp_row_tr = copy.deepcopy(first_row._tr)
        temp_row = table.add_row()
        temp_row._tr = temp_row_tr
        for col in temp_row.cells:
            for paragraph in col.paragraphs:
                for k, v in row_data.items():
                    if k in paragraph.text:
                        _simple_replace(paragraph, k, v)
                        if k in paragraph.text:
                            _complex_replace(paragraph, k, v)
        last_row = table.rows[-1]
        print(last_row)
        last_row._tr.addnext(temp_row._tr)


if __name__ == "__main__":
    template_path: str = r'D:\python_project\doc_gen\template\cong_ty_co_phan.docx'
    document: Document = Document(docx=template_path)
    docx_replace(document, **paragraph_datas)
    for key, value in table_datas.items():
        processing_table_data(key, value, document)
    save_path = r'D:\python_project\doc_gen\result\save_doc.docx'
    document.save(save_path)
