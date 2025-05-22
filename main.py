from PySide6.QtWidgets import (QApplication,QFileDialog, QMainWindow, QMessageBox, QTreeWidgetItem )
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from os import access
from ui_login import Ui_login
from ui_main import Ui_MainWindow
import sys 
from database import DataBase
from xml_files import read_xml
import sqlite3
import pandas as pd
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
import re
from datetime import date
import matplotlib.pyplot as plt

class Login(QMainWindow, Ui_login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        appIcon = QIcon('icon.ico')
        self.setWindowIcon(appIcon)

        
        self.btn_login.clicked.connect(self.checkLogin)

    def checkLogin(self):
        self.users = DataBase()
        self.users.conecta()
        authenticated = self.users.check_user(self.txt_user.text().upper(),self.txt_password.text())

        if authenticated.lower() == "administrador" or authenticated.lower() == "user":
            self.w = MainWindow(self.txt_user.text(), authenticated.lower())
            self.w.show()
            self.close()

        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao Acessar")
                msg.setText(f'Login ou Senha Incorreto \n \n Tentativa: {self.tentativas + 1} de 3')
                msg.exec()
                self.tentativas +=1

            if self.tentativas == 3:
                self.users.close_connection()
                sys.exit(0)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,username, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema De Gerenciamento")
        appIcon = QIcon('icon.ico')
        self.setWindowIcon(appIcon)

        self.user = username

        if user.lower() == "user":
            self.btn_pg_cadastro.setVisible(False)

        self.pages.setCurrentWidget(self.pg_home)

        self.btn_home.clicked.connect(lambda:self.pages.setCurrentWidget(self.pg_home))
        self.btn_tables.clicked.connect(lambda:self.pages.setCurrentWidget(self.pg_table))
        self.btn_contato.clicked.connect(lambda:self.pages.setCurrentWidget(self.pg_contato))
        self.btn_sobre.clicked.connect(lambda:self.pages.setCurrentWidget(self.pg_sobre))
        self.btn_pg_cadastro.clicked.connect(lambda:self.pages.setCurrentWidget(self.pg_cadastro))
        self.btn_pg_import.clicked.connect(lambda:self.pages.setCurrentWidget(self.pg_import))

        self.btn_cadastrar.clicked.connect(self.subcribe_user)

        #ARQUIVO XML
        self.btn_open_2.clicked.connect(self.open_path)
        self.btn_import.clicked.connect(self.import_xml_files)

        #filtro
        self.txt_filtro.textChanged.connect(self.update_filter)

        #Gerar saida e estorno
        self.btn_gerar.clicked.connect(self.gerar_saida)
        self.btn_estorno.clicked.connect(self.gerar_estorno)

        self.btn_excel.clicked.connect(self.excel_file)

        self.btn_chart.clicked.connect(self.graphic)
        
        self.reset_table()


    def subcribe_user(self):
        if self.txt_senha.text() != self.txt_senha_2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senha Divirgentes")
            msg.setText("A Senha não é igual!")
            msg.exec()
            return None
        
        nome = self.txt_nome.text()
        user = self.txt_usuario.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()

        db = DataBase()
        db.conecta()
        db.insert_user(nome,user, password, access)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Cadastro de Usuário")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec()

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_senha_2.setText("")

    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(
            self, "Selecionar pasta", "C:/Users", QFileDialog.ShowDirsOnly
        )
        self.txt_filtro.setText(self.path)
        
    def import_xml_files(self):
        if not hasattr(self, "path") or not self.path:
            QMessageBox.warning(self, "Erro", "Selecione um diretório antes de importar.")
            return
        xml = read_xml(self.txt_filtro.text())
        all = xml.all_files()
        self.progressBar.setMaximum(len(all))

        db = DataBase()
        db.conecta()
        cont = 1
        
        for i in all:
            self.progressBar.setValue(cont)
            fullDataSet = xml.nfe_data(i)
            db.insert_data(fullDataSet)
            cont+=1
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Importacao XML")
        msg.setText("Importacao Concluída!")
        msg.exec_()
        self.progressBar.setValue(0)



        db.close_connection()

    def table_estoque(self):
        self.tw_estoque.setStyleSheet(u" QHeaderView{color:white};color:#fff; font-size: 15px;")

        cn = sqlite3.connect('system.db')
        result= pd.read_sql_query("SELECT * FROM Notas WHERE data_saida= ''",cn)
        result = result.values.tolist()


        self.x = ""
        
        for i in result:
            #faz o check para identificar a mesma nota e adicionar um nivel
            if i[0] == self.x:
                QTreeWidgetItem(self.campo,i)
            else:
                self.campo = QTreeWidgetItem(self.tw_estoque,i)
                self.campo.setCheckState(0, Qt.Unchecked)

            self.x = i[0]

        self.tw_estoque.setSortingEnabled(True)

        for i in range(1,15):
            self.tw_estoque.resizeColumnToContents(i)

    def table_saida(self):
        self.tw_saida.setStyleSheet(u" QHeaderView{color:white};color:#fff; font-size: 15px;")

        cn = sqlite3.connect('system.db')
        result= pd.read_sql_query("""SELECT Nfe,serie, data_importacao, data_saida,usuario
            FROM Notas WHERE data_saida != ''""",cn)
        result = result.values.tolist()


        self.x = ""
        
        for i in result:
            #faz o check para identificar a mesma nota e adicionar um nivel
            if i[0] == self.x:
                QTreeWidgetItem(self.campo,i)
            else:
                self.campo = QTreeWidgetItem(self.tw_saida,i)
                self.campo.setCheckState(0, Qt.Unchecked)

            self.x = i[0]

        self.tw_saida.setSortingEnabled(True)

        for i in range(1,15):
            self.tw_saida.resizeColumnToContents(i)
    
    def table_geral(self):
        self.tb_geral.setStyleSheet(u" QHeaderView{color:white};color:#fff; font-size: 15px;")

        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tb_geral.setModel(self.model)
        self.model.setTable("notas")
        self.model.select()

    def reset_table(self):
        self.tw_estoque.clear()
        self.tw_saida.clear()

        self.table_saida()
        self.table_estoque()
        self.table_geral()
        self.model.setFilter("")  # remove o filtro antes de recarregar os dados


    def update_filter(self, s):
        s = re.sub(r'[%_"\'\\]', '', s)  # remove caracteres perigosos no LIKE
        filter_str = f'Nfe LIKE "%{s}%"'
        self.model.setFilter(filter_str)

    def gerar_saida(self):

        self.checked_itens_out = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == Qt.Checked:
                    self.checked_itens_out.append(child.text(0))

        recurse(self.tw_estoque.invisibleRootItem())

        #Pergunta se o usuário realmente deseja fazer isso

        self.question('Saida')

    def gerar_estorno(self):

        self.checked_itens=[]

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == Qt.Checked:
                    self.checked_itens.append(child.text(0))

        recurse(self.tw_saida.invisibleRootItem())
        self.question('estorno')
                    
    def question (self, table):

        msgBox = QMessageBox()

        if table == 'estorno':
            msgBox.setText("Deseja estornar as notas selecionadas?")
            msgBox.setInformativeText("As Selecionadas Voltarão para o estoque \n clique em yes para confirmar")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas:{self.checked_itens}")


        else:
            msgBox.setText("Deseja gerar saida das notas selecionadas?")
            msgBox.setInformativeText("As notas abaixo sera baixada no estoque \n clique em yes para confirmar")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas:{self.checked_itens_out}")

        msgBox.setIcon(QMessageBox.Icon.Question)
        ret = msgBox.exec()

        if ret == QMessageBox.Yes:
            db = DataBase()
            db.conecta()
            if table == 'estorno':
                db.update_estorno(self.user, self.checked_itens)
            else:
                data_saida = date.today()
                data_saida = data_saida.strftime('%d/%m/%Y')
                db.update_estoque(data_saida, self.user, self.checked_itens_out)
            db.close_connection()
            self.reset_table()

    def excel_file(self):

        cnx = sqlite3.connect('system.db')
        result = pd.read_sql_query("SELECT * FROM Notas", cnx)
        result.to_excel("Resumo de notas.xlsx", sheet_name='Notas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Relatório de notas")
        msg.setText("Relatório gerado com sucesso!")
        msg.exec()

    def graphic(self):
        cnx = sqlite3.connect("system.db")
        df_estoque = pd.read_sql_query('SELECT * FROM Notas', cnx)
        df_saida = pd.read_sql_query("SELECT * FROM Notas WHERE data_saida != ''", cnx)

        estoque = len(df_estoque)
        saida = len(df_saida)

        if estoque == 0 and saida == 0:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(None, "Sem dados", "Nenhum dado encontrado para gerar o gráfico.")
            return

        labels = ["Estoque", "Saídas"]
        sizes = [estoque, saida]

        fig1, axl = plt.subplots()
        axl.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        axl.axis("equal")
        plt.title("Distribuição de Notas")
        plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()  
    window.show()      
    app.exec()
