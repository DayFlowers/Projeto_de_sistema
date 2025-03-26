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
        self.frame.setGeometry(QRect(30, 10, 1061, 531))
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
        self.btn_Recomendacao_aleatorio = QPushButton(self.inicial)
        self.btn_Recomendacao_aleatorio.setObjectName(u"btn_Recomendacao_aleatorio")
        self.btn_Recomendacao_aleatorio.setGeometry(QRect(430, 20, 171, 24))
        self.btn_Recomendacao_aleatorio.setStyleSheet(u"color: rgb(255, 0, 0);")
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
        self.btn_Pousando_No_Amor = QLabel(self.frame)
        self.btn_Pousando_No_Amor.setObjectName(u"btn_Pousando_No_Amor")
        self.btn_Pousando_No_Amor.setGeometry(QRect(20, 70, 71, 121))
        self.btn_Pousando_No_Amor.setPixmap(QPixmap(u":/icon1/pousando no amor.jpg"))
        self.btn_Pousando_No_Amor.setScaledContents(True)
        self.img_Shop_For_Killers = QLabel(self.frame)
        self.img_Shop_For_Killers.setObjectName(u"img_Shop_For_Killers")
        self.img_Shop_For_Killers.setGeometry(QRect(20, 300, 71, 101))
        self.img_Shop_For_Killers.setPixmap(QPixmap(u":/icon2/shop for killer.jpeg"))
        self.img_Shop_For_Killers.setScaledContents(True)
        self.btn_Duna_Profecia = QLabel(self.frame)
        self.btn_Duna_Profecia.setObjectName(u"btn_Duna_Profecia")
        self.btn_Duna_Profecia.setGeometry(QRect(530, 70, 81, 131))
        self.btn_Duna_Profecia.setPixmap(QPixmap(u":/icon 3/duna serie.jpg"))
        self.btn_Duna_Profecia.setScaledContents(True)
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
        self.txt_Elenco_Lee_Dong_Wook_Kim_Hye_Jun_Park_Ji_bin.setGeometry(QRect(100, 340, 291, 16))
        self.txt_Nacionalidade_Coreana_2 = QLabel(self.frame)
        self.txt_Nacionalidade_Coreana_2.setObjectName(u"txt_Nacionalidade_Coreana_2")
        self.txt_Nacionalidade_Coreana_2.setGeometry(QRect(100, 360, 151, 16))
        self.txt_Sinopse_Shop_For_Killers = QTextBrowser(self.frame)
        self.txt_Sinopse_Shop_For_Killers.setObjectName(u"txt_Sinopse_Shop_For_Killers")
        self.txt_Sinopse_Shop_For_Killers.setGeometry(QRect(10, 400, 481, 81))
        self.txt_Desde_2024_1h_Ficcao_Cientifica = QLabel(self.frame)
        self.txt_Desde_2024_1h_Ficcao_Cientifica.setObjectName(u"txt_Desde_2024_1h_Ficcao_Cientifica")
        self.txt_Desde_2024_1h_Ficcao_Cientifica.setGeometry(QRect(630, 85, 211, 31))
        self.txt_Elenco_Emily_Watson_Olivia_Williams_Chloe_Lea = QLabel(self.frame)
        self.txt_Elenco_Emily_Watson_Olivia_Williams_Chloe_Lea.setObjectName(u"txt_Elenco_Emily_Watson_Olivia_Williams_Chloe_Lea")
        self.txt_Elenco_Emily_Watson_Olivia_Williams_Chloe_Lea.setGeometry(QRect(630, 110, 441, 31))
        self.txt_Nacionalidade_EUA = QLabel(self.frame)
        self.txt_Nacionalidade_EUA.setObjectName(u"txt_Nacionalidade_EUA")
        self.txt_Nacionalidade_EUA.setGeometry(QRect(630, 140, 121, 16))
        self.txt_Sinopse_Duna_Profecia = QTextBrowser(self.frame)
        self.txt_Sinopse_Duna_Profecia.setObjectName(u"txt_Sinopse_Duna_Profecia")
        self.txt_Sinopse_Duna_Profecia.setGeometry(QRect(530, 220, 491, 101))
        self.btn_01 = QPushButton(self.frame)
        self.btn_01.setObjectName(u"btn_01")
        self.btn_01.setGeometry(QRect(390, 480, 31, 31))
        self.btn_01.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn_02 = QPushButton(self.frame)
        self.btn_02.setObjectName(u"btn_02")
        self.btn_02.setGeometry(QRect(430, 480, 31, 31))
        self.btn_02.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn_03 = QPushButton(self.frame)
        self.btn_03.setObjectName(u"btn_03")
        self.btn_03.setGeometry(QRect(470, 480, 31, 31))
        self.btn_03.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn_04 = QPushButton(self.frame)
        self.btn_04.setObjectName(u"btn_04")
        self.btn_04.setGeometry(QRect(510, 480, 31, 31))
        self.btn_04.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn_05 = QPushButton(self.frame)
        self.btn_05.setObjectName(u"btn_05")
        self.btn_05.setGeometry(QRect(550, 480, 31, 31))
        self.btn_05.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        tela_filme_5.setCentralWidget(self.tela_filme_05)
        self.menubar = QMenuBar(tela_filme_5)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1120, 33))
        tela_filme_5.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(tela_filme_5)
        self.statusbar.setObjectName(u"statusbar")
        tela_filme_5.setStatusBar(self.statusbar)

        self.retranslateUi(tela_filme_5)

        QMetaObject.connectSlotsByName(tela_filme_5)
    # setupUi

    def retranslateUi(self, tela_filme_5):
        tela_filme_5.setWindowTitle(QCoreApplication.translate("tela_filme_5", u"MainWindow", None))
        self.btn_Cine_filme.setText(QCoreApplication.translate("tela_filme_5", u"CineFilmes", None))
        self.btn_Recomendacao_aleatorio.setText(QCoreApplication.translate("tela_filme_5", u"Recomenda\u00e7\u00e3o aleat\u00f3rio", None))
        self.btn_Inicio.setText(QCoreApplication.translate("tela_filme_5", u"Inicio", None))
        self.btn_Filmes_Series.setText(QCoreApplication.translate("tela_filme_5", u"Filmes e S\u00e9ries", None))
        self.btn_Pousando_No_Amor.setText("")
        self.img_Shop_For_Killers.setText("")
        self.btn_Duna_Profecia.setText("")
        self.txt_Pousando_No_Amor.setText(QCoreApplication.translate("tela_filme_5", u"Pousando No Amor", None))
        self.txt_Shop_For_Killers.setText(QCoreApplication.translate("tela_filme_5", u"Shop for Killer", None))
        self.txt_2019_2020_1h_Romance.setText(QCoreApplication.translate("tela_filme_5", u"2019-2020 I 1h I Romance", None))
        self.txt_Duna_Profecia.setText(QCoreApplication.translate("tela_filme_5", u"Duna: Profecia", None))
        self.txt_Elenco_Ye_Jin_Son_Hyun_Bin_Ji_Hye_Seo.setText(QCoreApplication.translate("tela_filme_5", u"Elenco:  Ye-jin Son, Hyun Bin, Ji-hye Seo", None))
        self.txt_Sinopse_Pousando_No_Amor.setHtml(QCoreApplication.translate("tela_filme_5", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:900; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Sinopse:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Um acidente de parapente leva uma herdeira sul-coreana \u00e0 Coreia do Norte. L\u00e1, ela acaba conhecendo um oficial do ex\u00e9rcito, que vai ajud\u00e1-la a"
                        " se esconder.</span><br /></p></body></html>", None))
        self.txt_Nacionalidade_Coreana.setText(QCoreApplication.translate("tela_filme_5", u"Nacionalidade: Coreana", None))
        self.txt_2024_1h_Drama_Suspense_Acao.setText(QCoreApplication.translate("tela_filme_5", u"2024 I 1h I Drama, Suspense", None))
        self.txt_Elenco_Lee_Dong_Wook_Kim_Hye_Jun_Park_Ji_bin.setText(QCoreApplication.translate("tela_filme_5", u"Elenco: Lee Dong Wook, Kim Hye Jun,Park Ji-bin", None))
        self.txt_Nacionalidade_Coreana_2.setText(QCoreApplication.translate("tela_filme_5", u"Nacionalidade: Coreana", None))
        self.txt_Sinopse_Shop_For_Killers.setHtml(QCoreApplication.translate("tela_filme_5", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:900; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Sinopse:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">A hist\u00f3ria gira em torno de Jeong Ji-an, uma jovem cuja vida aparentemente comum muda drasticamente depois que seu tio, Jeong Jin-man, morre inesperadamente"
                        ".</span></p></body></html>", None))
        self.txt_Desde_2024_1h_Ficcao_Cientifica.setText(QCoreApplication.translate("tela_filme_5", u"Desde: 2024 I 1h I Fic\u00e7\u00e3o Cient\u00edfica", None))
        self.txt_Elenco_Emily_Watson_Olivia_Williams_Chloe_Lea.setText(QCoreApplication.translate("tela_filme_5", u"Elenco: Emily Watson, Olivia Williams, Chloe Lea", None))
        self.txt_Nacionalidade_EUA.setText(QCoreApplication.translate("tela_filme_5", u"Nacionalidade: EUA", None))
        self.txt_Sinopse_Duna_Profecia.setHtml(QCoreApplication.translate("tela_filme_5", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:900; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Sinopse:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\"> Se passando 10.000 anos antes dos eventos dos filmes. A hist\u00f3ria ser\u00e1 baseada no livro Sisterhood of Dune, escrito por Brian Herbert e Kevin J. Anders"
                        "on, e segue duas irm\u00e3s Harkonnen enquanto elas combatem for\u00e7as que amea\u00e7am o futuro da humanidade e estabelecem a lend\u00e1ria seita que se tornar\u00e1 conhecida como Bene Gesserit.</span></p></body></html>", None))
        self.btn_01.setText(QCoreApplication.translate("tela_filme_5", u"01", None))
        self.btn_02.setText(QCoreApplication.translate("tela_filme_5", u"02", None))
        self.btn_03.setText(QCoreApplication.translate("tela_filme_5", u"03", None))
        self.btn_04.setText(QCoreApplication.translate("tela_filme_5", u"04", None))
        self.btn_05.setText(QCoreApplication.translate("tela_filme_5", u"05", None))
    # retranslateUi

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from tela_filme_5 import Ui_tela_filme_5

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_tela_filme_5()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

    