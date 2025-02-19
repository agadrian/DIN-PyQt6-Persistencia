
import os
from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
import pyrebase
import json
import sqlite3
from login import auth, FIREBASE_ERRORS
from db_functions import *
from utils import *

class RegisterWindow(QWidget):
    def __init__(self, main_app):
        super(RegisterWindow, self).__init__()
        self.main_app = main_app

        # Ruta del .ui
        ruta_ui = os.path.join(os.path.dirname(__file__), "ui", "pages", "Register.ui")
        uic.loadUi(ruta_ui, self)

        self.setFixedSize(self.size())

        # Conectar boton
        self.btn_singup.clicked.connect(self.register)

    
    def register(self):
        try:

            username = self.lineEdit_username.text()
            email = self.lineEdit_email.text()
            phone = self.lineEdit_phone.text()
            password = self.lineEdit_password.text()
            password2 = self.lineEdit_confirmPassword.text()
            
            comprobaciones_input(username, email, phone, password, password2)
            

            # Gurdarlo en SQLite -> usuarios
            conn, cursor = get_db_connection()
            if conn is None or cursor is None:
                raise Exception("No se pudo conectar a la base de datos.")
    
            cursor.execute("INSERT INTO usuarios (nombre, email, telefono) VALUES (?, ?, ?)", (username, email, phone))
            conn.commit()
            close_db_connection(conn)

            # Crear user en fireabse
            user = auth.create_user_with_email_and_password(email, password)

            QMessageBox.information(self, "Éxito", f"Usuario registrado correctamente")
            
            self.main_app.switch_to_main()



        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))
        except Exception as e:

            if len(e.args) > 1:
                try:
                    error_json = json.loads(e.args[1])
                    error_msg = error_json["error"]["message"]
                except (json.JSONDecodeError, KeyError):
                    error_msg = str(e)
            else:
                error_msg = str(e)
            
            mensaje = FIREBASE_ERRORS.get(error_msg, f"Error: {error_msg}")
            QMessageBox.warning(self, "Error", mensaje)

    
