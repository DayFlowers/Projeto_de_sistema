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

import filmedois

class Ui_tela_filme_2(object):
    def setupUi(self, tela_filme_2):
        if not tela_filme_2.objectName():
            tela_filme_2.setObjectName(u"tela_filme_2")
        tela_filme_2.resize(1157, 667)
        self.centralwidget = QWidget(tela_filme_2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 20, 1101, 591))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"font: 900 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.inicial_2 = QFrame(self.frame)
        self.inicial_2.setObjectName(u"inicial_2")
        self.inicial_2.setGeometry(QRect(0, 0, 1101, 51))
        self.inicial_2.setStyleSheet(u"background-color: rgb(34, 31, 31);")
        self.inicial_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.inicial_2.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_Cine_filme_2 = QLabel(self.inicial_2)
        self.btn_Cine_filme_2.setObjectName(u"btn_Cine_filme_2")
        self.btn_Cine_filme_2.setGeometry(QRect(10, 10, 161, 41))
        self.btn_Cine_filme_2.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 900 22pt \"Segoe UI\";")
        self.btn_Recomendacao_aleatorio_2 = QPushButton(self.inicial_2)
        self.btn_Recomendacao_aleatorio_2.setObjectName(u"btn_Recomendacao_aleatorio_2")
        self.btn_Recomendacao_aleatorio_2.setGeometry(QRect(430, 20, 171, 24))
        self.btn_Recomendacao_aleatorio_2.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Inicio_2 = QPushButton(self.inicial_2)
        self.btn_Inicio_2.setObjectName(u"btn_Inicio_2")
        self.btn_Inicio_2.setGeometry(QRect(180, 20, 101, 24))
        self.btn_Inicio_2.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(34, 31, 31);")
        self.btn_Filmes_Series_2 = QPushButton(self.inicial_2)
        self.btn_Filmes_Series_2.setObjectName(u"btn_Filmes_Series_2")
        self.btn_Filmes_Series_2.setGeometry(QRect(300, 20, 101, 24))
        self.btn_Filmes_Series_2.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(34, 31, 31);")
        self.btn_icon_perfil = QLabel(self.inicial_2)
        self.btn_icon_perfil.setObjectName(u"btn_icon_perfil")
        self.btn_icon_perfil.setGeometry(QRect(1060, 10, 31, 31))
        self.btn_icon_perfil.setPixmap(QPixmap(u":/perfil/icon_perfil.png"))
        self.btn_icon_perfil.setScaledContents(True)
        self.inicial_3 = QFrame(self.inicial_2)
        self.inicial_3.setObjectName(u"inicial_3")
        self.inicial_3.setGeometry(QRect(830, 50, 1101, 51))
        self.inicial_3.setStyleSheet(u"background-color: rgb(34, 31, 31);")
        self.inicial_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.inicial_3.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_Cine_filme_3 = QLabel(self.inicial_3)
        self.btn_Cine_filme_3.setObjectName(u"btn_Cine_filme_3")
        self.btn_Cine_filme_3.setGeometry(QRect(10, 10, 161, 41))
        self.btn_Cine_filme_3.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 900 22pt \"Segoe UI\";")
        self.btn_Recomendacao_aleatorio_3 = QPushButton(self.inicial_3)
        self.btn_Recomendacao_aleatorio_3.setObjectName(u"btn_Recomendacao_aleatorio_3")
        self.btn_Recomendacao_aleatorio_3.setGeometry(QRect(430, 20, 171, 24))
        self.btn_Recomendacao_aleatorio_3.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Inicio_3 = QPushButton(self.inicial_3)
        self.btn_Inicio_3.setObjectName(u"btn_Inicio_3")
        self.btn_Inicio_3.setGeometry(QRect(180, 20, 101, 24))
        self.btn_Inicio_3.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(34, 31, 31);")
        self.btn_Filmes_Series_3 = QPushButton(self.inicial_3)
        self.btn_Filmes_Series_3.setObjectName(u"btn_Filmes_Series_3")
        self.btn_Filmes_Series_3.setGeometry(QRect(300, 20, 101, 24))
        self.btn_Filmes_Series_3.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(34, 31, 31);")
        self.btn_icon_perfil_2 = QLabel(self.inicial_3)
        self.btn_icon_perfil_2.setObjectName(u"btn_icon_perfil_2")
        self.btn_icon_perfil_2.setGeometry(QRect(1060, 10, 31, 31))
        self.btn_icon_perfil_2.setPixmap(QPixmap(u":/perfil/icon_perfil.png"))
        self.btn_icon_perfil_2.setScaledContents(True)
        self.inicial_4 = QFrame(self.inicial_2)
        self.inicial_4.setObjectName(u"inicial_4")
        self.inicial_4.setGeometry(QRect(720, 40, 1101, 51))
        self.inicial_4.setStyleSheet(u"background-color: rgb(34, 31, 31);")
        self.inicial_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.inicial_4.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_Cine_filme_4 = QLabel(self.inicial_4)
        self.btn_Cine_filme_4.setObjectName(u"btn_Cine_filme_4")
        self.btn_Cine_filme_4.setGeometry(QRect(10, 10, 161, 41))
        self.btn_Cine_filme_4.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 900 22pt \"Segoe UI\";")
        self.btn_Recomendacao_aleatorio_4 = QPushButton(self.inicial_4)
        self.btn_Recomendacao_aleatorio_4.setObjectName(u"btn_Recomendacao_aleatorio_4")
        self.btn_Recomendacao_aleatorio_4.setGeometry(QRect(430, 20, 171, 24))
        self.btn_Recomendacao_aleatorio_4.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Inicio_4 = QPushButton(self.inicial_4)
        self.btn_Inicio_4.setObjectName(u"btn_Inicio_4")
        self.btn_Inicio_4.setGeometry(QRect(180, 20, 101, 24))
        self.btn_Inicio_4.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(34, 31, 31);")
        self.btn_Filmes_Series_4 = QPushButton(self.inicial_4)
        self.btn_Filmes_Series_4.setObjectName(u"btn_Filmes_Series_4")
        self.btn_Filmes_Series_4.setGeometry(QRect(300, 20, 101, 24))
        self.btn_Filmes_Series_4.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(34, 31, 31);")
        self.btn_icon_perfil_3 = QLabel(self.inicial_4)
        self.btn_icon_perfil_3.setObjectName(u"btn_icon_perfil_3")
        self.btn_icon_perfil_3.setGeometry(QRect(1060, 10, 31, 31))
        self.btn_icon_perfil_3.setPixmap(QPixmap(u":/perfil/icon_perfil.png"))
        self.btn_icon_perfil_3.setScaledContents(True)
        self.inicial_5 = QFrame(self.inicial_4)
        self.inicial_5.setObjectName(u"inicial_5")
        self.inicial_5.setGeometry(QRect(0, 0, 1101, 51))
        self.inicial_5.setStyleSheet(u"background-color: rgb(34, 31, 31);")
        self.inicial_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.inicial_5.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_Cine_filme_5 = QLabel(self.inicial_5)
        self.btn_Cine_filme_5.setObjectName(u"btn_Cine_filme_5")
        self.btn_Cine_filme_5.setGeometry(QRect(10, 10, 161, 41))
        self.btn_Cine_filme_5.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 900 22pt \"Segoe UI\";")
        self.btn_Recomendacao_aleatorio_5 = QPushButton(self.inicial_5)
        self.btn_Recomendacao_aleatorio_5.setObjectName(u"btn_Recomendacao_aleatorio_5")
        self.btn_Recomendacao_aleatorio_5.setGeometry(QRect(430, 20, 171, 24))
        self.btn_Recomendacao_aleatorio_5.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Inicio_5 = QPushButton(self.inicial_5)
        self.btn_Inicio_5.setObjectName(u"btn_Inicio_5")
        self.btn_Inicio_5.setGeometry(QRect(180, 20, 101, 24))
        self.btn_Inicio_5.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(34, 31, 31);")
        self.btn_Filmes_Series_5 = QPushButton(self.inicial_5)
        self.btn_Filmes_Series_5.setObjectName(u"btn_Filmes_Series_5")
        self.btn_Filmes_Series_5.setGeometry(QRect(300, 20, 101, 24))
        self.btn_Filmes_Series_5.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(34, 31, 31);")
        self.btn_icon_perfil_4 = QLabel(self.inicial_5)
        self.btn_icon_perfil_4.setObjectName(u"btn_icon_perfil_4")
        self.btn_icon_perfil_4.setGeometry(QRect(1060, 10, 31, 31))
        self.btn_icon_perfil_4.setPixmap(QPixmap(u":/perfil/icon_perfil.png"))
        self.btn_icon_perfil_4.setScaledContents(True)
        self.img_Ainda_Estou_Aqui = QLabel(self.frame)
        self.img_Ainda_Estou_Aqui.setObjectName(u"img_Ainda_Estou_Aqui")
        self.img_Ainda_Estou_Aqui.setGeometry(QRect(10, 70, 81, 121))
        self.img_Ainda_Estou_Aqui.setPixmap(QPixmap(u":/icon 1/Ainda_Estou_Aqui.jpg"))
        self.img_Ainda_Estou_Aqui.setScaledContents(True)
        self.txt_Ainda_Estou_Aqui = QLabel(self.frame)
        self.txt_Ainda_Estou_Aqui.setObjectName(u"txt_Ainda_Estou_Aqui")
        self.txt_Ainda_Estou_Aqui.setGeometry(QRect(110, 70, 101, 21))
        self.txt_Ainda_Estou_Aqui.setStyleSheet(u"font: 900 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.txt_7_de_Novembro_2024 = QLabel(self.frame)
        self.txt_7_de_Novembro_2024.setObjectName(u"txt_7_de_Novembro_2024")
        self.txt_7_de_Novembro_2024.setGeometry(QRect(110, 90, 351, 21))
        self.txt_7_de_Novembro_2024.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 9pt \"Segoe UI\";")
        self.txt_Direcao_Walter_SallesRoteiro_Murilo_Hauser = QLabel(self.frame)
        self.txt_Direcao_Walter_SallesRoteiro_Murilo_Hauser.setObjectName(u"txt_Direcao_Walter_SallesRoteiro_Murilo_Hauser")
        self.txt_Direcao_Walter_SallesRoteiro_Murilo_Hauser.setGeometry(QRect(110, 110, 371, 31))
        self.txt_Elenco_Fernanda_Torres = QLabel(self.frame)
        self.txt_Elenco_Fernanda_Torres.setObjectName(u"txt_Elenco_Fernanda_Torres")
        self.txt_Elenco_Fernanda_Torres.setGeometry(QRect(110, 140, 371, 16))
        self.txt_Sinopse_Ainda_Estou_aqui = QTextBrowser(self.frame)
        self.txt_Sinopse_Ainda_Estou_aqui.setObjectName(u"txt_Sinopse_Ainda_Estou_aqui")
        self.txt_Sinopse_Ainda_Estou_aqui.setGeometry(QRect(10, 200, 551, 81))
        self.img_Vingadores_Ultimato = QLabel(self.frame)
        self.img_Vingadores_Ultimato.setObjectName(u"img_Vingadores_Ultimato")
        self.img_Vingadores_Ultimato.setGeometry(QRect(560, 70, 81, 121))
        self.img_Vingadores_Ultimato.setPixmap(QPixmap(u":/icon 2/avengers.jpg"))
        self.img_Vingadores_Ultimato.setScaledContents(True)
        self.txt_Vingadores_Ultimato = QLabel(self.frame)
        self.txt_Vingadores_Ultimato.setObjectName(u"txt_Vingadores_Ultimato")
        self.txt_Vingadores_Ultimato.setGeometry(QRect(660, 70, 131, 16))
        self.txt_25_de_Abril_2019 = QLabel(self.frame)
        self.txt_25_de_Abril_2019.setObjectName(u"txt_25_de_Abril_2019")
        self.txt_25_de_Abril_2019.setGeometry(QRect(660, 90, 411, 16))
        self.txt_Direcao_Joe_Russo = QLabel(self.frame)
        self.txt_Direcao_Joe_Russo.setObjectName(u"txt_Direcao_Joe_Russo")
        self.txt_Direcao_Joe_Russo.setGeometry(QRect(660, 110, 401, 21))
        self.txt_Elenco_Robert_Downey_Jr = QLabel(self.frame)
        self.txt_Elenco_Robert_Downey_Jr.setObjectName(u"txt_Elenco_Robert_Downey_Jr")
        self.txt_Elenco_Robert_Downey_Jr.setGeometry(QRect(660, 130, 311, 31))
        self.txt_Sinopse_Vingadores_Ultimato = QTextBrowser(self.frame)
        self.txt_Sinopse_Vingadores_Ultimato.setObjectName(u"txt_Sinopse_Vingadores_Ultimato")
        self.txt_Sinopse_Vingadores_Ultimato.setGeometry(QRect(560, 200, 541, 81))
        self.img_Diverdida_mente_2 = QLabel(self.frame)
        self.img_Diverdida_mente_2.setObjectName(u"img_Diverdida_mente_2")
        self.img_Diverdida_mente_2.setGeometry(QRect(10, 300, 71, 111))
        self.img_Diverdida_mente_2.setPixmap(QPixmap(u":/icon 3/disney.jpeg"))
        self.img_Diverdida_mente_2.setScaledContents(True)
        self.txt_Diverdida_mente_2 = QLabel(self.frame)
        self.txt_Diverdida_mente_2.setObjectName(u"txt_Diverdida_mente_2")
        self.txt_Diverdida_mente_2.setGeometry(QRect(90, 300, 111, 16))
        self.txt_20_de_Junho_de_2024_1h_36_minutos_Animacao_Comedia = QLabel(self.frame)
        self.txt_20_de_Junho_de_2024_1h_36_minutos_Animacao_Comedia.setObjectName(u"txt_20_de_Junho_de_2024_1h_36_minutos_Animacao_Comedia")
        self.txt_20_de_Junho_de_2024_1h_36_minutos_Animacao_Comedia.setGeometry(QRect(90, 320, 351, 20))
        self.txt_Direcao_Kelsey_Man_Roteiro_Meg_LevFauve_Dave_Holstein = QLabel(self.frame)
        self.txt_Direcao_Kelsey_Man_Roteiro_Meg_LevFauve_Dave_Holstein.setObjectName(u"txt_Direcao_Kelsey_Man_Roteiro_Meg_LevFauve_Dave_Holstein")
        self.txt_Direcao_Kelsey_Man_Roteiro_Meg_LevFauve_Dave_Holstein.setGeometry(QRect(90, 340, 351, 16))
        self.txt_Elenco_Mia_Mello_Amy_Poehler_Isabella_Guarnieri = QLabel(self.frame)
        self.txt_Elenco_Mia_Mello_Amy_Poehler_Isabella_Guarnieri.setObjectName(u"txt_Elenco_Mia_Mello_Amy_Poehler_Isabella_Guarnieri")
        self.txt_Elenco_Mia_Mello_Amy_Poehler_Isabella_Guarnieri.setGeometry(QRect(90, 360, 301, 16))
        self.txt_Sinopse_Diverdida_Mente_2 = QTextBrowser(self.frame)
        self.txt_Sinopse_Diverdida_Mente_2.setObjectName(u"txt_Sinopse_Diverdida_Mente_2")
        self.txt_Sinopse_Diverdida_Mente_2.setGeometry(QRect(10, 420, 541, 81))
        self.img_Duna_2 = QLabel(self.frame)
        self.img_Duna_2.setObjectName(u"img_Duna_2")
        self.img_Duna_2.setGeometry(QRect(570, 290, 71, 111))
        self.img_Duna_2.setPixmap(QPixmap(u":/icon 4/duna 2.webp"))
        self.img_Duna_2.setScaledContents(True)
        self.txt_Duna_parte2 = QLabel(self.frame)
        self.txt_Duna_parte2.setObjectName(u"txt_Duna_parte2")
        self.txt_Duna_parte2.setGeometry(QRect(650, 290, 91, 16))
        self.txt_29_de_Fevereiro_de_2024_2h_46mintos_Drama_Ficcao_Cientifica = QLabel(self.frame)
        self.txt_29_de_Fevereiro_de_2024_2h_46mintos_Drama_Ficcao_Cientifica.setObjectName(u"txt_29_de_Fevereiro_de_2024_2h_46mintos_Drama_Ficcao_Cientifica")
        self.txt_29_de_Fevereiro_de_2024_2h_46mintos_Drama_Ficcao_Cientifica.setGeometry(QRect(650, 310, 391, 31))
        self.txt_Direcao_Dennis_Villeneuve_Roteiro_Denis_Vileneuve_Jon_Spaihts = QLabel(self.frame)
        self.txt_Direcao_Dennis_Villeneuve_Roteiro_Denis_Vileneuve_Jon_Spaihts.setObjectName(u"txt_Direcao_Dennis_Villeneuve_Roteiro_Denis_Vileneuve_Jon_Spaihts")
        self.txt_Direcao_Dennis_Villeneuve_Roteiro_Denis_Vileneuve_Jon_Spaihts.setGeometry(QRect(650, 340, 391, 21))
        self.txt_Elenco_Timothee_Chalamet_Zendeya_Rebecca_Ferguson = QLabel(self.frame)
        self.txt_Elenco_Timothee_Chalamet_Zendeya_Rebecca_Ferguson.setObjectName(u"txt_Elenco_Timothee_Chalamet_Zendeya_Rebecca_Ferguson")
        self.txt_Elenco_Timothee_Chalamet_Zendeya_Rebecca_Ferguson.setGeometry(QRect(650, 360, 331, 31))
        self.txt_Sinopse_Diverdida_Mente_3 = QTextBrowser(self.frame)
        self.txt_Sinopse_Diverdida_Mente_3.setObjectName(u"txt_Sinopse_Diverdida_Mente_3")
        self.txt_Sinopse_Diverdida_Mente_3.setGeometry(QRect(550, 420, 541, 81))
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(390, 530, 41, 24))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(440, 530, 41, 24))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(490, 530, 41, 24))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(540, 530, 41, 24))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(590, 530, 41, 24))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        tela_filme_2.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(tela_filme_2)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1157, 22))
        tela_filme_2.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(tela_filme_2)
        self.statusbar.setObjectName(u"statusbar")
        tela_filme_2.setStatusBar(self.statusbar)

        self.retranslateUi(tela_filme_2)

        QMetaObject.connectSlotsByName(tela_filme_2)
    # setupUi

    def retranslateUi(self, tela_filme_2):
        tela_filme_2.setWindowTitle(QCoreApplication.translate("tela_filme_2", u"MainWindow", None))
        self.btn_Cine_filme_2.setText(QCoreApplication.translate("tela_filme_2", u"CineFilmes", None))
        self.btn_Recomendacao_aleatorio_2.setText(QCoreApplication.translate("tela_filme_2", u"Recomenda\u00e7\u00e3o aleat\u00f3rio", None))
        self.btn_Inicio_2.setText(QCoreApplication.translate("tela_filme_2", u"Inicio", None))
        self.btn_Filmes_Series_2.setText(QCoreApplication.translate("tela_filme_2", u"Filmes e S\u00e9ries", None))
        self.btn_icon_perfil.setText("")
        self.btn_Cine_filme_3.setText(QCoreApplication.translate("tela_filme_2", u"CineFilmes", None))
        self.btn_Recomendacao_aleatorio_3.setText(QCoreApplication.translate("tela_filme_2", u"Recomenda\u00e7\u00e3o aleat\u00f3rio", None))
        self.btn_Inicio_3.setText(QCoreApplication.translate("tela_filme_2", u"Inicio", None))
        self.btn_Filmes_Series_3.setText(QCoreApplication.translate("tela_filme_2", u"Filmes e S\u00e9ries", None))
        self.btn_icon_perfil_2.setText("")
        self.btn_Cine_filme_4.setText(QCoreApplication.translate("tela_filme_2", u"CineFilmes", None))
        self.btn_Recomendacao_aleatorio_4.setText(QCoreApplication.translate("tela_filme_2", u"Recomenda\u00e7\u00e3o aleat\u00f3rio", None))
        self.btn_Inicio_4.setText(QCoreApplication.translate("tela_filme_2", u"Inicio", None))
        self.btn_Filmes_Series_4.setText(QCoreApplication.translate("tela_filme_2", u"Filmes e S\u00e9ries", None))
        self.btn_icon_perfil_3.setText("")
        self.btn_Cine_filme_5.setText(QCoreApplication.translate("tela_filme_2", u"CineFilmes", None))
        self.btn_Recomendacao_aleatorio_5.setText(QCoreApplication.translate("tela_filme_2", u"Recomenda\u00e7\u00e3o aleat\u00f3rio", None))
        self.btn_Inicio_5.setText(QCoreApplication.translate("tela_filme_2", u"Inicio", None))
        self.btn_Filmes_Series_5.setText(QCoreApplication.translate("tela_filme_2", u"Filmes e S\u00e9ries", None))
        self.btn_icon_perfil_4.setText("")
        self.img_Ainda_Estou_Aqui.setText("")
        self.txt_Ainda_Estou_Aqui.setText(QCoreApplication.translate("tela_filme_2", u"Ainda Estou Aqui", None))
        self.txt_7_de_Novembro_2024.setText(QCoreApplication.translate("tela_filme_2", u" 7 de Novembro de 2024 I 2h 15 minutos I Drama, Suspense", None))
        self.txt_Direcao_Walter_SallesRoteiro_Murilo_Hauser.setText(QCoreApplication.translate("tela_filme_2", u"Dire\u00e7\u00e3o: Walter Salles I Roteiro: Murilo Hauser, Heitor Lorenga", None))
        self.txt_Elenco_Fernanda_Torres.setText(QCoreApplication.translate("tela_filme_2", u"Elenco: Fernanda Torres, Fernanda Montenegro,  Selton Mello", None))
        self.txt_Sinopse_Ainda_Estou_aqui.setHtml(QCoreApplication.translate("tela_filme_2", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:900; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Sinopse:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">O filme Ainda Estou Aqui\u00a0conta a hist\u00f3ria de Eunice Paiva, que lutou por d\u00e9cadas para saber o paradeiro do marido, morto pela ditadura militar bra"
                        "sileira.\u00a0O filme \u00e9 baseado no livro hom\u00f4nimo de Marcelo Rubens Paiva, filho de Eunice e Rubens Paiva.\u00a0</span></p></body></html>", None))
        self.img_Vingadores_Ultimato.setText("")
        self.txt_Vingadores_Ultimato.setText(QCoreApplication.translate("tela_filme_2", u"Vingadores: Ultimato", None))
        self.txt_25_de_Abril_2019.setText(QCoreApplication.translate("tela_filme_2", u"25 de Abril de 2019 I 3h 01 minutos I Aventura, A\u00e7\u00e3o, Fic\u00e7\u00e3o Cient\u00edfica", None))
        self.txt_Direcao_Joe_Russo.setText(QCoreApplication.translate("tela_filme_2", u"Dire\u00e7\u00e3o: Joe Russo I Roteiro: Chistopher Markus, Stephen McFeely", None))
        self.txt_Elenco_Robert_Downey_Jr.setText(QCoreApplication.translate("tela_filme_2", u"Elenco:Robert Downey Jr, Chris Evans,Mark Ruffalo", None))
        self.txt_Sinopse_Vingadores_Ultimato.setHtml(QCoreApplication.translate("tela_filme_2", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:900; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Sinopse:<br />Ap\u00f3s Thanos eliminar metade das criaturas vivas, os Vingadores t\u00eam de lidar com a perda de amigos e entes queridos. Com Tony Stark vagando perdido no espa\u00e7o sem \u00e1gua e comida, Steve Rogers e Natasha Romanov lideram a resist\u00eancia contra o tit\u00e3 louco.</span></p></body></html>", None))
        self.img_Diverdida_mente_2.setText("")
        self.txt_Diverdida_mente_2.setText(QCoreApplication.translate("tela_filme_2", u"Diverdida Mente 2", None))
        self.txt_20_de_Junho_de_2024_1h_36_minutos_Animacao_Comedia.setText(QCoreApplication.translate("tela_filme_2", u"20 de Junho de 2024 I 1h 36 Minutos I Anima\u00e7\u00e3o, Com\u00e9dia", None))
        self.txt_Direcao_Kelsey_Man_Roteiro_Meg_LevFauve_Dave_Holstein.setText(QCoreApplication.translate("tela_filme_2", u"Dire\u00e7\u00e3o: Kelsey Man I Roteiro: Meg LeFauve, Dave Holstein", None))
        self.txt_Elenco_Mia_Mello_Amy_Poehler_Isabella_Guarnieri.setText(QCoreApplication.translate("tela_filme_2", u"Elenco: Mi\u00e1 Mello, Amy Poehler, Isabella Guarnieri", None))
        self.txt_Sinopse_Diverdida_Mente_2.setHtml(QCoreApplication.translate("tela_filme_2", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:900; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Sinopse:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Com o tempo, Riley cresce e enfrenta a adolesc\u00eancia. A sala de controle tamb\u00e9m se adapta, recebendo novas emo\u00e7\u00f5es. Alegria, Raiva, Medo, Noji"
                        "nho e Tristeza ficam confusas com a chegada desses novos sentimentos.</span></p></body></html>", None))
        self.img_Duna_2.setText("")
        self.txt_Duna_parte2.setText(QCoreApplication.translate("tela_filme_2", u"Duna: Parte 2", None))
        self.txt_29_de_Fevereiro_de_2024_2h_46mintos_Drama_Ficcao_Cientifica.setText(QCoreApplication.translate("tela_filme_2", u"29 de Fevereiro de 2024 I 2h 46 minutos I Drama, Fic\u00e7\u00e3o Cient\u00edfica ", None))
        self.txt_Direcao_Dennis_Villeneuve_Roteiro_Denis_Vileneuve_Jon_Spaihts.setText(QCoreApplication.translate("tela_filme_2", u"Dire\u00e7\u00e3o:Denis Villeneuve I Roteiro: Denis Villeneuve, Jon Spaihts", None))
        self.txt_Elenco_Timothee_Chalamet_Zendeya_Rebecca_Ferguson.setText(QCoreApplication.translate("tela_filme_2", u"Elenco: Timoth\u00e9e Chalamet, Zendaya, Rebecca Ferguson", None))
        self.txt_Sinopse_Diverdida_Mente_3.setHtml(QCoreApplication.translate("tela_filme_2", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:900; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Sinopse:<br />Paul Atreides se une a Chani e aos Fremen enquanto busca vingan\u00e7a contra os conspiradores que destru\u00edram sua fam\u00edlia. Enfrentando uma escolha entre o amor de sua vida e o destino do universo, ele deve evitar um futuro terr\u00edvel que s\u00f3 ele pode prever.</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("tela_filme_2", u"01", None))
        self.pushButton_2.setText(QCoreApplication.translate("tela_filme_2", u"02", None))
        self.pushButton_3.setText(QCoreApplication.translate("tela_filme_2", u"03", None))
        self.pushButton_4.setText(QCoreApplication.translate("tela_filme_2", u"04", None))
        self.pushButton_5.setText(QCoreApplication.translate("tela_filme_2", u"05", None))
    # retranslateUi

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from tela_filme_2 import Ui_tela_filme_2

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_tela_filme_2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())