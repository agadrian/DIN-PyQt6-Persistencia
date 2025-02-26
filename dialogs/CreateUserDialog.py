from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from db_functions import *
import os
import json
from utils import *


class UserDialog(QDialog):
    def __init__(self, parent=None):
        super(UserDialog, self).__init__(parent)

        ruta_ui = os.path.join(os.path.dirname(__file__), "../ui", "dialogs", "CreateUserDialog.ui")
        uic.loadUi(ruta_ui, self)

        self.btn_addUser.clicked.connect(self.insert_new_user)
        self.btn_cancel.clicked.connect(lambda: self.reject())

    
    def add_user(self):
        QMessageBox.information(self, "Éxito", f"okokokok")
    
    

    # Insertar usuario
    def insert_new_user(self):
        try:
            username = self.lineEdit_username.text()
            email = self.lineEdit_email.text()
            password = self.lineEdit_password.text()
            phone = self.lineEdit_phone.text()

            comprobaciones_input(username, email, phone, password)

            # Obtener cursor
            conn, cursor = get_db_connection()
            if conn is None or cursor is None:
                raise Exception("No se pudo conectar a la base de datos.")
            

            # Guardarlo en SQLite -> usuarios
            cursor.execute("INSERT INTO usuarios (nombre, email, telefono) VALUES (?, ?, ?)", (username, email, phone))
            conn.commit()
            close_db_connection(conn)

            # Crear user en fireabse
            user = auth.create_user_with_email_and_password(email, password)
        
            QMessageBox.information(self, "Éxito", f"Usuario registrado correctamente")
            self.reject()


        except Exception as e:
            print(e)
            if len(e.args) > 1: # Firebase
                try:
                    error_json = json.loads(e.args[1])
                    error_msg = error_json["error"]["message"]
                except (json.JSONDecodeError, KeyError):
                    error_msg = str(e)
            else: #SQLitee
                error_msg = str(e)

            
            mensaje = FIREBASE_ERRORS.get(error_msg, f"Error: {error_msg}")
            QMessageBox.warning(self, "Error", mensaje)
        finally:
            close_db_connection(conn)
    


    