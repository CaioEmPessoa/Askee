from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *

from telas.login import Ui_jan_login
from modulos.cadastro import cadastro
from modulos.telaposts import telaposts

import os,sys

class login(QDialog):
    def __init__(self, *args, **argvs):
        super(login,self).__init__(*args,**argvs)
        self.ui = Ui_jan_login()
        self.ui.setupUi(self)
        self.ui.log_butt_enter.clicked.connect(self.login)
        self.ui.log_butt_cadst.clicked.connect(self.add)

    def login(self):
        usuario = "luca"
        senha = "1234"

        user = self.ui.log_line_login.text()
        password = self.ui.log_line_passwd.text()

        if user == usuario and senha == password:
            self.window = telaposts()
            self.window.show()
        else:
            QMessageBox.warning(QMessageBox(),"login incorreto!")

    def add(self):
        add = cadastro()
        add.exec_()
