import sys
from time import sleep
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineCore import QWebEngineHttpRequest
from PyQt5 import QtTest
from urllib.parse import urlencode, urljoin, urlparse
from random import randint

# You can download this from:
# https://github.com/dwyl/english-words/blob/master/words.txt

with open("words.txt", "r") as w:
    words = w.readlines()

app = QApplication(sys.argv)

view = QWebEngineView()
view.setFixedSize(1280,480)

def Callable(html):
    if '<span class="gb_Rd">Sign in</span>' in html:
        print("PLEASE SIGN IN")
    else:
        url = "http://www.google.com/search?q=" + words[randint(0,len(words)-1)][:-1].replace(" ", "+")
        print(url)
        view.load(
            QWebEngineHttpRequest(
            QUrl(url)))
        QtTest.QTest.qWait(3000)

def on_load_finished(ok):
    if ok:
        view.page().toHtml(Callable)

view.loadFinished.connect(on_load_finished)
view.load(QWebEngineHttpRequest(QUrl("http://www.google.com")))
view.show()

sys.exit(app.exec_())