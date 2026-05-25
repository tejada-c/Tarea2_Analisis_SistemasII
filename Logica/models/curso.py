from Conexion.database_manager import DatabaseManager

class CursoLogic:
    def __init__(self):
        self.db = DatabaseManager()

    def registrar_curso(self, nombre, descripcion, id_docente=1):
        query = "INSERT INTO Curso (nombre_curso, descripcion, idDocente) VALUES (?, ?, ?)"
        self.db.ejecutar_consulta(query, (nombre, descripcion, id_docente))

    def obtener_todos(self):
        # Sincronizado con cargar_lista_cursos de notas_gui
        query = "SELECT idCurso, nombre_curso, descripcion FROM Curso"
        return self.db.obtener_datos(query)