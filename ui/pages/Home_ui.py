# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1253, 867)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.icons = QWidget(self.centralwidget)
        self.icons.setObjectName(u"icons")
        self.icons.setGeometry(QRect(10, 10, 131, 841))
        self.icons.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.btn_home = QPushButton(self.icons)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setGeometry(QRect(30, 100, 75, 41))
        self.btn_home.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/prefix/img/lupa.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(32, 32))
        self.label = QLabel(self.icons)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 40, 40, 40))
        self.label.setPixmap(QPixmap(u":/prefix/img/home.png"))
        self.label.setScaledContents(True)
        self.btn_home_2 = QPushButton(self.icons)
        self.btn_home_2.setObjectName(u"btn_home_2")
        self.btn_home_2.setGeometry(QRect(30, 160, 75, 41))
        self.btn_home_2.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/prefix/img/restaurante.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_home_2.setIcon(icon1)
        self.btn_home_2.setIconSize(QSize(32, 32))
        self.btn_home_3 = QPushButton(self.icons)
        self.btn_home_3.setObjectName(u"btn_home_3")
        self.btn_home_3.setGeometry(QRect(30, 230, 75, 41))
        self.btn_home_3.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/prefix/img/plato.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_home_3.setIcon(icon2)
        self.btn_home_3.setIconSize(QSize(32, 32))
        self.btn_home_4 = QPushButton(self.icons)
        self.btn_home_4.setObjectName(u"btn_home_4")
        self.btn_home_4.setGeometry(QRect(30, 300, 75, 41))
        self.btn_home_4.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/prefix/img/pedido.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_home_4.setIcon(icon3)
        self.btn_home_4.setIconSize(QSize(32, 32))
        self.btn_home_5 = QPushButton(self.icons)
        self.btn_home_5.setObjectName(u"btn_home_5")
        self.btn_home_5.setGeometry(QRect(30, 380, 75, 41))
        self.btn_home_5.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u":/prefix/img/detalles.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_home_5.setIcon(icon4)
        self.btn_home_5.setIconSize(QSize(32, 32))
        self.text = QWidget(self.centralwidget)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(160, 10, 191, 841))
        self.pushButton = QPushButton(self.text)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 70, 75, 24))
        self.label_2 = QLabel(self.text)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 49, 16))
        self.label_3 = QLabel(self.text)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 40, 49, 16))
        self.main_screen = QWidget(self.centralwidget)
        self.main_screen.setObjectName(u"main_screen")
        self.main_screen.setGeometry(QRect(360, 110, 881, 741))
        self.main_screen.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(360, 10, 881, 81))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText("")
        self.label.setText("")
        self.btn_home_2.setText("")
        self.btn_home_3.setText("")
        self.btn_home_4.setText("")
        self.btn_home_5.setText("")
        self.pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

