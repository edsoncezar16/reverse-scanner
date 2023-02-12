import pytesseract
import os
import tabula
import pypdf

INPUT_DIR = "test_images"
OUTPUT_DIR = "output_files"
OUTPUT_COLUMNS = [
    "N2 ROMANEIO / NF", "QTD. DE VOLUMES", "DESTINO", "CLIENTE","NECOLETA"
]

def image_to_excel(image_file_name, output_columns=None, output_dir=OUTPUT_DIR):
    'Reads an image with tabular data and export tables to an excel file.'
    print(f'Reading image {image_file_name}...')
    image_path = os.path.join(INPUT_DIR, image_file_name)
    pdf = pytesseract.image_to_pdf_or_hocr(image_path, extension="pdf")
    osd = pytesseract.image_to_osd(image_path)
    osd_dict = {
        key: value 
        for key, value in [
            line.split(":") for line in osd.split("\n")[:-1]
        ]
    }
    rotation_angle = float(osd_dict['Rotate'])

    with open("image.pdf", "w+b") as f:
        f.write(pdf)

    print('Pre processing...')
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
    print('Reading tables...')
    try:
        tables = tabula.read_pdf('rotated_image.pdf', pages="all")
    except:
        tables = tabula.read_pdf('image.pdf', pages="all")
    os.remove('image.pdf')
    os.remove('rotated_image.pdf')
    if not tables:
        print(f'No tables found in {image_file_name}.')
    else:
        print('Exporting tables...')
        for index, table in enumerate(tables):
            if not output_columns:
                data_to_export = table
            else:
                data_to_export = table[output_columns]
            output_path = os.path.join(
                output_dir, f'{image_file_name}-t{index + 1}.xlsx'
            )
            data_to_export.to_excel(output_path, index=False)
        print('Done.')

for filename in os.listdir(INPUT_DIR):
    image_to_excel(filename, OUTPUT_COLUMNS)