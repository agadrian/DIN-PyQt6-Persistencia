from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from db_functions import *
import os
import json
import re




class UpdateUserDialog(QDialog):
    def __init__(self, user_id, user_data):
        super().__init__()


        ruta_ui = os.path.join(os.path.dirname(__file__), "../ui", "dialogs", "UpdateUserDialog.ui")
        uic.loadUi(ruta_ui, self)


        self.user_id = user_id
        self.user_data = user_data


        self.btn_updateUser.clicked.connect(self.update_user)
        self.btn_cancel.clicked.connect(lambda: self.reject())

        self.set_previus_data()


        

    def set_previus_data(self):
        self.lineEdit_username.setText(self.user_data[1])  # Nombre
        self.lineEdit_email.setText(self.user_data[2])  # Email
        self.lineEdit_address.setText(self.user_data[3]) # Direccion
        self.lineEdit_phone.setText(self.user_data[4])  # Tlfn



    def update_user(self):
        new_name = self.lineEdit_username.text().strip()
        new_email = self.lineEdit_email.text().strip()
        new_address = self.lineEdit_address.text().strip()
        new_phone = self.lineEdit_phone.text().strip()

        try:
            conn, cursor = get_db_connection()

            # Comprobar los nuevos valores (funcion en uutils.py)
            # importar desdde aqui porque desde arriba provoca error de importacion circular
            from utils import comprobaciones_input
            comprobaciones_input(new_name, new_email, new_phone)

            cursor.execute("UPDATE usuarios SET nombre = ?, email = ?, direccion = ?, telefono = ? WHERE id = ?", (new_name, new_email, new_address, new_phone, self.user_id))
            conn.commit()
            QMessageBox.information(self, "Éxito", "Usuario actualizado correctamente")
            self.accept()


        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error: {str(e)}")
        finally:
            close_db_connection(conn)