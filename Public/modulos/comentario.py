from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *

from telas.comentario import Ui_Dialog
import os,sys

class comentario(QDialog):
    def __init__(self,*args,**argvs):
        super(comentario,self).__init__(*args,**argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)