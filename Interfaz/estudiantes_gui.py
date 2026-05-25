import tkinter as tk
from tkinter import ttk, messagebox
from Logica.models.estudiante import EstudianteLogic

class VentanaEstudiantes:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Estudiantes - INTES")
        self.root.geometry("1000x600")
        self.root.configure(bg="#ECEFF1")
        self.logic = EstudianteLogic()

        # --- Título ---
        tk.Label(root, text="REGISTRO DE ESTUDIANTES", font=("Arial", 16, "bold"), 
                 bg="#01579B", fg="white").pack(fill=tk.X, pady=10)

        # --- Contenedor Principal ---
        main_frame = tk.Frame(root, bg="#ECEFF1")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # --- Formulario (Izquierda) ---
        form_frame = tk.LabelFrame(main_frame, text="Datos del Estudiante", bg="#ECEFF1", padx=10, pady=10)
        form_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        self.crear_campo(form_frame, "Nombre:", 0)
        self.entry_nombre = tk.Entry(form_frame)
        self.entry_nombre.grid(row=0, column=1, pady=5)

        self.crear_campo(form_frame, "Apellidos:", 1)
        self.entry_apellidos = tk.Entry(form_frame)
        self.entry_apellidos.grid(row=1, column=1, pady=5)

        self.crear_campo(form_frame, "Código/NIE:", 2)
        self.entry_codigo = tk.Entry(form_frame)
        self.entry_codigo.grid(row=2, column=1, pady=5)

        self.crear_campo(form_frame, "Grado:", 3)
        self.combo_grado = ttk.Combobox(form_frame, values=["1° Año", "2° Año", "3° Año"])
        self.combo_grado.grid(row=3, column=1, pady=5)

        # Botón Guardar
        tk.Button(form_frame, text="Guardar Estudiante", bg="#8BC34A", fg="white",
                  command=self.guardar).grid(row=4, columnspan=2, pady=20)

        # --- Tabla de Datos (Derecha) ---
        table_frame = tk.Frame(main_frame, bg="white")
        table_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.tabla = ttk.Treeview(table_frame, columns=("ID", "Nombre", "Grado", "Estado"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre Completo")
        self.tabla.heading("Grado", text="Grado")
        self.tabla.heading("Estado", text="Estado")
        self.tabla.pack(fill=tk.BOTH, expand=True)

        self.cargar_datos_tabla()

    def crear_campo(self, parent, texto, fila):
        tk.Label(parent, text=texto, bg="#ECEFF1", font=("Arial", 10, "bold")).grid(row=fila, column=0, sticky="w")

    def guardar(self):
        # Lógica simplificada para el prototipo
        try:
            self.logic.registrar_estudiante(
                self.entry_nombre.get(), 
                self.entry_apellidos.get(),
                self.entry_codigo.get(),
                self.combo_grado.get(),
                15, "Activo", "2008-01-01", 1, 1 # Valores por defecto para el prototipo
            )
            messagebox.showinfo("Éxito", "Estudiante registrado correctamente", parent=self.root)
            self.cargar_datos_tabla()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar: {e}")

    def cargar_datos_tabla(self):
        # Limpiar tabla
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        # Llenar con BD
        for est in self.logic.obtener_todos():
            self.tabla.insert("", "end", values=(est['idEstudiante'], f"{est['nombre']} {est['apellidos']}", est['grado'], est['estado']))

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaEstudiantes(root)
    root.mainloop()