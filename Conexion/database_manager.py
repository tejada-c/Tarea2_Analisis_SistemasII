import sqlite3
import os

class DatabaseManager:
    def __init__(self):
        # Define la ruta según tu requerimiento
        self.db_path = os.path.join("Datos", "SistemaEscolarDB.sqlite")
        
    def conectar(self):
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row # Permite acceder a columnas por nombre
            return conn
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def ejecutar_consulta(self, consulta, parametros=()):
        conn = self.conectar()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(consulta, parametros)
                conn.commit()
                # Rcupera el ID generado automáticamente
                ultimo_id = cursor.lastrowid 
                return ultimo_id
            except Exception as e:
                print(f"Error en consulta: {e}")
                return None
            finally:
                conn.close()

    def obtener_datos(self, consulta, parametros=()):
        conn = self.conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta, parametros)
            resultados = cursor.fetchall()
            conn.close()
            return resultados
        return []