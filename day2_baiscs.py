from PIL import Image
import pytesseract
import cv2

img_path="sample_invoice.jpeg"
img=cv2.imread(img_path)

print(f"Image Shape {img.shape}")

#preprocessing
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.threshold(gray ,150 ,255,cv2.THRESH_BINARY)[1]
cv2.imwrite('processed_invoice.jpg',gray)

#extracting text
text=pytesseract.image_to_string(Image.open("processed_invoice.jpg"))
print(f"OCR OUTPUT{text}")

with open("invoice_text.txt", "w") as f:
    f.write(text)
print("Text Extracted Saved")