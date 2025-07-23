import streamlit as st
from ocr_module import extract_text_from_image, extract_text_from_path
from database import init_db, save_entry, fetch_recent_entries
import os

st.set_page_config(page_title="OCR Dashboard", layout="centered")
init_db()

st.title("🧠 OCR Web App")
st.markdown("Sube una imagen con texto para extraerlo automáticamente.")

uploaded_file = st.file_uploader("📤 Cargar imagen", type=["png", "jpg", "jpeg", "bmp"])

if uploaded_file:
    st.image(uploaded_file, caption="Imagen cargada", use_column_width=True)
    extracted = extract_text_from_image(uploaded_file)
    st.subheader("📄 Texto detectado")
    st.text_area("Resultado OCR", extracted, height=200)

    if st.button("📌 Guardar en historial"):
        save_entry(uploaded_file.name, extracted)
        st.success("Texto guardado en la base de datos.")

st.divider()
st.subheader("📜 Últimos análisis registrados")

entries = fetch_recent_entries()
for name, timestamp in entries:
    st.write(f"• **{name}** — {timestamp}")
