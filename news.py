import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from bs4 import BeautifulSoup as soup


class Ui_NewsWindow(object):

    # A function to close current window and show home window
    def closeCurrentShowMainWindow(self, main_window, news_window):
        main_window.show()
        news_window.close()

    def setupUi(self, NewsWindow, MainWindow):
        NewsWindow.setObjectName("NewsWindow")
        NewsWindow.resize(532, 602)
        font = QtGui.QFont()
        font.setPointSize(11)
        NewsWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(NewsWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Set background color, font color, font size, and font family for central widget
        self.centralwidget.setStyleSheet(
            "background-color: #3C4E60; color: #FFFFFF; font-size: 22px; font-family: Arial;"
        )

        self.headingLabel = QtWidgets.QLabel(self.centralwidget)
        self.headingLabel.setGeometry(QtCore.QRect(111, 0, 301, 41))
        self.headingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headingLabel.setObjectName("headingLabel")

        self.homeButton = QtWidgets.QPushButton(self.centralwidget,
                                                clicked = lambda: self.closeCurrentShowMainWindow(MainWindow, NewsWindow))
        self.homeButton.setGeometry(QtCore.QRect(10, 0, 91, 41))
        self.homeButton.setObjectName("homeButton")

        self.headlinesListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.headlinesListWidget.setGeometry(QtCore.QRect(5, 60, 521, 508))
        self.headlinesListWidget.setWordWrap(True)
        self.headlinesListWidget.setObjectName("headlinesListWidget")
        self.headlinesListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.headlinesListWidget.setStyleSheet(
            "QListWidget { background-color: rgba(0, 0, 0, 0.5); border: none; }"
            "QListWidget::item { padding: 5px; margin: 0px; line-height: 2.2em;"
            "font-size: 20px; } "
            "QListWidget::item:selected { background-color: #3C4E60; border: none;}"
        )

        NewsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NewsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 532, 36))
        self.menubar.setObjectName("menubar")

        NewsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NewsWindow)
        self.statusbar.setObjectName("statusbar")
        NewsWindow.setStatusBar(self.statusbar)

        self.display_news_headlines()

        self.retranslateUi(NewsWindow)
        QtCore.QMetaObject.connectSlotsByName(NewsWindow)

    def retranslateUi(self, NewsWindow):
        _translate = QtCore.QCoreApplication.translate
        NewsWindow.setWindowTitle(_translate("NewsWindow", "News Headlines"))
        self.headingLabel.setText(_translate("NewsWindow", "Today\'s News Headlines"))
        self.homeButton.setText(_translate("NewsWindow", "Home"))

    def display_news_headlines(self):
        # List of websites to crawl
        websites = {
            "NBCNEWS": "https://www.nbcnews.com",
            "BBC": "https://www.bbc.com/news",
            "CNN": "https://www.cnn.com",
            # Add more websites as needed
        }

        headlines = {}
        counter = 0

        for source, url in websites.items():
            try:
                # Fetch HTML content of the website
                r = requests.get(url)
                b = soup(r.content, 'lxml')

                # Extract headlines
                for headline in b.findAll('h2'):
                    if source not in headlines.keys():
                        headlines[source] = [headline.text.strip()]
                    else:
                        headlines[source].extend([headline.text.strip()])

                    if counter == 5:
                        counter = 0
                        break
                    counter += 1
            except:
                counter = 0
                continue

        # Display headlines in the list widget
        for src in headlines.keys():
            for hl in headlines[src]:
                if len(hl.split()) > 3:
                    item = QListWidgetItem(f"{src}: {hl}")
                    self.headlinesListWidget.addItem(item)
        else:
            if len(headlines) == 0:
                item = QListWidgetItem("Failed to load headlines")
                self.headlinesListWidget.addItem(item)
