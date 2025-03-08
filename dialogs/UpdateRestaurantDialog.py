from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from db_functions import *
import os
import json
import re

class UpdateRestaurantDialog(QDialog):
    def __init__(self, res_id, res_data):
        super().__init__()


        ruta_ui = os.path.join(os.path.dirname(__file__), "../ui", "dialogs", "UpdateRestaurantDialog.ui")
        uic.loadUi(ruta_ui, self)


        self.res_id = res_id
        self.res_data = res_data


        self.btn_updateRestaurant.clicked.connect(self.update_restaurant)
        self.btn_cancel.clicked.connect(lambda: self.reject())

        self.set_previus_data()


        

    def set_previus_data(self):
        self.lineEdit_name.setText(self.res_data[1])  
        self.lineEdit_address_2.setText(self.res_data[2])  
        self.lineEdit_category.setText(self.res_data[3]) 
        self.lineEdit_phone.setText(self.res_data[4]) 
        self.lineEdit_schedule.setText(self.res_data[5]) 
        self.lineEdit_qualification.setText(str(self.res_data[6]))  
        



    def update_restaurant(self):
        new_name = self.lineEdit_name.text().strip()
        new_address = self.lineEdit_address_2.text().strip()
        new_category = self.lineEdit_category.text().strip()
        new_phone = self.lineEdit_phone.text().strip()
        new_schedule = self.lineEdit_schedule.text().strip()
        new_qualification = self.lineEdit_qualification.text().strip()

        try:
            conn, cursor = get_db_connection()

            cursor.execute("UPDATE restaurantes SET nombre = ?, direccion = ?, categoria = ?, telefono = ?, horario = ?, calificacion = ? WHERE id = ?", (new_name, new_address, new_category, new_phone, new_schedule, new_qualification ,self.res_id))
            conn.commit()

            QMessageBox.information(self, "Éxito", "Restaurante actualizado correctamente")
            self.accept()


        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error: {str(e)}")
        finally:
            close_db_connection(conn)