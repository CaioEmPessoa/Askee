from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
from telas.post import Ui_MainWindow
from modulos.comentario import comentario
import os,sys

class post(QMainWindow):
    def __init__(self,*args,**argvs):
        super(post,self).__init__(*args,**argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.post_butt_coment.clicked.connect(self.add_comentario)

    def add_comentario(self):
        add = comentario()
        add.exec_()

