from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from db_functions import *
import os
import json
import re

class UpdateOrderDetailsDialog(QDialog):
    def __init__(self, details_id, details_data):
        super().__init__()


        ruta_ui = os.path.join(os.path.dirname(__file__), "../ui", "dialogs", "UpdateOrderDetailsDialog.ui")
        uic.loadUi(ruta_ui, self)


        self.details_id = details_id
        self.details_data = details_data


        self.btn_updateOrderDetails.clicked.connect(self.update_details)
        self.btn_cancel.clicked.connect(lambda: self.reject())

        self.set_previus_data()


        

    def set_previus_data(self):
        self.lineEdit_orderID.setText(str(self.details_data[1]))  
        self.lineEdit_plateID.setText(str(self.details_data[2]))  
        self.lineEdit_amount.setText(str(self.details_data[3]))
        
        


    def update_details(self):
        new_orderID = self.lineEdit_orderID.text().strip()
        new_plateID = self.lineEdit_plateID.text().strip()
        new_amount = self.lineEdit_amount.text().strip()
        

        try:
            conn, cursor = get_db_connection()

            cursor.execute("UPDATE detalles_pedido SET id_pedido = ?, id_plato = ?, cantidad = ? WHERE id = ?", (new_orderID, new_plateID, new_amount, self.details_id))
            conn.commit()

            QMessageBox.information(self, "Éxito", "Detalles actualizados correctamente")
            self.accept()


        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error: {str(e)}")
        finally:
            close_db_connection(conn)