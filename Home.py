from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import foto

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1001, 493)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Home = QFrame(self.centralwidget)
        self.Home.setObjectName(u"Home")
        self.Home.setGeometry(QRect(40, 40, 931, 411))
        self.Home.setFrameShape(QFrame.Shape.StyledPanel)
        self.Home.setFrameShadow(QFrame.Shadow.Raised)
        self.Home_2 = QLabel(self.Home)
        self.Home_2.setObjectName(u"Home_2")
        self.Home_2.setGeometry(QRect(-30, -20, 961, 441))
        self.Home_2.setStyleSheet(u"gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Home_2.setPixmap(QPixmap(u":/icon/filmes.jpg"))
        self.Home_2.setScaledContents(True)
        self.txt_CineFilmes = QLabel(self.Home)
        self.txt_CineFilmes.setObjectName(u"txt_CineFilmes")
        self.txt_CineFilmes.setGeometry(QRect(20, 10, 171, 41))
        self.txt_CineFilmes.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 22pt \"Segoe UI\";\n"
"font: 900 22pt \"Segoe UI\";")
        self.txt_Seu_Guia_de_Filmes_e_Series = QLabel(self.Home)
        self.txt_Seu_Guia_de_Filmes_e_Series.setObjectName(u"txt_Seu_Guia_de_Filmes_e_Series")
        self.txt_Seu_Guia_de_Filmes_e_Series.setGeometry(QRect(10, 120, 381, 51))
        self.txt_Seu_Guia_de_Filmes_e_Series.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 22pt \"Segoe UI\";")
        self.txt_Venha_conferir = QLabel(self.Home)
        self.txt_Venha_conferir.setObjectName(u"txt_Venha_conferir")
        self.txt_Venha_conferir.setGeometry(QRect(20, 170, 131, 16))
        self.txt_Venha_conferir.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 600 12pt \"Segoe UI\";")
        self.btn_Descubra_Filmes_e_Series = QPushButton(self.Home)
        self.btn_Descubra_Filmes_e_Series.setObjectName(u"btn_Descubra_Filmes_e_Series")
        self.btn_Descubra_Filmes_e_Series.setGeometry(QRect(20, 220, 231, 31))
        self.btn_Descubra_Filmes_e_Series.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_Entrar = QPushButton(self.Home)
        self.btn_Entrar.setObjectName(u"btn_Entrar")
        self.btn_Entrar.setGeometry(QRect(830, 20, 75, 24))
        self.btn_Entrar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Home_2.setText("")
        self.txt_CineFilmes.setText(QCoreApplication.translate("MainWindow", u"CineFilmes", None))
        self.txt_Seu_Guia_de_Filmes_e_Series.setText(QCoreApplication.translate("MainWindow", u"Seu Guia de Filmes e S\u00e9ries.", None))
        self.txt_Venha_conferir.setText(QCoreApplication.translate("MainWindow", u"Venha conferir.", None))
        self.btn_Descubra_Filmes_e_Series.setText(QCoreApplication.translate("MainWindow", u"Descubra Filmes e S\u00e9ries", None))
        self.btn_Entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
    # retranslateUi

import Home, sys
from Home import Ui_MainWindow
 
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())                    
