# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateRestaurantDialog.ui'
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

class Ui_AddRestaurantDialog(object):
    def setupUi(self, AddRestaurantDialog):
        if not AddRestaurantDialog.objectName():
            AddRestaurantDialog.setObjectName(u"AddRestaurantDialog")
        AddRestaurantDialog.resize(542, 658)
        AddRestaurantDialog.setStyleSheet(u"QDialog{\n"
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
        self.label = QLabel(AddRestaurantDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 231, 31))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget = QWidget(AddRestaurantDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 80, 481, 493))
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

        self.lineEdit_address = QLineEdit(self.layoutWidget)
        self.lineEdit_address.setObjectName(u"lineEdit_address")
        self.lineEdit_address.setMinimumSize(QSize(0, 35))
        self.lineEdit_address.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.lineEdit_address)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.lineEdit_category = QLineEdit(self.layoutWidget)
        self.lineEdit_category.setObjectName(u"lineEdit_category")
        self.lineEdit_category.setMinimumSize(QSize(0, 35))
        self.lineEdit_category.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.lineEdit_category)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.lineEdit_phone = QLineEdit(self.layoutWidget)
        self.lineEdit_phone.setObjectName(u"lineEdit_phone")
        self.lineEdit_phone.setMinimumSize(QSize(0, 35))
        self.lineEdit_phone.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.lineEdit_phone)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_6)

        self.lineEdit_schedule = QLineEdit(self.layoutWidget)
        self.lineEdit_schedule.setObjectName(u"lineEdit_schedule")
        self.lineEdit_schedule.setMinimumSize(QSize(0, 35))
        self.lineEdit_schedule.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_6.addWidget(self.lineEdit_schedule)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_7)

        self.lineEdit_qualification = QLineEdit(self.layoutWidget)
        self.lineEdit_qualification.setObjectName(u"lineEdit_qualification")
        self.lineEdit_qualification.setMinimumSize(QSize(0, 35))
        self.lineEdit_qualification.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_7.addWidget(self.lineEdit_qualification)


        self.verticalLayout_5.addLayout(self.verticalLayout_7)

        self.layoutWidget1 = QWidget(AddRestaurantDialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(260, 590, 251, 42))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_addRestaurant = QPushButton(self.layoutWidget1)
        self.btn_addRestaurant.setObjectName(u"btn_addRestaurant")
        self.btn_addRestaurant.setMinimumSize(QSize(0, 40))
        self.btn_addRestaurant.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.btn_addRestaurant)

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

        self.line = QFrame(AddRestaurantDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 541, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(AddRestaurantDialog)

        QMetaObject.connectSlotsByName(AddRestaurantDialog)
    # setupUi

    def retranslateUi(self, AddRestaurantDialog):
        AddRestaurantDialog.setWindowTitle(QCoreApplication.translate("AddRestaurantDialog", u"Add restaurant Dialog", None))
        self.label.setText(QCoreApplication.translate("AddRestaurantDialog", u"Add Restaurant", None))
        self.label_2.setText(QCoreApplication.translate("AddRestaurantDialog", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("AddRestaurantDialog", u"Address", None))
        self.label_4.setText(QCoreApplication.translate("AddRestaurantDialog", u"Category", None))
        self.label_5.setText(QCoreApplication.translate("AddRestaurantDialog", u"Phone", None))
        self.label_6.setText(QCoreApplication.translate("AddRestaurantDialog", u"Schedule", None))
        self.label_7.setText(QCoreApplication.translate("AddRestaurantDialog", u"Qualification", None))
        self.btn_addRestaurant.setText(QCoreApplication.translate("AddRestaurantDialog", u"Add Restaurant", None))
        self.btn_cancel.setText(QCoreApplication.translate("AddRestaurantDialog", u"Cancel", None))
    # retranslateUi

