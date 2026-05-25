from Conexion.database_manager import DatabaseManager
from Logica.auth_manager import AuthManager

class ResponsableLogic:
    def __init__(self):
        self.db = DatabaseManager()
        self.auth = AuthManager()

    def registrar_responsable(self, usuario, password, parentesco, telefono, id_estudiante):
        # 1. Crear el usuario de acceso
        pass_cifrada = self.auth.encriptar_password(password)
        
        # Insertamos al padre en la tabla Usuario
        query_user = "INSERT INTO Usuario (nombre, clave, rol) VALUES (?, ?, 'Padre')"
        # Obtenemos el ID generado para este nuevo usuario
        id_usuario_padre = self.db.ejecutar_consulta(query_user, (usuario, pass_cifrada))

        # 2. Guardar sus datos en la tabla Responsable vinculándolo al Usuario y al Estudiante
        query_resp = """
            INSERT INTO Responsable (parentesco, telefono, idUsuario, idEstudianteAsociado) 
            VALUES (?, ?, ?, ?)
        """
        self.db.ejecutar_consulta(query_resp, (parentesco, telefono, id_usuario_padre, id_estudiante))

    def obtener_estudiantes_lista(self):
        # Trae a los estudiantes para el combobox
        query = "SELECT idUsuario, nombre FROM Usuario WHERE rol = 'Estudiante'"
        res = self.db.obtener_datos(query)
        return [f"{r[0]} - {r[1]}" for r in res]

    def buscar_por_nombre(self, nombre):
        query = "SELECT * FROM Responsable WHERE nombre_responsable LIKE ?"
        return self.db.obtener_datos(query, (f"%{nombre}%",))

    def obtener_todos(self):
        query = "SELECT idResponsable, nombre_responsable, dui, telefono, parentesco FROM Responsable"
        return self.db.obtener_datos(query)