import os
from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from dialogs.userDialog import UserDialog




class HomeWindow(QWidget):
    def __init__(self):
        super(HomeWindow, self).__init__()
        
        # Ruta del .ui (home.ui (julio))
        ruta_ui = os.path.join(os.path.dirname(__file__), "ui", "pages", "stackedTesst.ui")
        uic.loadUi(ruta_ui, self)

        

        # Conectar botones menú
        #self.btn_home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_home)) # Home

        # Cargar la pagina inicial del stacked (será Home)
        #self.stackedWidget.setCurrentWidget(self.page_home)

        self.btn_addUser_2.clicked.connect(self.open_dialog)


    def open_dialog(self):
        dialog = UserDialog(self)
        dialog.exec()        

        
