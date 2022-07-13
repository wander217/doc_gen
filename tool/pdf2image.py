import fitz
import os
from PIL import Image


def convert2image(pdf_path, save_dir):
    file_number = len(os.listdir(save_dir))
    save_dir = os.path.join(save_dir, "{}".format(file_number))
    os.mkdir(save_dir)
    doc = fitz.open(pdf_path)
    for page in doc:
        pix = page.get_pixmap(alpha=True)
        pix.save(os.path.join(save_dir, "{}.png".format(page.number)))
        image = Image.open(os.path.join(save_dir, "{}.png".format(page.number)))
        w, h = image.size
        bg = Image.open(r"D:\python_project\doc_gen\background\bg4.png")
        bg = bg.resize((w, h))
        bg.paste(image, (0, 0), image)
        # bg = bg.resize((w * 2, h * 2))
        bg = bg.convert("RGB")
        bg.save(os.path.join(save_dir, "{}.png".format(page.number)))


if __name__ == "__main__":
    convert2image(r'D:\python_project\doc_gen\gen_by_type\cong_ty_co_phan\pdf_result\cong_ty_co_phan.pdf',
                  r'D:\python_project\doc_gen\gen_by_type\cong_ty_co_phan\image_result')
