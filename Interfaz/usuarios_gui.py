import tkinter as tk
from tkinter import ttk, messagebox
from Logica.models.usuario import Usuario

class VentanaUsuarios:
    def __init__(self, root):
        self.root = root
        self.root.title("Seguridad - INTES")
        self.root.geometry("700x500")
        self.root.configure(bg="#ECEFF1")
        
        self.logic = Usuario()

        # --- Título ---
        tk.Label(root, text="ADMINISTRACIÓN DE USUARIOS", font=("Arial", 14, "bold"), 
                 bg="#455A64", fg="white").pack(fill=tk.X, pady=10)

        # --- Formulario ---
        frame_form = tk.LabelFrame(root, text="Nuevo Usuario", bg="#ECEFF1", padx=10, pady=10)
        frame_form.pack(fill=tk.X, padx=20, pady=5)

        #tk.Label(frame_form, text="Nombre Real:", bg="#ECEFF1").grid(row=0, column=0, sticky="w")
        #self.ent_nombre = tk.Entry(frame_form, width=25)
        #self.ent_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Usuario:", bg="#ECEFF1").grid(row=0, column=0, sticky="w")
        self.ent_user = tk.Entry(frame_form, width=25)
        self.ent_user.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        tk.Label(frame_form, text="Contraseña:", bg="#ECEFF1").grid(row=1, column=0, sticky="w")
        self.ent_pass = tk.Entry(frame_form, width=25, show="*")
        self.ent_pass.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        tk.Label(frame_form, text="Rol:", bg="#ECEFF1").grid(row=1, column=2, sticky="w")
        self.combo_rol = ttk.Combobox(frame_form, values=["Docente", "Estudiante", "Padre"], width=17)
        self.combo_rol.grid(row=1, column=3, sticky="w", padx=5, pady=5)

        tk.Button(frame_form, text="Crear Usuario", bg="#00897B", fg="white", 
                  command=self.guardar_usuario).grid(row=2, column=0, columnspan=4, pady=10)

        # --- Tabla ---
        self.tabla = ttk.Treeview(root, columns=("ID", "User", "Rol"), show="headings")
        self.tabla.heading("ID", text="ID")
        # self.tabla.heading("Nombre", text="Nombre Real")
        self.tabla.heading("User", text="Usuario")
        self.tabla.heading("Rol", text="Rol")
        self.tabla.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.cargar_datos()

    def guardar_usuario(self):
        #nombre = self.ent_nombre.get()
        user = self.ent_user.get()
        pas = self.ent_pass.get()
        rol = self.combo_rol.get()

        if not (user and pas and rol):
            return messagebox.showerror("Error", "Todos los campos son obligatorios")

        try:
            self.logic.registrar_usuario(user, pas, rol)
            messagebox.showinfo("Éxito", "Usuario creado correctamente")
            self.limpiar_campos()
            self.cargar_datos()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear: {e}")

    def cargar_datos(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        
        usuarios = self.logic.obtener_usuarios()
        for u in usuarios:
            # u[0]=id, u[1]=nombre, u[2]=username, u[3]=rol
            #self.tabla.insert("", "end", values=(u[0], u[1], u[2], u[3]))
           
           #CAMBIOS SIN NOMBRE REAL
            # u[0]=idUsuario, u[1]=nombre, u[2]=rol [según tu query en UsuarioLogic]
            self.tabla.insert("", "end", values=(u[0], u[1], u[2]))

    def limpiar_campos(self):
        #self.ent_nombre.delete(0, tk.END)
        self.ent_user.delete(0, tk.END)
        self.ent_pass.delete(0, tk.END)
        self.combo_rol.set("")