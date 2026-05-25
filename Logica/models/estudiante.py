from Conexion.database_manager import DatabaseManager

class EstudianteLogic:
    def __init__(self):
        self.db = DatabaseManager()

    def registrar_estudiante(self, nombre, apellidos, codigo, grado, edad, estado, fecha_nac, id_usuario, id_responsable):
        query = """INSERT INTO Estudiante (nombre, apellidos, codigo, grado, edad, estado, fecha_nacimiento, idUsuario, idResponsable) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        parametros = (nombre, apellidos, codigo, grado, edad, estado, fecha_nac, id_usuario, id_responsable)
        self.db.ejecutar_consulta(query, parametros)

    def obtener_todos(self):
        query = "SELECT idEstudiante, nombre, apellidos, codigo, grado, estado FROM Estudiante"
        return self.db.obtener_datos(query)

    def buscar_por_nombre(self, nombre):
        query = "SELECT * FROM Estudiante WHERE nombre LIKE ?"
        return self.db.obtener_datos(query, (f"%{nombre}%",))