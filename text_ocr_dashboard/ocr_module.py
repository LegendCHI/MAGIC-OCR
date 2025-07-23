from PIL import Image, ImageFilter, ImageOps
import pytesseract

# Ruta válida para entornos Linux/Streamlit Cloud
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def preprocess_image(img: Image.Image):
    gray = ImageOps.grayscale(img)
    blur = gray.filter(ImageFilter.GaussianBlur(1))
    return blur

def extract_text_from_image(uploaded_img):
    pil_img = Image.open(uploaded_img)
    processed = preprocess_image(pil_img)
    return pytesseract.image_to_string(processed)
