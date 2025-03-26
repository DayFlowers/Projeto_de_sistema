from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QTextBrowser,
    QWidget)

import cinefilme

class Ui_tela_filme_1(object):
    def setupUi(self, tela_filme_1):
        if not tela_filme_1.objectName():
            tela_filme_1.setObjectName(u"tela_filme_1")
        tela_filme_1.resize(1152, 664)
        self.tela_filme_01 = QWidget(tela_filme_1)
        self.tela_filme_01.setObjectName(u"tela_filme_01")
        self.frame = QFrame(self.tela_filme_01)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 10, 1091, 621))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"font: 900 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.inicial_1 = QFrame(self.frame)
        self.inicial_1.setObjectName(u"inicial_1")
        self.inicial_1.setGeometry(QRect(0, 0, 1101, 51))
        self.inicial_1.setStyleSheet(u"background-color: rgb(34, 31, 31);")
        self.inicial_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.inicial_1.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_Cine_filme = QLabel(self.inicial_1)
        self.btn_Cine_filme.setObjectName(u"btn_Cine_filme")
        self.btn_Cine_filme.setGeometry(QRect(10, 10, 161, 41))
        self.btn_Cine_filme.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 900 22pt \"Segoe UI\";")
        self.btn_icon_perfil = QLabel(self.inicial_1)
        self.btn_icon_perfil.setObjectName(u"btn_icon_perfil")
        self.btn_icon_perfil.setGeometry(QRect(1030, 10, 27, 27))
        self.btn_icon_perfil.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_icon_perfil.setPixmap(QPixmap(u":/icon/icon_perfil.png"))
        self.btn_icon_perfil.setScaledContents(True)
        self.btn_Recomendacao_aleatorio = QPushButton(self.inicial_1)
        self.btn_Recomendacao_aleatorio.setObjectName(u"btn_Recomendacao_aleatorio")
        self.btn_Recomendacao_aleatorio.setGeometry(QRect(430, 20, 171, 24))
        self.btn_Recomendacao_aleatorio.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Inicio = QPushButton(self.inicial_1)
        self.btn_Inicio.setObjectName(u"btn_Inicio")
        self.btn_Inicio.setGeometry(QRect(180, 20, 101, 24))
        self.btn_Inicio.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(34, 31, 31);")
        self.btn_Filmes_Series = QPushButton(self.inicial_1)
        self.btn_Filmes_Series.setObjectName(u"btn_Filmes_Series")
        self.btn_Filmes_Series.setGeometry(QRect(300, 20, 101, 24))
        self.btn_Filmes_Series.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(34, 31, 31);")
        self.btn_Star_wars = QLabel(self.frame)
        self.btn_Star_wars.setObjectName(u"btn_Star_wars")
        self.btn_Star_wars.setGeometry(QRect(10, 80, 81, 111))
        self.btn_Star_wars.setPixmap(QPixmap(u":/icon 1/star wars.webp"))
        self.btn_Star_wars.setScaledContents(True)
        self.txt_Star_Wars_Episodio_IX = QLabel(self.frame)
        self.txt_Star_Wars_Episodio_IX.setObjectName(u"txt_Star_Wars_Episodio_IX")
        self.txt_Star_Wars_Episodio_IX.setGeometry(QRect(100, 80, 141, 16))
        self.txt_Star_Wars_Episodio_IX.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";\n"
"font: 900 9pt \"Segoe UI\";")
        self.txt_19_de_dezembro_2019_2h_22_minutos_Aventura_Ficcao_Cientifica = QLabel(self.frame)
        self.txt_19_de_dezembro_2019_2h_22_minutos_Aventura_Ficcao_Cientifica.setObjectName(u"txt_19_de_dezembro_2019_2h_22_minutos_Aventura_Ficcao_Cientifica")
        self.txt_19_de_dezembro_2019_2h_22_minutos_Aventura_Ficcao_Cientifica.setGeometry(QRect(100, 110, 421, 16))
        self.txt_19_de_dezembro_2019_2h_22_minutos_Aventura_Ficcao_Cientifica.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 9pt \"Segoe UI\";")
        self.txt_Direcao_J_J_Abrams = QLabel(self.frame)
        self.txt_Direcao_J_J_Abrams.setObjectName(u"txt_Direcao_J_J_Abrams")
        self.txt_Direcao_J_J_Abrams.setGeometry(QRect(100, 130, 331, 16))
        self.txt_Direcao_J_J_Abrams.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 9pt \"Segoe UI\";")
        self.txt_Elenco_Daisy_Ridley_John_Boyega = QLabel(self.frame)
        self.txt_Elenco_Daisy_Ridley_John_Boyega.setObjectName(u"txt_Elenco_Daisy_Ridley_John_Boyega")
        self.txt_Elenco_Daisy_Ridley_John_Boyega.setGeometry(QRect(100, 150, 301, 16))
        self.txt_Elenco_Daisy_Ridley_John_Boyega.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 9pt \"Segoe UI\";")
        self.txt_sinopse_Star_wars = QTextBrowser(self.frame)
        self.txt_sinopse_Star_wars.setObjectName(u"txt_sinopse_Star_wars")
        self.txt_sinopse_Star_wars.setGeometry(QRect(10, 200, 451, 81))
        self.btn_Wicked = QLabel(self.frame)
        self.btn_Wicked.setObjectName(u"btn_Wicked")
        self.btn_Wicked.setGeometry(QRect(560, 80, 81, 121))
        self.btn_Wicked.setPixmap(QPixmap(u":/icon 2/btn_img_wicked.png"))
        self.btn_Wicked.setScaledContents(True)
        self.txt_Wicked = QLabel(self.frame)
        self.txt_Wicked.setObjectName(u"txt_Wicked")
        self.txt_Wicked.setGeometry(QRect(660, 80, 49, 16))
        self.txt_Wicked.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 9pt \"Segoe UI\";")
        self.txt_21_de_novembro_de_2024_2h_40_Minutos_Fantasia_Comedia_Musical = QLabel(self.frame)
        self.txt_21_de_novembro_de_2024_2h_40_Minutos_Fantasia_Comedia_Musical.setObjectName(u"txt_21_de_novembro_de_2024_2h_40_Minutos_Fantasia_Comedia_Musical")
        self.txt_21_de_novembro_de_2024_2h_40_Minutos_Fantasia_Comedia_Musical.setGeometry(QRect(660, 110, 391, 16))
        self.txt_Direcao_Jon_M_Chu_Roteiro_Winnie_Holzman_Dana_Fox = QLabel(self.frame)
        self.txt_Direcao_Jon_M_Chu_Roteiro_Winnie_Holzman_Dana_Fox.setObjectName(u"txt_Direcao_Jon_M_Chu_Roteiro_Winnie_Holzman_Dana_Fox")
        self.txt_Direcao_Jon_M_Chu_Roteiro_Winnie_Holzman_Dana_Fox.setGeometry(QRect(660, 130, 351, 16))
        self.txt_Elenco_Cyntia_Erivo_Ariana_Grande_Jonathan_Bailey = QLabel(self.frame)
        self.txt_Elenco_Cyntia_Erivo_Ariana_Grande_Jonathan_Bailey.setObjectName(u"txt_Elenco_Cyntia_Erivo_Ariana_Grande_Jonathan_Bailey")
        self.txt_Elenco_Cyntia_Erivo_Ariana_Grande_Jonathan_Bailey.setGeometry(QRect(660, 150, 331, 16))
        self.txt_Sinopse_Wicked = QTextBrowser(self.frame)
        self.txt_Sinopse_Wicked.setObjectName(u"txt_Sinopse_Wicked")
        self.txt_Sinopse_Wicked.setGeometry(QRect(560, 210, 451, 81))
        self.btn_Flow = QLabel(self.frame)
        self.btn_Flow.setObjectName(u"btn_Flow")
        self.btn_Flow.setGeometry(QRect(10, 310, 71, 111))
        self.btn_Flow.setPixmap(QPixmap(u":/icon 3/flow.webp"))
        self.btn_Flow.setScaledContents(True)
        self.txt_Flow = QLabel(self.frame)
        self.txt_Flow.setObjectName(u"txt_Flow")
        self.txt_Flow.setGeometry(QRect(90, 310, 51, 16))
        self.txt_20_de_fevereiro_2025_1h_25minutos_Aventura_Animacao_Fantasia = QLabel(self.frame)
        self.txt_20_de_fevereiro_2025_1h_25minutos_Aventura_Animacao_Fantasia.setObjectName(u"txt_20_de_fevereiro_2025_1h_25minutos_Aventura_Animacao_Fantasia")
        self.txt_20_de_fevereiro_2025_1h_25minutos_Aventura_Animacao_Fantasia.setGeometry(QRect(90, 330, 401, 41))
        self.txt_Direcao_Gints_Zilbalodis = QLabel(self.frame)
        self.txt_Direcao_Gints_Zilbalodis.setObjectName(u"txt_Direcao_Gints_Zilbalodis")
        self.txt_Direcao_Gints_Zilbalodis.setGeometry(QRect(90, 360, 151, 31))
        self.txt_Roteiro_Gints_Zilbalodis_Matiss_Kaza = QLabel(self.frame)
        self.txt_Roteiro_Gints_Zilbalodis_Matiss_Kaza.setObjectName(u"txt_Roteiro_Gints_Zilbalodis_Matiss_Kaza")
        self.txt_Roteiro_Gints_Zilbalodis_Matiss_Kaza.setGeometry(QRect(90, 390, 241, 16))
        self.txt_Sinopse_Flow = QTextBrowser(self.frame)
        self.txt_Sinopse_Flow.setObjectName(u"txt_Sinopse_Flow")
        self.txt_Sinopse_Flow.setGeometry(QRect(10, 450, 451, 81))
        self.btn_O_Problema_dos_tres_corpos = QLabel(self.frame)
        self.btn_O_Problema_dos_tres_corpos.setObjectName(u"btn_O_Problema_dos_tres_corpos")
        self.btn_O_Problema_dos_tres_corpos.setGeometry(QRect(550, 310, 81, 121))
        self.btn_O_Problema_dos_tres_corpos.setPixmap(QPixmap(u":/icon 4/O_Problema_dos_3_Corpos.webp"))
        self.btn_O_Problema_dos_tres_corpos.setScaledContents(True)
        self.txt_O_Ptoblema_dos_tres_corpos = QLabel(self.frame)
        self.txt_O_Ptoblema_dos_tres_corpos.setObjectName(u"txt_O_Ptoblema_dos_tres_corpos")
        self.txt_O_Ptoblema_dos_tres_corpos.setGeometry(QRect(640, 310, 151, 21))
        self.txt_Desde_2024_60_Minutos_Drama_Ficcao_Cientifca = QLabel(self.frame)
        self.txt_Desde_2024_60_Minutos_Drama_Ficcao_Cientifca.setObjectName(u"txt_Desde_2024_60_Minutos_Drama_Ficcao_Cientifca")
        self.txt_Desde_2024_60_Minutos_Drama_Ficcao_Cientifca.setGeometry(QRect(640, 340, 311, 16))
        self.txt_Criado_por_David_Benioff_D_B_Weiss = QLabel(self.frame)
        self.txt_Criado_por_David_Benioff_D_B_Weiss.setObjectName(u"txt_Criado_por_David_Benioff_D_B_Weiss")
        self.txt_Criado_por_David_Benioff_D_B_Weiss.setGeometry(QRect(640, 360, 231, 16))
        self.txt_Elenco_Jovan_Adepo_Liam_Cunningham_Eiza_Gonzalez = QLabel(self.frame)
        self.txt_Elenco_Jovan_Adepo_Liam_Cunningham_Eiza_Gonzalez.setObjectName(u"txt_Elenco_Jovan_Adepo_Liam_Cunningham_Eiza_Gonzalez")
        self.txt_Elenco_Jovan_Adepo_Liam_Cunningham_Eiza_Gonzalez.setGeometry(QRect(640, 380, 331, 16))
        self.txt_Nacionalidade_EUA = QLabel(self.frame)
        self.txt_Nacionalidade_EUA.setObjectName(u"txt_Nacionalidade_EUA")
        self.txt_Nacionalidade_EUA.setGeometry(QRect(640, 400, 121, 16))
        self.txt_Sinopse_O_Problema_dos_tres_corpos = QTextBrowser(self.frame)
        self.txt_Sinopse_O_Problema_dos_tres_corpos.setObjectName(u"txt_Sinopse_O_Problema_dos_tres_corpos")
        self.txt_Sinopse_O_Problema_dos_tres_corpos.setGeometry(QRect(550, 460, 501, 81))
        self.btn_01 = QPushButton(self.frame)
        self.btn_01.setObjectName(u"btn_01")
        self.btn_01.setGeometry(QRect(370, 570, 41, 24))
        self.btn_01.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn_02 = QPushButton(self.frame)
        self.btn_02.setObjectName(u"btn_02")
        self.btn_02.setGeometry(QRect(420, 570, 41, 24))
        self.btn_02.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn_03 = QPushButton(self.frame)
        self.btn_03.setObjectName(u"btn_03")
        self.btn_03.setGeometry(QRect(470, 570, 41, 24))
        self.btn_03.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn_04 = QPushButton(self.frame)
        self.btn_04.setObjectName(u"btn_04")
        self.btn_04.setGeometry(QRect(520, 570, 41, 24))
        self.btn_04.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn_05 = QPushButton(self.frame)
        self.btn_05.setObjectName(u"btn_05")
        self.btn_05.setGeometry(QRect(570, 570, 41, 24))
        self.btn_05.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        tela_filme_1.setCentralWidget(self.tela_filme_01)
        self.menubar = QMenuBar(tela_filme_1)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1152, 33))
        tela_filme_1.setMenuBar(self.menubar)

        self.retranslateUi(tela_filme_1)

        QMetaObject.connectSlotsByName(tela_filme_1)
    # setupUi

    def retranslateUi(self, tela_filme_1):
        tela_filme_1.setWindowTitle(QCoreApplication.translate("tela_filme_1", u"MainWindow", None))
        self.btn_Cine_filme.setText(QCoreApplication.translate("tela_filme_1", u"CineFilmes", None))
        self.btn_icon_perfil.setText("")
        self.btn_Recomendacao_aleatorio.setText(QCoreApplication.translate("tela_filme_1", u"Recomenda\u00e7\u00e3o aleat\u00f3rio", None))
        self.btn_Inicio.setText(QCoreApplication.translate("tela_filme_1", u"Inicio", None))
        self.btn_Filmes_Series.setText(QCoreApplication.translate("tela_filme_1", u"Filmes e S\u00e9ries", None))
        self.btn_Star_wars.setText("")
        self.txt_Star_Wars_Episodio_IX.setText(QCoreApplication.translate("tela_filme_1", u"Star Wars: Epis\u00f3dio IX", None))
        self.txt_19_de_dezembro_2019_2h_22_minutos_Aventura_Ficcao_Cientifica.setText(QCoreApplication.translate("tela_filme_1", u"19 de Dezembro de 2019  I 2h 22 minutos I Aventura, Fic\u00e7\u00e3o Cientif\u00edca", None))
        self.txt_Direcao_J_J_Abrams.setText(QCoreApplication.translate("tela_filme_1", u"Dire\u00e7\u00e3o: J.J.Abrams I Roteiro: Chris Terrio, J.J.Abrams", None))
        self.txt_Elenco_Daisy_Ridley_John_Boyega.setText(QCoreApplication.translate("tela_filme_1", u"Elenco: Daisy Ridley, John Boyega, Adam Driver", None))
        self.txt_sinopse_Star_wars.setHtml(QCoreApplication.translate("tela_filme_1", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:900; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Sinopse:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Com o retorno do Imperador Palpatine, a Resist\u00eancia toma a frente da batalha. Treinando para ser uma completa Jedi, Rey se encontra em conflito com passado "
                        "e futuro, e teme pelas respostas que pode conseguir com Kylo Ren.</span></p></body></html>", None))
        self.btn_Wicked.setText("")
        self.txt_Wicked.setText(QCoreApplication.translate("tela_filme_1", u"Wicked", None))
        self.txt_21_de_novembro_de_2024_2h_40_Minutos_Fantasia_Comedia_Musical.setText(QCoreApplication.translate("tela_filme_1", u"21 de novembro de 2024 | 2h 40min | Fantasia, Com\u00e9dia Musical", None))
        self.txt_Direcao_Jon_M_Chu_Roteiro_Winnie_Holzman_Dana_Fox.setText(QCoreApplication.translate("tela_filme_1", u"Dire\u00e7\u00e3o: Jon M. Chu | Roteiro Winnie Holzman, Dana Fox", None))
        self.txt_Elenco_Cyntia_Erivo_Ariana_Grande_Jonathan_Bailey.setText(QCoreApplication.translate("tela_filme_1", u"Elenco: Cynthia Erivo, Ariana Grande, Jonathan Bailey", None))
        self.txt_Sinopse_Wicked.setHtml(QCoreApplication.translate("tela_filme_1", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:900; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Sinopse:<br />Na Terra de Oz, uma jovem chamada Elphaba forma uma improv\u00e1vel amizade com uma estudante popular chamada Glinda. Ap\u00f3s um encontro com o M\u00e1gico de Oz, o relacionamento delas logo chega a uma encruzilhada.</span></p></body></html>", None))
        self.btn_Flow.setText("")
        self.txt_Flow.setText(QCoreApplication.translate("tela_filme_1", u"Flow", None))
        self.txt_20_de_fevereiro_2025_1h_25minutos_Aventura_Animacao_Fantasia.setText(QCoreApplication.translate("tela_filme_1", u"20 de fevereiro de 2025 | 1h 25min | Aventura, Anima\u00e7\u00e3o, Fantasia", None))
        self.txt_Direcao_Gints_Zilbalodis.setText(QCoreApplication.translate("tela_filme_1", u"Dire\u00e7\u00e3o: Gints Zilbalodis |", None))
        self.txt_Roteiro_Gints_Zilbalodis_Matiss_Kaza.setText(QCoreApplication.translate("tela_filme_1", u"Roteiro: Gints Zilbalodis, Mat\u012bss Ka\u017ea", None))
        self.txt_Sinopse_Flow.setHtml(QCoreApplication.translate("tela_filme_1", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:900; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Sinopse:<br />Gato \u00e9 um animal solit\u00e1rio, mas quando seu lar \u00e9 devastado por uma grande inunda\u00e7\u00e3o, ele encontra ref\u00fagio em um barco povoado por v\u00e1rias esp\u00e9cies, e tem que se unir a elas apesar de suas diferen\u00e7as.</span></p></body></html>", None))
        self.btn_O_Problema_dos_tres_corpos.setText("")
        self.txt_O_Ptoblema_dos_tres_corpos.setText(QCoreApplication.translate("tela_filme_1", u"O Problema dos 3 corpos", None))
        self.txt_Desde_2024_60_Minutos_Drama_Ficcao_Cientifca.setText(QCoreApplication.translate("tela_filme_1", u"Desde 2024 | 60 minutos | Drama, Fic\u00e7\u00e3o Cient\u00edfica", None))
        self.txt_Criado_por_David_Benioff_D_B_Weiss.setText(QCoreApplication.translate("tela_filme_1", u"Criado por: David Benioff, D.B. Weiss", None))
        self.txt_Elenco_Jovan_Adepo_Liam_Cunningham_Eiza_Gonzalez.setText(QCoreApplication.translate("tela_filme_1", u"Elenco: Jovan Adepo, Liam Cunningham, Eiza Gonzalez", None))
        self.txt_Nacionalidade_EUA.setText(QCoreApplication.translate("tela_filme_1", u"Nacionalidade EUA", None))
        self.txt_Sinopse_O_Problema_dos_tres_corpos.setHtml(QCoreApplication.translate("tela_filme_1", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:900; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Sinopse:<br />China, final dos anos 1960. Enquanto o pa\u00eds inteiro est\u00e1 sendo devastado pela viol\u00eancia da Revolu\u00e7\u00e3o Cultural, um pequeno grupo de astrof\u00edsicos, militares e engenheiros come\u00e7a um projeto ultrassecreto envolvendo ondas sonoras e seres extraterrestres.</span></p></body></html>", None))
        self.btn_01.setText(QCoreApplication.translate("tela_filme_1", u"01", None))
        self.btn_02.setText(QCoreApplication.translate("tela_filme_1", u"02", None))
        self.btn_03.setText(QCoreApplication.translate("tela_filme_1", u"03", None))
        self.btn_04.setText(QCoreApplication.translate("tela_filme_1", u"04", None))
        self.btn_05.setText(QCoreApplication.translate("tela_filme_1", u"05", None))
    # retranslateUi

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from tela_filme_1 import Ui_tela_filme_1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_tela_filme_1()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())