import streamlit as st
from ocr_module import extract_text_from_image
from database import init_db, save_entry, fetch_recent_entries

init_db()
st.set_page_config(page_title="OCR Dashboard", layout="centered")

st.title("🧠 OCR Web App")
st.text("""
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

ast.divider()
st.text("""
Organización y herramientas utilizadas

Este proyecto fue desarrollado con enfoque colaborativo y uso estratégico de herramientas modernas:

- GitHub: Control de versiones, documentación y gestión del repositorio.  
- Streamlit: Framework para desarrollar la interfaz web interactiva de manera rápida y accesible.  
- EasyOCR: Motor principal para el reconocimiento óptico de caracteres en imágenes.  
- Discord: Organización del equipo, asignación de roles y seguimiento de tareas.

🎨 Diseño y desarrollo colaborativo
- RobDev Studios: Encargado de la lógica técnica, integración y estructura del backend.  
- Achuchumrra Studios: Responsable del diseño visual, experiencia de usuario (UI/UX), Publicidad y branding del proyecto.

🚀 Testing y promoción* 
- Validación y difusión realizada por miembros del equipo y colaboradores externos para asegurar funcionalidad, accesibilidad y estabilidad.

📁 Repositorio público: [github.com/LegendCHI/MAGIC-OCR](https://github.com/LegendCHI/MAGIC-OCR)
""")

