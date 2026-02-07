from _datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer

from weather import Ui_WeatherWindow
from news import Ui_NewsWindow
from music import Ui_MusicWindow
from voicechat import Ui_VoiceChatWindow


class Ui_MainWindow(object):
    # A function to open weather window

    def openNewWindow(self, window):
        self.window = QtWidgets.QMainWindow()
        self.ui = window()
        self.ui.setupUi(self.window, MainWindow)
        self.window.show()
        MainWindow.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 600)
        font = QtGui.QFont()
        font.setKerning(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Set background image
        self.centralwidget.setStyleSheet("background-color: #2C3E50; color: #FFFFFF; font-size: 22px; font-family: Arial;")

        # self.centralwidget.setStyleSheet(
        #     "background-image: url('weather.jpeg'); background-repeat: no-repeat; background-position: center;")

        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(130, 130, 341, 41 ))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(False)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")

        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(130, 280, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(False)
        self.date_label.setFont(font)
        self.date_label.setText("")
        self.date_label.setObjectName("date_label")

        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(130, 420, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(False)
        self.time_label.setFont(font)
        self.time_label.setText("")
        self.time_label.setObjectName("time_label")

        self.weather_button = QtWidgets.QPushButton(self.centralwidget)
        self.weather_button.clicked.connect(lambda: self.openNewWindow(Ui_WeatherWindow))
        self.weather_button.setGeometry(QtCore.QRect(80, 0, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(False)
        self.weather_button.setFont(font)
        self.weather_button.setObjectName("weather_button")
        self.home_label = QtWidgets.QLabel(self.centralwidget)
        self.home_label.setGeometry(QtCore.QRect(10, 0, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.home_label.setFont(font)
        self.home_label.setObjectName("home_label")

        self.news_button = QtWidgets.QPushButton(self.centralwidget)
        self.news_button.clicked.connect(lambda: self.openNewWindow(Ui_NewsWindow))
        self.news_button.setGeometry(QtCore.QRect(180, 0, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(False)
        self.news_button.setFont(font)
        self.news_button.setObjectName("news_button")

        self.voice_assstant_button = QtWidgets.QPushButton(self.centralwidget)
        self.voice_assstant_button.clicked.connect(lambda: self.openNewWindow(Ui_VoiceChatWindow))
        self.voice_assstant_button.setGeometry(QtCore.QRect(380, 0, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(False)
        self.voice_assstant_button.setFont(font)
        self.voice_assstant_button.setObjectName("voice_assistant_button")

        self.music_button = QtWidgets.QPushButton(self.centralwidget)
        self.music_button.clicked.connect(lambda: self.openNewWindow(Ui_MusicWindow))
        self.music_button.setGeometry(QtCore.QRect(280, 0, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(False)
        self.music_button.setFont(font)
        self.music_button.setObjectName("music_button")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Update date and time every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000)  # Update every second

        # Initial update
        self.updateDateTime()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Magic mirror"))
        self.welcome_label.setText(_translate("MainWindow", "Welcome to Magic Mirror"))
        self.weather_button.setText(_translate("MainWindow", "Weather"))
        self.home_label.setText(_translate("MainWindow", "Home"))
        self.news_button.setText(_translate("MainWindow", "News"))
        self.voice_assstant_button.setText(_translate("MainWindow", "Voice Chat"))
        self.music_button.setText(_translate("MainWindow", "Music"))


    def updateDateTime(self):
        # Get current datetime
        current_datetime = datetime.now()

        current_date = current_datetime.strftime("%A %d %B %Y")  # Format date as "Day DD Month Year"
        current_time = current_datetime.strftime("%H:%M:%S")  # Format time as "Hour:Minute:Second"
        self.date_label.setText(current_date)
        self.time_label.setText(current_time)

        # Apply lock screen style
        # self.date_label.setStyleSheet("background-color: #2C3E50; color: #FFFFFF; font-size: 36px; font-family: Arial;")
        # self.time_label.setStyleSheet("background-color: #2C3E50; color: #FFFFFF; font-size: 36px; font-family: Arial;")




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
