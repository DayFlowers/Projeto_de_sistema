from PySide6.QtCore import QCoreApplication, QRect
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QMainWindow, QPushButton, QSizePolicy, QTextBrowser, QWidget, QMenuBar, QStatusBar

import filmedois_rc 

class Ui_tela_filme_2(object):
    def setupUi(self, tela_filme_2):
        if not tela_filme_2.objectName():
            tela_filme_2.setObjectName(u"tela_filme_2")
        tela_filme_2.resize(1141, 631)
        
        # Central Widget e Frame
        self.centralwidget = QWidget(tela_filme_2)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 0, 1101, 591))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0); font: 900 9pt \"Segoe UI\"; color: rgb(255, 255, 255);")
        
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        # Frame Inicial
        self.inicial_2 = QFrame(self.frame)
        self.inicial_2.setObjectName(u"inicial_2")
        self.inicial_2.setGeometry(QRect(0, 0, 1101, 51))
        self.inicial_2.setStyleSheet(u"background-color: rgb(34, 31, 31);")
        self.inicial_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.inicial_2.setFrameShadow(QFrame.Shadow.Raised)

        # Labels e Buttons no frame
        self.btn_Cine_filme_2 = QLabel(self.inicial_2)
        self.btn_Cine_filme_2.setObjectName(u"btn_Cine_filme_2")
        self.btn_Cine_filme_2.setGeometry(QRect(10, 10, 161, 41))
        self.btn_Cine_filme_2.setStyleSheet(u"color: rgb(255, 0, 0); font: 900 22pt \"Segoe UI\";")
        
        self.btn_Recomendacao_aleatorio_2 = QPushButton(self.inicial_2)
        self.btn_Recomendacao_aleatorio_2.setObjectName(u"btn_Recomendacao_aleatorio_2")
        self.btn_Recomendacao_aleatorio_2.setGeometry(QRect(430, 20, 171, 24))
        self.btn_Recomendacao_aleatorio_2.setStyleSheet(u"color: rgb(255, 0, 0);")
        
        self.btn_Inicio_2 = QPushButton(self.inicial_2)
        self.btn_Inicio_2.setObjectName(u"btn_Inicio_2")
        self.btn_Inicio_2.setGeometry(QRect(180, 20, 101, 24))
        self.btn_Inicio_2.setStyleSheet(u"color: rgb(0, 255, 0); background-color: rgb(34, 31, 31);")
        
        self.btn_Filmes_Series_2 = QPushButton(self.inicial_2)
        self.btn_Filmes_Series_2.setObjectName(u"btn_Filmes_Series_2")
        self.btn_Filmes_Series_2.setGeometry(QRect(300, 20, 101, 24))
        self.btn_Filmes_Series_2.setStyleSheet(u"color: rgb(0, 255, 0); background-color: rgb(34, 31, 31);")

        self.btn_icon_perfil = QLabel(self.inicial_2)
        self.btn_icon_perfil.setObjectName(u"btn_icon_perfil")
        self.btn_icon_perfil.setGeometry(QRect(1060, 10, 31, 31))
        self.btn_icon_perfil.setPixmap(QPixmap(u":/perfil/icon_perfil.png"))
        self.btn_icon_perfil.setScaledContents(True)

        # Adicionando imagens e textos no frame
        self.img_Ainda_Estou_Aqui = QLabel(self.frame)
        self.img_Ainda_Estou_Aqui.setObjectName(u"img_Ainda_Estou_Aqui")
        self.img_Ainda_Estou_Aqui.setGeometry(QRect(10, 70, 81, 121))
        self.img_Ainda_Estou_Aqui.setPixmap(QPixmap(u":/icon 1/Ainda_Estou_Aqui.jpg"))
        self.img_Ainda_Estou_Aqui.setScaledContents(True)
        
        self.txt_Ainda_Estou_Aqui = QLabel(self.frame)
        self.txt_Ainda_Estou_Aqui.setObjectName(u"txt_Ainda_Estou_Aqui")
        self.txt_Ainda_Estou_Aqui.setGeometry(QRect(110, 70, 101, 21))
        self.txt_Ainda_Estou_Aqui.setStyleSheet(u"font: 900 9pt \"Segoe UI\"; color: rgb(255, 255, 255);")
        
        # Exemplo de tradução do título
        self.txt_Ainda_Estou_Aqui.setText(QCoreApplication.translate("tela_filme_2", u"Ainda Estou Aqui", None))

        # Definindo mais rótulos de filmes e detalhes
        self.txt_7_de_Novembro_2024 = QLabel(self.frame)
        self.txt_7_de_Novembro_2024.setObjectName(u"txt_7_de_Novembro_2024")
        self.txt_7_de_Novembro_2024.setGeometry(QRect(110, 90, 351, 21))
        self.txt_7_de_Novembro_2024.setStyleSheet(u"color: rgb(255, 255, 255); font: 900 9pt \"Segoe UI\";")
        self.txt_7_de_Novembro_2024.setText(QCoreApplication.translate("tela_filme_2", u"7 de Novembro de 2024 I 2h 15 minutos I Drama, Suspense", None))

        self.txt_Direcao_Walter_SallesRoteiro_Murilo_Hauser = QLabel(self.frame)
        self.txt_Direcao_Walter_SallesRoteiro_Murilo_Hauser.setObjectName(u"txt_Direcao_Walter_SallesRoteiro_Murilo_Hauser")
        self.txt_Direcao_Walter_SallesRoteiro_Murilo_Hauser.setGeometry(QRect(110, 110, 371, 31))
        self.txt_Direcao_Walter_SallesRoteiro_Murilo_Hauser.setText(QCoreApplication.translate("tela_filme_2", u"Direção: Walter Salles I Roteiro: Murilo Hauser, Heitor Lorenga", None))

        # Sinopse de 'Ainda Estou Aqui'
        self.txt_Sinopse_Ainda_Estou_aqui = QTextBrowser(self.frame)
        self.txt_Sinopse_Ainda_Estou_aqui.setObjectName(u"txt_Sinopse_Ainda_Estou_aqui")
        self.txt_Sinopse_Ainda_Estou_aqui.setGeometry(QRect(10, 200, 551, 81))
        self.txt_Sinopse_Ainda_Estou_aqui.setHtml(QCoreApplication.translate("tela_filme_2", 
            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">"
            "p, li { white-space: pre-wrap; }</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:900; font-style:normal;\">"
            "<p><span style=\" font-weight:400; color:#ffffff;\">Sinopse: O filme 'Ainda Estou Aqui' conta a história de Eunice Paiva...</span></p></body></html>", None))
        
        tela_filme_2.setCentralWidget(self.centralwidget)

        # Menu e status bar
        self.menubar = QMenuBar(tela_filme_2)
        self.menubar.setObjectName(u"menubar")
        self.men
