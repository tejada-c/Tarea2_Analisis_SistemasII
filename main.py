import tkinter as tk
from Interfaz.login_gui import LoginVentana

def lanzar_programa():
    # Creamos la ventana principal de Tkinter
    root = tk.Tk()
    
    # Instanciamos la clase de la interfaz de Login
    app = LoginVentana(root)
    
    # Iniciamos el bucle principal
    root.mainloop()

if __name__ == "__main__":
    lanzar_programa()