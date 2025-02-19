import os
from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Ruta del .ui
        ruta_ui = os.path.join(os.path.dirname(__file__), "ui", "pages", "stackedTesst.ui")
        uic.loadUi(ruta_ui, self)

        #self.setFixedSize(self.size())

        # Conectar boton
        #self.btn_singup.clicked.connect(self.register)