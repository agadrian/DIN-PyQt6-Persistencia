# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Register.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(345, 380)
        Form.setMinimumSize(QSize(345, 380))
        Form.setMaximumSize(QSize(400, 455))
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 301, 351))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_username = QLabel(self.frame)
        self.label_username.setObjectName(u"label_username")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_username.sizePolicy().hasHeightForWidth())
        self.label_username.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_username)

        self.lineEdit_username = QLineEdit(self.frame)
        self.lineEdit_username.setObjectName(u"lineEdit_username")

        self.verticalLayout.addWidget(self.lineEdit_username)

        self.label_email = QLabel(self.frame)
        self.label_email.setObjectName(u"label_email")
        sizePolicy.setHeightForWidth(self.label_email.sizePolicy().hasHeightForWidth())
        self.label_email.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_email)

        self.lineEdit_email = QLineEdit(self.frame)
        self.lineEdit_email.setObjectName(u"lineEdit_email")

        self.verticalLayout.addWidget(self.lineEdit_email)

        self.label_password = QLabel(self.frame)
        self.label_password.setObjectName(u"label_password")
        sizePolicy.setHeightForWidth(self.label_password.sizePolicy().hasHeightForWidth())
        self.label_password.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_password)

        self.lineEdit_password = QLineEdit(self.frame)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.lineEdit_password)

        self.label_password_2 = QLabel(self.frame)
        self.label_password_2.setObjectName(u"label_password_2")
        sizePolicy.setHeightForWidth(self.label_password_2.sizePolicy().hasHeightForWidth())
        self.label_password_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_password_2)

        self.lineEdit_confirmPassword = QLineEdit(self.frame)
        self.lineEdit_confirmPassword.setObjectName(u"lineEdit_confirmPassword")

        self.verticalLayout.addWidget(self.lineEdit_confirmPassword)

        self.btn_singup = QPushButton(self.frame)
        self.btn_singup.setObjectName(u"btn_singup")

        self.verticalLayout.addWidget(self.btn_singup)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_username.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_email.setText(QCoreApplication.translate("Form", u"Email", None))
        self.label_password.setText(QCoreApplication.translate("Form", u"Password", None))
        self.label_password_2.setText(QCoreApplication.translate("Form", u"Confirm Password", None))
        self.btn_singup.setText(QCoreApplication.translate("Form", u"Sing up", None))
    # retranslateUi

