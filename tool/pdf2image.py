import fitz
import os
from PIL import Image
from tqdm import tqdm


def convert2image(pdf_path, save_dir):
    os.mkdir(save_dir)
    doc = fitz.open(pdf_path)
    for page in doc:
        if page.number > 2:
            return
        pix = page.get_pixmap(alpha=True)
        pix.save(os.path.join(save_dir, "{}.png".format(page.number)))
        image = Image.open(os.path.join(save_dir, "{}.png".format(page.number)))
        w, h = image.size
        bg = Image.open(r"D:\python_project\doc_gen\background\bg1.png")
        bg = bg.resize((w, h))
        bg.paste(image, (0, 0), image)
        # bg = bg.resize((w * 2, h * 2))
        bg = bg.convert("RGB")
        bg.save(os.path.join(save_dir, "{}.png".format(page.number)))


if __name__ == "__main__":
    data_path = r'D:\python_project\doc_gen\gen_by_type\cong_ty_co_phan\pdf_result'
    save_path = r'D:\python_project\doc_gen\gen_by_type\cong_ty_co_phan\image_result'
    for file in tqdm(os.listdir(data_path)):
        file_name = file.split(".")[0]
        convert2image(os.path.join(data_path, file),
                      os.path.join(save_path, file_name))
