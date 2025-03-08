from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from db_functions import *
import os
from utils import *


class PlateDialog(QDialog):
    def __init__(self, parent=None):
        super(PlateDialog, self).__init__(parent)

        ruta_ui = os.path.join(os.path.dirname(__file__), "../ui", "dialogs", "CreatePlateDialog.ui")
        uic.loadUi(ruta_ui, self)

        self.btn_addPlate.clicked.connect(self.insert_new_plate)
        self.btn_cancel.clicked.connect(lambda: self.reject())


    

    # Insertar plato
    def insert_new_plate(self):
        try:
            name = self.lineEdit_name.text()
            price = self.lineEdit_price.text()
            description = self.lineEdit_description.text()
            restaurant_id = self.lineEdit_restaurantID.text()
           

            # Obtener cursor
            conn, cursor = get_db_connection()
            if conn is None or cursor is None:
                raise Exception("No se pudo conectar a la base de datos.")
            

            # Guardarlo en SQLite -> platos
            cursor.execute("INSERT INTO platos (nombre, precio, descripcion, id_restaurante) VALUES (?, ?, ?, ?)", (name, price, description, restaurant_id))

            conn.commit()
            close_db_connection(conn)

        
            QMessageBox.information(self, "Éxito", f"Plato creado correctamente")
            self.reject()


        except Exception as e:
            print(e)
            error_msg = str(e)
            QMessageBox.warning(self, "Error", error_msg)
        finally:
            close_db_connection(conn)
    