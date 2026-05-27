from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
from windows.cadastro import Ui_jan_cadastro
import os,sys

from AskeeRequests import *
from Interatcion.configs import Configs

class cadastro(QDialog):
    def __init__(self,*args,**argvs):
        super(cadastro,self).__init__(*args,**argvs)
        self.configs = Configs()
        self.authRequests = Auth()
        self.ui = Ui_jan_cadastro()
        self.ui.setupUi(self)

        self.ui.cad_butt_enter.clicked.connect(self.cadastro)

    def cadastro(self):
        print("cadastrando...")
        payload = {
            "name": self.ui.cad_line_login.text(),
            "email": self.ui.cad_line_login.text(),
            "username": self.ui.cad_line_login.text(),
            "password": self.ui.cad_line_passwd.text(),
            "icon": self.ui.cad_box_icon.currentText(),
            "about": self.ui.cad_txt_bio.toPlainText(),
            "is_super": False,
            "is_moderator": False
        }
        cadastro_response = self.authRequests.signup(payload)

        if cadastro_response.httpCode == 200:
            print("cadastrado!")
            self.configs.current_user = cadastro_response.jsonResponse.get('data')

            err_msg = QMessageBox()
            err_msg.setIcon(QMessageBox.Icon.Information)
            err_msg.setWindowTitle("Cadastrado com sucesso!")
            err_msg.setText("Por favor, volte a tela incial e realize seu login agora.")
            err_msg.exec()

            self.close()
        else:
            err_msg = QMessageBox()
            err_msg.setIcon(QMessageBox.Icon.Warning)
            err_msg.setWindowTitle("Erro ao cadastrar!")
            err_msg.setText(cadastro_response.jsonResponse.get('message'))
            err_msg.exec()