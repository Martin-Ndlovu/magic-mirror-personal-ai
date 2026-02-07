
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VoiceChatWindow(object):

    # A function to close current window and show home window
    def closeCurrentShowMainWindow(self, main_window, voicechat_window):
        main_window.show()
        voicechat_window.close()

    def setupUi(self, VoiceChatWindow, MainWindow):
        VoiceChatWindow.setObjectName("VoiceChatWindow")
        VoiceChatWindow.resize(531, 600)
        font = QtGui.QFont()
        font.setPointSize(13)
        VoiceChatWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(VoiceChatWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.homeButton = QtWidgets.QPushButton(self.centralwidget,
                                                clicked=lambda: self.closeCurrentShowMainWindow(MainWindow, VoiceChatWindow))
        self.homeButton.setGeometry(QtCore.QRect(10, 0, 93, 41))
        self.homeButton.setObjectName("homeButton")

        # set background
        self.centralwidget.setStyleSheet(
            "background-color: #2C3E50; color: #FFFFFF;")

        # self.centralwidget.setStyleSheet(
        #     "background-image: url('weather.jpeg'); background-repeat: no-repeat; background-position: center;")
        #
        self.wokeupButton = QtWidgets.QPushButton(self.centralwidget)
        self.wokeupButton.setGeometry(QtCore.QRect(200, 170, 131, 121))
        self.wokeupButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.wokeupButton.setFont(font)
        self.wokeupButton.setFlat(True)
        self.wokeupButton.setObjectName("wokeupButton")
        self.wokeupButton.clicked.connect(lambda: self.wakeup_callback())

        self.messageLabel = QtWidgets.QLabel(self.centralwidget)
        self.messageLabel.setGeometry(QtCore.QRect(20, 80, 511, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.messageLabel.setFont(font)
        self.messageLabel.setText("")
        self.messageLabel.setObjectName("messageLabel")
        self.messageLabel.setWordWrap(True)

        VoiceChatWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VoiceChatWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 36))
        self.menubar.setObjectName("menubar")
        VoiceChatWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VoiceChatWindow)
        self.statusbar.setObjectName("statusbar")
        VoiceChatWindow.setStatusBar(self.statusbar)

        self.retranslateUi(VoiceChatWindow)
        QtCore.QMetaObject.connectSlotsByName(VoiceChatWindow)

    def retranslateUi(self, VoiceChatWindow):
        _translate = QtCore.QCoreApplication.translate
        VoiceChatWindow.setWindowTitle(_translate("VoiceChatWindow", "Magic Mirror Voice Chat"))
        self.homeButton.setText(_translate("VoiceChatWindow", "Home"))
        self.wokeupButton.setText(_translate("VoiceChatWindow", "🎙️"))

    def wakeup_callback(self):
        self.messageLabel.setText("Functionality currently unavailable. Please go to music and try me!")
        # Call function to turn on voice interaction mode

    def music_play(self):
        pass
