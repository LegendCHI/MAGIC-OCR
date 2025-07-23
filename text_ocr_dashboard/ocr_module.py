import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    return blur

def extract_text_from_path(image_path):
    processed = preprocess_image(image_path)
    return pytesseract.image_to_string(processed)

def extract_text_from_image(uploaded_img):
    pil_img = Image.open(uploaded_img)
    return pytesseract.image_to_string(pil_img)
