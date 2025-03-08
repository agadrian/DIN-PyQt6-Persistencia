from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from db_functions import *
import os
import json
import re

class UpdatePlateDialog(QDialog):
    def __init__(self, plate_id, plate_data):
        super().__init__()


        ruta_ui = os.path.join(os.path.dirname(__file__), "../ui", "dialogs", "UpdatePlateDialog.ui")
        uic.loadUi(ruta_ui, self)


        self.plate_id = plate_id
        self.plate_data = plate_data


        self.btn_updatePlate.clicked.connect(self.update_plate)
        self.btn_cancel.clicked.connect(lambda: self.reject())

        self.set_previus_data()


        

    def set_previus_data(self):
        self.lineEdit_name.setText(self.plate_data[1])  
        self.lineEdit_price.setText(self.plate_data[2])  
        self.lineEdit_description.setText(self.plate_data[3]) 
        self.lineEdit_restaurantID.setText(str(self.plate_data[4])) 
        
        



    def update_plate(self):
        new_name = self.lineEdit_name.text().strip()
        new_price = self.lineEdit_price.text().strip()
        new_description = self.lineEdit_description.text().strip()
        new_restaurant_id = self.lineEdit_restaurantID.text().strip()
        

        try:
            conn, cursor = get_db_connection()

            cursor.execute("UPDATE platos SET nombre = ?, precio = ?, descripcion = ?, id_restaurante = ? WHERE id = ?", (new_name, new_price, new_description, new_restaurant_id, self.plate_id))
            conn.commit()

            QMessageBox.information(self, "Éxito", "Plato actualizado correctamente")
            self.accept()


        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error: {str(e)}")
        finally:
            close_db_connection(conn)