import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class VentanaAsistencia:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Asistencia - INTES")
        self.root.geometry("800x600")
        self.root.configure(bg="#ECEFF1")

        tk.Label(root, text="CONTROL DE ASISTENCIA DIARIA", font=("Arial", 14, "bold"), 
                 bg="#FBC02D", fg="black").pack(fill=tk.X, pady=10)

        # Selector de Fecha y Grado
        frame_top = tk.Frame(root, bg="#ECEFF1")
        frame_top.pack(pady=10)

        tk.Label(frame_top, text="Fecha:", bg="#ECEFF1").grid(row=0, column=0)
        self.lbl_fecha = tk.Label(frame_top, text=datetime.now().strftime('%d/%m/%Y'), font=("Arial", 10, "bold"))
        self.lbl_fecha.grid(row=0, column=1, padx=20)

        tk.Label(frame_top, text="Grado:", bg="#ECEFF1").grid(row=0, column=2)
        self.combo_grado = ttk.Combobox(frame_top, values=["1° Año", "2° Año", "3° Año"])
        self.combo_grado.grid(row=0, column=3, padx=10)

        # Tabla de asistencia con Checkboxes (o columna de estado)
        self.tabla = ttk.Treeview(root, columns=("ID", "Estudiante", "Asistencia"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Estudiante", text="Nombre del Estudiante")
        self.tabla.heading("Asistencia", text="Estado (Presente/Ausente)")
        self.tabla.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        tk.Button(root, text="Guardar Asistencia del Día", bg="#1976D2", fg="white", 
                  command=lambda: messagebox.showinfo("Éxito", "Asistencia guardada")).pack(pady=10)