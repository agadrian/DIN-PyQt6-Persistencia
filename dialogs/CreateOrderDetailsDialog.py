from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from db_functions import *
import os
from utils import *


class OrderDetailsDialog(QDialog):
    def __init__(self, parent=None):
        super(OrderDetailsDialog, self).__init__(parent)

        ruta_ui = os.path.join(os.path.dirname(__file__), "../ui", "dialogs", "CreateOrderDetailsDialog.ui")
        uic.loadUi(ruta_ui, self)

        self.btn_addOrderDetails.clicked.connect(self.insert_new_details)
        self.btn_cancel.clicked.connect(lambda: self.reject())


    

    # Insertar detalles pedido
    def insert_new_details(self):
        try:
            orderID = self.lineEdit_orderID.text()
            plateID = self.lineEdit_plateID.text()
            amount = self.lineEdit_amount.text()
    

            # Obtener cursor
            conn, cursor = get_db_connection()
            if conn is None or cursor is None:
                raise Exception("No se pudo conectar a la base de datos.")
            

            # Guardarlo en SQLite -> detalles_pedido
            cursor.execute("INSERT INTO detalles_pedido (id_pedido, id_plato, cantidad) VALUES (?, ?, ?)", (orderID, plateID, amount))

            conn.commit()
            close_db_connection(conn)

        
            QMessageBox.information(self, "Éxito", f"Detalles creados correctamente")
            self.reject()


        except Exception as e:
            print(e)
            error_msg = str(e)
            QMessageBox.warning(self, "Error", error_msg)
        finally:
            close_db_connection(conn)
    