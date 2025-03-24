from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QTextBrowser, QWidget, QFrame

class Ui_tela_filme_3(object):
    def setupUi(self, tela_filme_3):
        if not tela_filme_3.objectName():
            tela_filme_3.setObjectName(u"tela_filme_3")
        tela_filme_3.resize(1172, 611)

        self.centralwidget = QWidget(tela_filme_3)
        self.centralwidget.setObjectName(u"centralwidget")

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 0, 1101, 611))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0); font: 900 9pt 'Segoe UI'; color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        # Header Frame
        self.inicial_6 = QFrame(self.frame)
        self.inicial_6.setObjectName(u"inicial_6")
        self.inicial_6.setGeometry(QRect(0, 0, 1141, 51))
        self.inicial_6.setStyleSheet("background-color: rgb(34, 31, 31);")
        self.inicial_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.inicial_6.setFrameShadow(QFrame.Shadow.Raised)

        # Buttons in header
        self.btn_Cine_filme_6 = QLabel(self.inicial_6)
        self.btn_Cine_filme_6.setObjectName(u"btn_Cine_filme_6")
        self.btn_Cine_filme_6.setGeometry(QRect(10, 10, 161, 41))
        self.btn_Cine_filme_6.setStyleSheet("color: rgb(255, 0, 0); font: 900 22pt 'Segoe UI';")

        self.btn_Recomendacao_aleatorio_6 = QPushButton(self.inicial_6)
        self.btn_Recomendacao_aleatorio_6.setObjectName(u"btn_Recomendacao_aleatorio_6")
        self.btn_Recomendacao_aleatorio_6.setGeometry(QRect(430, 20, 171, 24))
        self.btn_Recomendacao_aleatorio_6.setStyleSheet("color: rgb(255, 0, 0);")

        self.btn_Inicio_6 = QPushButton(self.inicial_6)
        self.btn_Inicio_6.setObjectName(u"btn_Inicio_6")
        self.btn_Inicio_6.setGeometry(QRect(180, 20, 101, 24))
        self.btn_Inicio_6.setStyleSheet("color: rgb(255, 0, 0); background-color: rgb(34, 31, 31);")

        self.btn_Filmes_Series_6 = QPushButton(self.inicial_6)
        self.btn_Filmes_Series_6.setObjectName(u"btn_Filmes_Series_6")
        self.btn_Filmes_Series_6.setGeometry(QRect(300, 20, 101, 24))
        self.btn_Filmes_Series_6.setStyleSheet("color: rgb(255, 0, 0); background-color: rgb(34, 31, 31);")

        self.btn_icon_perfil = QLabel(self.inicial_6)
        self.btn_icon_perfil.setObjectName(u"btn_icon_perfil")
        self.btn_icon_perfil.setGeometry(QRect(1050, 10, 31, 31))
        self.btn_icon_perfil.setPixmap(QPixmap(u":/perfil/icon_perfil.png"))
        self.btn_icon_perfil.setScaledContents(True)

        # Movie Widgets
        self.img_John_Wicked_3 = QLabel(self.frame)
        self.img_John_Wicked_3.setObjectName(u"img_John_Wicked_3")
        self.img_John_Wicked_3.setGeometry(QRect(10, 80, 81, 131))
        self.img_John_Wicked_3.setPixmap(QPixmap(u":/icon 1/John_Wick_3.png"))
        self.img_John_Wicked_3.setScaledContents(True)

        self.txt_John_Wick_3 = QLabel(self.frame)
        self.txt_John_Wick_3.setObjectName(u"txt_John_Wick_3")
        self.txt_John_Wick_3.setGeometry(QRect(100, 80, 81, 16))
        self.txt_John_Wick_3.setStyleSheet("font: 900 9pt 'Segoe UI'; color: rgb(255, 255, 255);")
        self.txt_John_Wick_3.setText("John Wick 3")

        self.txt_16_de_Maio_2019 = QLabel(self.frame)
        self.txt_16_de_Maio_2019.setObjectName(u"txt_16_de_Maio_2019")
        self.txt_16_de_Maio_2019.setGeometry(QRect(100, 110, 251, 16))
        self.txt_16_de_Maio_2019.setStyleSheet("color: rgb(255, 255, 255); font: 900 9pt 'Segoe UI';")
        self.txt_16_de_Maio_2019.setText("16 de Maio de 2019 | 2h 12min | Ação")

        self.txt_Direcao_Chad_Stahel_Roteiro_Derek = QLabel(self.frame)
        self.txt_Direcao_Chad_Stahel_Roteiro_Derek.setObjectName(u"txt_Direcao_Chad_Stahel_Roteiro_Derek")
        self.txt_Direcao_Chad_Stahel_Roteiro_Derek.setGeometry(QRect(100, 130, 351, 16))
        self.txt_Direcao_Chad_Stahel_Roteiro_Derek.setStyleSheet("color: rgb(255, 255, 255); font: 900 9pt 'Segoe UI';")
        self.txt_Direcao_Chad_Stahel_Roteiro_Derek.setText("Direção: Chad Stahel | Roteiro: Derek Kolstad")

        self.txt_Elenco_Keanu_Reeves_Iam_McShanne_Halle_Berry = QLabel(self.frame)
        self.txt_Elenco_Keanu_Reeves_Iam_McShanne_Halle_Berry.setObjectName(u"txt_Elenco_Keanu_Reeves_Iam_McShanne_Halle_Berry")
        self.txt_Elenco_Keanu_Reeves_Iam_McShanne_Halle_Berry.setGeometry(QRect(100, 150, 281, 16))
        self.txt_Elenco_Keanu_Reeves_Iam_McShanne_Halle_Berry.setStyleSheet("color: rgb(255, 255, 255); font: 900 9pt 'Segoe UI';")
        self.txt_Elenco_Keanu_Reeves_Iam_McShanne_Halle_Berry.setText("Elenco: Keanu Reeves, Ian McShane, Halle Berry")

       
        self.txt_Sinopse_John_Wick_3 = QTextBrowser(self.frame)
        self.txt_Sinopse_John_Wick_3.setObjectName(u"txt_Sinopse_John_Wick_3")
        self.txt_Sinopse_John_Wick_3.setGeometry(QRect(20, 220, 371, 81))
        self.txt_Sinopse_John_Wick_3.setPlainText(
            "Sinopse: O lendário John Wick luta para sair de Nova York quando um contrato de 14 milhões de dólares faz dele o alvo dos maiores assassinos do mundo."
        )

        # Example of another movie widget
        self.img_Single_Seoul = QLabel(self.frame)
        self.img_Single_Seoul.setObjectName(u"img_Single_Seoul")
        self.img_Single_Seoul.setGeometry(QRect(550, 80, 81, 131))
        self.img_Single_Seoul.setPixmap(QPixmap(u":/icon2/Single seul wook.jpg"))
        self.img_Single_Seoul.setScaledContents(True)

        self.txt_Single_Seoul = QLabel(self.frame)
        self.txt_Single_Seoul.setObjectName(u"txt_Single_Seoul")
        self.txt_Single_Seoul.setGeometry(QRect(640, 80, 71, 16))
        self.txt_Single_Seoul.setStyleSheet("color: rgb(255, 255, 255); font: 900 9pt 'Segoe UI';")
        self.txt_Single_Seoul.setText("Single Seoul")

        self.txt_29_de_Novembro_de_2023 = QLabel(self.frame)
        self.txt_29_de_Novembro
