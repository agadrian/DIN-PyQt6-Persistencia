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
        self.label_2 = QLabel(self.page_usuarios)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 200, 161, 61))
        self.stackedWidget.addWidget(self.page_usuarios)
        self.page_restaurantes = QWidget()
        self.page_restaurantes.setObjectName(u"page_restaurantes")
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
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.page_repartidores)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 60, 221, 41))
        font1 = QFont()
        font1.setPointSize(13)
        self.label_4.setFont(font1)
        self.tableWidget = QTableWidget(self.page_repartidores)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
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
        self.widget = QWidget(self.page_repartidores)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 110, 401, 42))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_addUser = QPushButton(self.widget)
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

        self.btn_cancel = QPushButton(self.widget)
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

        self.btn_cancel_2 = QPushButton(self.widget)
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

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(main_screen_widget)
    # setupUi

    def retranslateUi(self, main_screen_widget):
        main_screen_widget.setWindowTitle(QCoreApplication.translate("main_screen_widget", u"Form", None))
        self.label.setText(QCoreApplication.translate("main_screen_widget", u"Consultas", None))
        self.label_2.setText(QCoreApplication.translate("main_screen_widget", u"Users Page", None))
        self.label_3.setText(QCoreApplication.translate("main_screen_widget", u"Users", None))
        self.label_4.setText(QCoreApplication.translate("main_screen_widget", u"Users management area", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("main_screen_widget", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("main_screen_widget", u"Email", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("main_screen_widget", u"Address", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("main_screen_widget", u"Phone", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("main_screen_widget", u"CreationDate", None));
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("main_screen_widget", u"Search by username, email...", None))
        self.btn_addUser.setText(QCoreApplication.translate("main_screen_widget", u"Add User", None))
        self.btn_cancel.setText(QCoreApplication.translate("main_screen_widget", u"Export to Excel", None))
        self.btn_cancel_2.setText(QCoreApplication.translate("main_screen_widget", u"Export to PDF", None))
    # retranslateUi

