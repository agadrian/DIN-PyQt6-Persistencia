# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpdateOrderDetailsDialog.ui'
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

class Ui_UpdateOrderDetailsDialog(object):
    def setupUi(self, UpdateOrderDetailsDialog):
        if not UpdateOrderDetailsDialog.objectName():
            UpdateOrderDetailsDialog.setObjectName(u"UpdateOrderDetailsDialog")
        UpdateOrderDetailsDialog.resize(542, 433)
        UpdateOrderDetailsDialog.setStyleSheet(u"QDialog{\n"
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
        self.label = QLabel(UpdateOrderDetailsDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 301, 31))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget = QWidget(UpdateOrderDetailsDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 80, 481, 261))
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

        self.lineEdit_orderID = QLineEdit(self.layoutWidget)
        self.lineEdit_orderID.setObjectName(u"lineEdit_orderID")
        self.lineEdit_orderID.setMinimumSize(QSize(0, 35))
        self.lineEdit_orderID.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.lineEdit_orderID)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.lineEdit_plateID = QLineEdit(self.layoutWidget)
        self.lineEdit_plateID.setObjectName(u"lineEdit_plateID")
        self.lineEdit_plateID.setMinimumSize(QSize(0, 35))
        self.lineEdit_plateID.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.lineEdit_plateID)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.lineEdit_amount = QLineEdit(self.layoutWidget)
        self.lineEdit_amount.setObjectName(u"lineEdit_amount")
        self.lineEdit_amount.setMinimumSize(QSize(0, 35))
        self.lineEdit_amount.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.lineEdit_amount)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.layoutWidget1 = QWidget(UpdateOrderDetailsDialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(180, 370, 331, 42))
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
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #28a766; \n"
"    cursor: pointer;\n"
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
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #7a7a7a;\n"
"    cursor: pointer; \n"
"}")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.line = QFrame(UpdateOrderDetailsDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 541, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(UpdateOrderDetailsDialog)

        QMetaObject.connectSlotsByName(UpdateOrderDetailsDialog)
    # setupUi

    def retranslateUi(self, UpdateOrderDetailsDialog):
        UpdateOrderDetailsDialog.setWindowTitle(QCoreApplication.translate("UpdateOrderDetailsDialog", u"Update order details Dialog", None))
        self.label.setText(QCoreApplication.translate("UpdateOrderDetailsDialog", u"Update Order Details", None))
        self.label_2.setText(QCoreApplication.translate("UpdateOrderDetailsDialog", u"Order ID", None))
        self.label_3.setText(QCoreApplication.translate("UpdateOrderDetailsDialog", u"Plate ID", None))
        self.label_4.setText(QCoreApplication.translate("UpdateOrderDetailsDialog", u"Amount", None))
        self.btn_updateOrderDetails.setText(QCoreApplication.translate("UpdateOrderDetailsDialog", u"Update Order Details", None))
        self.btn_cancel.setText(QCoreApplication.translate("UpdateOrderDetailsDialog", u"Cancel", None))
    # retranslateUi

