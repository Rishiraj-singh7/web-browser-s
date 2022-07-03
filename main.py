from pyqt5.QtWidges import *
from pyqt5.QtGui import *
from pyqt5.QtCore import *
from pyqt5.QtWenEngineWidgets import *

class MyWebBrowser(QMainWindow):

    def ___init__(self):
        super(MyWebBrowser,self).__init__(*args, **kwargs)

        self.Window = QtWidget()

        self.Window.setWindowTitle("NeuralNine Web Browser")
