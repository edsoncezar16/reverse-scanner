import cv2
import pytesseract
import pandas as pd

image = cv2.imread("test_image_cropped.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # needed because by default
# OpenCV stores images in BGR format and pytesseract assumes RGB format,
text = pytesseract.image_to_string(image_rgb)
rows = text.split("\n")
table = [row.split("\t") for row in rows]
image_data = pd.DataFrame(table[1:], columns=table[0])

print(image_data)

print(image_data.info())
