import os
from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from dialogs.CreateUserDialog import UserDialog
from usuarios import usuariosPage




class HomeWindow(QWidget):
    def __init__(self):
        super(HomeWindow, self).__init__()
        
        # Ruta del .ui (home.ui (julio))
        ruta_ui = os.path.join(os.path.dirname(__file__), "ui", "pages", "stackedTesst.ui")
        uic.loadUi(ruta_ui, self)


        ### Crear instancias de cada sub page del stack para que puedan acceder a los elementos de la UI   

        # self.home_page = ......
        self.users_page = usuariosPage(self)
        #self.restaurantes_page = ......}
        # .....
        

        # Conectar botones de navegación dentro del stackedWidget
        # self.btn_home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.home_page))
        # self.btn_users.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.users_page))
        # .....
        

        # Cargar la pagina inicial del stacked (será Home)
        # self.stackedWidget.setCurrentWidget(self.page_home)

