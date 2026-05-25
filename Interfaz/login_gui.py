import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Necesitaremos Pillow para manejar imagenes
from Logica.models.usuario import Usuario

class LoginVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("INTES - Inicio de Sesión")
        self.root.geometry("400x500")
        self.root.configure(bg="#CFD8DC") # Color gris claro 

        self.usuario_logic = Usuario()

        # --- Logo ---
        try:
            self.img = Image.open("logo_intes.png") # Nombre del logo según el PDF [cite: 1]
            self.img = self.img.resize((150, 150))
            self.logo = ImageTk.PhotoImage(self.img)
            tk.Label(root, image=self.logo, bg="#CFD8DC").pack(pady=20)
        except:
            tk.Label(root, text="LOGO INTES", font=("Arial", 14, "bold"), bg="#CFD8DC").pack(pady=20)

        # --- Campos de entrada ---
        tk.Label(root, text="Usuario:", bg="#CFD8DC", font=("Arial", 12, "bold")).pack()
        self.entry_usuario = tk.Entry(root, font=("Arial", 12), width=30)
        self.entry_usuario.pack(pady=5)

        tk.Label(root, text="Contraseña:", bg="#CFD8DC", font=("Arial", 12, "bold")).pack()
        self.entry_password = tk.Entry(root, font=("Arial", 12), width=30, show="*")
        self.entry_password.pack(pady=5)

        # --- Botones ---
        frame_botones = tk.Frame(root, bg="#CFD8DC")
        frame_botones.pack(pady=30)

        self.btn_salir = tk.Button(frame_botones, text="Salir", bg="#5C6BC0", fg="white", 
                                   width=10, command=root.quit) # Botón azul 
        
        self.btn_salir.pack(side=tk.LEFT, padx=10)

        self.btn_login = tk.Button(frame_botones, text="Iniciar Sesión", bg="#8BC34A", fg="white", 
                                    width=12, command=self.intentar_login) # Botón verde [cite: 20]
        self.btn_login.pack(side=tk.LEFT, padx=10)

    def intentar_login(self):
        user = self.entry_usuario.get()
        password = self.entry_password.get()

        # Obtenemos los datos de la base de datos
        user_id, rol = self.usuario_logic.validar_acceso(user, password) 

        if user_id:  # Si existe el ID, la contraseña es correcta
            if rol == "Profesor":
                messagebox.showinfo("Acceso", f"Bienvenido, Docente {user}")
                self.root.withdraw() # Oculta el login
                self.abrir_menu_principal(user)
            
            elif rol in ["Estudiante", "Responsable", "Padre"]:
                # IMPORTANTE: Verifica que el nombre del rol en la DB coincida con estos
                messagebox.showinfo("Acceso", f"Bienvenido al Portal de Consulta")
                self.root.withdraw() # Oculta el login
                # PASAMOS el user_id para que vea sus propias notas
                self.abrir_ventana_consulta(user_id)
            
            else:
                messagebox.showwarning("Rol no reconocido", f"El rol '{rol}' no tiene una interfaz asignada.")
        else:
            # Solo llegamos aquí si validar_acceso devolvió (None, None)
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")   



       # if rol == "Profesor":
           # messagebox.showinfo("Acceso", f"Bienvenido, Docente {user}")
            # Pasamos el nombre del usuario para el menú
            #self.abrir_menu_principal(user)
        #elif rol in ["Estudiante", "Responsable"]:
         #   messagebox.showinfo("Acceso", f"Bienvenido, {rol}")
            # PASAMOS el user_id a la siguiente función
         #   self.abrir_ventana_padres(user_id)
       # else:
        #    messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def abrir_menu_principal(self, nombre_usuario):
        # Capturamos el nombre ANTES de destruir nada
        nombre_usuario = self.entry_usuario.get()

        # Cerramos la ventana de login
        self.root.destroy()
        
        # Iniciamos el menú principal
        import tkinter as tk
        from Interfaz.main_menu_gui import MenuPrincipal
        
        main_root = tk.Tk() 
        
        # Ahora el menú sabe quién entró
        MenuPrincipal(main_root, nombre_usuario)
        main_root.mainloop()

    def abrir_ventana_consulta(self, user_id):
        # Ahora la función recibe el user_id correctamente
        self.root.withdraw()
    
        import tkinter as tk
        from Interfaz.consulta_gui import VentanaConsulta
    
        nueva_ventana = tk.Toplevel(self.root)
        # Usamos el user_id real para filtrar las notas del estudiante
        app = VentanaConsulta(nueva_ventana, user_id) 

        # Si cierran esa ventana, cerramos toda la aplicación (opcional)
        nueva_ventana.protocol("WM_DELETE_WINDOW", self.root.destroy)
        nueva_ventana.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginVentana(root)
    root.mainloop()