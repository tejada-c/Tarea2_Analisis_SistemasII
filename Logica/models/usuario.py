from Conexion.database_manager import DatabaseManager
from Logica.auth_manager import AuthManager

class Usuario:
    def __init__(self):
        self.db = DatabaseManager()
        self.auth = AuthManager()

    def validar_acceso(self, nombre_usuario, password_ingresada):
        query = "SELECT idUsuario, clave, rol FROM Usuario WHERE nombre = ?"
        resultado = self.db.obtener_datos(query, (nombre_usuario,))
        if resultado:
            datos = resultado[0]
            if self.auth.verificar_password(password_ingresada, datos['clave']):
                return datos['idUsuario'], datos['rol']
        return None, None

    # MÉTODO PARA REGISTRAR CON ENCRIPTACIÓN
    def registrar_usuario(self, username, password, rol):
        # Encriptamos la contraseña antes de guardarla
        password_encriptada = self.auth.encriptar_password(password)
        query = """INSERT INTO Usuario (nombre, clave, rol) 
                   VALUES (?, ?, ?)"""
        self.db.ejecutar_consulta(query, ( username, password_encriptada, rol))

    # MÉTODO PARA LA TABLA DE LA GUI
    def obtener_usuarios(self):
        query = "SELECT idUsuario, nombre, rol FROM Usuario"
        return self.db.obtener_datos(query)