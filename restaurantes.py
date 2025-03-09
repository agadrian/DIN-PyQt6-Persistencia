from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from db_functions import *
from utils import *
from dialogs.CreateRestaurantDialog import RestaurantDialog
from dialogs.UpdateRestaurantDialog import UpdateRestaurantDialog
from PDFGenerator import PDFGenerator

class restaurantesPage(QWidget):
    def __init__(self, home_window):
        super().__init__()

        self.home = home_window

        # Conectar botones
        self.btn_addRestaurant = self.home.btn_addRestaurant
        self.btn_addRestaurant.clicked.connect(self.open_dialog)

        self.btn_exportToPDF_5 = self.home.btn_exportToPDF_5
        self.btn_exportToPDF_5.clicked.connect(self.export_pdf)
        

        self.tabla_restaurants = self.home.tabla_restaurants

        
        # Cargar los restaurantes
        self.load_restaurants()

        # Conectar la funcion de lineEdit_searchByNameCategoryTlfn con el cambio de input del lineEdit
        self.home.lineEdit_searchByNameCategoryTlfn.textChanged.connect(self.search_by)


        # Espacio de cada columna de la tabla
        self.tabla_restaurants.setColumnWidth(0, 40)
        self.tabla_restaurants.setColumnWidth(1, 100)
        self.tabla_restaurants.setColumnWidth(2, 130)
        self.tabla_restaurants.setColumnWidth(3, 130)
        self.tabla_restaurants.setColumnWidth(4, 80)
        self.tabla_restaurants.setColumnWidth(5, 80)
        self.tabla_restaurants.setColumnWidth(6, 80)
        self.tabla_restaurants.setColumnWidth(7, 35)


    def export_pdf(self):
        pdf = PDFGenerator()
        pdf.generate_table_from_qtwidget(self.tabla_restaurants, title="Informe de datos de la tabla")
        pdf.save("Informe_Restaurantes.pdf")


    # Abre el dialogo para crear nuevo restaurante
    def open_dialog(self):
        dialog = RestaurantDialog(self.home)
        dialog.exec()
        self.load_restaurants()    
    

    def load_restaurants(self):
        try:
            conn, cursor = get_db_connection()

            self.tabla_restaurants.setRowCount(0)

            if not self.tabla_restaurants:
                raise Exception("Error: 'tabla_restaurants' no se encontró en la UI.")
            
            cursor.execute("SELECT id, nombre, direccion, categoria, telefono, horario, calificacion FROM restaurantes")
            restaurants = cursor.fetchall()
            print(restaurants) # TODO: BORRAR


            for row_index, row_data in enumerate(restaurants):
                self.tabla_restaurants.insertRow(row_index)
                for col_index, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.tabla_restaurants.setItem(row_index, col_index, item)

                # Crear los dos iconos finales de editar y eliminar (clase ubicada en utils.py)
                edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data, UpdateRestaurantDialog, self.load_restaurants, self.delete_restaurant)

                # Establecer los botones
                self.tabla_restaurants.setCellWidget(row_index, 7, edit_delete_widget)
                self.tabla_restaurants.setRowHeight(row_index, 50)

        except Exception as e:
            QMessageBox.warning(self.home, "Error", f"Error cargando restaurantes: {str(e)}")
        finally:
            close_db_connection(conn)

    


    def search_by(self):
        # Limpiar la tabla
        self.tabla_restaurants.setRowCount(0)

        # Input del lineedit
        input = self.home.lineEdit_searchByNameCategoryTlfn.text().strip()

        # Si n hay nada escrito, recargar la tabla con todo los datos
        if not input:
            self.load_restaurants()
            return
            

        # SQL
        try:
            conn, cursor = get_db_connection()

            cursor.execute("SELECT * FROM restaurantes WHERE nombre LIKE ? OR telefono LIKE ? OR categoria LIKE ?", (f"%{input}%", f"%{input}%", f"%{input}%"))

            restaurants = cursor.fetchall()
        
            # Mostrar filas
            for row_index, row_data in enumerate(restaurants):
                self.tabla_restaurants.insertRow(row_index)
                for col_index, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.tabla_restaurants.setItem(row_index, col_index, item)

                # Crear los dos iconos finales de editar y eliminar (clase ubicada en utils.py)
                #edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data)

                edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data, UpdateRestaurantDialog, self.load_restaurants, self.delete_restaurant)

                # Establecer los botones
                self.tabla_restaurants.setCellWidget(row_index, 7, edit_delete_widget)
                self.tabla_restaurants.setRowHeight(row_index, 50)

        except Exception as e:
            QMessageBox.warning(self.home, "Error", f"Error: {str(e)}")
        finally:
            close_db_connection(conn)





    
    def delete_restaurant(self, restaurant_id, restaurant_name):
        reply = QMessageBox.question(
            self.home,
            "Eliminar restaurante",
            f"¿Estás seguro de que quieres eliminar '{restaurant_name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                conn, cursor = get_db_connection()
                cursor.execute("DELETE FROM restaurantes WHERE id = ?", (restaurant_id,))
                conn.commit()

                QMessageBox.information(self.home, "Eliminado", f"'{restaurant_name}' ha sido eliminado correctamente.")

                self.load_restaurants()  # Recargar la tabla

            except Exception as e:
                QMessageBox.warning(self.home, "Error", f"Error al eliminar: {str(e)}")

            finally:
                close_db_connection(conn)