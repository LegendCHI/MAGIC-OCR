from PIL import Image, ImageFilter, ImageOps
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # En Streamlit Cloud ya está instalado

def preprocess_image_pil(img: Image.Image):
    gray = ImageOps.grayscale(img)
    blur = gray.filter(ImageFilter.GaussianBlur(1))  # Nivel de difuminado
    return blur

def extract_text_from_image(uploaded_img):
    pil_img = Image.open(uploaded_img)
    processed = preprocess_image_pil(pil_img)
    return pytesseract.image_to_string(processed)
