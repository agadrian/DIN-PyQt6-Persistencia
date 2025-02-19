
import re
from db_functions import auth

def comprobaciones_input(username, email, phone, password, password2 = None):
    
        # Comprobaciones de los campos
        
        if not username:
            raise Exception("El nombre de usuario no puede estar vacío.")
        
        if not email:
            raise Exception("El correo electrónico no puede estar vacío.")
    
        if not validar_email(email):
            raise Exception("El correo electrónico no es válido.")
        
        if not validar_password(password):
            raise Exception("Contraseña demasiado débil")
        
        if not password:
            raise Exception("La contraseña no puede estar vacía.")
        
        if not phone:
            raise Exception("El úmero de telefono no puede estar vacío")
        
        if password2 is not None:
            if password != password2:
                raise Exception("Las contraseñas no coinciden")
        
        

def validar_email(email):
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email) is not None

def validar_password(password):
    if len(password) < 8:
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    
    return True