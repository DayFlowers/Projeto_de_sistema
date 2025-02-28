# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget, QMainWindow)
from qrc import *
from cadastro import Ui_tela_Cadastro

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(1089, 509)
        self.tela_login = QFrame(login)
        self.tela_login.setObjectName(u"tela_login")
        self.tela_login.setGeometry(QRect(70, 20, 981, 441))
        self.tela_login.setFrameShape(QFrame.Shape.StyledPanel)
        self.tela_login.setFrameShadow(QFrame.Shadow.Raised)
        self.img_foto_fundo = QLabel(self.tela_login)
        self.img_foto_fundo.setObjectName(u"img_foto_fundo")
        self.img_foto_fundo.setGeometry(QRect(0, 0, 981, 441))
        self.img_foto_fundo.setPixmap(QPixmap(u":/fme/fme.jpg"))
        self.img_foto_fundo.setScaledContents(True)
        self.rtn_login = QFrame(self.tela_login)
        self.rtn_login.setObjectName(u"rtn_login")
        self.rtn_login.setGeometry(QRect(330, 30, 331, 391))
        self.rtn_login.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.rtn_login.setFrameShape(QFrame.Shape.StyledPanel)
        self.rtn_login.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_Email = QLineEdit(self.rtn_login)
        self.btn_Email.setObjectName(u"btn_Email")
        self.btn_Email.setGeometry(QRect(20, 130, 291, 21))
        self.btn_Email.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_Senha = QLineEdit(self.rtn_login)
        self.btn_Senha.setObjectName(u"btn_Senha")
        self.btn_Senha.setGeometry(QRect(20, 200, 291, 21))
        self.btn_Senha.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_Senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.btn_Entrar = QPushButton(self.rtn_login)
        self.btn_Entrar.setObjectName(u"btn_Entrar")
        self.btn_Entrar.setGeometry(QRect(80, 270, 161, 31))
        self.btn_Entrar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.txt_login = QLabel(self.rtn_login)
        self.txt_login.setObjectName(u"txt_login")
        self.txt_login.setGeometry(QRect(120, 30, 91, 41))
        self.txt_login.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 22pt \"Segoe UI\";")
        self.txt_Email = QLabel(self.rtn_login)
        self.txt_Email.setObjectName(u"txt_Email")
        self.txt_Email.setGeometry(QRect(20, 110, 49, 16))
        self.txt_Email.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.txt_Senha = QLabel(self.rtn_login)
        self.txt_Senha.setObjectName(u"txt_Senha")
        self.txt_Senha.setGeometry(QRect(20, 180, 49, 16))
        self.txt_Senha.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Cadastrese = QPushButton(self.rtn_login)
        self.btn_Cadastrese.setObjectName(u"btn_Cadastrese")
        self.btn_Cadastrese.setGeometry(QRect(120, 320, 75, 24))
        self.btn_Cadastrese.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.btn_Cadastrese.clicked.connect(self.cadastrese)

        self.retranslateUi(login)

    def cadastrese(self):
        self.window_cadastro=QMainWindow()
        self.Ui_cadastro=Ui_tela_Cadastro()
        self.Ui_cadastro.setupUi(self.window_cadastro)
        self.window_cadastro.show()

        #QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.img_foto_fundo.setText("")
        self.btn_Senha.setText("")
        self.btn_Entrar.setText(QCoreApplication.translate("login", u"Entrar", None))
        self.txt_login.setText(QCoreApplication.translate("login", u"Login", None))
        self.txt_Email.setText(QCoreApplication.translate("login", u"E-mail", None))
        self.txt_Senha.setText(QCoreApplication.translate("login", u"Senha", None))
        self.btn_Cadastrese.setText(QCoreApplication.translate("login", u"Cadastre-se", None))
    # retranslateUi

