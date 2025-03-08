from dialogs.CreateUserDialog import *
from db_functions import *
from utils import *

class usuariosPage:
    def __init__(self, home_window):
        self.home = home_window

        # Conectar botones
        self.btn_addUser_2 = self.home.btn_addUser_2
        self.btn_addUser_2.clicked.connect(self.open_dialog)
        

        self.tabla_users = self.home.tabla_users

        
        # Cargar los usuarios
        self.load_users()

        # Conectar la funcion de search_by_email con el cambio de input del lineEdit
        self.home.lineEdit_search_email.textChanged.connect(self.search_by_email)


        # Espacio de cada columna de la tabla
        self.tabla_users.setColumnWidth(0, 40)
        self.tabla_users.setColumnWidth(1, 100)
        self.tabla_users.setColumnWidth(2, 130)
        self.tabla_users.setColumnWidth(3, 130)
        self.tabla_users.setColumnWidth(4, 100)
        self.tabla_users.setColumnWidth(5, 100)
        self.tabla_users.setColumnWidth(6, 100)
    

    #~Abre el dialogo para crear nuevo user
    def open_dialog(self):
        dialog = UserDialog(self.home)
        dialog.exec()
        self.load_users()        

    
    # Cargar todos los usuarios de la db
    def load_users(self):
        try:
            conn, cursor = get_db_connection()

            self.tabla_users.setRowCount(0)

            if not self.tabla_users:
                raise Exception("Error: 'tabla_users' no se encontró en la UI.")
            
            cursor.execute("SELECT id, nombre, email, direccion, telefono, fecha_registro FROM usuarios")
            users = cursor.fetchall()
            print(users) # TODO: BORRAR


            for row_index, row_data in enumerate(users):
                self.tabla_users.insertRow(row_index)
                for col_index, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.tabla_users.setItem(row_index, col_index, item)

                # Crear los dos iconos finales de editar y eliminar (clase ubicada en utils.py)
                edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data, UpdateUserDialog, self.load_users, self.delete_user)

                # Establecer los botones
                self.tabla_users.setCellWidget(row_index, 6, edit_delete_widget)
                self.tabla_users.setRowHeight(row_index, 50)

        except Exception as e:
            QMessageBox.warning(self.home, "Error", f"Error cargando usuarios: {str(e)}")
        finally:
            close_db_connection(conn)


    def search_by_email(self):
        # Limpiar la tabla
        self.tabla_users.setRowCount(0)

        # Input del lineedit
        input = self.home.lineEdit_search_email.text().strip()

        # Si n hay nada escrito, recargar la tabla con todo los datos
        if not input:
            self.load_users()
            return
            

        # SQL
        try:
            conn, cursor = get_db_connection()

            cursor.execute("SELECT * FROM usuarios WHERE email LIKE ? OR nombre LIKE ?", (f"%{input}%", f"%{input}%"))
            users = cursor.fetchall()
        
            # Mostrar filas
            for row_index, row_data in enumerate(users):
                self.tabla_users.insertRow(row_index)
                for col_index, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.tabla_users.setItem(row_index, col_index, item)

                # Crear los dos iconos finales de editar y eliminar (clase ubicada en utils.py)
                edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data, UpdateUserDialog, self.load_users, self.delete_user)

                # Establecer los botones
                self.tabla_users.setCellWidget(row_index, 6, edit_delete_widget)
                self.tabla_users.setRowHeight(row_index, 50)

        except Exception as e:
            QMessageBox.warning(self.home, "Error", f"Error: {str(e)}")
        finally:
            close_db_connection(conn)



        
    def delete_user(self, user_id, user_name):
        reply = QMessageBox.question(
            self.home,
            "Eliminar usuario",
            f"¿Estás seguro de que quieres eliminar '{user_name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                conn, cursor = get_db_connection()
                cursor.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
                conn.commit()

                QMessageBox.information(self.home, "Eliminado", f"'{user_name}' ha sido eliminado correctamente.")

                self.load_users()  # Recargar la tabla

            except Exception as e:
                QMessageBox.warning(self.home, "Error", f"Error al eliminar: {str(e)}")

            finally:
                close_db_connection(conn)
