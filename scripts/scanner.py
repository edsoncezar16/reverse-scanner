from PIL import Image
import pytesseract
import pandas as pd

image = Image.open('test_image_cropped.jpg')
text = pytesseract.image_to_string(image)
rows = text.split("\n")
table = [row.split("\t") for row in rows]
image_data = pd.DataFrame(table[1:], columns=table[0])

print(image_data)

print(image_data.info())