# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(345, 380)
        Form.setMinimumSize(QSize(345, 380))
        Form.setMaximumSize(QSize(345, 380))
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 10, 311, 361))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(89, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(75, 75))
        self.label.setPixmap(QPixmap(u"img/logoLogin.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(89, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_password = QLineEdit(self.frame)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit_password, 3, 0, 1, 1)

        self.label_singup = QLabel(self.frame)
        self.label_singup.setObjectName(u"label_singup")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_singup.sizePolicy().hasHeightForWidth())
        self.label_singup.setSizePolicy(sizePolicy)
        self.label_singup.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_singup, 5, 0, 1, 1)

        self.lineEdit_username = QLineEdit(self.frame)
        self.lineEdit_username.setObjectName(u"lineEdit_username")

        self.gridLayout.addWidget(self.lineEdit_username, 1, 0, 1, 1)

        self.label_password = QLabel(self.frame)
        self.label_password.setObjectName(u"label_password")
        sizePolicy.setHeightForWidth(self.label_password.sizePolicy().hasHeightForWidth())
        self.label_password.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_password, 2, 0, 1, 1)

        self.label_username = QLabel(self.frame)
        self.label_username.setObjectName(u"label_username")
        sizePolicy.setHeightForWidth(self.label_username.sizePolicy().hasHeightForWidth())
        self.label_username.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_username, 0, 0, 1, 1)

        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")

        self.gridLayout.addWidget(self.btn_login, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.lineEdit_password.setPlaceholderText("")
        self.label_singup.setText(QCoreApplication.translate("Form", u"Not a memeber? <a href=\"#\"> Sing up</a>", None))
        self.lineEdit_username.setPlaceholderText("")
        self.label_password.setText(QCoreApplication.translate("Form", u"Password", None))
        self.label_username.setText(QCoreApplication.translate("Form", u"Email", None))
        self.btn_login.setText(QCoreApplication.translate("Form", u"Login", None))
    # retranslateUi

