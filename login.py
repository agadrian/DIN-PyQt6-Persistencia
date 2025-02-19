from PyQt6.QtWidgets import * 
from PyQt6 import uic  
import os
import json

from db_functions import *



# TODO: Cuando se cree un usuario manualmente desde el panel, meterlo primero en firebase con las comprobaciones, y luego en la base de datos de sqlite con la id de firbase (como si fuera registro normal)
# TODO: 
# TODO: 
# TODO: 


class LoginWindow(QWidget):

    def __init__(self, main_app):
        super(LoginWindow, self).__init__()
        self.main_app = main_app

        # Ruta del .ui
        ruta_ui = os.path.join(os.path.dirname(__file__), "ui", "pages", "Login.ui")
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
            conn, cursor = get_db_connection()
            if conn is None or cursor is None:
                raise Exception("No se pudo conectar a la base de datos.")
            
            cursor.execute("SELECT nombre FROM usuarios WHERE id = ?", (user_id,))
            result = cursor.fetchone()
            close_db_connection(conn)

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
           

   
    



            
        





