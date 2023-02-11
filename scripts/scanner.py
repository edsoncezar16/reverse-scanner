import cv2
import pytesseract
import pandas as pd

image = cv2.imread("test_image_cropped.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(image)
rows = text.split("\n")
table = [row.split("\t") for row in rows]
image_data = pd.DataFrame(table[1:], columns=table[0])

print(image_data)

print(image_data.info())
