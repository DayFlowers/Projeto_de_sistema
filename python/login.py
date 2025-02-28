
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import fme

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(1115, 509)
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
        self.lineEdit = QLineEdit(self.rtn_login)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 200, 291, 21))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
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
        self.txt_Cadastrase = QLabel(self.rtn_login)
        self.txt_Cadastrase.setObjectName(u"txt_Cadastrase")
        self.txt_Cadastrase.setGeometry(QRect(130, 320, 71, 16))
        self.txt_Cadastrase.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.img_foto_fundo.setText("")
        self.lineEdit.setText("")
        self.btn_Entrar.setText(QCoreApplication.translate("login", u"Entrar", None))
        self.txt_login.setText(QCoreApplication.translate("login", u"Login", None))
        self.txt_Email.setText(QCoreApplication.translate("login", u"E-mail", None))
        self.txt_Senha.setText(QCoreApplication.translate("login", u"Senha", None))
        self.txt_Cadastrase.setText(QCoreApplication.translate("login", u"Cadastra-se", None))
    # retranslateUi

import sys
from PySide6.QtWidgets import QApplication, QWidget
from login import Ui_login

class LoginScreen(QWidget):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_login()  
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginScreen()  
    window.show()  
    sys.exit(app.exec())

    