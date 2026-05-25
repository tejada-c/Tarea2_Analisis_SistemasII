from Conexion.database_manager import DatabaseManager

class CalificacionLogic:
    def __init__(self):
        self.db = DatabaseManager()

    def registrar_nota(self, id_estudiante, id_curso, nota, periodo):
        query = """INSERT INTO Calificacion (nota, periodo, idEstudiante, idCurso) 
                   VALUES (?, ?, ?, ?)"""
        parametros = (nota, periodo, id_estudiante, id_curso)
        self.db.ejecutar_consulta(query, parametros)

    def obtener_notas_por_estudiante(self, id_estudiante):
        query = """SELECT c.idCalificacion, cu.nombre_curso, c.nota, c.periodo 
                   FROM Calificacion c
                   LEFT JOIN Curso cu ON c.idCurso = cu.idCurso
                   WHERE c.idEstudiante = ?"""
        return self.db.obtener_datos(query, (int(id_estudiante),))