import os
from docx import Document
from tool.table_gen import processing_table_data
from python_docx_replace.docx_replace import docx_replace
from docx2pdf import convert

document_data = {
    "paragraph": {
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
        "branch_name": "Abc",
        "branch_address": "Số 1, đường A, phố B, khu C, Thành phố D",
        "branch_code": "Abc",
        "representation_name": "Abc",
        "representation_address": "Số 1, đường A, phố B, khu C, Thành phố D",
        "representation_code": "Abc",
        "place_name": "Abc",
        "place_address": "Số 1, đường A, phố B, khu C, Thành phố D",
        "place_code": "Abc",
        "sale_capital": "1000",
        "legal_capital": "1000"
    },
    "table": {
        "bt": {
            "link": r"D:\python_project\doc_gen\template\table\business_type.docx",
            "target": [
                {"bt_id": "0", "bt_name": "Abc", "bt_code": "123"},
                {"bt_id": "1", "bt_name": "Def", "bt_code": "345"},
            ]
        },
        "sh": {
            "link": r"D:\python_project\doc_gen\template\table\shareholder.docx",
            "target": [
                {
                    "sh_id": "0",
                    "sh_nm": "Abc",
                    "sh_ad": "123",
                    "sh_tp": "abc",
                    "sh_vl": "abc",
                    "sh_pc": "10%",
                    "sh_cd": "100",
                    "sh_ca": "100000000000000",
                    "sh_an": "abc"
                },
            ]
        }
    }
}

if __name__ == "__main__":
    template_path: str = r'D:\python_project\doc_gen\gen_by_type\cong_ty_co_phan\template\cong_ty_co_phan_1.docx'
    document: Document = Document(docx=template_path)
    docx_replace(document, **document_data['paragraph'])
    for tbl_key, tbl_data in document_data['table'].items():
        processing_table_data(tbl_key, tbl_data, document)
    doc_save_path = r'D:\python_project\doc_gen\gen_by_type\cong_ty_co_phan\doc_result\save_doc.docx'
    document.save(doc_save_path)
    pdf_save_path = r'D:\python_project\doc_gen\gen_by_type\cong_ty_co_phan\pdf_result\cong_ty_co_phan.pdf'
    convert(doc_save_path, pdf_save_path)

