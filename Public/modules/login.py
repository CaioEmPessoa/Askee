from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *

from AskeeRequests import *
from Interatcion.configs import Configs

from windows.login import Ui_jan_login
from modules.cadastro import cadastro
from modules.telaposts import telaposts

import os,sys

class login(QDialog):
    def __init__(self, *args, **argvs):
        super(login,self).__init__(*args,**argvs)
        self.usersRequests = Users()
        self.authRequests = Auth()
        self.configs = Configs()

        self.ui = Ui_jan_login()
        self.ui.setupUi(self)
        self.ui.log_butt_enter.clicked.connect(self.login)
        self.ui.log_butt_cadst.clicked.connect(self.tela_cadastro)

    def login(self):
        login_response = self.authRequests.login({
            "email": self.ui.log_line_login.text(),
            "password": self.ui.log_line_passwd.text()
        })

        if login_response.httpCode == 200:
            self.configs.current_user = login_response.jsonResponse.get('data')
            self.window = telaposts()
            self.window.show()
        else:
            err_msg = QMessageBox()
            err_msg.setIcon(QMessageBox.Icon.Warning)
            err_msg.setText("Login incorreto!")
            err_msg.exec()

    def tela_cadastro(self):
        add = cadastro()
        add.exec_()
