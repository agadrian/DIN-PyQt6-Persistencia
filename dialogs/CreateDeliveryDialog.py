from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from db_functions import *
import os
from utils import *


class DeliveryDialog(QDialog):
    def __init__(self, parent=None):
        super(DeliveryDialog, self).__init__(parent)

        ruta_ui = os.path.join(os.path.dirname(__file__), "../ui", "dialogs", "CreateDeliveryDialog.ui")
        uic.loadUi(ruta_ui, self)

        self.btn_addDelivery.clicked.connect(self.insert_new_delivery)
        self.btn_cancel.clicked.connect(lambda: self.reject())


    

    # Insertar repartidor
    def insert_new_delivery(self):
        try:
            nif = self.lineEdit_NIF.text()
            name = self.lineEdit_name.text()
            orderID = self.lineEdit_orderID.text()
            vehicle = self.lineEdit_vehicle.text()
    

            # Obtener cursor
            conn, cursor = get_db_connection()
            if conn is None or cursor is None:
                raise Exception("No se pudo conectar a la base de datos.")
            

            # Guardarlo en SQLite -> reapartidores
            cursor.execute("INSERT INTO repartidores (nif, nombre, id_pedido_asignado, vehiculo) VALUES (?, ?, ?, ?)", (nif, name, orderID, vehicle))

            conn.commit()
            close_db_connection(conn)

        
            QMessageBox.information(self, "Éxito", f"Repartidor creado correctamente")
            self.reject()


        except Exception as e:
            print(e)
            error_msg = str(e)
            QMessageBox.warning(self, "Error", error_msg)
        finally:
            close_db_connection(conn)
    