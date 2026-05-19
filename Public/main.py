from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *

from modulos.login import login
import os,sys

app = QApplication(sys.argv)
if (QDialog.Accepted -- True):
    window = login()
    window.show()
sys.exit(app.exec_())


