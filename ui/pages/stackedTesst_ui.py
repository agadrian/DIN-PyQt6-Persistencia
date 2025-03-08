# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stackedTesst.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_main_screen_widget(object):
    def setupUi(self, main_screen_widget):
        if not main_screen_widget.objectName():
            main_screen_widget.setObjectName(u"main_screen_widget")
        main_screen_widget.resize(845, 740)
        main_screen_widget.setMinimumSize(QSize(845, 740))
        main_screen_widget.setMaximumSize(QSize(845, 740))
        main_screen_widget.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 20, 841, 701))
        self.page_consultas = QWidget()
        self.page_consultas.setObjectName(u"page_consultas")
        self.label = QLabel(self.page_consultas)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 220, 91, 61))
        self.stackedWidget.addWidget(self.page_consultas)
        self.page_usuarios = QWidget()
        self.page_usuarios.setObjectName(u"page_usuarios")
        self.tabla_users = QTableWidget(self.page_usuarios)
        if (self.tabla_users.columnCount() < 7):
            self.tabla_users.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_users.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_users.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_users.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_users.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_users.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_users.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_users.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_users.setObjectName(u"tabla_users")
        self.tabla_users.setGeometry(QRect(20, 160, 781, 531))
        self.tabla_users.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.tabla_users.setAlternatingRowColors(True)
        self.tabla_users.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.tabla_users.setColumnCount(7)
        self.tabla_users.horizontalHeader().setVisible(True)
        self.tabla_users.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_users.horizontalHeader().setDefaultSectionSize(80)
        self.tabla_users.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tabla_users.horizontalHeader().setStretchLastSection(True)
        self.tabla_users.verticalHeader().setVisible(False)
        self.tabla_users.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_users.verticalHeader().setStretchLastSection(False)
        self.lineEdit_search_email = QLineEdit(self.page_usuarios)
        self.lineEdit_search_email.setObjectName(u"lineEdit_search_email")
        self.lineEdit_search_email.setGeometry(QRect(530, 100, 271, 35))
        self.lineEdit_search_email.setMinimumSize(QSize(0, 35))
        self.lineEdit_search_email.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_search_email.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.users_management = QLabel(self.page_usuarios)
        self.users_management.setObjectName(u"users_management")
        self.users_management.setGeometry(QRect(20, 50, 221, 41))
        font = QFont()
        font.setPointSize(13)
        self.users_management.setFont(font)
        self.users_tittle = QLabel(self.page_usuarios)
        self.users_tittle.setObjectName(u"users_tittle")
        self.users_tittle.setGeometry(QRect(20, 0, 121, 51))
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.users_tittle.setFont(font1)
        self.layoutWidget = QWidget(self.page_usuarios)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 100, 401, 42))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_addUser_2 = QPushButton(self.layoutWidget)
        self.btn_addUser_2.setObjectName(u"btn_addUser_2")
        self.btn_addUser_2.setMinimumSize(QSize(0, 40))
        self.btn_addUser_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_addUser_2)

        self.btn_exportToExcel = QPushButton(self.layoutWidget)
        self.btn_exportToExcel.setObjectName(u"btn_exportToExcel")
        self.btn_exportToExcel.setMinimumSize(QSize(0, 40))
        self.btn_exportToExcel.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_exportToExcel)

        self.btn_exportToPDF = QPushButton(self.layoutWidget)
        self.btn_exportToPDF.setObjectName(u"btn_exportToPDF")
        self.btn_exportToPDF.setMinimumSize(QSize(0, 40))
        self.btn_exportToPDF.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(218, 29, 29);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_exportToPDF)

        self.stackedWidget.addWidget(self.page_usuarios)
        self.page_restaurantes = QWidget()
        self.page_restaurantes.setObjectName(u"page_restaurantes")
        self.tabla_restaurants = QTableWidget(self.page_restaurantes)
        if (self.tabla_restaurants.columnCount() < 8):
            self.tabla_restaurants.setColumnCount(8)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_restaurants.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_restaurants.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_restaurants.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_restaurants.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_restaurants.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_restaurants.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_restaurants.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabla_restaurants.setHorizontalHeaderItem(7, __qtablewidgetitem14)
        self.tabla_restaurants.setObjectName(u"tabla_restaurants")
        self.tabla_restaurants.setGeometry(QRect(20, 160, 781, 531))
        self.tabla_restaurants.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.tabla_restaurants.setAlternatingRowColors(True)
        self.tabla_restaurants.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.tabla_restaurants.setColumnCount(8)
        self.tabla_restaurants.horizontalHeader().setVisible(True)
        self.tabla_restaurants.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_restaurants.horizontalHeader().setDefaultSectionSize(80)
        self.tabla_restaurants.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tabla_restaurants.horizontalHeader().setStretchLastSection(True)
        self.tabla_restaurants.verticalHeader().setVisible(False)
        self.tabla_restaurants.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_restaurants.verticalHeader().setStretchLastSection(False)
        self.lineEdit_searchByNameCategoryTlfn = QLineEdit(self.page_restaurantes)
        self.lineEdit_searchByNameCategoryTlfn.setObjectName(u"lineEdit_searchByNameCategoryTlfn")
        self.lineEdit_searchByNameCategoryTlfn.setGeometry(QRect(530, 100, 271, 35))
        self.lineEdit_searchByNameCategoryTlfn.setMinimumSize(QSize(0, 35))
        self.lineEdit_searchByNameCategoryTlfn.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_searchByNameCategoryTlfn.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.restaurant_management = QLabel(self.page_restaurantes)
        self.restaurant_management.setObjectName(u"restaurant_management")
        self.restaurant_management.setGeometry(QRect(20, 50, 261, 41))
        self.restaurant_management.setFont(font)
        self.layoutWidget_2 = QWidget(self.page_restaurantes)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 100, 401, 42))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_addRestaurant = QPushButton(self.layoutWidget_2)
        self.btn_addRestaurant.setObjectName(u"btn_addRestaurant")
        self.btn_addRestaurant.setMinimumSize(QSize(0, 40))
        self.btn_addRestaurant.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_addRestaurant)

        self.btn_exportToExcel_5 = QPushButton(self.layoutWidget_2)
        self.btn_exportToExcel_5.setObjectName(u"btn_exportToExcel_5")
        self.btn_exportToExcel_5.setMinimumSize(QSize(0, 40))
        self.btn_exportToExcel_5.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_exportToExcel_5)

        self.btn_exportToPDF_5 = QPushButton(self.layoutWidget_2)
        self.btn_exportToPDF_5.setObjectName(u"btn_exportToPDF_5")
        self.btn_exportToPDF_5.setMinimumSize(QSize(0, 40))
        self.btn_exportToPDF_5.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(218, 29, 29);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_exportToPDF_5)

        self.restaurant_tittle = QLabel(self.page_restaurantes)
        self.restaurant_tittle.setObjectName(u"restaurant_tittle")
        self.restaurant_tittle.setGeometry(QRect(20, 0, 241, 51))
        self.restaurant_tittle.setFont(font1)
        self.stackedWidget.addWidget(self.page_restaurantes)
        self.page_platos = QWidget()
        self.page_platos.setObjectName(u"page_platos")
        self.tabla_plates = QTableWidget(self.page_platos)
        if (self.tabla_plates.columnCount() < 6):
            self.tabla_plates.setColumnCount(6)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabla_plates.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabla_plates.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabla_plates.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabla_plates.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabla_plates.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabla_plates.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        self.tabla_plates.setObjectName(u"tabla_plates")
        self.tabla_plates.setGeometry(QRect(20, 160, 781, 531))
        self.tabla_plates.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.tabla_plates.setAlternatingRowColors(True)
        self.tabla_plates.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.tabla_plates.setColumnCount(6)
        self.tabla_plates.horizontalHeader().setVisible(True)
        self.tabla_plates.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_plates.horizontalHeader().setDefaultSectionSize(106)
        self.tabla_plates.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tabla_plates.horizontalHeader().setStretchLastSection(True)
        self.tabla_plates.verticalHeader().setVisible(False)
        self.tabla_plates.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_plates.verticalHeader().setStretchLastSection(False)
        self.lineEdit_searchByNameDescription = QLineEdit(self.page_platos)
        self.lineEdit_searchByNameDescription.setObjectName(u"lineEdit_searchByNameDescription")
        self.lineEdit_searchByNameDescription.setGeometry(QRect(530, 100, 271, 35))
        self.lineEdit_searchByNameDescription.setMinimumSize(QSize(0, 35))
        self.lineEdit_searchByNameDescription.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_searchByNameDescription.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.plates_tittle = QLabel(self.page_platos)
        self.plates_tittle.setObjectName(u"plates_tittle")
        self.plates_tittle.setGeometry(QRect(20, 0, 241, 51))
        self.plates_tittle.setFont(font1)
        self.layoutWidget_3 = QWidget(self.page_platos)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 100, 401, 42))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_addPlate = QPushButton(self.layoutWidget_3)
        self.btn_addPlate.setObjectName(u"btn_addPlate")
        self.btn_addPlate.setMinimumSize(QSize(0, 40))
        self.btn_addPlate.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_addPlate)

        self.btn_exportToExcel_2 = QPushButton(self.layoutWidget_3)
        self.btn_exportToExcel_2.setObjectName(u"btn_exportToExcel_2")
        self.btn_exportToExcel_2.setMinimumSize(QSize(0, 40))
        self.btn_exportToExcel_2.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_exportToExcel_2)

        self.btn_exportToPDF_2 = QPushButton(self.layoutWidget_3)
        self.btn_exportToPDF_2.setObjectName(u"btn_exportToPDF_2")
        self.btn_exportToPDF_2.setMinimumSize(QSize(0, 40))
        self.btn_exportToPDF_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(218, 29, 29);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_exportToPDF_2)

        self.plates_management = QLabel(self.page_platos)
        self.plates_management.setObjectName(u"plates_management")
        self.plates_management.setGeometry(QRect(20, 50, 261, 41))
        self.plates_management.setFont(font)
        self.stackedWidget.addWidget(self.page_platos)
        self.page_pedidos = QWidget()
        self.page_pedidos.setObjectName(u"page_pedidos")
        self.tabla_orders = QTableWidget(self.page_pedidos)
        if (self.tabla_orders.columnCount() < 5):
            self.tabla_orders.setColumnCount(5)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabla_orders.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tabla_orders.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tabla_orders.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tabla_orders.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tabla_orders.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        self.tabla_orders.setObjectName(u"tabla_orders")
        self.tabla_orders.setGeometry(QRect(20, 160, 781, 531))
        self.tabla_orders.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.tabla_orders.setAlternatingRowColors(True)
        self.tabla_orders.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.tabla_orders.setColumnCount(5)
        self.tabla_orders.horizontalHeader().setVisible(True)
        self.tabla_orders.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_orders.horizontalHeader().setDefaultSectionSize(149)
        self.tabla_orders.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tabla_orders.horizontalHeader().setStretchLastSection(True)
        self.tabla_orders.verticalHeader().setVisible(False)
        self.tabla_orders.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_orders.verticalHeader().setStretchLastSection(False)
        self.lineEdit_searchByUserID = QLineEdit(self.page_pedidos)
        self.lineEdit_searchByUserID.setObjectName(u"lineEdit_searchByUserID")
        self.lineEdit_searchByUserID.setGeometry(QRect(530, 100, 271, 35))
        self.lineEdit_searchByUserID.setMinimumSize(QSize(0, 35))
        self.lineEdit_searchByUserID.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_searchByUserID.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.plates_management_2 = QLabel(self.page_pedidos)
        self.plates_management_2.setObjectName(u"plates_management_2")
        self.plates_management_2.setGeometry(QRect(20, 50, 261, 41))
        self.plates_management_2.setFont(font)
        self.plates_tittle_2 = QLabel(self.page_pedidos)
        self.plates_tittle_2.setObjectName(u"plates_tittle_2")
        self.plates_tittle_2.setGeometry(QRect(20, 0, 241, 51))
        self.plates_tittle_2.setFont(font1)
        self.layoutWidget_4 = QWidget(self.page_pedidos)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(20, 100, 401, 42))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_addOrder = QPushButton(self.layoutWidget_4)
        self.btn_addOrder.setObjectName(u"btn_addOrder")
        self.btn_addOrder.setMinimumSize(QSize(0, 40))
        self.btn_addOrder.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_addOrder)

        self.btn_exportToExcel_3 = QPushButton(self.layoutWidget_4)
        self.btn_exportToExcel_3.setObjectName(u"btn_exportToExcel_3")
        self.btn_exportToExcel_3.setMinimumSize(QSize(0, 40))
        self.btn_exportToExcel_3.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_exportToExcel_3)

        self.btn_exportToPDF_3 = QPushButton(self.layoutWidget_4)
        self.btn_exportToPDF_3.setObjectName(u"btn_exportToPDF_3")
        self.btn_exportToPDF_3.setMinimumSize(QSize(0, 40))
        self.btn_exportToPDF_3.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(218, 29, 29);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_exportToPDF_3)

        self.stackedWidget.addWidget(self.page_pedidos)
        self.page_detallesPedidos = QWidget()
        self.page_detallesPedidos.setObjectName(u"page_detallesPedidos")
        self.plates_management_3 = QLabel(self.page_detallesPedidos)
        self.plates_management_3.setObjectName(u"plates_management_3")
        self.plates_management_3.setGeometry(QRect(20, 50, 261, 41))
        self.plates_management_3.setFont(font)
        self.layoutWidget_5 = QWidget(self.page_detallesPedidos)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(20, 100, 421, 42))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_addOrderDetails = QPushButton(self.layoutWidget_5)
        self.btn_addOrderDetails.setObjectName(u"btn_addOrderDetails")
        self.btn_addOrderDetails.setMinimumSize(QSize(0, 40))
        self.btn_addOrderDetails.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout_9.addWidget(self.btn_addOrderDetails)

        self.btn_exportToExcel_4 = QPushButton(self.layoutWidget_5)
        self.btn_exportToExcel_4.setObjectName(u"btn_exportToExcel_4")
        self.btn_exportToExcel_4.setMinimumSize(QSize(0, 40))
        self.btn_exportToExcel_4.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout_9.addWidget(self.btn_exportToExcel_4)

        self.btn_exportToPDF_4 = QPushButton(self.layoutWidget_5)
        self.btn_exportToPDF_4.setObjectName(u"btn_exportToPDF_4")
        self.btn_exportToPDF_4.setMinimumSize(QSize(0, 40))
        self.btn_exportToPDF_4.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(218, 29, 29);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout_9.addWidget(self.btn_exportToPDF_4)

        self.plates_tittle_3 = QLabel(self.page_detallesPedidos)
        self.plates_tittle_3.setObjectName(u"plates_tittle_3")
        self.plates_tittle_3.setGeometry(QRect(20, 0, 281, 51))
        self.plates_tittle_3.setFont(font1)
        self.lineEdit_searchByOrderID = QLineEdit(self.page_detallesPedidos)
        self.lineEdit_searchByOrderID.setObjectName(u"lineEdit_searchByOrderID")
        self.lineEdit_searchByOrderID.setGeometry(QRect(530, 100, 271, 35))
        self.lineEdit_searchByOrderID.setMinimumSize(QSize(0, 35))
        self.lineEdit_searchByOrderID.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_searchByOrderID.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.tabla_ordersDetails = QTableWidget(self.page_detallesPedidos)
        if (self.tabla_ordersDetails.columnCount() < 5):
            self.tabla_ordersDetails.setColumnCount(5)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tabla_ordersDetails.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tabla_ordersDetails.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tabla_ordersDetails.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tabla_ordersDetails.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tabla_ordersDetails.setHorizontalHeaderItem(4, __qtablewidgetitem30)
        self.tabla_ordersDetails.setObjectName(u"tabla_ordersDetails")
        self.tabla_ordersDetails.setGeometry(QRect(20, 160, 781, 531))
        self.tabla_ordersDetails.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.tabla_ordersDetails.setAlternatingRowColors(True)
        self.tabla_ordersDetails.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.tabla_ordersDetails.setColumnCount(5)
        self.tabla_ordersDetails.horizontalHeader().setVisible(True)
        self.tabla_ordersDetails.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_ordersDetails.horizontalHeader().setDefaultSectionSize(149)
        self.tabla_ordersDetails.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tabla_ordersDetails.horizontalHeader().setStretchLastSection(True)
        self.tabla_ordersDetails.verticalHeader().setVisible(False)
        self.tabla_ordersDetails.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_ordersDetails.verticalHeader().setStretchLastSection(False)
        self.stackedWidget.addWidget(self.page_detallesPedidos)
        self.page_repartidores = QWidget()
        self.page_repartidores.setObjectName(u"page_repartidores")
        self.label_3 = QLabel(self.page_repartidores)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 0, 311, 51))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.page_repartidores)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 50, 281, 41))
        self.label_4.setFont(font)
        self.tabla_delivery = QTableWidget(self.page_repartidores)
        if (self.tabla_delivery.columnCount() < 6):
            self.tabla_delivery.setColumnCount(6)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tabla_delivery.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tabla_delivery.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tabla_delivery.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tabla_delivery.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tabla_delivery.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tabla_delivery.setHorizontalHeaderItem(5, __qtablewidgetitem36)
        self.tabla_delivery.setObjectName(u"tabla_delivery")
        self.tabla_delivery.setGeometry(QRect(20, 160, 781, 531))
        self.tabla_delivery.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.tabla_delivery.setAlternatingRowColors(True)
        self.tabla_delivery.horizontalHeader().setVisible(True)
        self.tabla_delivery.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_delivery.horizontalHeader().setDefaultSectionSize(110)
        self.tabla_delivery.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tabla_delivery.horizontalHeader().setStretchLastSection(True)
        self.tabla_delivery.verticalHeader().setVisible(False)
        self.tabla_delivery.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_delivery.verticalHeader().setStretchLastSection(False)
        self.lineEdit_searchBy = QLineEdit(self.page_repartidores)
        self.lineEdit_searchBy.setObjectName(u"lineEdit_searchBy")
        self.lineEdit_searchBy.setGeometry(QRect(530, 100, 271, 35))
        self.lineEdit_searchBy.setMinimumSize(QSize(0, 35))
        self.lineEdit_searchBy.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_searchBy.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.layoutWidget1 = QWidget(self.page_repartidores)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 100, 401, 42))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_addDelivery = QPushButton(self.layoutWidget1)
        self.btn_addDelivery.setObjectName(u"btn_addDelivery")
        self.btn_addDelivery.setMinimumSize(QSize(0, 40))
        self.btn_addDelivery.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.btn_addDelivery)

        self.btn_exportExcel = QPushButton(self.layoutWidget1)
        self.btn_exportExcel.setObjectName(u"btn_exportExcel")
        self.btn_exportExcel.setMinimumSize(QSize(0, 40))
        self.btn_exportExcel.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.btn_exportExcel)

        self.btn_exportPDF = QPushButton(self.layoutWidget1)
        self.btn_exportPDF.setObjectName(u"btn_exportPDF")
        self.btn_exportPDF.setMinimumSize(QSize(0, 40))
        self.btn_exportPDF.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(218, 29, 29);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.btn_exportPDF)

        self.stackedWidget.addWidget(self.page_repartidores)

        self.retranslateUi(main_screen_widget)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(main_screen_widget)
    # setupUi

    def retranslateUi(self, main_screen_widget):
        main_screen_widget.setWindowTitle(QCoreApplication.translate("main_screen_widget", u"Form", None))
        self.label.setText(QCoreApplication.translate("main_screen_widget", u"Consultas", None))
        ___qtablewidgetitem = self.tabla_users.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("main_screen_widget", u"Id", None));
        ___qtablewidgetitem1 = self.tabla_users.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("main_screen_widget", u"Username", None));
        ___qtablewidgetitem2 = self.tabla_users.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("main_screen_widget", u"Email", None));
        ___qtablewidgetitem3 = self.tabla_users.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("main_screen_widget", u"Address", None));
        ___qtablewidgetitem4 = self.tabla_users.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("main_screen_widget", u"Phone", None));
        ___qtablewidgetitem5 = self.tabla_users.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("main_screen_widget", u"CreationDate", None));
        ___qtablewidgetitem6 = self.tabla_users.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("main_screen_widget", u"Items", None));
        self.lineEdit_search_email.setPlaceholderText(QCoreApplication.translate("main_screen_widget", u"Search by username or email...", None))
        self.users_management.setText(QCoreApplication.translate("main_screen_widget", u"Users management area", None))
        self.users_tittle.setText(QCoreApplication.translate("main_screen_widget", u"Users", None))
        self.btn_addUser_2.setText(QCoreApplication.translate("main_screen_widget", u"Add User", None))
        self.btn_exportToExcel.setText(QCoreApplication.translate("main_screen_widget", u"Export to Excel", None))
        self.btn_exportToPDF.setText(QCoreApplication.translate("main_screen_widget", u"Export to PDF", None))
        ___qtablewidgetitem7 = self.tabla_restaurants.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("main_screen_widget", u"Id", None));
        ___qtablewidgetitem8 = self.tabla_restaurants.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("main_screen_widget", u"Name", None));
        ___qtablewidgetitem9 = self.tabla_restaurants.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("main_screen_widget", u"Address", None));
        ___qtablewidgetitem10 = self.tabla_restaurants.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("main_screen_widget", u"Category", None));
        ___qtablewidgetitem11 = self.tabla_restaurants.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("main_screen_widget", u"Phone", None));
        ___qtablewidgetitem12 = self.tabla_restaurants.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("main_screen_widget", u"Schedule", None));
        ___qtablewidgetitem13 = self.tabla_restaurants.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("main_screen_widget", u"Qualification", None));
        ___qtablewidgetitem14 = self.tabla_restaurants.horizontalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("main_screen_widget", u"Items", None));
        self.lineEdit_searchByNameCategoryTlfn.setPlaceholderText(QCoreApplication.translate("main_screen_widget", u"Search by name, phone, category...", None))
        self.restaurant_management.setText(QCoreApplication.translate("main_screen_widget", u"Restaurants management area", None))
        self.btn_addRestaurant.setText(QCoreApplication.translate("main_screen_widget", u"Add Restaurant", None))
        self.btn_exportToExcel_5.setText(QCoreApplication.translate("main_screen_widget", u"Export to Excel", None))
        self.btn_exportToPDF_5.setText(QCoreApplication.translate("main_screen_widget", u"Export to PDF", None))
        self.restaurant_tittle.setText(QCoreApplication.translate("main_screen_widget", u"Restaurants", None))
        ___qtablewidgetitem15 = self.tabla_plates.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("main_screen_widget", u"Id", None));
        ___qtablewidgetitem16 = self.tabla_plates.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("main_screen_widget", u"Name", None));
        ___qtablewidgetitem17 = self.tabla_plates.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("main_screen_widget", u"Price", None));
        ___qtablewidgetitem18 = self.tabla_plates.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("main_screen_widget", u"Description", None));
        ___qtablewidgetitem19 = self.tabla_plates.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("main_screen_widget", u"Restaurant ID", None));
        ___qtablewidgetitem20 = self.tabla_plates.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("main_screen_widget", u"Items", None));
        self.lineEdit_searchByNameDescription.setPlaceholderText(QCoreApplication.translate("main_screen_widget", u"Search by name, description ...", None))
        self.plates_tittle.setText(QCoreApplication.translate("main_screen_widget", u"Plates", None))
        self.btn_addPlate.setText(QCoreApplication.translate("main_screen_widget", u"Add Plate", None))
        self.btn_exportToExcel_2.setText(QCoreApplication.translate("main_screen_widget", u"Export to Excel", None))
        self.btn_exportToPDF_2.setText(QCoreApplication.translate("main_screen_widget", u"Export to PDF", None))
        self.plates_management.setText(QCoreApplication.translate("main_screen_widget", u"Plates management area", None))
        ___qtablewidgetitem21 = self.tabla_orders.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("main_screen_widget", u"Id", None));
        ___qtablewidgetitem22 = self.tabla_orders.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("main_screen_widget", u"User ID", None));
        ___qtablewidgetitem23 = self.tabla_orders.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("main_screen_widget", u"Restaurant ID", None));
        ___qtablewidgetitem24 = self.tabla_orders.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("main_screen_widget", u"State", None));
        ___qtablewidgetitem25 = self.tabla_orders.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("main_screen_widget", u"Items", None));
        self.lineEdit_searchByUserID.setText("")
        self.lineEdit_searchByUserID.setPlaceholderText(QCoreApplication.translate("main_screen_widget", u"Search by UserID ...", None))
        self.plates_management_2.setText(QCoreApplication.translate("main_screen_widget", u"Orders management area", None))
        self.plates_tittle_2.setText(QCoreApplication.translate("main_screen_widget", u"Orders", None))
        self.btn_addOrder.setText(QCoreApplication.translate("main_screen_widget", u"Add Order", None))
        self.btn_exportToExcel_3.setText(QCoreApplication.translate("main_screen_widget", u"Export to Excel", None))
        self.btn_exportToPDF_3.setText(QCoreApplication.translate("main_screen_widget", u"Export to PDF", None))
        self.plates_management_3.setText(QCoreApplication.translate("main_screen_widget", u"Orders details management area", None))
        self.btn_addOrderDetails.setText(QCoreApplication.translate("main_screen_widget", u"Add Order Details", None))
        self.btn_exportToExcel_4.setText(QCoreApplication.translate("main_screen_widget", u"Export to Excel", None))
        self.btn_exportToPDF_4.setText(QCoreApplication.translate("main_screen_widget", u"Export to PDF", None))
        self.plates_tittle_3.setText(QCoreApplication.translate("main_screen_widget", u"Orders Details", None))
        self.lineEdit_searchByOrderID.setText("")
        self.lineEdit_searchByOrderID.setPlaceholderText(QCoreApplication.translate("main_screen_widget", u"Search by OrderID ...", None))
        ___qtablewidgetitem26 = self.tabla_ordersDetails.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("main_screen_widget", u"Id", None));
        ___qtablewidgetitem27 = self.tabla_ordersDetails.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("main_screen_widget", u"Order ID", None));
        ___qtablewidgetitem28 = self.tabla_ordersDetails.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("main_screen_widget", u"Plate ID", None));
        ___qtablewidgetitem29 = self.tabla_ordersDetails.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("main_screen_widget", u"Amount", None));
        ___qtablewidgetitem30 = self.tabla_ordersDetails.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("main_screen_widget", u"Items", None));
        self.label_3.setText(QCoreApplication.translate("main_screen_widget", u"Delivery People", None))
        self.label_4.setText(QCoreApplication.translate("main_screen_widget", u"Delivery People management area", None))
        ___qtablewidgetitem31 = self.tabla_delivery.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("main_screen_widget", u"Id", None));
        ___qtablewidgetitem32 = self.tabla_delivery.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("main_screen_widget", u"NIF", None));
        ___qtablewidgetitem33 = self.tabla_delivery.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("main_screen_widget", u"Name", None));
        ___qtablewidgetitem34 = self.tabla_delivery.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("main_screen_widget", u"Order ID", None));
        ___qtablewidgetitem35 = self.tabla_delivery.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("main_screen_widget", u"Vehicle", None));
        ___qtablewidgetitem36 = self.tabla_delivery.horizontalHeaderItem(5)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("main_screen_widget", u"Items", None));
        self.lineEdit_searchBy.setPlaceholderText(QCoreApplication.translate("main_screen_widget", u"Search by NIF, name ...", None))
        self.btn_addDelivery.setText(QCoreApplication.translate("main_screen_widget", u"Add Delivery", None))
        self.btn_exportExcel.setText(QCoreApplication.translate("main_screen_widget", u"Export to Excel", None))
        self.btn_exportPDF.setText(QCoreApplication.translate("main_screen_widget", u"Export to PDF", None))
    # retranslateUi

