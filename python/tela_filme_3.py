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

import filmetres

class Ui_tela_filme_3(object):
    def setupUi(self, tela_filme_3):
        if not tela_filme_3.objectName():
            tela_filme_3.setObjectName(u"tela_filme_3")
        tela_filme_3.resize(1178, 675)
        self.tela_filme_03 = QWidget(tela_filme_3)
        self.tela_filme_03.setObjectName(u"tela_filme_03")
        self.frame = QFrame(self.tela_filme_03)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 10, 1101, 621))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"font: 900 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.inicial_6 = QFrame(self.frame)
        self.inicial_6.setObjectName(u"inicial_6")
        self.inicial_6.setGeometry(QRect(0, 0, 1141, 51))
        self.inicial_6.setStyleSheet(u"background-color: rgb(34, 31, 31);")
        self.inicial_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.inicial_6.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_Cine_filme = QLabel(self.inicial_6)
        self.btn_Cine_filme.setObjectName(u"btn_Cine_filme")
        self.btn_Cine_filme.setGeometry(QRect(10, 10, 161, 41))
        self.btn_Cine_filme.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 900 22pt \"Segoe UI\";")
        self.btn_Recomendacao_aleatorio = QPushButton(self.inicial_6)
        self.btn_Recomendacao_aleatorio.setObjectName(u"btn_Recomendacao_aleatorio")
        self.btn_Recomendacao_aleatorio.setGeometry(QRect(430, 20, 171, 24))
        self.btn_Recomendacao_aleatorio.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Inicio = QPushButton(self.inicial_6)
        self.btn_Inicio.setObjectName(u"btn_Inicio")
        self.btn_Inicio.setGeometry(QRect(180, 20, 101, 24))
        self.btn_Inicio.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(34, 31, 31);")
        self.btn_Filmes_Series = QPushButton(self.inicial_6)
        self.btn_Filmes_Series.setObjectName(u"btn_Filmes_Series")
        self.btn_Filmes_Series.setGeometry(QRect(300, 20, 101, 24))
        self.btn_Filmes_Series.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(34, 31, 31);")
        self.btn_John_Wicked_3 = QLabel(self.frame)
        self.btn_John_Wicked_3.setObjectName(u"btn_John_Wicked_3")
        self.btn_John_Wicked_3.setGeometry(QRect(10, 70, 81, 131))
        self.btn_John_Wicked_3.setPixmap(QPixmap(u":/icon 1/John_Wick_3.png"))
        self.btn_John_Wicked_3.setScaledContents(True)
        self.txt_John_Wick_3 = QLabel(self.frame)
        self.txt_John_Wick_3.setObjectName(u"txt_John_Wick_3")
        self.txt_John_Wick_3.setGeometry(QRect(100, 80, 81, 16))
        self.txt_John_Wick_3.setStyleSheet(u"font: 900 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.txt_16_de_Maio_2019_2h_12_minutos_Acao = QLabel(self.frame)
        self.txt_16_de_Maio_2019_2h_12_minutos_Acao.setObjectName(u"txt_16_de_Maio_2019_2h_12_minutos_Acao")
        self.txt_16_de_Maio_2019_2h_12_minutos_Acao.setGeometry(QRect(100, 110, 251, 16))
        self.txt_16_de_Maio_2019_2h_12_minutos_Acao.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 9pt \"Segoe UI\";")
        self.txt_Direcao_Chad_Stahel_Roteiro_Derek_Shay_Hatten = QLabel(self.frame)
        self.txt_Direcao_Chad_Stahel_Roteiro_Derek_Shay_Hatten.setObjectName(u"txt_Direcao_Chad_Stahel_Roteiro_Derek_Shay_Hatten")
        self.txt_Direcao_Chad_Stahel_Roteiro_Derek_Shay_Hatten.setGeometry(QRect(100, 130, 351, 16))
        self.txt_Direcao_Chad_Stahel_Roteiro_Derek_Shay_Hatten.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 9pt \"Segoe UI\";")
        self.txt_Elenco_Keanu_Reeves_Iam_McShanne_Halle_Berry = QLabel(self.frame)
        self.txt_Elenco_Keanu_Reeves_Iam_McShanne_Halle_Berry.setObjectName(u"txt_Elenco_Keanu_Reeves_Iam_McShanne_Halle_Berry")
        self.txt_Elenco_Keanu_Reeves_Iam_McShanne_Halle_Berry.setGeometry(QRect(100, 150, 291, 16))
        self.txt_Elenco_Keanu_Reeves_Iam_McShanne_Halle_Berry.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 9pt \"Segoe UI\";")
        self.txt_Sinopse_John_Wick_3 = QTextBrowser(self.frame)
        self.txt_Sinopse_John_Wick_3.setObjectName(u"txt_Sinopse_John_Wick_3")
        self.txt_Sinopse_John_Wick_3.setGeometry(QRect(20, 220, 371, 81))
        self.img_Single_Seoul = QLabel(self.frame)
        self.img_Single_Seoul.setObjectName(u"img_Single_Seoul")
        self.img_Single_Seoul.setGeometry(QRect(550, 70, 81, 131))
        self.img_Single_Seoul.setPixmap(QPixmap(u":/icon2/Single seul wook.jpg"))
        self.img_Single_Seoul.setScaledContents(True)
        self.txt_Single_Seoul = QLabel(self.frame)
        self.txt_Single_Seoul.setObjectName(u"txt_Single_Seoul")
        self.txt_Single_Seoul.setGeometry(QRect(640, 70, 71, 16))
        self.txt_Single_Seoul.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 9pt \"Segoe UI\";")
        self.txt_29_de_Novembro_de_2023_1h_43_minutos_Romance = QLabel(self.frame)
        self.txt_29_de_Novembro_de_2023_1h_43_minutos_Romance.setObjectName(u"txt_29_de_Novembro_de_2023_1h_43_minutos_Romance")
        self.txt_29_de_Novembro_de_2023_1h_43_minutos_Romance.setGeometry(QRect(640, 100, 311, 16))
        self.txt_Direcao_Park_Beom_Su_Roteiro_Lee_Ji_Min = QLabel(self.frame)
        self.txt_Direcao_Park_Beom_Su_Roteiro_Lee_Ji_Min.setObjectName(u"txt_Direcao_Park_Beom_Su_Roteiro_Lee_Ji_Min")
        self.txt_Direcao_Park_Beom_Su_Roteiro_Lee_Ji_Min.setGeometry(QRect(640, 120, 261, 16))
        self.txt_Elenco_Lee_Dong_Wook_Lee_Su_Jeong_Esom = QLabel(self.frame)
        self.txt_Elenco_Lee_Dong_Wook_Lee_Su_Jeong_Esom.setObjectName(u"txt_Elenco_Lee_Dong_Wook_Lee_Su_Jeong_Esom")
        self.txt_Elenco_Lee_Dong_Wook_Lee_Su_Jeong_Esom.setGeometry(QRect(640, 140, 271, 16))
        self.txt_Sinopse_Single_Seoul = QTextBrowser(self.frame)
        self.txt_Sinopse_Single_Seoul.setObjectName(u"txt_Sinopse_Single_Seoul")
        self.txt_Sinopse_Single_Seoul.setGeometry(QRect(550, 220, 371, 81))
        self.btn_One_Piece_Red = QLabel(self.frame)
        self.btn_One_Piece_Red.setObjectName(u"btn_One_Piece_Red")
        self.btn_One_Piece_Red.setGeometry(QRect(20, 350, 71, 111))
        self.btn_One_Piece_Red.setPixmap(QPixmap(u":/icon3/one piece red.jpg"))
        self.btn_One_Piece_Red.setScaledContents(True)
        self.btn_Ghost_in_the_shell = QLabel(self.frame)
        self.btn_Ghost_in_the_shell.setObjectName(u"btn_Ghost_in_the_shell")
        self.btn_Ghost_in_the_shell.setGeometry(QRect(550, 330, 81, 111))
        self.btn_Ghost_in_the_shell.setPixmap(QPixmap(u":/icon 4/ghost in the shell.jpg"))
        self.btn_Ghost_in_the_shell.setScaledContents(True)
        self.txt_One_Piece_Red = QLabel(self.frame)
        self.txt_One_Piece_Red.setObjectName(u"txt_One_Piece_Red")
        self.txt_One_Piece_Red.setGeometry(QRect(100, 350, 91, 16))
        self.txt_2_de_Novembro_de_2022_1h_55_minutos_Aventura = QLabel(self.frame)
        self.txt_2_de_Novembro_de_2022_1h_55_minutos_Aventura.setObjectName(u"txt_2_de_Novembro_de_2022_1h_55_minutos_Aventura")
        self.txt_2_de_Novembro_de_2022_1h_55_minutos_Aventura.setGeometry(QRect(100, 380, 301, 21))
        self.txt_Direcao_Goro_Tanigushi_Roteiro_Tsutomo_Kuroiwa = QLabel(self.frame)
        self.txt_Direcao_Goro_Tanigushi_Roteiro_Tsutomo_Kuroiwa.setObjectName(u"txt_Direcao_Goro_Tanigushi_Roteiro_Tsutomo_Kuroiwa")
        self.txt_Direcao_Goro_Tanigushi_Roteiro_Tsutomo_Kuroiwa.setGeometry(QRect(100, 400, 321, 31))
        self.txt_Elenco_Mayumi_Tanaka_Kaori_Nazuka_Ikue_Otani = QLabel(self.frame)
        self.txt_Elenco_Mayumi_Tanaka_Kaori_Nazuka_Ikue_Otani.setObjectName(u"txt_Elenco_Mayumi_Tanaka_Kaori_Nazuka_Ikue_Otani")
        self.txt_Elenco_Mayumi_Tanaka_Kaori_Nazuka_Ikue_Otani.setGeometry(QRect(100, 430, 301, 16))
        self.txt_Sinopse_One_Piece_Red = QTextBrowser(self.frame)
        self.txt_Sinopse_One_Piece_Red.setObjectName(u"txt_Sinopse_One_Piece_Red")
        self.txt_Sinopse_One_Piece_Red.setGeometry(QRect(20, 470, 371, 81))
        self.txt_Ghost_in_the_shel = QLabel(self.frame)
        self.txt_Ghost_in_the_shel.setObjectName(u"txt_Ghost_in_the_shel")
        self.txt_Ghost_in_the_shel.setGeometry(QRect(640, 330, 111, 16))
        self.txt_30_de_Marco_2017_1h_47_minutos_Acao_Ficcao_Cientifica = QLabel(self.frame)
        self.txt_30_de_Marco_2017_1h_47_minutos_Acao_Ficcao_Cientifica.setObjectName(u"txt_30_de_Marco_2017_1h_47_minutos_Acao_Ficcao_Cientifica")
        self.txt_30_de_Marco_2017_1h_47_minutos_Acao_Ficcao_Cientifica.setGeometry(QRect(640, 360, 361, 16))
        self.txt_Direcao_Rubert_Sanderson_Roteiro_Jamie_Moss_William_Wheeler = QLabel(self.frame)
        self.txt_Direcao_Rubert_Sanderson_Roteiro_Jamie_Moss_William_Wheeler.setObjectName(u"txt_Direcao_Rubert_Sanderson_Roteiro_Jamie_Moss_William_Wheeler")
        self.txt_Direcao_Rubert_Sanderson_Roteiro_Jamie_Moss_William_Wheeler.setGeometry(QRect(640, 380, 391, 16))
        self.txt_Elenco_Scarlett_Johansson_Pilou_Asbaek_Takeshi_Kitano = QLabel(self.frame)
        self.txt_Elenco_Scarlett_Johansson_Pilou_Asbaek_Takeshi_Kitano.setObjectName(u"txt_Elenco_Scarlett_Johansson_Pilou_Asbaek_Takeshi_Kitano")
        self.txt_Elenco_Scarlett_Johansson_Pilou_Asbaek_Takeshi_Kitano.setGeometry(QRect(640, 400, 341, 16))
        self.txt_Sinopse_Ghost_in_the_Shell = QTextBrowser(self.frame)
        self.txt_Sinopse_Ghost_in_the_Shell.setObjectName(u"txt_Sinopse_Ghost_in_the_Shell")
        self.txt_Sinopse_Ghost_in_the_Shell.setGeometry(QRect(550, 460, 511, 81))
        self.btn_01 = QPushButton(self.frame)
        self.btn_01.setObjectName(u"btn_01")
        self.btn_01.setGeometry(QRect(400, 570, 31, 31))
        self.btn_01.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn_02 = QPushButton(self.frame)
        self.btn_02.setObjectName(u"btn_02")
        self.btn_02.setGeometry(QRect(440, 570, 31, 31))
        self.btn_02.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn_03 = QPushButton(self.frame)
        self.btn_03.setObjectName(u"btn_03")
        self.btn_03.setGeometry(QRect(480, 570, 31, 31))
        self.btn_03.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn_04 = QPushButton(self.frame)
        self.btn_04.setObjectName(u"btn_04")
        self.btn_04.setGeometry(QRect(520, 570, 31, 31))
        self.btn_04.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn_05 = QPushButton(self.frame)
        self.btn_05.setObjectName(u"btn_05")
        self.btn_05.setGeometry(QRect(560, 570, 31, 31))
        self.btn_05.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.txt_Sinopse_Single_Seoul.raise_()
        self.inicial_6.raise_()
        self.btn_John_Wicked_3.raise_()
        self.txt_John_Wick_3.raise_()
        self.txt_16_de_Maio_2019_2h_12_minutos_Acao.raise_()
        self.txt_Direcao_Chad_Stahel_Roteiro_Derek_Shay_Hatten.raise_()
        self.txt_Elenco_Keanu_Reeves_Iam_McShanne_Halle_Berry.raise_()
        self.txt_Sinopse_John_Wick_3.raise_()
        self.img_Single_Seoul.raise_()
        self.txt_Single_Seoul.raise_()
        self.txt_29_de_Novembro_de_2023_1h_43_minutos_Romance.raise_()
        self.txt_Direcao_Park_Beom_Su_Roteiro_Lee_Ji_Min.raise_()
        self.txt_Elenco_Lee_Dong_Wook_Lee_Su_Jeong_Esom.raise_()
        self.btn_One_Piece_Red.raise_()
        self.btn_Ghost_in_the_shell.raise_()
        self.txt_One_Piece_Red.raise_()
        self.txt_2_de_Novembro_de_2022_1h_55_minutos_Aventura.raise_()
        self.txt_Direcao_Goro_Tanigushi_Roteiro_Tsutomo_Kuroiwa.raise_()
        self.txt_Elenco_Mayumi_Tanaka_Kaori_Nazuka_Ikue_Otani.raise_()
        self.txt_Sinopse_One_Piece_Red.raise_()
        self.txt_Ghost_in_the_shel.raise_()
        self.txt_30_de_Marco_2017_1h_47_minutos_Acao_Ficcao_Cientifica.raise_()
        self.txt_Direcao_Rubert_Sanderson_Roteiro_Jamie_Moss_William_Wheeler.raise_()
        self.txt_Elenco_Scarlett_Johansson_Pilou_Asbaek_Takeshi_Kitano.raise_()
        self.txt_Sinopse_Ghost_in_the_Shell.raise_()
        self.btn_01.raise_()
        self.btn_02.raise_()
        self.btn_03.raise_()
        self.btn_04.raise_()
        self.btn_05.raise_()
        tela_filme_3.setCentralWidget(self.tela_filme_03)
        self.menubar = QMenuBar(tela_filme_3)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1178, 33))
        tela_filme_3.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(tela_filme_3)
        self.statusbar.setObjectName(u"statusbar")
        tela_filme_3.setStatusBar(self.statusbar)

        self.retranslateUi(tela_filme_3)

        QMetaObject.connectSlotsByName(tela_filme_3)
    # setupUi

    def retranslateUi(self, tela_filme_3):
        tela_filme_3.setWindowTitle(QCoreApplication.translate("tela_filme_3", u"MainWindow", None))
        self.btn_Cine_filme.setText(QCoreApplication.translate("tela_filme_3", u"CineFilmes", None))
        self.btn_Recomendacao_aleatorio.setText(QCoreApplication.translate("tela_filme_3", u"Recomenda\u00e7\u00e3o aleat\u00f3rio", None))
        self.btn_Inicio.setText(QCoreApplication.translate("tela_filme_3", u"Inicio", None))
        self.btn_Filmes_Series.setText(QCoreApplication.translate("tela_filme_3", u"Filmes e S\u00e9ries", None))
        self.btn_John_Wicked_3.setText("")
        self.txt_John_Wick_3.setText(QCoreApplication.translate("tela_filme_3", u"John Wick 3", None))
        self.txt_16_de_Maio_2019_2h_12_minutos_Acao.setText(QCoreApplication.translate("tela_filme_3", u"16 de Maio de 2019 I 2h 12 minutos I A\u00e7\u00e3o", None))
        self.txt_Direcao_Chad_Stahel_Roteiro_Derek_Shay_Hatten.setText(QCoreApplication.translate("tela_filme_3", u"Dire\u00e7\u00e3o: Chad Stahel I Roteiro: Derek kolstad, Shay Hatten", None))
        self.txt_Elenco_Keanu_Reeves_Iam_McShanne_Halle_Berry.setText(QCoreApplication.translate("tela_filme_3", u"Elenco: Keanu Reeves, Ian McShane,Halle Barry", None))
        self.txt_Sinopse_John_Wick_3.setHtml(QCoreApplication.translate("tela_filme_3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:900; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Sinopse:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">O lend\u00e1rio John Wick luta para sair de Nova York quando um contrato de 14 milh\u00f5es de d\u00f3lares faz dele o alvo dos maiores assassinos do mundo</span"
                        "></p></body></html>", None))
        self.img_Single_Seoul.setText("")
        self.txt_Single_Seoul.setText(QCoreApplication.translate("tela_filme_3", u"Single Seoul", None))
        self.txt_29_de_Novembro_de_2023_1h_43_minutos_Romance.setText(QCoreApplication.translate("tela_filme_3", u"29 de Novembro de 2023 I 1h 43 Minutos I Romance", None))
        self.txt_Direcao_Park_Beom_Su_Roteiro_Lee_Ji_Min.setText(QCoreApplication.translate("tela_filme_3", u"Dire\u00e7\u00e3o: Park Beom-Su I Roteiro: Lee Ji-min", None))
        self.txt_Elenco_Lee_Dong_Wook_Lee_Su_Jeong_Esom.setText(QCoreApplication.translate("tela_filme_3", u"Elenco: Lee Dong Wook, Lee Su-Jeong, Esom", None))
        self.txt_Sinopse_Single_Seoul.setHtml(QCoreApplication.translate("tela_filme_3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:900; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Sinopse:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">O filme segue Yeong-ho, que gosta de ficar sozinho, e Hyeon-jin, um editor greg\u00e1rio, que escreve um ensaio sobre a vida de solteiro.</span></p></body></html"
                        ">", None))
        self.btn_One_Piece_Red.setText("")
        self.btn_Ghost_in_the_shell.setText("")
        self.txt_One_Piece_Red.setText(QCoreApplication.translate("tela_filme_3", u"One Piece Red", None))
        self.txt_2_de_Novembro_de_2022_1h_55_minutos_Aventura.setText(QCoreApplication.translate("tela_filme_3", u"2 de Novembro de 2022 I 1h 55 minutos I Aventura", None))
        self.txt_Direcao_Goro_Tanigushi_Roteiro_Tsutomo_Kuroiwa.setText(QCoreApplication.translate("tela_filme_3", u"Dire\u00e7\u00e3o: Goro Taniguchi I Roteiro: Tsutomo Kuroiwa", None))
        self.txt_Elenco_Mayumi_Tanaka_Kaori_Nazuka_Ikue_Otani.setText(QCoreApplication.translate("tela_filme_3", u"Elenco:  Mayumi Tanaka, Kaori Nazuka, Ikue \u00d4tani", None))
        self.txt_Sinopse_One_Piece_Red.setHtml(QCoreApplication.translate("tela_filme_3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:900; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Sinopse:<br />Luffy e sua equipe assistem a um show onde a cantora Uta n\u00e3o \u00e9 outra sen\u00e3o a filha de Shanks.</span></p></body></html>", None))
        self.txt_Ghost_in_the_shel.setText(QCoreApplication.translate("tela_filme_3", u"Ghost in the Shell", None))
        self.txt_30_de_Marco_2017_1h_47_minutos_Acao_Ficcao_Cientifica.setText(QCoreApplication.translate("tela_filme_3", u"30 de Mar\u00e7o de 2017 I 1h 47 minutos I A\u00e7\u00e3o, Fic\u00e7\u00e3o Cient\u00edfica", None))
        self.txt_Direcao_Rubert_Sanderson_Roteiro_Jamie_Moss_William_Wheeler.setText(QCoreApplication.translate("tela_filme_3", u"Dire\u00e7\u00e3o: Rupert Sanders I Roteiro:  Jamie Moss, William Wheeler", None))
        self.txt_Elenco_Scarlett_Johansson_Pilou_Asbaek_Takeshi_Kitano.setText(QCoreApplication.translate("tela_filme_3", u"Elenco: Scarlett Johansson,  Pilou Asb\u00e6k, Takeshi Kitano", None))
        self.txt_Sinopse_Ghost_in_the_Shell.setHtml(QCoreApplication.translate("tela_filme_3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:900; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\">Sinopse:<br />Em um mundo p\u00f3s-2029, c\u00e9rebros se fundem facilmente a computadores e a tecnologia est\u00e1 em todos os lugares. Motoko Kusanagi \u00e9 uma ciborgue com experi\u00eancia militar que comanda um esquadr\u00e3o de elite especializado em combater crimes cibern\u00e9ticos.</span></p></body></html>", None))
        self.btn_01.setText(QCoreApplication.translate("tela_filme_3", u"01", None))
        self.btn_02.setText(QCoreApplication.translate("tela_filme_3", u"02", None))
        self.btn_03.setText(QCoreApplication.translate("tela_filme_3", u"03", None))
        self.btn_04.setText(QCoreApplication.translate("tela_filme_3", u"04", None))
        self.btn_05.setText(QCoreApplication.translate("tela_filme_3", u"05", None))
    # retranslateUi

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from tela_filme_3 import Ui_tela_filme_3

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_tela_filme_3()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())