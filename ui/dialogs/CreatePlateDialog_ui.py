# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreatePlateDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_AddPlateDialog(object):
    def setupUi(self, AddPlateDialog):
        if not AddPlateDialog.objectName():
            AddPlateDialog.setObjectName(u"AddPlateDialog")
        AddPlateDialog.resize(542, 525)
        AddPlateDialog.setStyleSheet(u"QDialog{\n"
"	background-color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 1px solid gray;\n"
"	border-radius: 6px;\n"
"	padding-left: 15px;\n"
"height: 35px;\n"
"}\n"
"\n"
"")
        self.label = QLabel(AddPlateDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 231, 31))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget = QWidget(AddPlateDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 80, 481, 351))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit_name = QLineEdit(self.layoutWidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setMinimumSize(QSize(0, 35))
        self.lineEdit_name.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.lineEdit_name)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.lineEdit_price = QLineEdit(self.layoutWidget)
        self.lineEdit_price.setObjectName(u"lineEdit_price")
        self.lineEdit_price.setMinimumSize(QSize(0, 35))
        self.lineEdit_price.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.lineEdit_price)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.lineEdit_description = QLineEdit(self.layoutWidget)
        self.lineEdit_description.setObjectName(u"lineEdit_description")
        self.lineEdit_description.setMinimumSize(QSize(0, 35))
        self.lineEdit_description.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.lineEdit_description)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.lineEdit_restaurantID = QLineEdit(self.layoutWidget)
        self.lineEdit_restaurantID.setObjectName(u"lineEdit_restaurantID")
        self.lineEdit_restaurantID.setMinimumSize(QSize(0, 35))
        self.lineEdit_restaurantID.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.lineEdit_restaurantID)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.layoutWidget1 = QWidget(AddPlateDialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(260, 460, 251, 42))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_addPlate = QPushButton(self.layoutWidget1)
        self.btn_addPlate.setObjectName(u"btn_addPlate")
        self.btn_addPlate.setMinimumSize(QSize(0, 40))
        self.btn_addPlate.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.btn_addPlate)

        self.btn_cancel = QPushButton(self.layoutWidget1)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(0, 40))
        self.btn_cancel.setStyleSheet(u"QPushButton{\n"
"	background-color: #585858;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.line = QFrame(AddPlateDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 541, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(AddPlateDialog)

        QMetaObject.connectSlotsByName(AddPlateDialog)
    # setupUi

    def retranslateUi(self, AddPlateDialog):
        AddPlateDialog.setWindowTitle(QCoreApplication.translate("AddPlateDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("AddPlateDialog", u"Add Plate", None))
        self.label_2.setText(QCoreApplication.translate("AddPlateDialog", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("AddPlateDialog", u"Price", None))
        self.label_4.setText(QCoreApplication.translate("AddPlateDialog", u"Description", None))
        self.label_5.setText(QCoreApplication.translate("AddPlateDialog", u"Restaurant ID", None))
        self.btn_addPlate.setText(QCoreApplication.translate("AddPlateDialog", u"Add Plate", None))
        self.btn_cancel.setText(QCoreApplication.translate("AddPlateDialog", u"Cancel", None))
    # retranslateUi

