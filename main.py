from login import *
from register import RegisterWindow
from home import HomeWindow
import sys


# TODO: Quitar marcos de los dialog
# TODO: Flecha para volver al login desde el register
# TODO: Añadir campo telefono en register


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación CRUD")
        #self.setGeometry(100, 100, 800, 600)
        
        # Crear stack para navegar 
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.stack.setSizePolicy(self.sizePolicy())


        # Instanciar clases
        self.login_page = LoginWindow(self)
        self.register_page = RegisterWindow(self)
        
        
        # Agregar pages al stack
        self.stack.addWidget(self.login_page)
        self.stack.addWidget(self.register_page)
        
        
        # Predeterminada
        self.stack.setCurrentWidget(self.login_page)
        
    

    def switch_to_register(self):
        self.stack.setCurrentWidget(self.register_page)
        
    
    def switch_to_login(self):
        self.stack.setCurrentWidget(self.login_page)
    
        
    def switch_to_main(self):
        self.close()
        self.mainWindow = HomeWindow()
        self.mainWindow.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()