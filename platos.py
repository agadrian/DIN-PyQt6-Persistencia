from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from db_functions import *
from utils import *
from dialogs.CreatePlateDialog import PlateDialog
from dialogs.UpdatePlateDialog import UpdatePlateDialog
from PDFGenerator import PDFGenerator

class platosPage(QWidget):
    def __init__(self, home_window):
        super().__init__()
        self.home = home_window

        # Conectar botones
        self.btn_addPlate = self.home.btn_addPlate
        self.btn_addPlate.clicked.connect(self.open_dialog)

        self.btn_exportToPDF_2 = self.home.btn_exportToPDF_2
        self.btn_exportToPDF_2.clicked.connect(self.export_pdf)
        

        self.tabla_plates = self.home.tabla_plates

        
        # Cargar los platos
        self.load_plates()

        # Conectar la funcion de lineEdit_searchByNameDescription con el cambio de input del lineEdit
        self.home.lineEdit_searchByNameDescription.textChanged.connect(self.search_by)


        # Espacio de cada columna de la tabla
        self.tabla_plates.setColumnWidth(0, 40)
        self.tabla_plates.setColumnWidth(1, 100)
        self.tabla_plates.setColumnWidth(2, 130)
        self.tabla_plates.setColumnWidth(3, 130)
        self.tabla_plates.setColumnWidth(4, 100)
        self.tabla_plates.setColumnWidth(5, 50)
       

    def export_pdf(self):
        pdf = PDFGenerator()
        pdf.generate_table_from_qtwidget(self.tabla_plates, title="Informe de datos de la tabla")
        pdf.save("Informe_Platos.pdf")

    # Abre el dialogo para crear nuevo plato
    def open_dialog(self):
        dialog = PlateDialog(self.home)
        dialog.exec()
        self.load_plates()    
    

    def load_plates(self):
        try:
            conn, cursor = get_db_connection()

            self.tabla_plates.setRowCount(0)

            if not self.tabla_plates:
                raise Exception("Error: 'tabla_plates' no se encontró en la UI.")
            
            cursor.execute("SELECT id, nombre, precio, descripcion, id_restaurante FROM platos")
            plates = cursor.fetchall()

            print(plates) # TODO: BORRAR


            for row_index, row_data in enumerate(plates):
                self.tabla_plates.insertRow(row_index)
                for col_index, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.tabla_plates.setItem(row_index, col_index, item)

                # Crear los dos iconos finales de editar y eliminar (clase ubicada en utils.py)
                edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data, UpdatePlateDialog, self.load_plates, self.delete_plates)

                # Establecer los botones
                self.tabla_plates.setCellWidget(row_index, 5, edit_delete_widget)
                self.tabla_plates.setRowHeight(row_index, 50)

        except Exception as e:
            QMessageBox.warning(self.home, "Error", f"Error cargando platos: {str(e)}")
        finally:
            close_db_connection(conn)

    


    def search_by(self):
        # Limpiar la tabla
        self.tabla_plates.setRowCount(0)

        # Input del lineedit
        input = self.home.lineEdit_searchByNameDescription.text().strip()

        # Si n hay nada escrito, recargar la tabla con todo los datos
        if not input:
            self.load_plates()
            return
            

        # SQL
        try:
            conn, cursor = get_db_connection()

            cursor.execute("SELECT * FROM plaos WHERE nombre LIKE ? OR descripcion LIKE ? ", (f"%{input}%", f"%{input}%"))

            plates = cursor.fetchall()
        
            # Mostrar filas 
            for row_index, row_data in enumerate(plates):
                self.tabla_plates.insertRow(row_index)
                for col_index, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.tabla_plates.setItem(row_index, col_index, item)

                # Crear los dos iconos finales de editar y eliminar (clase ubicada en utils.py)
                #edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data)

                edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data, UpdatePlateDialog, self.load_plates, self.delete_plates)

                # Establecer los botones
                self.tabla_plates.setCellWidget(row_index, 5, edit_delete_widget)
                self.tabla_plates.setRowHeight(row_index, 50)

        except Exception as e:
            QMessageBox.warning(self.home, "Error", f"Error: {str(e)}")
        finally:
            close_db_connection(conn)


    
    def delete_plates(self, plate_id, plate_name):
        reply = QMessageBox.question(
            self.home,
            "Eliminar plato",
            f"¿Estás seguro de que quieres eliminar '{plate_name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                conn, cursor = get_db_connection()
                cursor.execute("DELETE FROM platos WHERE id = ?", (plate_id,))
                conn.commit()

                QMessageBox.information(self.home, "Eliminado", f"'{plate_name}' ha sido eliminado correctamente.")

                self.load_plates()  # Recargar la tabla

            except Exception as e:
                QMessageBox.warning(self.home, "Error", f"Error al eliminar: {str(e)}")

            finally:
                close_db_connection(conn)