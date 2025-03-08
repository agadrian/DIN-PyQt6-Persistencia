from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from db_functions import *
import os
from utils import *


class OrderDialog(QDialog):
    def __init__(self, parent=None):
        super(OrderDialog, self).__init__(parent)

        ruta_ui = os.path.join(os.path.dirname(__file__), "../ui", "dialogs", "CreateOrderDialog.ui")
        uic.loadUi(ruta_ui, self)

        self.btn_addOrder.clicked.connect(self.insert_new_order)
        self.btn_cancel.clicked.connect(lambda: self.reject())


    

    # Insertar order
    def insert_new_order(self):
        try:
            userID = self.lineEdit_userID.text()
            restaurantID = self.lineEdit_restaurantID.text()
            state = self.lineEdit_state.text()
            

            # Obtener cursor
            conn, cursor = get_db_connection()
            if conn is None or cursor is None:
                raise Exception("No se pudo conectar a la base de datos.")
            

            # Guardarlo en SQLite -> pedidos
            cursor.execute("INSERT INTO pedidos (id_cliente, id_restaurante, estado) VALUES (?, ?, ?)", (userID, restaurantID, state))

            conn.commit()
            close_db_connection(conn)

        
            QMessageBox.information(self, "Éxito", f"Pedido creado correctamente")
            self.reject()


        except Exception as e:
            print(e)
            error_msg = str(e)
            QMessageBox.warning(self, "Error", error_msg)
        finally:
            close_db_connection(conn)
    