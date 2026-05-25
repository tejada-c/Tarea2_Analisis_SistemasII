import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Importamos las interfaces que ya desarrollamos
from Interfaz.estudiantes_gui import VentanaEstudiantes
from Interfaz.notas_gui import VentanaNotas

class MenuPrincipal:
    def __init__(self, root, nombre_usuario):
        self.root = root
        self.root.title("SISTEMA DE REGISTRO ACADÉMICO - MENÚ PRINCIPAL")
        self.root.geometry("800x600")
        self.root.update_idletasks() # Obliga a Tkinter a renderizar los widgets antes de mostrar
        self.root.configure(bg="#ECEFF1") # Gris azulado muy claro
        self.nombre_usuario = nombre_usuario

       

        # --- Barra Superior ---
        self.barra_superior = tk.Frame(root, bg="#01579B", height=40) # Azul oscuro
        self.barra_superior.pack(fill=tk.X)
        
        tk.Label(self.barra_superior, text="SISTEMA DE REGISTRO ACADÉMICO - MENÚ PRINCIPAL", 
                 fg="white", bg="#01579B", font=("Arial", 12, "bold")).pack(pady=5)

        # --- Botones de Control Superior ---
        self.frame_controles = tk.Frame(root, bg="#ECEFF1")
        self.frame_controles.pack(fill=tk.X, padx=10, pady=5)

        tk.Button(self.frame_controles, text="Gestionar Usuarios", command=self.abrir_gestion_usuarios).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_controles, text="Cerrar Sesión", command=self.cerrar_sesion).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_controles, text="Salir", command=root.quit).pack(side=tk.RIGHT, padx=5)

        # --- Cuadrícula de Botones (Grid) ---
        self.contenedor_grid = tk.Frame(root, bg="#ECEFF1")
        self.contenedor_grid.pack(expand=True)

        # Definición de botones basados en el PDF 
        opciones = [
            ("Estudiantes", "icon_estudiante.png", self.abrir_estudiantes),
            ("Cursos", "icon_cursos.png", self.abrir_cursos),
            ("Notas", "icon_notas.png", self.abrir_notas),
            ("Docentes", "icon_docentes.png", self.abrir_docentes),
            ("Asistencia", "icon_asistencia.png", self.abrir_asistencia),
            ("Responsables", "icon_responsables.png", self.abrir_responsables)
        ]

        fila = 0
        columna = 0
        for texto, icono, comando in opciones:
            self.crear_boton_menu(texto, icono, comando, fila, columna)
            columna += 1
            if columna > 2: # 3 columnas por fila
                columna = 0
                fila += 1

    def crear_boton_menu(self, texto, nombre_icono, comando, f, c):
        # Frame para cada botón
        frame_btn = tk.Frame(self.contenedor_grid, bg="#ECEFF1", padx=20, pady=20)
        frame_btn.grid(row=f, column=c)

        # Intento de cargar icono
        try:
            img = Image.open(nombre_icono).resize((80, 80))
            photo = ImageTk.PhotoImage(img)
            btn = tk.Button(frame_btn, image=photo, command=comando, bg="white", relief="flat")
            btn.image = photo # Referencia para que no desaparezca
            btn.pack()
        except:
            # Botón de respaldo si no hay imagen
            tk.Button(frame_btn, text="[ICONO]", width=10, height=5, command=comando).pack()

        tk.Label(frame_btn, text=texto, font=("Arial", 12, "bold"), bg="#ECEFF1", fg="#1A237E").pack(pady=5)

    # --- Funciones de Navegación ---
    def abrir_estudiantes(self):
       # Ocultamos el Menú Principal
        self.root.withdraw()
                
        # Aquí llamaremos a la ventana estudiantes
        nueva_ventana = tk.Toplevel(self.root) # Toplevel para que dependa de la principal
        VentanaEstudiantes(nueva_ventana)

       # Usamos un método dedicado para configurar el cierre
        self.configurar_retorno(nueva_ventana)
    
    # método genérico para configurar cualquier ventana hija
    def configurar_retorno(self, ventana_hija):
        # ventana_hija ya entra como parámetro
        ventana_hija.protocol("WM_DELETE_WINDOW", lambda: self.al_cerrar_hija(ventana_hija))


    def al_cerrar_hija(self, ventana_hija):
        ventana_hija.destroy() # Destruimos la ventana de registro
        self.root.deiconify()  # Volvemos a mostrar el Menú Principal

    def abrir_docentes(self):
        # Ocultamos el Menú Principal
        self.root.withdraw()

        from Interfaz.docentes_gui import VentanaDocentes
        nueva = tk.Toplevel(self.root)
        VentanaDocentes(nueva)

        # Configuramos el retorno
        self.configurar_retorno(nueva)

    def abrir_responsables(self):

        # Ocultamos el Menú Principal
        self.root.withdraw()

        from Interfaz.responsables_gui import VentanaResponsables
        # Creamos la ventana hija
        nueva_ventana = tk.Toplevel(self.root)
        VentanaResponsables(nueva_ventana)

        # Configuramos el retorno
        self.configurar_retorno(nueva_ventana)

    def abrir_cursos(self): 
        # Ocultamos el Menú Principal
        self.root.withdraw()

        from Interfaz.cursos_gui import VentanaCursos # Importación local para evitar ciclos
        nueva = tk.Toplevel(self.root)
        VentanaCursos(nueva)

        # Configuramos el retorno
        self.configurar_retorno(nueva)

    def abrir_notas(self): 

        # Ocultamos el Menú Principal
        self.root.withdraw()

        #Abre la gestión de calificaciones
        nueva_ventana = tk.Toplevel(self.root)
        VentanaNotas(nueva_ventana)

        # Configuramos el retorno
        self.configurar_retorno(nueva_ventana)
        
    def abrir_asistencia(self): 

        # Ocultamos el Menú Principal
        self.root.withdraw()

        from Interfaz.asistencia_gui import VentanaAsistencia
        nueva = tk.Toplevel(self.root)
        VentanaAsistencia(nueva)

        # Configuramos el retorno
        self.configurar_retorno(nueva)

    def abrir_gestion_usuarios(self): 

        # Ocultamos el Menú Principal
        self.root.withdraw()

        from Interfaz.usuarios_gui import VentanaUsuarios
        ventana_hija = tk.Toplevel(self.root)
        VentanaUsuarios(ventana_hija)

         # Configuramos el retorno
        self.configurar_retorno(ventana_hija)

    def cerrar_sesion(self):
        if messagebox.askyesno("Cerrar Sesión", "¿Está seguro que desea salir al Login?"):
            self.root.destroy()
            # Aquí se reiniciaría el archivo login_gui.py

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuPrincipal(root, "Docente de Prueba")
    root.mainloop()