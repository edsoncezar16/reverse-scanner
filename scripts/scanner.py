import pytesseract
#import pandas as pd
import tabula
import pypdf

PATH_TO_TEST_IMAGE = "test_image_cropped.jpg"

pdf = pytesseract.image_to_pdf_or_hocr(PATH_TO_TEST_IMAGE, extension="pdf")
osd = pytesseract.image_to_osd(PATH_TO_TEST_IMAGE)
osd_dict = {
    key: value 
    for key, value in [
        line.split(":") for line in osd.split("\n")[:-1]
    ]
}
rotation_angle = float(osd_dict['Rotate'])

with open("image.pdf", "w+b") as f:
    f.write(pdf)

with open("image.pdf", "rb") as f:
    pdf = pypdf.PdfReader(f)
    if rotation_angle != 0.0:
        for page in pdf.pages:
            page.rotate(rotation_angle)
            with open("rotated_image.pdf", 'wb') as rotated_f:
                pdf_writer = pypdf.PdfWriter()
                for page in pdf.pages:
                    pdf_writer.add_page(page)
                pdf_writer.write(rotated_f)

try:
    tables = tabula.read_pdf('rotated_image.pdf', pages="all")
except:
    tables = tabula.read_pdf('image.pdf', pages="all")

for index, table in enumerate(tables):
    data_to_export = table.iloc[:, [1, 5, 6, 7, 8]]
    data_to_export.to_csv('2023-01-25.csv', index=False)