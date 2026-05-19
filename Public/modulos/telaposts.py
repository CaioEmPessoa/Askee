from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *

from telas.telaposts import Ui_MainWindow
from modulos.post import post
import os,sys

class telaposts(QMainWindow):
    def __init__(self,*args,**argvs):
        super(telaposts,self).__init__(*args,**argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.main_butt_post.clicked.connect(self.post)

    def post(self):
        self.window = post()
        self.window.show()

    