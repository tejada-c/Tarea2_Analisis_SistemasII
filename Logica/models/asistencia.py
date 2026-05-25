from Conexion.database_manager import DatabaseManager

class AsistenciaLogic:
    def __init__(self):
        self.db = DatabaseManager()

    def registrar_asistencia(self, id_estudiante, fecha, estado):
        # estado: 'Presente' o 'Ausente'
        query = "INSERT INTO Asistencia (idEstudiante, fecha, estado) VALUES (?, ?, ?)"
        self.db.ejecutar_consulta(query, (id_estudiante, fecha, estado))

    def obtener_asistencia_fecha(self, fecha, grado):
        query = """SELECT e.idEstudiante, e.nombre || ' ' || e.apellidos as estudiante, a.estado 
                   FROM Estudiante e
                   LEFT JOIN Asistencia a ON e.idEstudiante = a.idEstudiante AND a.fecha = ?
                   WHERE e.grado = ?"""
        return self.db.obtener_datos(query, (fecha, grado))