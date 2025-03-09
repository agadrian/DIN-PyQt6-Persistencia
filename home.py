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
       

        # Añadir las páginas al QStackedWidget
        self.stackedWidget.addWidget(self.users_page)
        

        

        # Conectar botones de navegación dentro del stackedWidget
        self.btn_users.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.btn_restaurants.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.btn_querys.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.btn_home.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.btn_dishes.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.btn_orders.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.btn_orderDetails.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        self.btn_delivery.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))

    
        # self.btn_users.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.users_page))
        # .....

        # Cargar la pagina inicial del stacked (será Home)
        self.stackedWidget.setCurrentWidget(self.page_home)
        

       

