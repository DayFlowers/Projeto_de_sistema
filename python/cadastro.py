from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QRect)
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QVBoxLayout, QWidget)

# Supondo que cadastrar_usuario esteja no arquivo 'cadastro.py'
from cadastro import cadastrar_usuario

class Ui_tela_Cadastro(object):
    def setupUi(self, tela_Cadastro):
        if not tela_Cadastro.objectName():
            tela_Cadastro.setObjectName(u"tela_Cadastro")
        tela_Cadastro.resize(1115, 509)
        
        self.Cadastro = QWidget(tela_Cadastro)
        self.Cadastro.setObjectName(u"Cadastro")

        # Frame para os campos de cadastro
        self.Cadastrar = QFrame(self.Cadastro)
        self.Cadastrar.setObjectName(u"Cadastrar")
        self.Cadastrar.setGeometry(QRect(60, 10, 981, 441))
        self.Cadastrar.setFrameShape(QFrame.Shape.StyledPanel)
        self.Cadastrar.setFrameShadow(QFrame.Shadow.Raised)

        self.rtn_Cadastro = QLabel(self.Cadastrar)
        self.rtn_Cadastro.setObjectName(u"rtn_Cadastro")
        self.rtn_Cadastro.setGeometry(QRect(0, 0, 981, 441))
        self.rtn_Cadastro.setPixmap(QPixmap(u":/fme/fme.jpg"))
        self.rtn_Cadastro.setScaledContents(True)

        # Frame para o formulário de cadastro
        self.Tela_Cadastro = QFrame(self.Cadastrar)
        self.Tela_Cadastro.setObjectName(u"Tela_Cadastro")
        self.Tela_Cadastro.setGeometry(QRect(330, 30, 341, 391))
        self.Tela_Cadastro.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.Tela_Cadastro.setFrameShape(QFrame.Shape.StyledPanel)
        self.Tela_Cadastro.setFrameShadow(QFrame.Shadow.Raised)

        self.txt_Cadastro = QLabel(self.Tela_Cadastro)
        self.txt_Cadastro.setObjectName(u"txt_Cadastro")
        self.txt_Cadastro.setGeometry(QRect(100, 30, 141, 31))
        self.txt_Cadastro.setStyleSheet(u"color: rgb(255, 0, 0);\nfont: 22pt \"Segoe UI\";")

        self.txt_Nome = QLabel(self.Tela_Cadastro)
        self.txt_Nome.setObjectName(u"txt_Nome")
        self.txt_Nome.setGeometry(QRect(20, 80, 49, 16))
        self.txt_Nome.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.txt_Email = QLabel(self.Tela_Cadastro)
        self.txt_Email.setObjectName(u"txt_Email")
        self.txt_Email.setGeometry(QRect(20, 140, 49, 16))
        self.txt_Email.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.txt_Senha = QLabel(self.Tela_Cadastro)
        self.txt_Senha.setObjectName(u"txt_Senha")
        self.txt_Senha.setGeometry(QRect(20, 200, 49, 16))
        self.txt_Senha.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.btn_Senha = QLineEdit(self.Tela_Cadastro)
        self.btn_Senha.setObjectName(u"btn_Senha")
        self.btn_Senha.setGeometry(QRect(20, 220, 301, 21))
        self.btn_Senha.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_Senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.btn_Email = QLineEdit(self.Tela_Cadastro)
        self.btn_Email.setObjectName(u"btn_Email")
        self.btn_Email.setGeometry(QRect(20, 160, 301, 21))
        self.btn_Email.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.btn_Nome = QLineEdit(self.Tela_Cadastro)
        self.btn_Nome.setObjectName(u"btn_Nome")
        self.btn_Nome.setGeometry(QRect(20, 100, 301, 21))
        self.btn_Nome.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        # Botão de cadastro
        self.btn_Cadastro = QPushButton(self.Tela_Cadastro)
        self.btn_Cadastro.setObjectName(u"btn_Cadastro")
        self.btn_Cadastro.setGeometry(QRect(80, 290, 171, 31))
        self.btn_Cadastro.setStyleSheet(u"color: rgb(255, 255, 255);\nbackground-color: rgb(255, 0, 0);")

        # Conectando o botão de cadastro à função
        self.btn_Cadastro.clicked.connect(self.cadastrar)

        tela_Cadastro.setCentralWidget(self.Cadastro)
        self.menubar = QMenuBar(tela_Cadastro)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1115, 33))
        tela_Cadastro.setMenuBar(self.menubar)

        self.retranslateUi(tela_Cadastro)

        QMetaObject.connectSlotsByName(tela_Cadastro)

    def retranslateUi(self, tela_Cadastro):
        tela_Cadastro.setWindowTitle(QCoreApplication.translate("tela_Cadastro", u"MainWindow", None))
        self.rtn_Cadastro.setText("")
        self.txt_Cadastro.setText(QCoreApplication.translate("tela_Cadastro", u"Cadastrar", None))
        self.txt_Nome.setText(QCoreApplication.translate("tela_Cadastro", u"Nome", None))
        self.txt_Email.setText(QCoreApplication.translate("tela_Cadastro", u"E-mail", None))
        self.txt_Senha.setText(QCoreApplication.translate("tela_Cadastro", u"Senha", None))
        self.btn_Cadastro.setText(QCoreApplication.translate("tela_Cadastro", u"Cadastrar", None))

    # Função chamada ao clicar no botão de cadastro
    def cadastrar(self):
        nome = self.btn_Nome.text()
        email = self.btn_Email.text()
        senha = self.btn_Senha.text()
        cadastrar_usuario(nome, email, senha)

# Código principal
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from cadastro import Ui_tela_Cadastro

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()  
    ui = Ui_tela_Cadastro()  
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())