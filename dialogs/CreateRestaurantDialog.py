from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from db_functions import *
import os
from utils import *


class RestaurantDialog(QDialog):
    def __init__(self, parent=None):
        super(RestaurantDialog, self).__init__(parent)

        ruta_ui = os.path.join(os.path.dirname(__file__), "../ui", "dialogs", "CreateRestaurantDialog.ui")
        uic.loadUi(ruta_ui, self)

        self.btn_addRestaurant.clicked.connect(self.insert_new_restaurant)
        self.btn_cancel.clicked.connect(lambda: self.reject())


    

    # Insertar restaurante
    def insert_new_restaurant(self):
        try:
            name = self.lineEdit_name.text()
            address = self.lineEdit_address.text()
            category = self.lineEdit_category.text()
            phone = self.lineEdit_phone.text()
            schedule = self.lineEdit_schedule.text()
            qual = self.lineEdit_qualification.text()

            ## comprobaciones_input(username, email, phone, password)

            # Obtener cursor
            conn, cursor = get_db_connection()
            if conn is None or cursor is None:
                raise Exception("No se pudo conectar a la base de datos.")
            

            # Guardarlo en SQLite -> restaurantes
            cursor.execute("INSERT INTO restaurantes (nombre, direccion, categoria, telefono, horario, calificacion) VALUES (?, ?, ?, ?, ?, ?)", (name, address, category, phone, schedule, qual))

            conn.commit()
            close_db_connection(conn)

        
            QMessageBox.information(self, "Éxito", f"Restaurante creado correctamente")
            self.reject()


        except Exception as e:
            print(e)
            error_msg = str(e)

            #mensaje = FIREBASE_ERRORS.get(error_msg, f"Error: {error_msg}")
            QMessageBox.warning(self, "Error", error_msg)
        finally:
            close_db_connection(conn)
    