from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from db_functions import *
import os


class UpdateOrderDialog(QDialog):
    def __init__(self, order_id, order_data):
        super().__init__()

        ruta_ui = os.path.join(os.path.dirname(__file__), "../ui", "dialogs", "UpdateOrderDialog.ui")
        uic.loadUi(ruta_ui, self)


        self.order_id = order_id
        self.order_data = order_data


        self.btn_updateOrder.clicked.connect(self.update_order)
        self.btn_cancel.clicked.connect(lambda: self.reject())

        self.set_previus_data()


        

    def set_previus_data(self):
        self.lineEdit_userID.setText(str(self.order_data[1]))  
        self.lineEdit_restaurantID.setText(str(self.order_data[2]))
        self.lineEdit_state.setText(self.order_data[3]) 
        
        


    def update_order(self):
        new_userID = self.lineEdit_userID.text().strip()
        new_restaurantID = self.lineEdit_restaurantID.text().strip()
        new_state = self.lineEdit_state.text().strip()
        

        try:
            conn, cursor = get_db_connection()

            cursor.execute("UPDATE pedidos SET id_cliente = ?, id_restaurante = ?, estado = ? WHERE id = ?", (new_userID, new_restaurantID, new_state, self.order_id))
            conn.commit()

            QMessageBox.information(self, "Éxito", "Pedido actualizado correctamente")
            self.accept()


        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error: {str(e)}")
        finally:
            close_db_connection(conn)