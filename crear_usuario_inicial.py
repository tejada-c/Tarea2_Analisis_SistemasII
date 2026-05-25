import sqlite3
import os
import bcrypt
from Logica.auth_manager import AuthManager

def crear_usuario_maestro():
    # 1. Configurar la ruta a la base de datos
    db_path = os.path.join("Datos", "SistemaEscolarDB.sqlite")
    
    # 2. Datos del usuario inicial
    nombre_usuario = "admin"
    password_plana = "INTES20123" # Esta es la que escribirás en el Login
    rol = "Profesor"
    
    # 3. Encriptar la contraseña usando tu clase AuthManager
    # Si no tienes la clase a mano, usamos bcrypt directamente:
    salt = bcrypt.gensalt()
    password_encriptada = bcrypt.hashpw(password_plana.encode('utf-8'), salt)

    # 4. Insertar en la base de datos
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Ajustamos a las columnas de tu tabla 'Usuario' según el PDF
        query = "INSERT INTO Usuario (nombre, clave, rol) VALUES (?, ?, ?)"
        cursor.execute(query, (nombre_usuario, password_encriptada, rol))
        
        conn.commit()
        print(f"¡Éxito! Usuario '{nombre_usuario}' creado correctamente.")
        print(f"Rol: {rol}")
        print(f"Contraseña: {password_plana}")
        
    except sqlite3.Error as e:
        print(f"Error al insertar el usuario: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    # Asegurarse que la carpeta de la base de Datos exista antes de ejecutar
    if not os.path.exists("Datos"):
        os.makedirs("Datos")
    crear_usuario_maestro()