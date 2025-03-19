# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_Star_Wars.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QWidget)

import cartaz_rc

class Ui_tela_star_wars(object):
    def setupUi(self, tela_star_wars):
        if not tela_star_wars.objectName():
            tela_star_wars.setObjectName(u"tela_star_wars")
        tela_star_wars.resize(1135, 540)
        self.Tela_Star_Wars = QWidget(tela_star_wars)
        self.Tela_Star_Wars.setObjectName(u"Tela_Star_Wars")
        self.frame = QFrame(self.Tela_Star_Wars)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 10, 1041, 461))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_Cine_filme = QLabel(self.frame)
        self.btn_Cine_filme.setObjectName(u"btn_Cine_filme")
        self.btn_Cine_filme.setGeometry(QRect(10, 0, 161, 41))
        self.btn_Cine_filme.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 900 22pt \"Segoe UI\";")
        self.btn_Filmes_e_Series = QLabel(self.frame)
        self.btn_Filmes_e_Series.setObjectName(u"btn_Filmes_e_Series")
        self.btn_Filmes_e_Series.setGeometry(QRect(190, 20, 111, 16))
        self.btn_Filmes_e_Series.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.btn_Recomendao_aleatoria = QLabel(self.frame)
        self.btn_Recomendao_aleatoria.setObjectName(u"btn_Recomendao_aleatoria")
        self.btn_Recomendao_aleatoria.setGeometry(QRect(320, 20, 181, 16))
        self.btn_Recomendao_aleatoria.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.icon_perfil = QLabel(self.frame)
        self.icon_perfil.setObjectName(u"icon_perfil")
        self.icon_perfil.setEnabled(True)
        self.icon_perfil.setGeometry(QRect(990, 10, 41, 41))
        self.icon_perfil.setPixmap(QPixmap(u":/icon 1/icon_perfil.png"))
        self.icon_perfil.setScaledContents(True)
        self.txt_Com_Retorno_doImperqador = QLabel(self.frame)
        self.txt_Com_Retorno_doImperqador.setObjectName(u"txt_Com_Retorno_doImperqador")
        self.txt_Com_Retorno_doImperqador.setGeometry(QRect(20, 170, 331, 51))
        self.txt_Com_Retorno_doImperqador.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";")
        self.txt_Resistencia = QLabel(self.frame)
        self.txt_Resistencia.setObjectName(u"txt_Resistencia")
        self.txt_Resistencia.setGeometry(QRect(20, 200, 351, 31))
        self.txt_Resistencia.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.txt_Para_Ser_uma_completa = QLabel(self.frame)
        self.txt_Para_Ser_uma_completa.setObjectName(u"txt_Para_Ser_uma_completa")
        self.txt_Para_Ser_uma_completa.setGeometry(QRect(20, 220, 341, 21))
        self.txt_Para_Ser_uma_completa.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.txt_Conflito = QLabel(self.frame)
        self.txt_Conflito.setObjectName(u"txt_Conflito")
        self.txt_Conflito.setGeometry(QRect(20, 230, 331, 41))
        self.txt_Conflito.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";")
        self.txt_Respostas = QLabel(self.frame)
        self.txt_Respostas.setObjectName(u"txt_Respostas")
        self.txt_Respostas.setGeometry(QRect(20, 260, 331, 21))
        self.txt_Respostas.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";")
        self.img_Star_wars = QLabel(self.frame)
        self.img_Star_wars.setObjectName(u"img_Star_wars")
        self.img_Star_wars.setGeometry(QRect(0, -11, 1041, 481))
        self.img_Star_wars.setPixmap(QPixmap(u":/icon 1/star wars 1.jpg"))
        self.img_Star_wars.setScaledContents(True)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 140, 211, 31))
        self.label_2.setStyleSheet(u"font: 900 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-10, 0, 1051, 471))
        self.label_3.setPixmap(QPixmap(u":/ICON 1/star wars 1.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.raise_()
        self.img_Star_wars.raise_()
        self.btn_Cine_filme.raise_()
        self.btn_Filmes_e_Series.raise_()
        self.btn_Recomendao_aleatoria.raise_()
        self.icon_perfil.raise_()
        self.txt_Com_Retorno_doImperqador.raise_()
        self.txt_Resistencia.raise_()
        self.txt_Para_Ser_uma_completa.raise_()
        self.txt_Conflito.raise_()
        self.txt_Respostas.raise_()
        self.label_2.raise_()
        tela_star_wars.setCentralWidget(self.Tela_Star_Wars)
        self.menubar = QMenuBar(tela_star_wars)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1135, 22))
        tela_star_wars.setMenuBar(self.menubar)

        self.retranslateUi(tela_star_wars)

        QMetaObject.connectSlotsByName(tela_star_wars)
    # setupUi

    def retranslateUi(self, tela_star_wars):
        tela_star_wars.setWindowTitle(QCoreApplication.translate("tela_star_wars", u"MainWindow", None))
        self.btn_Cine_filme.setText(QCoreApplication.translate("tela_star_wars", u"CineFilmes", None))
        self.btn_Filmes_e_Series.setText(QCoreApplication.translate("tela_star_wars", u"Filmes e S\u00e9ries", None))
        self.btn_Recomendao_aleatoria.setText(QCoreApplication.translate("tela_star_wars", u"Recomenda\u00e7\u00e3o aleat\u00f3ria", None))
        self.icon_perfil.setText("")
        self.txt_Com_Retorno_doImperqador.setText(QCoreApplication.translate("tela_star_wars", u"Com o retorno do Imperador Palpatine, a", None))
        self.txt_Resistencia.setText(QCoreApplication.translate("tela_star_wars", u"Resist\u00eancia toma a frente da batalha. Treinando", None))
        self.txt_Para_Ser_uma_completa.setText(QCoreApplication.translate("tela_star_wars", u"para ser uma completa Jedi, Rey se encontra em ", None))
        self.txt_Conflito.setText(QCoreApplication.translate("tela_star_wars", u"conflito com o passado e futuro, e teme pelas", None))
        self.txt_Respostas.setText(QCoreApplication.translate("tela_star_wars", u"respostas que pode conseguir com Kylon Ren.", None))
        self.img_Star_wars.setText("")
        self.label_2.setText(QCoreApplication.translate("tela_star_wars", u"Star Wars: Epis\u00f3dio IX", None))
        self.label_3.setText("")
    # retranslateUi

