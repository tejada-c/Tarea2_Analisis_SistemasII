import tkinter as tk
from tkinter import ttk, messagebox
from Logica.models.responsable import ResponsableLogic # Asegúrate de crear este archivo

class VentanaResponsables:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Responsables - INTES")
        self.root.geometry("900x600")
        self.root.configure(bg="#ECEFF1")
        
        self.logic = ResponsableLogic()

        # --- Título ---
        tk.Label(root, text="REGISTRO DE PADRES / RESPONSABLES", font=("Arial", 14, "bold"), 
                 bg="#3949AB", fg="white").pack(fill=tk.X, pady=10)

        # --- Formulario de Registro ---
        frame_form = tk.LabelFrame(root, text="Datos del Responsable y Acceso", bg="#ECEFF1", padx=10, pady=10)
        frame_form.pack(fill=tk.X, padx=20, pady=5)

        # Nombre y DUI (El DUI será el Usuario)
        tk.Label(frame_form, text="Nombre Completo:", bg="#ECEFF1").grid(row=0, column=0, sticky="w")
        self.entry_nombre = tk.Entry(frame_form, width=30)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="DUI (Usuario):", bg="#ECEFF1").grid(row=0, column=2, sticky="w")
        self.entry_dui = tk.Entry(frame_form, width=20)
        self.entry_dui.grid(row=0, column=3, padx=5, pady=5)

        # Teléfono y Parentesco
        tk.Label(frame_form, text="Teléfono:", bg="#ECEFF1").grid(row=1, column=0, sticky="w")
        self.entry_tel = tk.Entry(frame_form, width=30)
        self.entry_tel.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Parentesco:", bg="#ECEFF1").grid(row=1, column=2, sticky="w")
        self.combo_parentesco = ttk.Combobox(frame_form, values=["Padre", "Madre", "Tío/a", "Abuelo/a", "Tutor"], width=17)
        self.combo_parentesco.grid(row=1, column=3, padx=5, pady=5)

        # Contraseña y Estudiante Asociado
        tk.Label(frame_form, text="Contraseña:", bg="#ECEFF1").grid(row=2, column=0, sticky="w")
        self.entry_pass = tk.Entry(frame_form, width=30, show="*")
        self.entry_pass.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Vincular Estudiante:", bg="#ECEFF1").grid(row=2, column=2, sticky="w")
        self.combo_estudiante = ttk.Combobox(frame_form, width=17) # Se llena desde la BD
        self.combo_estudiante.grid(row=2, column=3, padx=5, pady=5)

        # Botón Guardar
        tk.Button(frame_form, text="Guardar Responsable", bg="#8BC34A", fg="white", 
                  font=("Arial", 10, "bold"), command=self.guardar, height=2).grid(row=0, column=4, rowspan=3, padx=20)

        # --- Tabla ---
        self.tabla = ttk.Treeview(root, columns=("ID", "Nombre", "DUI", "Tel", "Hijo"), show="headings")
        self.tabla.heading("ID", text="ID"); self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("DUI", text="DUI"); self.tabla.heading("Tel", text="Teléfono")
        self.tabla.heading("Hijo", text="Estudiante")
        self.tabla.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # --- Buscador ---
        frame_busqueda = tk.Frame(root, bg="#ECEFF1")
        frame_busqueda.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(frame_busqueda, text="Buscar por Nombre:", bg="#ECEFF1").pack(side=tk.LEFT)
        self.entry_buscar = tk.Entry(frame_busqueda, width=30)
        self.entry_buscar.pack(side=tk.LEFT, padx=10)
        tk.Button(frame_busqueda, text="Buscar").pack(side=tk.LEFT)

        self.cargar_estudiantes()
    def cargar_estudiantes(self):
        # Aquí llamarías a una función que traiga idUsuario y nombre de los 'Estudiantes'
        estudiantes = self.logic.obtener_estudiantes_lista()
        self.combo_estudiante['values'] = estudiantes

    def guardar(self):
        dui = self.entry_dui.get().strip()
        contra = self.entry_pass.get().strip()
        parentesco = self.combo_parentesco.get()
        tel = self.entry_tel.get().strip()
        estudiante_data = self.combo_estudiante.get()

        if not (dui and contra and parentesco and estudiante_data):
            messagebox.showwarning("Error", "Faltan datos críticos para el acceso")
            return

        id_hijo = estudiante_data.split(" - ")[0] # Extrae el ID del combo

        try:
            self.logic.registrar_responsable(dui, contra, parentesco, tel, id_hijo)
            messagebox.showinfo("Éxito", f"Acceso creado para el padre con usuario: {dui}")
            self.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", f"Fallo: {e}")

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_dui.delete(0, tk.END)
        self.entry_tel.delete(0, tk.END)
        self.combo_parentesco.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaResponsables(root)
    root.mainloop()