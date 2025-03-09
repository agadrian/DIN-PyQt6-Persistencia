from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from db_functions import *
from utils import *
from dialogs.CreateDeliveryDialog import DeliveryDialog
from dialogs.UpdateDeliveryDialog import UpdateDeliveryDialog
from PDFGenerator import PDFGenerator

class repartidoresPage:
    def __init__(self, home_window):
        self.home = home_window

        # Conectar botones
        self.btn_addDelivery = self.home.btn_addDelivery
        self.btn_addDelivery.clicked.connect(self.open_dialog)
        
        self.btn_exportPDF = self.home.btn_exportPDF
        self.btn_exportPDF.clicked.connect(self.export_pdf)

        self.tabla_delivery = self.home.tabla_delivery

        
        # Cargar los repartidores
        self.load_delivery()

        # Conectar la funcion de lineEdit_searchBy con el cambio de input del lineEdit
        self.home.lineEdit_searchBy.textChanged.connect(self.search_by)


        # Espacio de cada columna de la tabla
        self.tabla_delivery.setColumnWidth(0, 40)
        self.tabla_delivery.setColumnWidth(1, 120)
        self.tabla_delivery.setColumnWidth(2, 130)
        self.tabla_delivery.setColumnWidth(3, 130)
        self.tabla_delivery.setColumnWidth(4, 120)
        self.tabla_delivery.setColumnWidth(5, 50)
       

    def export_pdf(self):
        pdf = PDFGenerator()
        pdf.generate_table_from_qtwidget(self.tabla_delivery, title="Informe de datos de la tabla")
        pdf.save("Informe_Repartidores.pdf")
    

    # Abre el dialogo para crear nuevo repartidor
    def open_dialog(self):
        dialog = DeliveryDialog(self.home)
        dialog.exec()
        self.load_delivery()    
    

    def load_delivery(self):
        try:
            conn, cursor = get_db_connection()

            self.tabla_delivery.setRowCount(0)

            if not self.tabla_delivery:
                raise Exception("Error: 'tabla_delivery' no se encontró en la UI.")
            
            cursor.execute("SELECT id, nif, nombre, id_pedido_asignado, vehiculo FROM repartidores")
            deliveries = cursor.fetchall()
            print(deliveries) # TODO: BORRAR


            for row_index, row_data in enumerate(deliveries):
                self.tabla_delivery.insertRow(row_index)
                for col_index, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.tabla_delivery.setItem(row_index, col_index, item)

                # Crear los dos iconos finales de editar y eliminar (clase ubicada en utils.py)
                edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data, UpdateDeliveryDialog, self.load_delivery, self.delete_delivery)

                # Establecer los botones
                self.tabla_delivery.setCellWidget(row_index, 5, edit_delete_widget)
                self.tabla_delivery.setRowHeight(row_index, 50)

        except Exception as e:
            QMessageBox.warning(self.home, "Error", f"Error cargando repartidores: {str(e)}")
        finally:
            close_db_connection(conn)

    


    def search_by(self):
        # Limpiar la tabla
        self.tabla_delivery.setRowCount(0)

        # Input del lineedit
        input = self.home.lineEdit_searchBy.text().strip()

        # Si n hay nada escrito, recargar la tabla con todo los datos
        if not input:
            self.load_delivery()
            return
            

        # SQL
        try:
            conn, cursor = get_db_connection()

            cursor.execute("SELECT * FROM repartidores WHERE nif LIKE ? OR nombre LIKE ? ", (f"%{input}%", f"%{input}%"))

            deliveries = cursor.fetchall()
        
            # Mostrar filas
            for row_index, row_data in enumerate(deliveries):
                self.tabla_delivery.insertRow(row_index)
                for col_index, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.tabla_delivery.setItem(row_index, col_index, item)

                # Crear los dos iconos finales de editar y eliminar (clase ubicada en utils.py)
                #edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data)

                edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data, UpdateDeliveryDialog, self.load_delivery, self.delete_delivery)

                # Establecer los botones
                self.tabla_delivery.setCellWidget(row_index, 5, edit_delete_widget)
                self.tabla_delivery.setRowHeight(row_index, 50)

        except Exception as e:
            QMessageBox.warning(self.home, "Error", f"Error: {str(e)}")
        finally:
            close_db_connection(conn)



    
    def delete_delivery(self, delivery_id, delivery_name):
        reply = QMessageBox.question(
            self.home,
            "Eliminar repartidor",
            f"¿Estás seguro de que quieres eliminar '{delivery_name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                conn, cursor = get_db_connection()
                cursor.execute("DELETE FROM repartidores WHERE id = ?", (delivery_id,))
                conn.commit()

                QMessageBox.information(self.home, "Eliminado", f"'{delivery_name}' ha sido eliminado correctamente.")

                self.load_delivery()  # Recargar la tabla

            except Exception as e:
                QMessageBox.warning(self.home, "Error", f"Error al eliminar: {str(e)}")

            finally:
                close_db_connection(conn)