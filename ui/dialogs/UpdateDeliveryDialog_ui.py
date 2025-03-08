# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpdateDeliveryDialog.ui'
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

class Ui_UpdateOrderDialog(object):
    def setupUi(self, UpdateOrderDialog):
        if not UpdateOrderDialog.objectName():
            UpdateOrderDialog.setObjectName(u"UpdateOrderDialog")
        UpdateOrderDialog.resize(542, 515)
        UpdateOrderDialog.setStyleSheet(u"QDialog{\n"
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
        self.label = QLabel(UpdateOrderDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 301, 31))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget = QWidget(UpdateOrderDialog)
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

        self.lineEdit_NIF = QLineEdit(self.layoutWidget)
        self.lineEdit_NIF.setObjectName(u"lineEdit_NIF")
        self.lineEdit_NIF.setMinimumSize(QSize(0, 35))
        self.lineEdit_NIF.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.lineEdit_NIF)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.lineEdit_name = QLineEdit(self.layoutWidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setMinimumSize(QSize(0, 35))
        self.lineEdit_name.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.lineEdit_name)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.lineEdit_orderID = QLineEdit(self.layoutWidget)
        self.lineEdit_orderID.setObjectName(u"lineEdit_orderID")
        self.lineEdit_orderID.setMinimumSize(QSize(0, 35))
        self.lineEdit_orderID.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.lineEdit_orderID)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.lineEdit_vehicle = QLineEdit(self.layoutWidget)
        self.lineEdit_vehicle.setObjectName(u"lineEdit_vehicle")
        self.lineEdit_vehicle.setMinimumSize(QSize(0, 35))
        self.lineEdit_vehicle.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.lineEdit_vehicle)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.layoutWidget1 = QWidget(UpdateOrderDialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(180, 450, 331, 42))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_updateOrderDetails = QPushButton(self.layoutWidget1)
        self.btn_updateOrderDetails.setObjectName(u"btn_updateOrderDetails")
        self.btn_updateOrderDetails.setMinimumSize(QSize(0, 40))
        self.btn_updateOrderDetails.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.btn_updateOrderDetails)

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

        self.line = QFrame(UpdateOrderDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 541, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(UpdateOrderDialog)

        QMetaObject.connectSlotsByName(UpdateOrderDialog)
    # setupUi

    def retranslateUi(self, UpdateOrderDialog):
        UpdateOrderDialog.setWindowTitle(QCoreApplication.translate("UpdateOrderDialog", u"Update Delivery Dialog", None))
        self.label.setText(QCoreApplication.translate("UpdateOrderDialog", u"Update Delivery", None))
        self.label_2.setText(QCoreApplication.translate("UpdateOrderDialog", u"NIF", None))
        self.label_3.setText(QCoreApplication.translate("UpdateOrderDialog", u"Name", None))
        self.label_4.setText(QCoreApplication.translate("UpdateOrderDialog", u"Order ID", None))
        self.label_5.setText(QCoreApplication.translate("UpdateOrderDialog", u"Vehicle", None))
        self.btn_updateOrderDetails.setText(QCoreApplication.translate("UpdateOrderDialog", u"Update Delivery", None))
        self.btn_cancel.setText(QCoreApplication.translate("UpdateOrderDialog", u"Cancel", None))
    # retranslateUi

