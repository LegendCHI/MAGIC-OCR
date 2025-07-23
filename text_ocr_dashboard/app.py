import streamlit as st
from ocr_module import extract_text_from_image
from database import init_db, save_entry, fetch_recent_entries

init_db()
st.set_page_config(page_title="OCR Dashboard", layout="centered")

st.title("🧠 OCR Web App")
st.markdown("Extrae texto desde imágenes con reconocimiento OCR automático.")

uploaded_file = st.file_uploader("📤 Cargar imagen", type=["png", "jpg", "jpeg", "bmp"])

if uploaded_file:
    st.image(uploaded_file, use_container_width=True)
    extracted_text = extract_text_from_image(uploaded_file)
    st.subheader("📄 Texto detectado")
    st.text_area("Resultado", extracted_text, height=200)

    if st.button("📌 Guardar resultado"):
        save_entry(uploaded_file.name, extracted_text)
        st.success("Guardado exitosamente.")

st.divider()
st.subheader("📜 Últimos archivos procesados")
for name, timestamp in fetch_recent_entries():
    st.write(f"• **{name}** — {timestamp}")
