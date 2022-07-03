from pyqt5.QtWidges import *
from pyqt5.QtGui import *
from pyqt5.QtCore import *
from pyqt5.QtWenEngineWidgets import *

class MyWebBrowser(QMainWindow):

    def ___init__(self,*args, **kwargs):
        super(MyWebBrowser,self).__init__(*args, **kwargs)

        self.Window = QWidget()

        self.Window.setWindowTitle("NeuralNine Web Browser")

        #ui elements

        self.layout= QVBoxLayout()
        self.horizontal  = QHBoxLayout()
        
        self.url_bar = QTextEdit()
        self.url_bar.setMaximuMHeight(30)

        self.go_btn =QPushButton("Go")
        self.go_btn.setMinmumHeight(30)

        self.back_btn =QPushButton("<")
        self.back_btn.setMinmumHeight(30)

        self.forwad_btn =QPushButton(">")
        self.forwad_btn.setMinmumHeight(30)

        self.horizontal.addWidget(self.url_btn)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forwad_btn)

        self.browser = QWebEngineView()

       
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()

