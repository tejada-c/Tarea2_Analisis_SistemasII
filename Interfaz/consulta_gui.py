import tkinter as tk
from tkinter import ttk, messagebox
from Logica.models.reporte import ReporteLogic

class VentanaConsulta:
    def __init__(self, root, id_usuario_logueado):
        self.root = root
        self.root.title("Consulta Familiar - INTES")
        self.root.geometry("600x500")
        self.root.configure(bg="#ECEFF1")
        
        self.id_usuario = id_usuario_logueado
        self.logic = ReporteLogic()

        # --- Encabezado ---
        header = tk.Frame(root, bg="#455A64", height=80)
        header.pack(fill=tk.X)
        tk.Label(header, text="PANEL DE CONSULTA ACADÉMICA", fg="white", 
                 bg="#455A64", font=("Arial", 14, "bold")).pack(pady=20)

        # --- Contenedor de Botones (Solo los 2 permitidos) ---
        frame_opciones = tk.Frame(root, bg="#ECEFF1")
        frame_opciones.pack(pady=30)

        # Botón Notas
        self.btn_notas = tk.Button(frame_opciones, text="Ver Calificaciones", 
                                   bg="#0288D1", fg="white", width=20, height=2,
                                   command=self.mostrar_notas)
        self.btn_notas.grid(row=0, column=0, padx=20)

        # Botón Asistencia
        self.btn_asistencia = tk.Button(frame_opciones, text="Ver Asistencia", 
                                        bg="#FBC02D", fg="black", width=20, height=2,
                                        command=self.mostrar_asistencia)
        self.btn_asistencia.grid(row=0, column=1, padx=20)

        # --- Área de Visualización ---
        self.label_info = tk.Label(root, text="Seleccione una opción para ver detalles", 
                                   bg="#ECEFF1", font=("Arial", 10, "italic"))
        self.label_info.pack(pady=10)

        self.tabla = ttk.Treeview(root, columns=("Col1", "Col2", "Col3"), show="headings", height=8)
        self.tabla.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        tk.Button(root, text="Cerrar Sesión", command=root.quit).pack(pady=10)

    def mostrar_notas(self):
        self.label_info.config(text="Mostrando: CALIFICACIONES ACTUALES", fg="#0288D1")
        # Configurar columnas para notas
        self.tabla.heading("Col1", text="Materia")
        self.tabla.heading("Col2", text="Nota")
        self.tabla.heading("Col3", text="Periodo")
        
        # Limpiar y cargar
        for i in self.tabla.get_children(): self.tabla.delete(i)
        
        notas = self.logic.obtener_mis_notas(self.id_usuario)
        if notas:
            for n in notas:
                self.tabla.insert("", "end", values=(n['nombre_curso'], n['nota'], n['periodo']))
        else:
            messagebox.showinfo("Info", "Aún no hay notas registradas para este estudiante.")

    def mostrar_asistencia(self):
        self.label_info.config(text="Mostrando: REGISTRO DE ASISTENCIA", fg="#F67C00")
        # En un prototipo real, aquí conectarías con la tabla Asistencia de tu DB
        messagebox.showinfo("Asistencia", "Funcionalidad de asistencia en desarrollo para la Fase 2.")

if __name__ == "__main__":
    root = tk.Tk()
    # Simulamos que entró el usuario ID 1 (que debería ser un estudiante)
    app = VentanaConsulta(root, 1)
    root.mainloop()