from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *

from windows.telaposts import Ui_MainWindow
from modules.post import post
from modules.criarpost import criarpost
import os,sys

class telaposts(QMainWindow):
    def __init__(self,*args,**argvs):
        super(telaposts,self).__init__(*args,**argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.main_butt_post.clicked.connect(self.post)
        self.ui.main_butt_criarpost.clicked.connect(self.tela_criar_post)

    def post(self):
        self.window = post()
        self.window.show()

    def tela_criar_post(self):
        add = criarpost()
        add.exec_()
    