# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QTabWidget,
    QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(1063, 645)
        main.setMinimumSize(QSize(0, 0))
        self.tabWidget = QTabWidget(main)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 1041, 611))
        self.tab_usuarios = QWidget()
        self.tab_usuarios.setObjectName(u"tab_usuarios")
        self.label = QLabel(self.tab_usuarios)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 120, 49, 16))
        self.tabWidget.addTab(self.tab_usuarios, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 140, 49, 16))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 140, 49, 16))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 100, 49, 16))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_5 = QLabel(self.tab_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 190, 49, 16))
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_ = QWidget()
        self.tab_.setObjectName(u"tab_")
        self.label_6 = QLabel(self.tab_)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 140, 49, 16))
        self.tabWidget.addTab(self.tab_, "")

        self.retranslateUi(main)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"Form", None))
        self.label.setText(QCoreApplication.translate("main", u"1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_usuarios), QCoreApplication.translate("main", u"Usuarios", None))
        self.label_2.setText(QCoreApplication.translate("main", u"2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("main", u"P\u00e1gina", None))
        self.label_3.setText(QCoreApplication.translate("main", u"3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("main", u"P\u00e1gina", None))
        self.label_4.setText(QCoreApplication.translate("main", u"4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("main", u"P\u00e1gina", None))
        self.label_5.setText(QCoreApplication.translate("main", u"5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("main", u"P\u00e1gina", None))
        self.label_6.setText(QCoreApplication.translate("main", u"6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_), QCoreApplication.translate("main", u"Tab 2", None))
    # retranslateUi

