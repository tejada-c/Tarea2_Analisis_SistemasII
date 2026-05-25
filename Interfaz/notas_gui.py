import tkinter as tk
from tkinter import ttk, messagebox
from Logica.models.calificacion import CalificacionLogic
from Logica.models.estudiante import EstudianteLogic

class VentanaNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Calificaciones - INTES")
        self.root.geometry("900x600")
        self.root.configure(bg="#ECEFF1")
        
        self.logic_notas = CalificacionLogic()
        self.logic_estudiantes = EstudianteLogic()

        # --- Título ---
        tk.Label(root, text="GESTIÓN DE CALIFICACIONES", font=("Arial", 16, "bold"), 
                 bg="#1A237E", fg="white").pack(fill=tk.X, pady=10)

        # --- Selector de Estudiante ---
        frame_seleccion = tk.LabelFrame(root, text="1. Seleccionar Estudiante", bg="#ECEFF1", padx=10, pady=10)
        frame_seleccion.pack(fill=tk.X, padx=20, pady=5)

        tk.Label(frame_seleccion, text="Buscar Estudiante (Nombre):", bg="#ECEFF1").pack(side=tk.LEFT)
        self.entry_busqueda = tk.Entry(frame_seleccion)
        self.entry_busqueda.pack(side=tk.LEFT, padx=10)
        tk.Button(frame_seleccion, text="Buscar", command=self.buscar_estudiante).pack(side=tk.LEFT)

        self.combo_estudiantes = ttk.Combobox(frame_seleccion, width=50, state="readonly")
        self.combo_estudiantes.pack(side=tk.LEFT, padx=10)

        # Esto hace que la tabla se cargue apenas se elija a alguien
        self.combo_estudiantes.bind("<<ComboboxSelected>>", self.cargar_datos_tabla)


        # --- Formulario de Nota ---
        frame_nota = tk.LabelFrame(root, text="2. Ingresar Calificación", bg="#ECEFF1", padx=10, pady=10)
        frame_nota.pack(fill=tk.X, padx=20, pady=5)

        
        # ETIQUETA Y COMBOBOX PARA CURSOS
        tk.Label(frame_nota, text="Materia:", bg="#ECEFF1").grid(row=0, column=0, padx=5)
        self.combo_cursos = ttk.Combobox(frame_nota, width=30, state="readonly")
        self.combo_cursos.grid(row=0, column=1, padx=5)

        # ETIQUETA PARA PERIODO
        tk.Label(frame_nota, text="Periodo:", bg="#ECEFF1").grid(row=0, column=0, padx=5)
        self.combo_periodo = ttk.Combobox(frame_nota, values=["Periodo 1", "Periodo 2", "Periodo 3", "Periodo 4"])
        self.combo_periodo.grid(row=0, column=3, padx=5)

        tk.Label(frame_nota, text="Nota (0.0 - 10.0):", bg="#ECEFF1").grid(row=0, column=4, padx=5)
        self.entry_nota = tk.Entry(frame_nota, width=8)
        self.entry_nota.grid(row=0, column=5, padx=5)

        tk.Button(frame_nota, text="Asignar Calificación", bg="#8BC34A", fg="white", 
                  command=self.guardar_nota).grid(row=0, column=6, padx=20)

        # --- Tabla de Visualización ---
        self.tabla = ttk.Treeview(root, columns=("Curso", "Nota", "Periodo"), show="headings")
        self.tabla.heading("Curso", text="Materia / Curso")
        self.tabla.heading("Nota", text="Calificación")
        self.tabla.heading("Periodo", text="Periodo")
        self.tabla.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # AGREGAR: LLAMADA AL MÉTODO PARA CARGAR CURSOS AL INICIAR
        self.cargar_lista_cursos()

    #  MÉTODO PARA LLENAR EL COMBOBOX DE CURSOS DESDE LA BD
    def cargar_lista_cursos(self):
        try:
            query = "SELECT idCurso, nombre_curso FROM Curso"
            cursos = self.logic_notas.db.obtener_datos(query)
            # FORMATEAMOS COMO "ID - NOMBRE"
            lista = [f"{c[0]} - {c[1]}" for c in cursos]
            self.combo_cursos['values'] = lista
            if lista:
                self.combo_cursos.current(0)
        except Exception as e:
            print(f"Error al cargar cursos: {e}")


    def buscar_estudiante(self):
        nombre = self.entry_busqueda.get()
        resultados = self.logic_estudiantes.buscar_por_nombre(nombre)
        if resultados:
            # Formateamos para el combo: "ID - Nombre Apellido"
            lista = [f"{r['idEstudiante']} - {r['nombre']} {r['apellidos']}" for r in resultados]
            self.combo_estudiantes['values'] = lista
            self.combo_estudiantes.current(0)

            #Llamar al método para cargar datos en tabla
            self.cargar_datos_tabla()
        else:
            messagebox.showwarning("Sin resultados", "No se encontró el estudiante.")

    def guardar_nota(self):
        seleccion_est = self.combo_estudiantes.get()

        # OBTENER SELECCIÓN DEL CURSO
        seleccion_cur = self.combo_cursos.get()
        
        if not seleccion_est or not seleccion_cur:
            return messagebox.showerror("Error", "Seleccione un estudiante y un curso")
        
        try:
            id_est = seleccion_est.split(" - ")[0]

            # EXTRAER EL ID DEL CURSO SELECCIONADO
            id_cur = seleccion_cur.split(" - ")[0]

            nota = float(self.entry_nota.get())
            periodo = self.combo_periodo.get()
            
            # llamar idcurso de la clase calificaciones
            self.logic_notas.registrar_nota(id_est, id_cur, nota, periodo)
            messagebox.showinfo("Éxito", "Nota registrada")
            self.limpiar_campos()

            #Llamar al método para cargar datos en tabla
            self.cargar_datos_tabla()
            self.entry_nota.delete(0, tk.END)
            
        except ValueError:
            messagebox.showerror("Error", "La nota debe ser un número válido")

    def limpiar_campos(self):
        self.entry_nota.delete(0, tk.END)

        # TABLA NOTAS ---- Mostrar calificaciones en Tabla  
    def cargar_datos_tabla(self, event = None):
       # Limpiar la tabla antes de cargar nuevos datos
        for i in self.tabla.get_children():
            self.tabla.delete(i)

        # Obtener el texto del Combobox de estudiantes
        seleccion = self.combo_estudiantes.get() 
    
        if not seleccion:
        # Si no hay nadie seleccionado, no intentamos buscar notas
            return

        try:
            # Extraer el ID (asumiendo que el formato es "ID - Nombre")
            id_estudiante = seleccion.split(" - ")[0]

            # PASAR EL ID a la función
            notas = self.logic_notas.obtener_notas_por_estudiante(id_estudiante)

        # Insertar los datos en la tabla
            for cali in notas:
            # Ajusta los nombres de las columnas según consulta SQL
                self.tabla.insert("", "end", values=(
                cali['nombre_curso'], 
                cali['nota'], 
                cali['periodo']
            ))
        except Exception as e:
            print(f"Error al cargar tabla: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaNotas(root)
    root.mainloop()