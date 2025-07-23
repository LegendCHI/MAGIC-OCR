import streamlit as st
from ocr_module import extract_text_from_image
from database import init_db, save_entry, fetch_recent_entries

init_db()
st.set_page_config(page_title="OCR Dashboard", layout="centered")

st.title("🧠 OCR Web App")
st.markdown("""
Esta aplicación permite **extraer texto desde imágenes** usando tecnología OCR (Reconocimiento Óptico de Caracteres) alimentada por inteligencia artificial.

🧩 **¿Para qué sirve?**
- Leer documentos escaneados
- Extraer contenido desde fotos o capturas
- Digitalizar texto desde papel impreso

⚙️ **¿Cómo usarla?**
1. **Cargá una imagen** en formato `.png`, `.jpg`, `.jpeg` o `.bmp`.
2. La app procesará la imagen y te mostrará el texto detectado automáticamente.
3. Podés copiar ese texto, guardarlo, o visualizar el historial de imágenes procesadas.

🎯 Funciona tanto desde tu computador como desde cualquier dispositivo móvil con acceso a internet.
""")


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
    st.divider()
    
st.text("""
🧠 **Organización y herramientas utilizadas**

Este proyecto fue desarrollado siguiendo buenas prácticas de organización técnica y colaboración digital. A continuación se detallan los recursos aplicados:

• **GitHub**: Control de versiones, documentación colaborativa y gestión del repositorio principal.  
• **Streamlit**: Interfaz web interactiva optimizada para dispositivos móviles y escritorio.  
• **OCR Toolkit**: Tecnología basada en inteligencia artificial para el reconocimiento óptico de caracteres (OCR).  
• **Base de datos integrada**: Guardado de resultados con historial para seguimiento de uso.  
• **Discord y Trello** *(opcional si usaste)*: Coordinación del equipo de desarrollo y comunicación interna.

📁 Repositorio: [github.com/LegendCHI/MAGIC-OCR](https://github.com/LegendCHI/MAGIC-OCR)  
🎨 Diseño colaborativo entre RobDev Studios y Achuchumrra Studios  
🚀 Tester y promoción realizados por miembros del equipo + colaboradores externos

---

Podés complementar esto mencionando que el proyecto se basa en principios de accesibilidad, colaboración y eficiencia. Si querés que te ayude a integrarlo directamente en tu app, ¡también te doy una mano! ¿Querés que te lo traduzca a código `st.markdown()` para colocarlo tal cual en Streamlit?
""")
