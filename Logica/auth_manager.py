import bcrypt

class AuthManager:
    @staticmethod
    def encriptar_password(password):
        # Genera el hash para guardar en la base de datos 
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed

    @staticmethod
    def verificar_password(password_plano, password_hasheado):
        # Compara la entrada del login con lo guardado en la BD 
        return bcrypt.checkpw(password_plano.encode('utf-8'), password_hasheado)