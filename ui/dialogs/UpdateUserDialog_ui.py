# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpdateUserDialog.ui'
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

class Ui_UpdateUserDialog(object):
    def setupUi(self, UpdateUserDialog):
        if not UpdateUserDialog.objectName():
            UpdateUserDialog.setObjectName(u"UpdateUserDialog")
        UpdateUserDialog.resize(542, 580)
        UpdateUserDialog.setStyleSheet(u"QDialog{\n"
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
        self.label = QLabel(UpdateUserDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 191, 31))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget = QWidget(UpdateUserDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 80, 481, 411))
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

        self.lineEdit_username = QLineEdit(self.layoutWidget)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setMinimumSize(QSize(0, 35))
        self.lineEdit_username.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.lineEdit_username)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.lineEdit_email = QLineEdit(self.layoutWidget)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setMinimumSize(QSize(0, 35))
        self.lineEdit_email.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.lineEdit_email)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.lineEdit_address = QLineEdit(self.layoutWidget)
        self.lineEdit_address.setObjectName(u"lineEdit_address")
        self.lineEdit_address.setMinimumSize(QSize(0, 35))
        self.lineEdit_address.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.lineEdit_address)


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

        self.layoutWidget1 = QWidget(UpdateUserDialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(290, 510, 221, 42))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_updateUser = QPushButton(self.layoutWidget1)
        self.btn_updateUser.setObjectName(u"btn_updateUser")
        self.btn_updateUser.setMinimumSize(QSize(0, 40))
        self.btn_updateUser.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.btn_updateUser)

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

        self.line = QFrame(UpdateUserDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 541, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(UpdateUserDialog)

        QMetaObject.connectSlotsByName(UpdateUserDialog)
    # setupUi

    def retranslateUi(self, UpdateUserDialog):
        UpdateUserDialog.setWindowTitle(QCoreApplication.translate("UpdateUserDialog", u"Update User Dialog", None))
        self.label.setText(QCoreApplication.translate("UpdateUserDialog", u"Update User", None))
        self.label_2.setText(QCoreApplication.translate("UpdateUserDialog", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("UpdateUserDialog", u"Email", None))
        self.label_4.setText(QCoreApplication.translate("UpdateUserDialog", u"Address", None))
        self.label_5.setText(QCoreApplication.translate("UpdateUserDialog", u"Phone", None))
        self.btn_updateUser.setText(QCoreApplication.translate("UpdateUserDialog", u"Update User", None))
        self.btn_cancel.setText(QCoreApplication.translate("UpdateUserDialog", u"Cancel", None))
    # retranslateUi

