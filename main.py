import fitz

data_path = r"C:\Users\thinhtq\Downloads\business_summary.pdf"
doc = fitz.Document(data_path)
page: fitz.Page = doc.load_page(0)
print(page.get_text("lines", sort=False))
print(page.get_text("words", sort=False))
# print(doc.extractText("a"))
