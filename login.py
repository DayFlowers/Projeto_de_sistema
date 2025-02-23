from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
import foto

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1005, 537)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 30, 901, 441))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.login = QLabel(self.frame)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(-80, 0, 981, 441))
        self.login.setPixmap(QPixmap(u":/icon/filmes.jpg"))
        self.login.setScaledContents(True)
        self.rtn_Tela = QPlainTextEdit(self.frame)
        self.rtn_Tela.setObjectName(u"rtn_Tela")
        self.rtn_Tela.setGeometry(QRect(290, 40, 311, 351))
        self.rtn_Tela.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.txt_Login = QLabel(self.frame)
        self.txt_Login.setObjectName(u"txt_Login")
        self.txt_Login.setGeometry(QRect(410, 50, 81, 31))
        self.txt_Login.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 18pt \"Segoe UI\";")
        self.txt_Email = QLabel(self.frame)
        self.txt_Email.setObjectName(u"txt_Email")
        self.txt_Email.setGeometry(QRect(310, 120, 49, 16))
        self.txt_Email.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.txt_Senha = QLabel(self.frame)
        self.txt_Senha.setObjectName(u"txt_Senha")
        self.txt_Senha.setGeometry(QRect(310, 190, 49, 16))
        self.txt_Senha.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Ema = QLineEdit(self.frame)
        self.btn_Ema.setObjectName(u"btn_Ema")
        self.btn_Ema.setGeometry(QRect(310, 140, 251, 22))
        self.btn_Senha = QLineEdit(self.frame)
        self.btn_Senha.setObjectName(u"btn_Senha")
        self.btn_Senha.setGeometry(QRect(310, 210, 251, 22))
        self.btn_Senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.btn_Entrar = QPushButton(self.frame)
        self.btn_Entrar.setObjectName(u"btn_Entrar")
        self.btn_Entrar.setGeometry(QRect(370, 280, 141, 24))
        self.btn_Entrar.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.txt_Cadastrase = QLabel(self.frame)
        self.txt_Cadastrase.setObjectName(u"txt_Cadastrase")
        self.txt_Cadastrase.setGeometry(QRect(410, 320, 71, 16))
        self.txt_Cadastrase.setStyleSheet(u"color: rgb(255, 0, 0);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.login.setText("")
        self.txt_Login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.txt_Email.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.txt_Senha.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.btn_Senha.setText("")
        self.btn_Entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.txt_Cadastrase.setText(QCoreApplication.translate("MainWindow", u"Cadastrar-se", None))
    # retranslateUi

import login, sys
from login import Ui_MainWindow
 
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())                    
