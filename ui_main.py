# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableView, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(864, 660)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 10);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 35))
        font1 = QFont()
        font1.setBold(True)
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 2px;\n"
"	font-size:18px;\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color:#fff; color: black;}")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_pg_import = QPushButton(self.frame)
        self.btn_pg_import.setObjectName(u"btn_pg_import")
        self.btn_pg_import.setMinimumSize(QSize(167, 35))
        self.btn_pg_import.setMaximumSize(QSize(167, 16777215))
        self.btn_pg_import.setFont(font1)
        self.btn_pg_import.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pg_import.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 2px;\n"
"	font-size:18px;\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color:#fff; color: black;}")

        self.horizontalLayout.addWidget(self.btn_pg_import)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setMinimumSize(QSize(0, 35))
        self.btn_tables.setFont(font1)
        self.btn_tables.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_tables.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 2px;\n"
"	font-size:18px;\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color:#fff; color: black;}")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 35))
        self.btn_sobre.setFont(font1)
        self.btn_sobre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 2px;\n"
"	font-size:18px;\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color:#fff; color: black;}")
        self.btn_sobre.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setMinimumSize(QSize(0, 35))
        self.btn_contato.setFont(font1)
        self.btn_contato.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_contato.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 2px;\n"
"	font-size:18px;\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color:#fff; color: black;}")

        self.horizontalLayout.addWidget(self.btn_contato)


        self.verticalLayout_2.addWidget(self.frame)

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pages.setMinimumSize(QSize(846, 581))
        self.pages.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout = QVBoxLayout(self.pg_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(0, 80, 121);")

        self.verticalLayout.addWidget(self.label)

        self.btn_pg_cadastro = QPushButton(self.pg_home)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")
        self.btn_pg_cadastro.setMinimumSize(QSize(0, 35))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.btn_pg_cadastro.setFont(font2)
        self.btn_pg_cadastro.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pg_cadastro.setStyleSheet(u"QPushButton{color:#fff;}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(255,255,255); \n"
"	color: black;\n"
"}")

        self.verticalLayout.addWidget(self.btn_pg_cadastro)

        self.pages.addWidget(self.pg_home)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_9 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_14 = QLabel(self.pg_cadastro)
        self.label_14.setObjectName(u"label_14")
        font3 = QFont()
        font3.setPointSize(20)
        self.label_14.setFont(font3)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_14)

        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(50, -1, -1, -1)
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setStyleSheet(u"color:rgba(211, 239, 251, 1);\n"
"border-bottom:1px solid white;\n"
"border-radius:1px;\n"
"background-color:rgba(85,115,115,0.1);\n"
"font-family:Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_8.addWidget(self.txt_nome)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(50, -1, -1, -1)
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setStyleSheet(u"color:rgba(211, 239, 251, 1);\n"
"border-bottom:1px solid white;\n"
"border-radius:1px;\n"
"background-color:rgba(85,115,115,0.1);\n"
"font-family:Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_7.addWidget(self.txt_usuario)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(50, -1, -1, -1)
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"color:rgba(211, 239, 251, 1);\n"
"border-bottom:1px solid white;\n"
"border-radius:1px;\n"
"background-color:rgba(85,115,115,0.1);\n"
"font-family:Trebuchet MS;\n"
"font-size:21px;")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.txt_senha)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(50, -1, -1, -1)
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_5.addWidget(self.label_10)

        self.txt_senha_2 = QLineEdit(self.pg_cadastro)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        self.txt_senha_2.setStyleSheet(u"color:rgba(211, 239, 251, 1);\n"
"border-bottom:1px solid white;\n"
"border-radius:1px;\n"
"background-color:rgba(85,115,115,0.1);\n"
"font-family:Trebuchet MS;\n"
"font-size:21px;")
        self.txt_senha_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.txt_senha_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.cb_perfil.setFont(font4)
        self.cb_perfil.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_9.addWidget(self.cb_perfil)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        font5 = QFont()
        font5.setBold(False)
        self.btn_cadastrar.setFont(font5)
        self.btn_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"	border-radius: 10px;\n"
"	font-size:16px;\n"
"	background-color:#fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(170,255,255); \n"
"	color: black;\n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.pages.addWidget(self.pg_cadastro)
        self.pg_import = QWidget()
        self.pg_import.setObjectName(u"pg_import")
        self.verticalLayout_10 = QVBoxLayout(self.pg_import)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_4 = QLabel(self.pg_import)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_10.addWidget(self.label_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit = QLineEdit(self.pg_import)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 28))
        font6 = QFont()
        font6.setPointSize(12)
        self.lineEdit.setFont(font6)
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.btn_open_2 = QPushButton(self.pg_import)
        self.btn_open_2.setObjectName(u"btn_open_2")
        self.btn_open_2.setMinimumSize(QSize(120, 28))
        font7 = QFont()
        self.btn_open_2.setFont(font7)
        self.btn_open_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"	border-top-right-radius: 15px;\n"
"	font-size:16px;\n"
"	background-color:#fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(170,255,255); \n"
"	color: black;\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_open_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_17 = QLabel(self.pg_import)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_11.addWidget(self.label_17)

        self.btn_import = QPushButton(self.pg_import)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setMinimumSize(QSize(0, 35))
        self.btn_import.setFont(font7)
        self.btn_import.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"	border-radius: 10px;\n"
"	font-size:16px;\n"
"	background-color:#fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(170,255,255); \n"
"	color: black;\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_import)

        self.label_5 = QLabel(self.pg_import)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.progressBar = QProgressBar(self.pg_import)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar{	background-color: rgba(0, 0, 0,0.1);\n"
"                    	color: rgb(255, 255, 255);\n"
"                		border-style: none;\n"
"                		text-align: center;\n"
"                		border-radius:10px;\n"
"                \n"
"                }\n"
" \n"
"               \n"
"QProgressBar::chunk{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(6, 75, 149, 255), stop:1 rgba(72, 130, 157, 255));\n"
"                				border-radius:10px;\n"
"                                }")
        self.progressBar.setValue(24)

        self.verticalLayout_10.addWidget(self.progressBar)

        self.pages.addWidget(self.pg_import)
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.verticalLayout_8 = QVBoxLayout(self.pg_table)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tb_base = QTabWidget(self.pg_table)
        self.tb_base.setObjectName(u"tb_base")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout_7 = QVBoxLayout(self.tables)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.tw_estoque = QTreeWidget(self.tables)
        self.tw_estoque.setObjectName(u"tw_estoque")

        self.verticalLayout_5.addWidget(self.tw_estoque)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.tables)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.tw_saida = QTreeWidget(self.tables)
        self.tw_saida.setObjectName(u"tw_saida")

        self.verticalLayout_4.addWidget(self.tw_saida)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.widget = QWidget(self.tables)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_gerar = QPushButton(self.widget)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setMinimumSize(QSize(100, 27))
        self.btn_gerar.setFont(font7)
        self.btn_gerar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"	border-radius: 10px;\n"
"	font-size:16px;\n"
"	background-color:#fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(170,255,255); \n"
"	color: black;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_gerar)

        self.btn_estorno = QPushButton(self.widget)
        self.btn_estorno.setObjectName(u"btn_estorno")
        self.btn_estorno.setMinimumSize(QSize(100, 27))
        self.btn_estorno.setFont(font7)
        self.btn_estorno.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"	border-radius: 10px;\n"
"	font-size:16px;\n"
"	background-color:#fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(170,255,255); \n"
"	color: black;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_estorno)

        self.btn_importar = QPushButton(self.widget)
        self.btn_importar.setObjectName(u"btn_importar")
        self.btn_importar.setMinimumSize(QSize(100, 27))
        self.btn_importar.setFont(font7)
        self.btn_importar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"	border-radius: 10px;\n"
"	font-size:16px;\n"
"	background-color:#fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(170,255,255); \n"
"	color: black;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_importar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.widget)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.tb_base.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_11 = QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_18)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_chart = QPushButton(self.tab_2)
        self.btn_chart.setObjectName(u"btn_chart")
        self.btn_chart.setMinimumSize(QSize(0, 30))
        self.btn_chart.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"	border-radius: 10px;\n"
"	font-size:16px;\n"
"	background-color:#fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(170,255,255); \n"
"	color: black;\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_chart)

        self.btn_excel = QPushButton(self.tab_2)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(0, 30))
        self.btn_excel.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"	border-radius: 10px;\n"
"	font-size:16px;\n"
"	background-color:#fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(170,255,255); \n"
"	color: black;\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_excel)


        self.verticalLayout_11.addLayout(self.horizontalLayout_12)

        self.txt_filtro = QLineEdit(self.tab_2)
        self.txt_filtro.setObjectName(u"txt_filtro")
        self.txt_filtro.setMinimumSize(QSize(0, 28))
        self.txt_filtro.setFont(font6)
        self.txt_filtro.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_filtro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.txt_filtro)

        self.tb_geral = QTableView(self.tab_2)
        self.tb_geral.setObjectName(u"tb_geral")

        self.verticalLayout_11.addWidget(self.tb_geral)

        self.tb_base.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.tb_base)

        self.pages.addWidget(self.pg_table)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_12 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_16 = QLabel(self.pg_sobre)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 50))
        self.label_16.setFont(font3)

        self.verticalLayout_12.addWidget(self.label_16)

        self.label_19 = QLabel(self.pg_sobre)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_19)

        self.pages.addWidget(self.pg_sobre)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.verticalLayout_13 = QVBoxLayout(self.pg_contato)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_15 = QLabel(self.pg_contato)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.verticalLayout_13.addWidget(self.label_15)

        self.label_20 = QLabel(self.pg_contato)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 50))
        self.label_20.setFont(font3)

        self.verticalLayout_13.addWidget(self.label_20)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_26 = QLabel(self.pg_contato)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_16.addWidget(self.label_26)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_21 = QLabel(self.pg_contato)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_13.addWidget(self.label_21)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_13)

        self.label_27 = QLabel(self.pg_contato)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_16.addWidget(self.label_27)


        self.verticalLayout_13.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_28 = QLabel(self.pg_contato)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_17.addWidget(self.label_28)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_22 = QLabel(self.pg_contato)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_14.addWidget(self.label_22)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_14)

        self.label_29 = QLabel(self.pg_contato)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_17.addWidget(self.label_29)


        self.verticalLayout_13.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_30 = QLabel(self.pg_contato)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_15.addWidget(self.label_30)

        self.label_23 = QLabel(self.pg_contato)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_15.addWidget(self.label_23)

        self.label_31 = QLabel(self.pg_contato)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_15.addWidget(self.label_31)


        self.verticalLayout_13.addLayout(self.horizontalLayout_15)

        self.pages.addWidget(self.pg_contato)

        self.verticalLayout_2.addWidget(self.pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(5)
        self.tb_base.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_pg_import.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"TABLES", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">PYTAMBO</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Sistema De Gerenciamento</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.btn_pg_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">TELA DE CADASTRO</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"./imagens/user.png\"/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">CADASTRAR USU\u00c1RIO</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">NOME:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">USU\u00c1RIO:</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">SENHA:</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">SENHA:</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">PERFIL:</span></p></body></html>", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_12.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.label_13.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">IMPORTAR XML</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta com os arquivos XML --->", None))
        self.btn_open_2.setText(QCoreApplication.translate("MainWindow", u"ABRIR", None))
        self.label_17.setText("")
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.label_5.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-weight:bold; color:#ffffff;\">ESTOQUE</span></p></body></html>", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(14, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtreewidgetitem.setText(13, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(12, QCoreApplication.translate("MainWindow", u"Valor Produto", None));
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Unidade Medida", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"Cod Item", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Total Nfe", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Emitente", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"CNPJ Emitente", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Chave", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Data Emiss\u00e3o", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Serie", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-weight:bold; color:#ffffff;\">SA\u00cdDA</span></p></body></html>", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Data Sa\u00edda", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Serie", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"NFE", None));
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar Saida", None))
        self.btn_estorno.setText(QCoreApplication.translate("MainWindow", u"Estorno", None))
        self.btn_importar.setText("")
        self.tb_base.setTabText(self.tb_base.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"Base", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-weight:bold; color:#ffffff;\">GERAL</span></p></body></html>", None))
        self.btn_chart.setText(QCoreApplication.translate("MainWindow", u"GR\u00c1FICO", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"EXCEL", None))
        self.txt_filtro.setText("")
        self.txt_filtro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.tb_base.setTabText(self.tb_base.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Geral", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Sobre</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Este sistema faz a importa\u00e7\u00e3o de arquivos XML e faz o controle do estoque de acordo com a entrada de notas e sa\u00eddas apontadas pelo usu\u00e1rio</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Contatos</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Desenvolvedor: Giovanni Tamborim</span></p></body></html>", None))
        self.label_26.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Email:Tamborimgiovanni2017@gmail.com</span></p></body></html>", None))
        self.label_27.setText("")
        self.label_28.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Telefone: (14) 997894174</span></p></body></html>", None))
        self.label_29.setText("")
        self.label_30.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">PyTambo</span></p></body></html>", None))
        self.label_31.setText("")
    # retranslateUi

