from Conexion.database_manager import DatabaseManager

class DocenteLogic:
    def __init__(self):
        self.db = DatabaseManager()

    def registrar_docente(self, nombre, especialidad):
        query = "INSERT INTO Docente (nombre_docente, especialidad) VALUES (?, ?)"
        self.db.ejecutar_consulta(query, (nombre, especialidad))

    def obtener_todos(self):
        # Sincronizado con la tabla de docentes_gui
        query = "SELECT idDocente, nombre_docente, especialidad FROM Docente"
        return self.db.obtener_datos(query)