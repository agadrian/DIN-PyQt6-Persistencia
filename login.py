from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
import sys
import os
import pyrebase
import json
import sqlite3
from dotenv import load_dotenv

load_dotenv()

# TODO: Cuando se cree un usuario manualmente desde el panel, meterlo primero en firebase con las comprobaciones, y luego en la base de datos de sqlite con la id de firbase (como si fuera registro normal)
# TODO: 
# TODO: 
# TODO: 


# Configuración FireBase

firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID")
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()


FIREBASE_ERRORS = {
    "EMAIL_NOT_FOUND": "Este correo no está registrado.",
    "INVALID_PASSWORD": "La contraseña ingresada es incorrecta.",
    "MISSING_PASSWORD": "Contraseña requerida.",
    "USER_DISABLED": "Esta cuenta ha sido deshabilitada.",
    "INVALID_EMAIL": "El correo ingresado no es válido.",
    "INVALID_LOGIN_CREDENTIALS": "Credenciales incorrectas.",
    "TOO_MANY_ATTEMPTS_TRY_LATER": "Has intentado demasiadas veces. Intenta más tarde.",
    "WEAK_PASSWORD": "Contraseña demasiado débil.",
    "EMAIL_EXISTS": "El correo ingresado ya está registrado.",
}


class LoginWindow(QWidget):

    def __init__(self, main_app):
        super(LoginWindow, self).__init__()
        self.main_app = main_app

        # Ruta del .ui
        ruta_ui = os.path.join(os.path.dirname(__file__), "ui", "pages", "Login.ui")
        uic.loadUi(ruta_ui, self)

        self.setFixedSize(self.size())

        # Conectar botones
        self.btn_login.clicked.connect(self.login)
        self.label_singup.linkActivated.connect(lambda: self.main_app.switch_to_register())


    def login(self):
        email = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        try:
            # Verificar credenciales en firebase
            user = auth.sign_in_with_email_and_password(email, password)
            user_id = user["localId"]

            # Conexion con sqlite3
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute("SELECT nombre FROM usuarios WHERE id = ?", (user_id,))
            result = cursor.fetchone()
            conn.close()

            if result:
                username = result[0]
                QMessageBox.information(self, "Éxito", f"Bienvenid@, {username}.")
                self.main_app.switch_to_main()
            else:
                QMessageBox.warning(self, "Error", f"No se econtró el usuario en la base de datos local.")

    

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
           

   
    



            
        





