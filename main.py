from pyqt5.QtWidges import *
from pyqt5.QtCore import *
from pyqt5.QtWenEngineWidgets import *

class MyWebBrowser():

    def ___init__(self):
    

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

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forwad_btn.clicked.connect(self.browser.forwad)
       
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()


    def navigate(self , url):
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))


app =QApplication()
window = MyWebBrowser()
app.exec_()

