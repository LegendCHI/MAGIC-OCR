import tkinter as tk
from tkinter import filedialog, messagebox
from ocr_module import extract_text
from database import init_db, save_to_db, get_recent_entries

init_db()

def process_fixed_image():
    file_path = "assets/imagen.png"
    try:
        text = extract_text(file_path)
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, text)
        save_to_db("imagen.png", text)
        update_log()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo procesar la imagen:\n{str(e)}")

def process_image_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
    if file_path:
        try:
            text = extract_text(file_path)
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, text)
            save_to_db(file_path.split("/")[-1], text)
            update_log()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo procesar:\n{str(e)}")

def update_log():
    entries = get_recent_entries()
    log_list.delete(0, tk.END)
    for fname, time in entries:
        log_list.insert(tk.END, f"{fname} — {time}")

app = tk.Tk()
app.title("🧠 OCR Dashboard")
app.geometry("750x520")
app.config(bg="#f0f0f0")

tk.Label(app, text="🖼 Procesar texto desde imágenes", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)

tk.Button(app, text="Subir imagen manual", command=process_image_dialog,
          font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=5)

tk.Button(app, text="Procesar imagen fija (imagen.png)", command=process_fixed_image,
          font=("Arial", 12), bg="#2196F3", fg="white").pack(pady=5)

text_box = tk.Text(app, wrap=tk.WORD, height=15, font=("Arial", 11))
text_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

tk.Label(app, text="🕒 Últimos archivos procesados:", font=("Arial", 13), bg="#f0f0f0").pack(pady=5)
log_list = tk.Listbox(app, font=("Arial", 10), height=6)
log_list.pack(padx=10, fill=tk.X)

app.mainloop()
