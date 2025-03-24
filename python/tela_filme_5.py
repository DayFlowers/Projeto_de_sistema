from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QWidget)

import filmecinco

class Ui_tela_filme_5(object):
    def setupUi(self, tela_filme_5):
        if not tela_filme_5.objectName():
            tela_filme_5.setObjectName(u"tela_filme_5")
        tela_filme_5.resize(1120, 596)
        self.tela_filme_05 = QWidget(tela_filme_5)
        self.tela_filme_05.setObjectName(u"tela_filme_05")
        self.frame = QFrame(self.tela_filme_05)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 10, 1071, 531))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"font: 900 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.inicial = QFrame(self.frame)
        self.inicial.setObjectName(u"inicial")
        self.inicial.setGeometry(QRect(-10, 0, 1141, 51))
        self.inicial.setStyleSheet(u"background-color: rgb(34, 31, 31);")
        self.inicial.setFrameShape(QFrame.Shape.StyledPanel)
        self.inicial.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_Cine_filme = QLabel(self.inicial)
        self.btn_Cine_filme.setObjectName(u"btn_Cine_filme")
        self.btn_Cine_filme.setGeometry(QRect(20, 10, 161, 41))
        self.btn_Cine_filme.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 900 22pt \"Segoe UI\";")
        self.btn_Recomendacao_aleatorio_8 = QPushButton(self.inicial)
        self.btn_Recomendacao_aleatorio_8.setObjectName(u"btn_Recomendacao_aleatorio_8")
        self.btn_Recomendacao_aleatorio_8.setGeometry(QRect(430, 20, 171, 24))
        self.btn_Recomendacao_aleatorio_8.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Inicio = QPushButton(self.inicial)
        self.btn_Inicio.setObjectName(u"btn_Inicio")
        self.btn_Inicio.setGeometry(QRect(180, 20, 101, 24))
        self.btn_Inicio.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(34, 31, 31);")
        self.btn_Filmes_Series = QPushButton(self.inicial)
        self.btn_Filmes_Series.setObjectName(u"btn_Filmes_Series")
        self.btn_Filmes_Series.setGeometry(QRect(300, 20, 101, 24))
        self.btn_Filmes_Series.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(34, 31, 31);")
        self.btn_Icon_Perfil = QLabel(self.inicial)
        self.btn_Icon_Perfil.setObjectName(u"btn_Icon_Perfil")
        self.btn_Icon_Perfil.setGeometry(QRect(1040, 10, 31, 31))
        self.btn_Icon_Perfil.setPixmap(QPixmap(u":/icon4/icon_perfil.png"))
        self.btn_Icon_Perfil.setScaledContents(True)
        self.img_Pousando_No_Amor = QLabel(self.frame)
        self.img_Pousando_No_Amor.setObjectName(u"img_Pousando_No_Amor")
        self.img_Pousando_No_Amor.setGeometry(QRect(20, 70, 71, 121))
        self.img_Pousando_No_Amor.setPixmap(QPixmap(u":/icon1/pousando no amor.jpg"))
        self.img_Pousando_No_Amor.setScaledContents(True)
        self.img_Shop_For_Killers = QLabel(self.frame)
        self.img_Shop_For_Killers.setObjectName(u"img_Shop_For_Killers")
        self.img_Shop_For_Killers.setGeometry(QRect(20, 300, 71, 101))
        self.img_Shop_For_Killers.setPixmap(QPixmap(u":/icon2/shop for killer.jpeg"))
        self.img_Shop_For_Killers.setScaledContents(True)
        self.img_Duna_Profecia = QLabel(self.frame)
        self.img_Duna_Profecia.setObjectName(u"img_Duna_Profecia")
        self.img_Duna_Profecia.setGeometry(QRect(530, 70, 81, 131))
        self.img_Duna_Profecia.setPixmap(QPixmap(u":/icon 3/duna serie.jpg"))
        self.img_Duna_Profecia.setScaledContents(True)
        self.txt_Pousando_No_Amor = QLabel(self.frame)
        self.txt_Pousando_No_Amor.setObjectName(u"txt_Pousando_No_Amor")
        self.txt_Pousando_No_Amor.setGeometry(QRect(100, 70, 121, 16))
        self.txt_Pousando_No_Amor.setStyleSheet(u"color: rgb(144, 194, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 900 9pt \"Segoe UI\";")
        self.txt_Shop_For_Killers = QLabel(self.frame)
        self.txt_Shop_For_Killers.setObjectName(u"txt_Shop_For_Killers")
        self.txt_Shop_For_Killers.setGeometry(QRect(100, 300, 91, 16))
        self.txt_Shop_For_Killers.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 9pt \"Segoe UI\";")
        self.txt_2019_2020_1h_Romance = QLabel(self.frame)
        self.txt_2019_2020_1h_Romance.setObjectName(u"txt_2019_2020_1h_Romance")
        self.txt_2019_2020_1h_Romance.setGeometry(QRect(100, 90, 161, 16))
        self.txt_2019_2020_1h_Romance.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 9pt \"Segoe UI\";")
        self.txt_Duna_Profecia = QLabel(self.frame)
        self.txt_Duna_Profecia.setObjectName(u"txt_Duna_Profecia")
        self.txt_Duna_Profecia.setGeometry(QRect(630, 70, 91, 16))
        self.txt_Elenco_Ye_Jin_Son_Hyun_Bin_Ji_Hye_Seo = QLabel(self.frame)
        self.txt_Elenco_Ye_Jin_Son_Hyun_Bin_Ji_Hye_Seo.setObjectName(u"txt_Elenco_Ye_Jin_Son_Hyun_Bin_Ji_Hye_Seo")
        self.txt_Elenco_Ye_Jin_Son_Hyun_Bin_Ji_Hye_Seo.setGeometry(QRect(100, 110, 241, 16))
        self.txt_Sinopse_Pousando_No_Amor = QTextBrowser(self.frame)
        self.txt_Sinopse_Pousando_No_Amor.setObjectName(u"txt_Sinopse_Pousando_No_Amor")
        self.txt_Sinopse_Pousando_No_Amor.setGeometry(QRect(10, 200, 481, 81))
        self.txt_Nacionalidade_Coreana = QLabel(self.frame)
        self.txt_Nacionalidade_Coreana.setObjectName(u"txt_Nacionalidade_Coreana")
        self.txt_Nacionalidade_Coreana.setGeometry(QRect(100, 130, 151, 16))
        self.txt_2024_1h_Drama_Suspense_Acao = QLabel(self.frame)
        self.txt_2024_1h_Drama_Suspense_Acao.setObjectName(u"txt_2024_1h_Drama_Suspense_Acao")
        self.txt_2024_1h_Drama_Suspense_Acao.setGeometry(QRect(100, 320, 171, 16))
        self.txt_Elenco_Lee_Dong_Wook_Kim_Hye_Jun_Park_Ji_bin = QLabel(self.frame)
        self.txt_Elenco_Lee_Dong_Wook_Kim_Hye_Jun_Park_Ji_bin.setObjectName(u"txt_Elenco_Lee_Dong_Wook_Kim_Hye_Jun_Park_Ji_bin")
       
       
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from tela_principal import Ui_tela_filme_5

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_tela_filme_5()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())