from PIL import Image, ImageFilter, ImageOps
import pytesseract

# En Streamlit Cloud pytesseract ya está instalado y configurado
def preprocess_image_pil(pil_img):
    gray = ImageOps.grayscale(pil_img)
    blur = gray.filter(ImageFilter.GaussianBlur(1))
    return blur

def extract_text_from_image(uploaded_img):
    pil_img = Image.open(uploaded_img)
    processed = preprocess_image_pil(pil_img)
    text = pytesseract.image_to_string(processed)
    return text
