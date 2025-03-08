from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from db_functions import *
import os


class UpdateDeliveryDialog(QDialog):
    def __init__(self, delivery_id, delivery_data):
        super().__init__()

        ruta_ui = os.path.join(os.path.dirname(__file__), "../ui", "dialogs", "UpdateRestaurantDialog.ui")
        uic.loadUi(ruta_ui, self)


        self.delivery_id = delivery_id
        self.delivery_data = delivery_data


        self.btn_updateOrderDetails.clicked.connect(self.update_delivery)
        self.btn_cancel.clicked.connect(lambda: self.reject())

        self.set_previus_data()


        

    def set_previus_data(self):
        self.lineEdit_NIF.setText(self.delivery_data[1])  
        self.lineEdit_name.setText(self.delivery_data[2])  
        self.lineEdit_orderID.setText(str(self.delivery_data[3])) 
        self.lineEdit_vehicle.setText(self.delivery_data[4]) 
       



    def update_delivery(self):
        new_NIF = self.lineEdit_NIF.text().strip()
        new_name = self.lineEdit_name.text().strip()
        new_orderID = self.lineEdit_orderID.text().strip()
        new_vehicle = self.lineEdit_vehicle.text().strip()
        

        try:
            conn, cursor = get_db_connection()

            cursor.execute("UPDATE repartidores SET nif = ?, nombre = ?, id_pedido_asignado = ?, vehiculo = ? WHERE id = ?", (new_NIF, new_name, new_orderID, new_vehicle, self.delivery_id))
            conn.commit()

            QMessageBox.information(self, "Éxito", "Repartidor actualizado correctamente")
            self.accept()


        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error: {str(e)}")
        finally:
            close_db_connection(conn)