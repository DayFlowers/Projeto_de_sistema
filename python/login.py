from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import foto

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(944, 504)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 901, 441))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(330, 70, 261, 321))
        self.frame_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 120);\n"
"background-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_Login = QLabel(self.frame_2)
        self.txt_Login.setObjectName(u"txt_Login")
        self.txt_Login.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 18pt \"Segoe UI\";\n"
"background-color: rgba(0, 0, 0, 0);")

        self.verticalLayout.addWidget(self.txt_Login)

        self.txt_Email = QLabel(self.frame_2)
        self.txt_Email.setObjectName(u"txt_Email")
        self.txt_Email.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);color: rgb(255, 0, 0);")

        self.verticalLayout.addWidget(self.txt_Email)

        self.btn_Email = QLineEdit(self.frame_2)
        self.btn_Email.setObjectName(u"btn_Email")
        self.btn_Email.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")

        self.verticalLayout.addWidget(self.btn_Email)

        self.txt_Senha = QLabel(self.frame_2)
        self.txt_Senha.setObjectName(u"txt_Senha")
        self.txt_Senha.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_Senha.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);color: rgb(255, 0, 0);")

        self.verticalLayout.addWidget(self.txt_Senha)

        self.btn_Senha = QLineEdit(self.frame_2)
        self.btn_Senha.setObjectName(u"btn_Senha")
        self.btn_Senha.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Senha.sizePolicy().hasHeightForWidth())
        self.btn_Senha.setSizePolicy(sizePolicy)
        self.btn_Senha.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.btn_Senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.btn_Senha)

        self.btn_Entrar = QPushButton(self.frame_2)
        self.btn_Entrar.setObjectName(u"btn_Entrar")
        self.btn_Entrar.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.btn_Entrar)

        self.txt_Cadastrase = QLabel(self.frame_2)
        self.txt_Cadastrase.setObjectName(u"txt_Cadastrase")
        self.txt_Cadastrase.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.verticalLayout.addWidget(self.txt_Cadastrase)

        self.login = QLabel(self.frame)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(-10, -10, 991, 451))
        self.login.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.login.setPixmap(QPixmap(u":/icon/filmes.jpg"))
        self.login.setScaledContents(True)
        self.login.raise_()
        self.frame_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_Login.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Login</p></body></html>", None))
        self.txt_Email.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.txt_Senha.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.btn_Senha.setText("")
        self.btn_Senha.setPlaceholderText("")
        self.btn_Entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.txt_Cadastrase.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Cadastrar-se</p></body></html>", None))
        self.login.setText("")
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