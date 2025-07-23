from PIL import Image
import easyocr
import numpy as np

# Crear lector OCR con inglés y español como idiomas permitidos
reader = easyocr.Reader(['en', 'es'], gpu=False)

def extract_text_from_image(uploaded_img):
    # Cargar imagen desde Streamlit uploader
    pil_img = Image.open(uploaded_img).convert('RGB')
    img_array = np.array(pil_img)

    # Ejecutar OCR
    results = reader.readtext(img_array)

    # Combinar los bloques de texto detectado
    text = "\n".join([res[1] for res in results])
    return text
