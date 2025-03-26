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
        tela_filme_2.resize(1192, 688)
        self.centralwidget = QWidget(tela_filme_2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 10, 1121, 631))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"font: 900 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.inicial_2 = QFrame(self.frame)
        self.inicial_2.setObjectName(u"inicial_2")
        self.inicial_2.setGeometry(QRect(0, 0, 1171, 51))
        self.inicial_2.setStyleSheet(u"background-color: rgb(34, 31, 31);")
        self.inicial_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.inicial_2.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_Cine_filme = QLabel(self.inicial_2)
        self.btn_Cine_filme.setObjectName(u"btn_Cine_filme")
        self.btn_Cine_filme.setGeometry(QRect(10, 10, 161, 41))
        self.btn_Cine_filme.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 900 22pt \"Segoe UI\";")
        self.btn_Recomendacao_aleatorio = QPushButton(self.inicial_2)
        self.btn_Recomendacao_aleatorio.setObjectName(u"btn_Recomendacao_aleatorio")
        self.btn_Recomendacao_aleatorio.setGeometry(QRect(430, 20, 171, 24))
        self.btn_Recomendacao_aleatorio.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Inicio = QPushButton(self.inicial_2)
        self.btn_Inicio.setObjectName(u"btn_Inicio")
        self.btn_Inicio.setGeometry(QRect(180, 20, 101, 24))
        self.btn_Inicio.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(34, 31, 31);")
        self.btn_Filmes_Series = QPushButton(self.inicial_2)
        self.btn_Filmes_Series.setObjectName(u"btn_Filmes_Series")
        self.btn_Filmes_Series.setGeometry(QRect(300, 20, 101, 24))
        self.btn_Filmes_Series.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(34, 31, 31);")
        self.btn_Ainda_Estou_Aqui = QLabel(self.frame)
        self.btn_Ainda_Estou_Aqui.setObjectName(u"btn_Ainda_Estou_Aqui")
        self.btn_Ainda_Estou_Aqui.setGeometry(QRect(10, 70, 81, 131))
        self.btn_Ainda_Estou_Aqui.setPixmap(QPixmap(u":/icon 1/Ainda_Estou_Aqui.jpg"))
        self.btn_Ainda_Estou_Aqui.setScaledContents(True)
        self.txt_Ainda_Estou_Aqui = QLabel(self.frame)
        self.txt_Ainda_Estou_Aqui.setObjectName(u"txt_Ainda_Estou_Aqui")
        self.txt_Ainda_Estou_Aqui.setGeometry(QRect(100, 70, 101, 21))
        self.txt_Ainda_Estou_Aqui.setStyleSheet(u"font: 900 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.txt_7_de_Novembro_2024_3h_15_minutos_Drma_Suspense = QLabel(self.frame)
        self.txt_7_de_Novembro_2024_3h_15_minutos_Drma_Suspense.setObjectName(u"txt_7_de_Novembro_2024_3h_15_minutos_Drma_Suspense")
        self.txt_7_de_Novembro_2024_3h_15_minutos_Drma_Suspense.setGeometry(QRect(100, 100, 351, 21))
        self.txt_7_de_Novembro_2024_3h_15_minutos_Drma_Suspense.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 9pt \"Segoe UI\";")
        self.txt_Direcao_Walter_Salles_Roteiro_Murilo_Hauser_Heitor_Lorenga = QLabel(self.frame)
        self.txt_Direcao_Walter_Salles_Roteiro_Murilo_Hauser_Heitor_Lorenga.setObjectName(u"txt_Direcao_Walter_Salles_Roteiro_Murilo_Hauser_Heitor_Lorenga")
        self.txt_Direcao_Walter_Salles_Roteiro_Murilo_Hauser_Heitor_Lorenga.setGeometry(QRect(100, 120, 371, 31))
        self.txt_Elenco_Fernanda_Torres_Fernanda_Montenegro_Selton_Mello = QLabel(self.frame)
        self.txt_Elenco_Fernanda_Torres_Fernanda_Montenegro_Selton_Mello.setObjectName(u"txt_Elenco_Fernanda_Torres_Fernanda_Montenegro_Selton_Mello")
        self.txt_Elenco_Fernanda_Torres_Fernanda_Montenegro_Selton_Mello.setGeometry(QRect(100, 150, 371, 16))
        self.txt_Sinopse_Ainda_Estou_aqui = QTextBrowser(self.frame)
        self.txt_Sinopse_Ainda_Estou_aqui.setObjectName(u"txt_Sinopse_Ainda_Estou_aqui")
        self.txt_Sinopse_Ainda_Estou_aqui.setGeometry(QRect(10, 200, 481, 81))
        self.btn_Vingadores_Ultimato = QLabel(self.frame)
        self.btn_Vingadores_Ultimato.setObjectName(u"btn_Vingadores_Ultimato")
        self.btn_Vingadores_Ultimato.setGeometry(QRect(550, 70, 91, 131))
        self.btn_Vingadores_Ultimato.setPixmap(QPixmap(u":/icon 2/avengers.jpg"))
        self.btn_Vingadores_Ultimato.setScaledContents(True)
        self.txt_Vingadores_Ultimato = QLabel(self.frame)
        self.txt_Vingadores_Ultimato.setObjectName(u"txt_Vingadores_Ultimato")
        self.txt_Vingadores_Ultimato.setGeometry(QRect(660, 80, 131, 16))
        self.txt_25_de_Abril_2019_3h_01_minutos_Aventura_Acao_Ficcao_Cientifica = QLabel(self.frame)
        self.txt_25_de_Abril_2019_3h_01_minutos_Aventura_Acao_Ficcao_Cientifica.setObjectName(u"txt_25_de_Abril_2019_3h_01_minutos_Aventura_Acao_Ficcao_Cientifica")
        self.txt_25_de_Abril_2019_3h_01_minutos_Aventura_Acao_Ficcao_Cientifica.setGeometry(QRect(660, 110, 411, 16))
        self.txt_Direcao_Joe_Russo_Russo_Roteiro_Chistopher_Markus_Stephen_Mcfeely = QLabel(self.frame)
        self.txt_Direcao_Joe_Russo_Russo_Roteiro_Chistopher_Markus_Stephen_Mcfeely.setObjectName(u"txt_Direcao_Joe_Russo_Russo_Roteiro_Chistopher_Markus_Stephen_Mcfeely")
        self.txt_Direcao_Joe_Russo_Russo_Roteiro_Chistopher_Markus_Stephen_Mcfeely.setGeometry(QRect(660, 130, 401, 21))
        self.txt_Elenco_Robert_Downey_Jr_Chris_Evans_Mark_Ruffalo = QLabel(self.frame)
        self.txt_Elenco_Robert_Downey_Jr_Chris_Evans_Mark_Ruffalo.setObjectName(u"txt_Elenco_Robert_Downey_Jr_Chris_Evans_Mark_Ruffalo")
        self.txt_Elenco_Robert_Downey_Jr_Chris_Evans_Mark_Ruffalo.setGeometry(QRect(660, 150, 311, 31))
        self.txt_Sinopse_Vingadores_Ultimato = QTextBrowser(self.frame)
        self.txt_Sinopse_Vingadores_Ultimato.setObjectName(u"txt_Sinopse_Vingadores_Ultimato")
        self.txt_Sinopse_Vingadores_Ultimato.setGeometry(QRect(550, 200, 491, 81))
        self.btn_Diverdida_mente_2 = QLabel(self.frame)
        self.btn_Diverdida_mente_2.setObjectName(u"btn_Diverdida_mente_2")
        self.btn_Diverdida_mente_2.setGeometry(QRect(10, 330, 71, 111))
        self.btn_Diverdida_mente_2.setPixmap(QPixmap(u":/icon 3/disney.jpeg"))
        self.btn_Diverdida_mente_2.setScaledContents(True)
        self.txt_Diverdida_mente_2 = QLabel(self.frame)
        self.txt_Diverdida_mente_2.setObjectName(u"txt_Diverdida_mente_2")
        self.txt_Diverdida_mente_2.setGeometry(QRect(90, 330, 111, 16))
        self.txt_20_de_Junho_de_2024_1h_36_minutos_Animacao_Comedia = QLabel(self.frame)
        self.txt_20_de_Junho_de_2024_1h_36_minutos_Animacao_Comedia.setObjectName(u"txt_20_de_Junho_de_2024_1h_36_minutos_Animacao_Comedia")
        self.txt_20_de_Junho_de_2024_1h_36_minutos_Animacao_Comedia.setGeometry(QRect(90, 350, 351, 31))
        self.txt_Direcao_Kelsey_Man_Roteiro_Meg_LevFauve_Dave_Holstein = QLabel(self.frame)
        self.txt_Direcao_Kelsey_Man_Roteiro_Meg_LevFauve_Dave_Holstein.setObjectName(u"txt_Direcao_Kelsey_Man_Roteiro_Meg_LevFauve_Dave_Holstein")
        self.txt_Direcao_Kelsey_Man_Roteiro_Meg_LevFauve_Dave_Holstein.setGeometry(QRect(90, 380, 351, 16))
        self.txt_Elenco_Mia_Mello_Amy_Poehler_Isabella_Guarnieri = QLabel(self.frame)
        self.txt_Elenco_Mia_Mello_Amy_Poehler_Isabella_Guarnieri.setObjectName(u"txt_Elenco_Mia_Mello_Amy_Poehler_Isabella_Guarnieri")
        self.txt_Elenco_Mia_Mello_Amy_Poehler_Isabella_Guarnieri.setGeometry(QRect(90, 400, 301, 16))
        self.txt_Sinopse_Diverdida_Mente_2 = QTextBrowser(self.frame)
        self.txt_Sinopse_Diverdida_Mente_2.setObjectName(u"txt_Sinopse_Diverdida_Mente_2")
        self.txt_Sinopse_Diverdida_Mente_2.setGeometry(QRect(10, 450, 501, 81))
        self.btn_Duna_Parte_2 = QLabel(self.frame)
        self.btn_Duna_Parte_2.setObjectName(u"btn_Duna_Parte_2")
        self.btn_Duna_Parte_2.setGeometry(QRect(550, 310, 81, 121))
        self.btn_Duna_Parte_2.setPixmap(QPixmap(u":/icon 4/duna 2.webp"))
        self.btn_Duna_Parte_2.setScaledContents(True)
        self.txt_Duna_parte2 = QLabel(self.frame)
        self.txt_Duna_parte2.setObjectName(u"txt_Duna_parte2")
        self.txt_Duna_parte2.setGeometry(QRect(650, 310, 91, 16))
        self.txt_29_de_Fevereiro_de_2024_2h_46mintos_Drama_Ficcao_Cientifica = QLabel(self.frame)
        self.txt_29_de_Fevereiro_de_2024_2h_46mintos_Drama_Ficcao_Cientifica.setObjectName(u"txt_29_de_Fevereiro_de_2024_2h_46mintos_Drama_Ficcao_Cientifica")
        self.txt_29_de_Fevereiro_de_2024_2h_46mintos_Drama_Ficcao_Cientifica.setGeometry(QRect(650, 330, 391, 31))
        self.txt_Direcao_Dennis_Villeneuve_Roteiro_Denis_Vileneuve_Jon_Spaihts = QLabel(self.frame)
        self.txt_Direcao_Dennis_Villeneuve_Roteiro_Denis_Vileneuve_Jon_Spaihts.setObjectName(u"txt_Direcao_Dennis_Villeneuve_Roteiro_Denis_Vileneuve_Jon_Spaihts")
        self.txt_Direcao_Dennis_Villeneuve_Roteiro_Denis_Vileneuve_Jon_Spaihts.setGeometry(QRect(650, 360, 391, 21))
        self.txt_Elenco_Timothee_Chalamet_Zendeya_Rebecca_Ferguson = QLabel(self.frame)
        self.txt_Elenco_Timothee_Chalamet_Zendeya_Rebecca_Ferguson.setObjectName(u"txt_Elenco_Timothee_Chalamet_Zendeya_Rebecca_Ferguson")
        self.txt_Elenco_Timothee_Chalamet_Zendeya_Rebecca_Ferguson.setGeometry(QRect(650, 380, 331, 31))
        self.txt_Sinopse_Diverdida_Mente_3 = QTextBrowser(self.frame)
        self.txt_Sinopse_Diverdida_Mente_3.setObjectName(u"txt_Sinopse_Diverdida_Mente_3")
        self.txt_Sinopse_Diverdida_Mente_3.setGeometry(QRect(560, 440, 491, 81))
        self.btn_01 = QPushButton(self.frame)
        self.btn_01.setObjectName(u"btn_01")
        self.btn_01.setGeometry(QRect(380, 580, 41, 24))
        self.btn_01.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn_02 = QPushButton(self.frame)
        self.btn_02.setObjectName(u"btn_02")
        self.btn_02.setGeometry(QRect(430, 580, 41, 24))
        self.btn_02.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn_03 = QPushButton(self.frame)
        self.btn_03.setObjectName(u"btn_03")
        self.btn_03.setGeometry(QRect(480, 580, 41, 24))
        self.btn_03.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn_04 = QPushButton(self.frame)
        self.btn_04.setObjectName(u"btn_04")
        self.btn_04.setGeometry(QRect(530, 580, 41, 24))
        self.btn_04.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn_05 = QPushButton(self.frame)
        self.btn_05.setObjectName(u"btn_05")
        self.btn_05.setGeometry(QRect(580, 580, 41, 24))
        self.btn_05.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        tela_filme_2.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(tela_filme_2)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1192, 33))
        tela_filme_2.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(tela_filme_2)
        self.statusbar.setObjectName(u"statusbar")
        tela_filme_2.setStatusBar(self.statusbar)

        self.retranslateUi(tela_filme_2)

        QMetaObject.connectSlotsByName(tela_filme_2)
    # setupUi

    def retranslateUi(self, tela_filme_2):
        tela_filme_2.setWindowTitle(QCoreApplication.translate("tela_filme_2", u"MainWindow", None))
        self.btn_Cine_filme.setText(QCoreApplication.translate("tela_filme_2", u"CineFilmes", None))
        self.btn_Recomendacao_aleatorio.setText(QCoreApplication.translate("tela_filme_2", u"Recomenda\u00e7\u00e3o aleat\u00f3rio", None))
        self.btn_Inicio.setText(QCoreApplication.translate("tela_filme_2", u"Inicio", None))
        self.btn_Filmes_Series.setText(QCoreApplication.translate("tela_filme_2", u"Filmes e S\u00e9ries", None))
        self.btn_Ainda_Estou_Aqui.setText("")
        self.txt_Ainda_Estou_Aqui.setText(QCoreApplication.translate("tela_filme_2", u"Ainda Estou Aqui", None))
        self.txt_7_de_Novembro_2024_3h_15_minutos_Drma_Suspense.setText(QCoreApplication.translate("tela_filme_2", u" 7 de Novembro de 2024 I 2h 15 minutos I Drama, Suspense", None))
        self.txt_Direcao_Walter_Salles_Roteiro_Murilo_Hauser_Heitor_Lorenga.setText(QCoreApplication.translate("tela_filme_2", u"Dire\u00e7\u00e3o: Walter Salles I Roteiro: Murilo Hauser, Heitor Lorenga", None))
        self.txt_Elenco_Fernanda_Torres_Fernanda_Montenegro_Selton_Mello.setText(QCoreApplication.translate("tela_filme_2", u"Elenco: Fernanda Torres, Fernanda Montenegro,  Selton Mello", None))
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
        self.btn_Vingadores_Ultimato.setText("")
        self.txt_Vingadores_Ultimato.setText(QCoreApplication.translate("tela_filme_2", u"Vingadores: Ultimato", None))
        self.txt_25_de_Abril_2019_3h_01_minutos_Aventura_Acao_Ficcao_Cientifica.setText(QCoreApplication.translate("tela_filme_2", u"25 de Abril de 2019 I 3h 01 minutos I Aventura, A\u00e7\u00e3o, Fic\u00e7\u00e3o Cient\u00edfica", None))
        self.txt_Direcao_Joe_Russo_Russo_Roteiro_Chistopher_Markus_Stephen_Mcfeely.setText(QCoreApplication.translate("tela_filme_2", u"Dire\u00e7\u00e3o: Joe Russo I Roteiro: Chistopher Markus, Stephen McFeely", None))
        self.txt_Elenco_Robert_Downey_Jr_Chris_Evans_Mark_Ruffalo.setText(QCoreApplication.translate("tela_filme_2", u"Elenco:Robert Downey Jr, Chris Evans,Mark Ruffalo", None))
        self.txt_Sinopse_Vingadores_Ultimato.setHtml(QCoreApplication.translate("tela_filme_2", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:900; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Sinopse:<br />Ap\u00f3s Thanos eliminar metade das criaturas vivas, os Vingadores t\u00eam de lidar com a perda de amigos e entes queridos. Com Tony Stark vagando perdido no espa\u00e7o sem \u00e1gua e comida, Steve Rogers e Natasha Romanov lideram a resist\u00eancia contra o tit\u00e3 louco.</span></p></body></html>", None))
        self.btn_Diverdida_mente_2.setText("")
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
        self.btn_Duna_Parte_2.setText("")
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
        self.btn_01.setText(QCoreApplication.translate("tela_filme_2", u"01", None))
        self.btn_02.setText(QCoreApplication.translate("tela_filme_2", u"02", None))
        self.btn_03.setText(QCoreApplication.translate("tela_filme_2", u"03", None))
        self.btn_04.setText(QCoreApplication.translate("tela_filme_2", u"04", None))
        self.btn_05.setText(QCoreApplication.translate("tela_filme_2", u"05", None))
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