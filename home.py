import os
from PyQt6.QtWidgets import * 
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from dialogs.CreateUserDialog import UserDialog
from usuarios import usuariosPage
from restaurantes import restaurantesPage
from platos import platosPage
from pedidos import pedidosPage
from detalles_pedido import detallesPedidoPage
from repartidores import repartidoresPage
from ui.pages.Home_ui import Ui_MainWindow




class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()
        
        # Ruta del .ui (home.ui (julio))
        ruta_ui = os.path.join(os.path.dirname(__file__), "ui", "pages", "Home.ui")
        uic.loadUi(ruta_ui, self)


        ### Crear instancias de cada sub page del stack para que puedan acceder a los elementos de la UI   
       
        self.users_page = usuariosPage(self)
        self.restaurantes_page = restaurantesPage(self)
        self.platos_page = platosPage(self)
        self.pedidos_page = pedidosPage(self)
        self.detalles_pedido_page = detallesPedidoPage(self)
        self.repartidores_page = repartidoresPage(self)

        self.stackedWidget.addWidget(self.users_page)
        '''self.stackedWidget.addWidget(self.restaurantes_page)
        self.stackedWidget.addWidget(self.platos_page)
        self.stackedWidget.addWidget(self.pedidos_page)
        self.stackedWidget.addWidget(self.detalles_pedido_page)
        self.stackedWidget.addWidget(self.repartidores_page)'''

       



        # Conectar botones de navegación dentro del stackedWidget
        self.btn_users.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        
        self.btn_restaurants.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
    
        # self.btn_users.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.users_page))
        # .....

        # Cargar la pagina inicial del stacked (será Home)
        self.stackedWidget.setCurrentWidget(self.page_home)
        

       

