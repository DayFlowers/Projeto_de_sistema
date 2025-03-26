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

import extra

class Ui_tela_recomendar(object):
    def setupUi(self, tela_recomendar):
        if not tela_recomendar.objectName():
            tela_recomendar.setObjectName(u"tela_recomendar")
        tela_recomendar.resize(1101, 600)
        self.tela_recom = QWidget(tela_recomendar)
        self.tela_recom.setObjectName(u"tela_recom")
        self.frame = QFrame(self.tela_recom)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 10, 1051, 531))
        self.frame.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.inicial_2 = QFrame(self.frame)
        self.inicial_2.setObjectName(u"inicial_2")
        self.inicial_2.setGeometry(QRect(-10, 0, 1141, 51))
        self.inicial_2.setStyleSheet(u"background-color: rgb(34, 31, 31);")
        self.inicial_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.inicial_2.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_Cine_filme_2 = QLabel(self.inicial_2)
        self.btn_Cine_filme_2.setObjectName(u"btn_Cine_filme_2")
        self.btn_Cine_filme_2.setGeometry(QRect(20, 10, 161, 41))
        self.btn_Cine_filme_2.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 900 22pt \"Segoe UI\";")
        self.btn_Recomendacao_aleatorio_9 = QPushButton(self.inicial_2)
        self.btn_Recomendacao_aleatorio_9.setObjectName(u"btn_Recomendacao_aleatorio_9")
        self.btn_Recomendacao_aleatorio_9.setGeometry(QRect(430, 20, 171, 24))
        self.btn_Recomendacao_aleatorio_9.setStyleSheet(u"color: rgb(255, 0, 0);")
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
        self.btn_Icon_Perfil_2 = QLabel(self.inicial_2)
        self.btn_Icon_Perfil_2.setObjectName(u"btn_Icon_Perfil_2")
        self.btn_Icon_Perfil_2.setGeometry(QRect(1040, 10, 31, 31))
        self.btn_Icon_Perfil_2.setPixmap(QPixmap(u":/icon4/icon_perfil.png"))
        self.btn_Icon_Perfil_2.setScaledContents(True)
        self.img_One_Piece_Serie = QLabel(self.frame)
        self.img_One_Piece_Serie.setObjectName(u"img_One_Piece_Serie")
        self.img_One_Piece_Serie.setGeometry(QRect(20, 70, 101, 151))
        self.img_One_Piece_Serie.setPixmap(QPixmap(u":/icon 1/one piece serie.webp"))
        self.img_One_Piece_Serie.setScaledContents(True)
        self.img_Orgulho_Preconceito = QLabel(self.frame)
        self.img_Orgulho_Preconceito.setObjectName(u"img_Orgulho_Preconceito")
        self.img_Orgulho_Preconceito.setGeometry(QRect(540, 170, 101, 151))
        self.img_Orgulho_Preconceito.setPixmap(QPixmap(u":/icon 3/orgulho e preconceito.webp"))
        self.img_Orgulho_Preconceito.setScaledContents(True)
        self.img_Avatar_2 = QLabel(self.frame)
        self.img_Avatar_2.setObjectName(u"img_Avatar_2")
        self.img_Avatar_2.setGeometry(QRect(20, 350, 101, 151))
        self.img_Avatar_2.setPixmap(QPixmap(u":/icon 2/Avatar.jpeg"))
        self.img_Avatar_2.setScaledContents(True)
        self.txt_One_Piece = QLabel(self.frame)
        self.txt_One_Piece.setObjectName(u"txt_One_Piece")
        self.txt_One_Piece.setGeometry(QRect(140, 70, 61, 16))
        self.txt_One_Piece.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_Sinopse_One_Piece = QTextBrowser(self.frame)
        self.txt_Sinopse_One_Piece.setObjectName(u"txt_Sinopse_One_Piece")
        self.txt_Sinopse_One_Piece.setGeometry(QRect(140, 100, 321, 111))
        self.txt_Avatar_2 = QLabel(self.frame)
        self.txt_Avatar_2.setObjectName(u"txt_Avatar_2")
        self.txt_Avatar_2.setGeometry(QRect(140, 350, 49, 16))
        self.txt_Avatar_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_Sinopse_Avatar_2 = QTextBrowser(self.frame)
        self.txt_Sinopse_Avatar_2.setObjectName(u"txt_Sinopse_Avatar_2")
        self.txt_Sinopse_Avatar_2.setGeometry(QRect(140, 380, 321, 111))
        self.txt_Orgulho_e_Preconceito = QLabel(self.frame)
        self.txt_Orgulho_e_Preconceito.setObjectName(u"txt_Orgulho_e_Preconceito")
        self.txt_Orgulho_e_Preconceito.setGeometry(QRect(660, 170, 121, 16))
        self.txt_Orgulho_e_Preconceito.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_Sinopse_Orgulho_e_Preconceito = QTextBrowser(self.frame)
        self.txt_Sinopse_Orgulho_e_Preconceito.setObjectName(u"txt_Sinopse_Orgulho_e_Preconceito")
        self.txt_Sinopse_Orgulho_e_Preconceito.setGeometry(QRect(660, 200, 371, 111))
        self.txt_Genero_Acao_Aventura = QLabel(self.frame)
        self.txt_Genero_Acao_Aventura.setObjectName(u"txt_Genero_Acao_Aventura")
        self.txt_Genero_Acao_Aventura.setGeometry(QRect(140, 220, 131, 16))
        self.txt_Genero_Acao_Aventura.setStyleSheet(u"color: rgb(152, 216, 255);\n"
"color: rgb(255, 255, 255);")
        self.txt_Acao_Aventura = QLabel(self.frame)
        self.txt_Acao_Aventura.setObjectName(u"txt_Acao_Aventura")
        self.txt_Acao_Aventura.setGeometry(QRect(140, 500, 131, 16))
        self.txt_Acao_Aventura.setStyleSheet(u"color: rgb(152, 216, 255);\n"
"color: rgb(255, 255, 255);")
        self.txt_Genero_Epoca_Romance = QLabel(self.frame)
        self.txt_Genero_Epoca_Romance.setObjectName(u"txt_Genero_Epoca_Romance")
        self.txt_Genero_Epoca_Romance.setGeometry(QRect(670, 320, 141, 16))
        self.txt_Genero_Epoca_Romance.setStyleSheet(u"color: rgb(152, 216, 255);\n"
"color: rgb(255, 255, 255);")
        tela_recomendar.setCentralWidget(self.tela_recom)
        self.menubar = QMenuBar(tela_recomendar)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1101, 22))
        tela_recomendar.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(tela_recomendar)
        self.statusbar.setObjectName(u"statusbar")
        tela_recomendar.setStatusBar(self.statusbar)

        self.retranslateUi(tela_recomendar)

        QMetaObject.connectSlotsByName(tela_recomendar)
    # setupUi

    def retranslateUi(self, tela_recomendar):
        tela_recomendar.setWindowTitle(QCoreApplication.translate("tela_recomendar", u"MainWindow", None))
        self.btn_Cine_filme_2.setText(QCoreApplication.translate("tela_recomendar", u"CineFilmes", None))
        self.btn_Recomendacao_aleatorio_9.setText(QCoreApplication.translate("tela_recomendar", u"Recomenda\u00e7\u00e3o aleat\u00f3rio", None))
        self.btn_Inicio_2.setText(QCoreApplication.translate("tela_recomendar", u"Inicio", None))
        self.btn_Filmes_Series_2.setText(QCoreApplication.translate("tela_recomendar", u"Filmes e S\u00e9ries", None))
        self.btn_Icon_Perfil_2.setText("")
        self.img_One_Piece_Serie.setText("")
        self.img_Orgulho_Preconceito.setText("")
        self.img_Avatar_2.setText("")
        self.txt_One_Piece.setText(QCoreApplication.translate("tela_recomendar", u"One Piece ", None))
        self.txt_Sinopse_One_Piece.setHtml(QCoreApplication.translate("tela_recomendar", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">O pirata Monkey D. Luffy e sua tripula\u00e7\u00e3o exploram um mundo fant\u00e1stico de oceanos infinitos e ilhas ex\u00f3ticas em busca do maior tesouro do mundo. Luffy tem apenas um objetivo: se tornar o pr\u00f3ximo Rei dos Piratas.</span></p></body></html>", None))
        self.txt_Avatar_2.setText(QCoreApplication.translate("tela_recomendar", u"Avatar 2", None))
        self.txt_Sinopse_Avatar_2.setHtml(QCoreApplication.translate("tela_recomendar", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Ap\u00f3s formar uma fam\u00edlia, Jake Sully e Ney'tiri fazem de tudo para ficarem juntos. No entanto, eles devem sair de casa e explorar as regi\u00f5es de Pandora quando uma antiga amea\u00e7a ressurge, e Jake deve travar uma guerra dif\u00edcil contra os humanos.</span></p></body></html>", None))
        self.txt_Orgulho_e_Preconceito.setText(QCoreApplication.translate("tela_recomendar", u"Orgulho e Preconceito", None))
        self.txt_Sinopse_Orgulho_e_Preconceito.setHtml(QCoreApplication.translate("tela_recomendar", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Elizabeth Bennet vive com sua m\u00e3e, pai e irm\u00e3s no campo, na Inglaterra. Por ser uma das filhas mais velhas, ela enfrenta uma crescente press\u00e3o de seus pais para se casar. Quando Elizabeth \u00e9 apresentada ao belo e rico Darcy, fa\u00edscas voam. Embora haja uma qu\u00edmica \u00f3bvia entre os dois, a natureza excessivamente reservada de Darcy amea\u00e7"
                        "a a rela\u00e7\u00e3o.</span></p></body></html>", None))
        self.txt_Genero_Acao_Aventura.setText(QCoreApplication.translate("tela_recomendar", u"G\u00eanero: A\u00e7\u00e3o, Aventura", None))
        self.txt_Acao_Aventura.setText(QCoreApplication.translate("tela_recomendar", u"G\u00eanero: A\u00e7\u00e3o, Aventura", None))
        self.txt_Genero_Epoca_Romance.setText(QCoreApplication.translate("tela_recomendar", u"G\u00eanero: \u00c9poca, Romance", None))
    # retranslateUi

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from tela_recom import Ui_tela_recomendar

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_tela_recomendar()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())