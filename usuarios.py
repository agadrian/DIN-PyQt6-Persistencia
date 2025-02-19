from dialogs.userDialog import *
from db_functions import *

class usuariosPage:
    def __init__(self, home_window):
        self.home = home_window
      # Esto imprimirá todos los atributos del objeto home


        self.btn_addUser_2 = self.home.btn_addUser_2
        self.btn_addUser_2.clicked.connect(self.open_dialog)

        self.table_usuarios = self.home.findChild(QTableWidget, "table_usuarios")
        self.load_users()
        
    


    def open_dialog(self):
        dialog = UserDialog(self.home)
        dialog.exec()        

    
    def load_users(self):
        conn, cursor = get_db_connection()

        try:

            if not self.table_usuarios:
                raise Exception("Error: 'table_usuarios' no se encontró en la UI.")
            

            cursor.execute("SELECT id, nombre, email, telefono, fecha_registro FROM usuarios")
            users = cursor.fetchall()

            self.table_usuarios.setRowCount(0)

            #self.table_usuarios.setRowCount(len(users))
            for row_idx, user in enumerate(users):
                for col_index, data in enumerate(user):
                    data = QTableWidgetItem(str(data))
                    self.table_usuarios.setItem(row_idx, col_index, data)
        except Exception as e:
            QMessageBox.warning(self.home, "Error", f"Error cargando usuarios: {str(e)}")
        
        finally:
            close_db_connection(conn)