from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)
import foto

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1038, 549)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 10, 951, 481))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.Tela = QLabel(self.frame)
        self.Tela.setObjectName(u"Tela")
        self.Tela.setGeometry(QRect(-50, -10, 1011, 491))
        self.Tela.setPixmap(QPixmap(u":/icon/filmes.jpg"))
        self.Tela.setScaledContents(True)
        self.rtn_Cadastrase = QTextBrowser(self.frame)
        self.rtn_Cadastrase.setObjectName(u"rtn_Cadastrase")
        self.rtn_Cadastrase.setGeometry(QRect(260, 10, 401, 461))
        self.rtn_Cadastrase.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.Cadastrase = QLabel(self.frame)
        self.Cadastrase.setObjectName(u"Cadastrase")
        self.Cadastrase.setGeometry(QRect(380, 40, 191, 31))
        self.Cadastrase.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 22pt \"Segoe UI\";")
        self.txt_Usuario = QLabel(self.frame)
        self.txt_Usuario.setObjectName(u"txt_Usuario")
        self.txt_Usuario.setGeometry(QRect(290, 100, 49, 16))
        self.txt_Usuario.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.txt_Email = QLabel(self.frame)
        self.txt_Email.setObjectName(u"txt_Email")
        self.txt_Email.setGeometry(QRect(290, 160, 49, 16))
        self.txt_Email.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.txt_Senha = QLabel(self.frame)
        self.txt_Senha.setObjectName(u"txt_Senha")
        self.txt_Senha.setGeometry(QRect(290, 210, 49, 16))
        self.txt_Senha.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Usuario = QLineEdit(self.frame)
        self.btn_Usuario.setObjectName(u"btn_Usuario")
        self.btn_Usuario.setGeometry(QRect(290, 120, 311, 22))
        self.btn_Email = QLineEdit(self.frame)
        self.btn_Email.setObjectName(u"btn_Email")
        self.btn_Email.setGeometry(QRect(290, 180, 311, 22))
        self.btn_Senha = QLineEdit(self.frame)
        self.btn_Senha.setObjectName(u"btn_Senha")
        self.btn_Senha.setGeometry(QRect(290, 230, 311, 22))
        self.btn_Senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.txt_Confirmar_senha = QLabel(self.frame)
        self.txt_Confirmar_senha.setObjectName(u"txt_Confirmar_senha")
        self.txt_Confirmar_senha.setGeometry(QRect(290, 270, 101, 16))
        self.txt_Confirmar_senha.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Confirmar_senha = QLineEdit(self.frame)
        self.btn_Confirmar_senha.setObjectName(u"btn_Confirmar_senha")
        self.btn_Confirmar_senha.setGeometry(QRect(290, 290, 311, 22))
        self.btn_Confirmar_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.btn_Cadastrar = QPushButton(self.frame)
        self.btn_Cadastrar.setObjectName(u"btn_Cadastrar")
        self.btn_Cadastrar.setGeometry(QRect(370, 370, 171, 31))
        self.btn_Cadastrar.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1038, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Tela.setText("")
        self.Cadastrase.setText(QCoreApplication.translate("MainWindow", u"Cadastre-se", None))
        self.txt_Usuario.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.txt_Email.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.txt_Senha.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.txt_Confirmar_senha.setText(QCoreApplication.translate("MainWindow", u"Confirmar senha", None))
        self.btn_Confirmar_senha.setText("")
        self.btn_Cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
    # retranslateUi

import cadastrar, sys
from cadastrar import Ui_MainWindow
 
if __name__=="__main__":
    app=QApplication(sys.argv)
    Form = QMainWindow()  
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())