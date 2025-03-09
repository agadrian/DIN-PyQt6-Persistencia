from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from db_functions import *
from utils import *
from dialogs.CreateOrderDetailsDialog import OrderDetailsDialog
from dialogs.UpdateOrderDetailsDialog import UpdateOrderDetailsDialog
from PDFGenerator import PDFGenerator

class detallesPedidoPage:
    def __init__(self, home_window):
        self.home = home_window

        # Conectar botones
        self.btn_addOrderDetails = self.home.btn_addOrderDetails
        self.btn_addOrderDetails.clicked.connect(self.open_dialog)
        

        self.btn_exportToPDF_4 = self.home.btn_exportToPDF_4
        self.btn_exportToPDF_4.clicked.connect(self.export_pdf)

        self.tabla_ordersDetails = self.home.tabla_ordersDetails

        
        # Cargar los detalles pedidos
        self.load_details()

        # Conectar la funcion de lineEdit_searchByOrderID con el cambio de input del lineEdit
        self.home.lineEdit_searchByOrderID.textChanged.connect(self.search_by)


        # Espacio de cada columna de la tabla
        self.tabla_ordersDetails.setColumnWidth(0, 40)
        self.tabla_ordersDetails.setColumnWidth(1, 120)
        self.tabla_ordersDetails.setColumnWidth(2, 130)
        self.tabla_ordersDetails.setColumnWidth(3, 130)
        self.tabla_ordersDetails.setColumnWidth(4, 100)
        self.tabla_ordersDetails.setColumnWidth(5, 50)
        


    def export_pdf(self):
        pdf = PDFGenerator()
        pdf.generate_table_from_qtwidget(self.tabla_ordersDetails, title="Informe de datos de la tabla")
        pdf.save("Informe_DetallesPedidos.pdf")


    # Abre el dialogo para crear nuevo detalles
    def open_dialog(self):
        dialog = OrderDetailsDialog(self.home)
        dialog.exec()
        self.load_details()    
    

    def load_details(self):
        try:
            conn, cursor = get_db_connection()

            self.tabla_ordersDetails.setRowCount(0)

            if not self.tabla_ordersDetails:
                raise Exception("Error: 'tabla_ordersDetails' no se encontró en la UI.")
            
            cursor.execute("SELECT id, id_pedido, id_plato, cantidad FROM detalles_pedido")
            detalles_pedidos = cursor.fetchall()
            print(detalles_pedidos) # TODO: BORRAR


            for row_index, row_data in enumerate(detalles_pedidos):
                self.tabla_ordersDetails.insertRow(row_index)
                for col_index, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.tabla_ordersDetails.setItem(row_index, col_index, item)

                # Crear los dos iconos finales de editar y eliminar (clase ubicada en utils.py)
                edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data, UpdateOrderDetailsDialog, self.load_details, self.delete_orderDetails)

                # Establecer los botones
                self.tabla_ordersDetails.setCellWidget(row_index, 4, edit_delete_widget)
                self.tabla_ordersDetails.setRowHeight(row_index, 50)

        except Exception as e:
            QMessageBox.warning(self.home, "Error", f"Error cargando restaurantes: {str(e)}")
        finally:
            close_db_connection(conn)

    


    def search_by(self):
        # Limpiar la tabla
        self.tabla_ordersDetails.setRowCount(0)

        # Input del lineedit
        input = self.home.lineEdit_searchByOrderID.text().strip()

        # Si n hay nada escrito, recargar la tabla con todo los datos
        if not input:
            self.load_details()
            return
            

        # SQL
        try:
            conn, cursor = get_db_connection()

            cursor.execute("SELECT * FROM detalles_pedido WHERE id_pedido  LIKE ?", (f"%{input}%",))

            detalles_pedidos = cursor.fetchall()
        
            # Mostrar filas
            for row_index, row_data in enumerate(detalles_pedidos):
                self.tabla_ordersDetails.insertRow(row_index)
                for col_index, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.tabla_ordersDetails.setItem(row_index, col_index, item)

                # Crear los dos iconos finales de editar y eliminar (clase ubicada en utils.py)
                #edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data)

                edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data, UpdateOrderDetailsDialog, self.load_details, self.delete_orderDetails)

                # Establecer los botones
                self.tabla_ordersDetails.setCellWidget(row_index, 4, edit_delete_widget)
                self.tabla_ordersDetails.setRowHeight(row_index, 50)

        except Exception as e:
            QMessageBox.warning(self.home, "Error", f"Error: {str(e)}")
        finally:
            close_db_connection(conn)





    
    def delete_orderDetails(self, detalles_id, detalles_name):
        reply = QMessageBox.question(
            self.home,
            "Eliminar detalles pedido",
            f"¿Estás seguro de que quieres eliminar '{detalles_name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                conn, cursor = get_db_connection()
                cursor.execute("DELETE FROM detalles_pedido WHERE id = ?", (detalles_id,))
                conn.commit()

                QMessageBox.information(self.home, "Eliminado", f"'{detalles_name}' ha sido eliminado correctamente.")

                self.load_details()  # Recargar la tabla

            except Exception as e:
                QMessageBox.warning(self.home, "Error", f"Error al eliminar: {str(e)}")

            finally:
                close_db_connection(conn)