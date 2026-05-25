from Conexion.database_manager import DatabaseManager

class ReporteLogic:
    def __init__(self):
        self.db = DatabaseManager()

    def obtener_mis_notas(self, id_usuario):
        # 1. Averiguamos el rol del que está logueado
        query_rol = "SELECT rol FROM Usuario WHERE idUsuario = ?"
        res_rol = self.db.obtener_datos(query_rol, (id_usuario,))
    
        if not res_rol: return []
        rol = res_rol[0][0]

        # 2. Definimos el ID del estudiante para buscar sus notas
        if rol == 'Estudiante':
             # Si es estudiante, el id_usuario_actual es el que usamos
            id_estudiante_objetivo = id_usuario
        elif rol == 'Padre':
            # SI ES PADRE: Buscamos en la tabla Estudiante quién tiene este Responsable
            # Primero necesitamos saber el ID de responsable asociado a este Usuario
            query_hijo = """
            SELECT idUsuario FROM Estudiante 
            WHERE idResponsable = (SELECT idResponsable FROM Responsable WHERE idUsuario = ?)
            """
            res_hijo = self.db.obtener_datos(query_hijo, (id_usuario,))
            if not res_hijo: return []
            id_estudiante_objetivo = res_hijo[0][0] # Tomamos el idUsuario del estudiante
        else:
            return []

        # 3. Consulta final de notas usando el idUsuario del Estudiante
        query_notas = """
        SELECT m.nombre_curso, c.nota, c.periodo 
        FROM Calificacion c
        JOIN Curso m ON c.idCurso = m.idCurso
        WHERE c.idEstudiante = ?
        """
        return self.db.obtener_datos(query_notas, (id_estudiante_objetivo,))


        ## cODIGO ANTERIOR
        # Primero buscamos el idEstudiante asociado a ese idUsuario
        #query_est = "SELECT idEstudiante FROM Estudiante WHERE idUsuario = ?"
       # estudiante = self.db.obtener_datos(query_est, (id_usuario,))
        
        #if estudiante:
          #   id_est = estudiante[0]['idEstudiante']
           # # Traemos las notas vinculadas a ese estudiante
            #query_notas = """
             #   SELECT cu.nombre_curso, c.nota, c.periodo 
              #  FROM Calificacion c
               # JOIN Curso cu ON c.idCurso = cu.idCurso
                #WHERE c.idEstudiante = ?
            #"""
            #return self.db.obtener_datos(query_notas, (id_est,))
        return []