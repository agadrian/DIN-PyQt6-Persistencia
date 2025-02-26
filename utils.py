
import re
from db_functions import auth
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic   
from dialogs.UpdateUserDialog import UpdateUserDialog


def comprobaciones_input(username, email, phone, password= None, password2 = None):
    
        # Comprobaciones de los campos
        
        if not username:
            raise Exception("El nombre de usuario no puede estar vacío.")
        
        if not email:
            raise Exception("El correo electrónico no puede estar vacío.")
    
        if not validar_email(email):
            raise Exception("El correo electrónico no es válido.")
        
        if password is not None:
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



# Crear los botones de editar y eliminar una fila de la tabla
class Edit_delete_widget_function(QWidget):
    def __init__(self,parent, row_index, row_data):
        super().__init__()
        self.parent = parent
        # Instanciar el index y el data 
        self.row_index = row_index
        self.row_data = row_data

        # Variable de la tupla+
        self.item_id = self.row_data[0]
        self.item_name = self.row_data[1]

        layout = QHBoxLayout(self)

        # Boton edit - blue 
        self.edit_button = QPushButton("", self)
        #self.edit_button.setStyleSheet("background-color: blue")
        self.edit_button.setFixedSize(60,30)
        icon = QIcon("ui/lupaa.png")
        self.edit_button.setIcon(icon)
        self.edit_button.clicked.connect(self.edit_clicked) # Abrir el dialog


        # Boton delete - red 
        self.delete_button = QPushButton("", self)
        #self.delete_button.setStyleSheet("background-color: red")
        self.delete_button.setFixedSize(60,30)
        icon2 = QIcon("ui/lupaa.png")
        self.delete_button.setIcon(icon2)


        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)


    def edit_clicked(self):
        # Instanciar la clase del UpdateDIalog
        dialog = UpdateUserDialog(self.item_id, self.row_data)

        # Ejectura el Dialog
        if dialog.exec():
            self.parent.load_users()

