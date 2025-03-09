from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from db_functions import *
from utils import *
from dialogs.UpdaterOrderDialog import UpdateOrderDialog
from dialogs.CreateOrderDialog import OrderDialog
from PDFGenerator import PDFGenerator

class pedidosPage(QWidget):
    def __init__(self, home_window):
        super().__init__()
        self.home = home_window

        # Conectar botones
        self.btn_addOrder = self.home.btn_addOrder
        self.btn_addOrder.clicked.connect(self.open_dialog)

        self.btn_exportToPDF_3 = self.home.btn_exportToPDF_3
        self.btn_exportToPDF_3.clicked.connect(self.export_pdf)
        
        self.tabla_orders = self.home.tabla_orders

    

        
        # Cargar los pedidos
        self.load_orders()

        # Conectar la funcion de lineEdit_searchByUserID con el cambio de input del lineEdit
        self.home.lineEdit_searchByUserID.textChanged.connect(self.search_by)


        # Espacio de cada columna de la tabla
        self.tabla_orders.setColumnWidth(0, 40)
        self.tabla_orders.setColumnWidth(1, 120)
        self.tabla_orders.setColumnWidth(2, 130)
        self.tabla_orders.setColumnWidth(3, 130)
        self.tabla_orders.setColumnWidth(4, 35)
   
    
    def export_pdf(self):
        pdf = PDFGenerator()
        pdf.generate_table_from_qtwidget(self.tabla_orders, title="Informe de datos de la tabla")
        pdf.save("Informe_Pedidos.pdf")


    # Abre el dialogo para crear nuevo pedido
    def open_dialog(self):
        dialog = OrderDialog(self.home)
        dialog.exec()
        self.load_orders()    
    

    def load_orders(self):
        try:
            conn, cursor = get_db_connection()

            self.tabla_orders.setRowCount(0)

            if not self.tabla_orders:
                raise Exception("Error: 'tabla_orders' no se encontró en la UI.")
            
            cursor.execute("SELECT id, id_cliente, id_restaurante, estado FROM pedidos")
            pedidos = cursor.fetchall()
            print(pedidos) # TODO: BORRAR


            for row_index, row_data in enumerate(pedidos):
                self.tabla_orders.insertRow(row_index)
                for col_index, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.tabla_orders.setItem(row_index, col_index, item)

                # Crear los dos iconos finales de editar y eliminar (clase ubicada en utils.py)
                edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data, UpdateOrderDialog, self.load_orders, self.delete_order)

                # Establecer los botones
                self.tabla_orders.setCellWidget(row_index, 4, edit_delete_widget)
                self.tabla_orders.setRowHeight(row_index, 50)

        except Exception as e:
            QMessageBox.warning(self.home, "Error", f"Error cargando pedidos: {str(e)}")
        finally:
            close_db_connection(conn)

    


    def search_by(self):
        # Limpiar la tabla
        self.tabla_orders.setRowCount(0)

        # Input del lineedit
        input = self.home.lineEdit_searchByUserID.text().strip()

        # Si n hay nada escrito, recargar la tabla con todo los datos
        if not input:
            self.load_orders()
            return
            

        # SQL
        try:
            conn, cursor = get_db_connection()

            cursor.execute("SELECT * FROM pedidos WHERE id_cliente LIKE ? ", (f"%{input}%",))

            pedidos = cursor.fetchall()
        
            # Mostrar filas
            for row_index, row_data in enumerate(pedidos):
                self.tabla_orders.insertRow(row_index)
                for col_index, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.tabla_orders.setItem(row_index, col_index, item)

                # Crear los dos iconos finales de editar y eliminar (clase ubicada en utils.py)
                #edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data)

                edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data, UpdateOrderDialog, self.load_orders, self.delete_order)

                # Establecer los botones
                self.tabla_orders.setCellWidget(row_index, 4, edit_delete_widget)
                self.tabla_orders.setRowHeight(row_index, 50)

        except Exception as e:
            QMessageBox.warning(self.home, "Error", f"Error: {str(e)}")
        finally:
            close_db_connection(conn)





    
    def delete_order(self, order_id, order_name):
        reply = QMessageBox.question(
            self.home,
            "Eliminar pedido",
            f"¿Estás seguro de que quieres eliminar '{order_name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                conn, cursor = get_db_connection()
                cursor.execute("DELETE FROM pedidos WHERE id = ?", (order_id,))
                conn.commit()

                QMessageBox.information(self.home, "Eliminado", f"'{order_name}' ha sido eliminado correctamente.")

                self.load_orders()  # Recargar la tabla

            except Exception as e:
                QMessageBox.warning(self.home, "Error", f"Error al eliminar: {str(e)}")

            finally:
                close_db_connection(conn)