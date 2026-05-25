import tkinter as tk
from tkinter import ttk, messagebox

# from Logica.models.curso import CursosLogic 

class VentanaCursos:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Cursos - INTES")
        self.root.geometry("800x500")
        self.root.configure(bg="#ECEFF1")

        # Título
        tk.Label(root, text="REGISTRO DE CURSOS / MATERIAS", font=("Arial", 14, "bold"), 
                 bg="#E64A19", fg="white").pack(fill=tk.X, pady=10)

        # Formulario
        frame_form = tk.LabelFrame(root, text="Datos del Curso", bg="#ECEFF1", padx=10, pady=10)
        frame_form.pack(fill=tk.X, padx=20, pady=5)

        tk.Label(frame_form, text="Nombre del Curso:", bg="#ECEFF1").grid(row=0, column=0)
        self.entry_nombre = tk.Entry(frame_form, width=30)
        self.entry_nombre.grid(row=0, column=1, padx=10)

        tk.Label(frame_form, text="Descripción:", bg="#ECEFF1").grid(row=0, column=2)
        self.entry_desc = tk.Entry(frame_form, width=30)
        self.entry_desc.grid(row=0, column=3, padx=10)

        tk.Button(frame_form, text="Guardar Curso", bg="#8BC34A", command=self.guardar).grid(row=0, column=4, padx=10)

        # Tabla
        self.tabla = ttk.Treeview(root, columns=("ID", "Nombre", "Descripcion"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre del Curso")
        self.tabla.heading("Descripcion", text="Descripción")
        self.tabla.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def guardar(self):
        # AQUÍ CONECTAR CON LOGICA POSTERIORMENTE
        messagebox.showinfo("Info", "Lógica de guardado para Cursos pendiente de implementar")