import tkinter as tk
from tkinter import ttk, messagebox

class VentanaDocentes:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Docentes - INTES")
        self.root.geometry("800x500")
        self.root.configure(bg="#ECEFF1")

        tk.Label(root, text="REGISTRO DE DOCENTES", font=("Arial", 14, "bold"), 
                 bg="#00796B", fg="white").pack(fill=tk.X, pady=10)

        frame = tk.Frame(root, bg="#ECEFF1")
        frame.pack(padx=20, pady=10, fill=tk.X)

        tk.Label(frame, text="Nombre completo:", bg="#ECEFF1").pack(side=tk.LEFT)
        self.ent_docente = tk.Entry(frame, width=40)
        self.ent_docente.pack(side=tk.LEFT, padx=10)
        
        tk.Button(frame, text="Registrar Docente", bg="#8BC34A", command=lambda: messagebox.showinfo("OK", "Docente registrado")).pack(side=tk.LEFT)

        self.tabla = ttk.Treeview(root, columns=("ID", "Nombre", "Especialidad"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre del Docente")
        self.tabla.heading("Especialidad", text="Especialidad")
        self.tabla.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)