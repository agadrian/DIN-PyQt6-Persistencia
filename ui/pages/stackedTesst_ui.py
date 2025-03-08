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
        main_screen_widget.resize(840, 740)
        main_screen_widget.setMinimumSize(QSize(840, 740))
        main_screen_widget.setMaximumSize(QSize(840, 740))
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
        self.stackedWidget.addWidget(self.page_platos)
        self.page_pedidos = QWidget()
        self.page_pedidos.setObjectName(u"page_pedidos")
        self.stackedWidget.addWidget(self.page_pedidos)
        self.page_detallesPedidos = QWidget()
        self.page_detallesPedidos.setObjectName(u"page_detallesPedidos")
        self.stackedWidget.addWidget(self.page_detallesPedidos)
        self.page_repartidores = QWidget()
        self.page_repartidores.setObjectName(u"page_repartidores")
        self.label_3 = QLabel(self.page_repartidores)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 121, 51))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.page_repartidores)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 60, 221, 41))
        self.label_4.setFont(font)
        self.tableWidget = QTableWidget(self.page_repartidores)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 170, 781, 531))
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(156)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.lineEdit = QLineEdit(self.page_repartidores)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(530, 110, 271, 35))
        self.lineEdit.setMinimumSize(QSize(0, 35))
        self.lineEdit.setMaximumSize(QSize(16777215, 35))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.layoutWidget1 = QWidget(self.page_repartidores)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 110, 401, 42))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_addUser = QPushButton(self.layoutWidget1)
        self.btn_addUser.setObjectName(u"btn_addUser")
        self.btn_addUser.setMinimumSize(QSize(0, 40))
        self.btn_addUser.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.btn_addUser)

        self.btn_cancel = QPushButton(self.layoutWidget1)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(0, 40))
        self.btn_cancel.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_cancel_2 = QPushButton(self.layoutWidget1)
        self.btn_cancel_2.setObjectName(u"btn_cancel_2")
        self.btn_cancel_2.setMinimumSize(QSize(0, 40))
        self.btn_cancel_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(218, 29, 29);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.btn_cancel_2)

        self.stackedWidget.addWidget(self.page_repartidores)

        self.retranslateUi(main_screen_widget)

        self.stackedWidget.setCurrentIndex(2)


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
        self.label_3.setText(QCoreApplication.translate("main_screen_widget", u"Users", None))
        self.label_4.setText(QCoreApplication.translate("main_screen_widget", u"Users management area", None))
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("main_screen_widget", u"Name", None));
        ___qtablewidgetitem16 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("main_screen_widget", u"Email", None));
        ___qtablewidgetitem17 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("main_screen_widget", u"Address", None));
        ___qtablewidgetitem18 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("main_screen_widget", u"Phone", None));
        ___qtablewidgetitem19 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("main_screen_widget", u"CreationDate", None));
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("main_screen_widget", u"Search by username, email...", None))
        self.btn_addUser.setText(QCoreApplication.translate("main_screen_widget", u"Add User", None))
        self.btn_cancel.setText(QCoreApplication.translate("main_screen_widget", u"Export to Excel", None))
        self.btn_cancel_2.setText(QCoreApplication.translate("main_screen_widget", u"Export to PDF", None))
    # retranslateUi

