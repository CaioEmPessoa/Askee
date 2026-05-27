from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *

from modules.login import login
from modules.telaposts import telaposts
import os,sys

app = QApplication(sys.argv)
if (QDialog.Accepted -- True):
    # window = telaposts()
    window = login()
    window.show()
sys.exit(app.exec_())


