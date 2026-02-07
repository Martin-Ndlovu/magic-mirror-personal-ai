import sys
import os
import random
import speech_recognition as sr
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QListWidget, QListWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MusicWindow(object):

    # A function to close current window and show home window
    def closeCurrentShowMainWindow(self, main_window, music_window):
        main_window.show()
        music_window.close()

    def setupUi(self, MusicWindow, MainWindow):
        MusicWindow.setObjectName("MusicWindow")
        MusicWindow.resize(531, 602)
        self.centralwidget = QtWidgets.QWidget(MusicWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Main layout for the central widget
        main_layout = QVBoxLayout(self.centralwidget)

        # Header layout
        header_layout = QHBoxLayout()

        self.songLabel = QtWidgets.QLabel(self.centralwidget)
        self.songLabel.setGeometry(QtCore.QRect(80, 0, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.songLabel.setFont(font)
        self.songLabel.setMouseTracking(False)
        self.songLabel.setAutoFillBackground(True)
        self.songLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.songLabel.setObjectName("songLabel")

        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(30, 90, 93, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.playButton.setFont(font)
        self.playButton.setAutoFillBackground(False)
        self.playButton.setDefault(False)
        self.playButton.setFlat(False)

        # set background
        self.centralwidget.setStyleSheet(
            "background-color: #2C3E50; color: #FFFFFF; font-size: 22px; font-family: Arial;")

        self.playButton.setObjectName("playButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(152, 90, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.nextButton.setFont(font)
        self.nextButton.setObjectName("nextButton")

        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(280, 90, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")

        self.voiceButton = QtWidgets.QPushButton(self.centralwidget)
        self.voiceButton.setGeometry(QtCore.QRect(410, 90, 93, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.voiceButton.setFont(font)
        self.voiceButton.setObjectName("voiceButton")

        self.SpeechResponseLabel = QtWidgets.QLabel(self.centralwidget)
        self.SpeechResponseLabel.setGeometry(QtCore.QRect(10, 50, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.SpeechResponseLabel.setFont(font)
        self.SpeechResponseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SpeechResponseLabel.setObjectName("SpeechResponseLabel")

        self.iconLabel = QtWidgets.QPushButton(self.centralwidget,
                                                clicked=lambda: self.closeCurrentShowMainWindow(MainWindow, MusicWindow))
        self.iconLabel.setGeometry(QtCore.QRect(10, 0, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.iconLabel.setFont(font)
        self.iconLabel.setObjectName("iconLabel")

        self.songsListView = QtWidgets.QListWidget(self.centralwidget)
        self.songsListView.setGeometry(QtCore.QRect(5, 161, 521, 410))
        self.songsListView.setStyleSheet(
            "QListWidget { border: none; padding: 10px; }"
            "QListWidget::item { padding: 20px; margin: 0px; border-radius: 1px; } "
            "QListWidget::item:selected { background-color: #3C4E60; border: none;}"

        )
        self.songsListView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        font = QtGui.QFont()
        font.setPointSize(13)
        self.songsListView.setFont(font)
        self.songsListView.setObjectName("songsListView")

        MusicWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MusicWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 26))
        self.menubar.setObjectName("menubar")
        MusicWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MusicWindow)
        self.statusbar.setObjectName("statusbar")
        MusicWindow.setStatusBar(self.statusbar)

        # Initialize Pygame
        pygame.init()

        # Load music files
        self.music_folder = "music"
        self.music_files = os.listdir(self.music_folder)

        # Populate music list widget
        for music_file in self.music_files:
            item = QListWidgetItem(music_file)
            self.songsListView.addItem(item)

        # Connect button signals to slots
        self.playButton.clicked.connect(self.play_music)
        self.nextButton.clicked.connect(self.next_song)
        self.stopButton.clicked.connect(self.close_playback)
        self.voiceButton.clicked.connect(self.start_speech_recognition)
        self.songsListView.itemDoubleClicked.connect(self.select_song)

        # Initialize SpeechRecognizer
        self.recognizer = sr.Recognizer()

        # Variable to store selected song
        self.selected_song = random.choice(self.music_files)

        self.retranslateUi(MusicWindow)
        QtCore.QMetaObject.connectSlotsByName(MusicWindow)

    def retranslateUi(self, MusicWindow):
        _translate = QtCore.QCoreApplication.translate
        MusicWindow.setWindowTitle(_translate("MusicWindow", "Music"))
        self.songLabel.setText(_translate("MusicWindow", "You can use voice to control music"))
        self.playButton.setText(_translate("MusicWindow", "Play ⏯️"))
        self.nextButton.setText(_translate("MusicWindow", "Next ⏭️"))
        self.stopButton.setText(_translate("MusicWindow", "Stop 🛑"))
        self.voiceButton.setText(_translate("MusicWindow", "Voice🎙️"))
        self.SpeechResponseLabel.setText(_translate("MusicWindow", ""))
        self.iconLabel.setText(_translate("MusicWindow", "<-🎵"))


    def play_music(self):
        if not self.selected_song:
            return

        # Play the selected music file
        music_path = os.path.join(self.music_folder, self.selected_song)
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play()
        self.songLabel.setText("Playing: " + self.selected_song)
        self.songsListView.itemDoubleClicked.connect(self.select_song)
        self.highlight_current_song()

    def next_song(self):
        # Stop the current music and play the next one
        pygame.mixer.music.stop()
        self.selected_song = random.choice(self.music_files)
        self.play_music()

    def close_playback(self):
        # Stop the music and close the app
        pygame.mixer.music.stop()

    def quit_music(self):
        # quit music application
        self.close_playback()
        QApplication.quit()

    def start_speech_recognition(self):
        self.selected_song = random.choice(self.music_files)
        self.voiceButton.setEnabled(False)
        with sr.Microphone() as source:
            self.SpeechResponseLabel.setText("Listening for speech...")
            try:
                audio = self.recognizer.listen(source)
                command = self.recognizer.recognize_google(audio)
                self.SpeechResponseLabel.setText("Recognized command: {}".format(command))
                # Execute command based on recognized speech
                if "play" in command.lower():
                    self.play_music()
                elif "next" in command.lower():
                    self.next_song()
                elif "stop" in command.lower():
                    self.close_playback()
                elif "close" in command.lower():
                    self.quit_music()
            except sr.UnknownValueError:
                self.SpeechResponseLabel.setText("Could not understand speech")
            except sr.RequestError as e:
                self.SpeechResponseLabel.setText(f"Error: {e}")
        self.voiceButton.setEnabled(True)

    def select_song(self, item):
        self.selected_song = item.text()
        self.play_music()

    def highlight_current_song(self):
        items = self.songsListView.findItems(self.selected_song, QtCore.Qt.MatchExactly)
        if items:
            item = items[0]
            self.songsListView.setCurrentItem(item)
            item.setSelected(True)
            self.songsListView.scrollToItem(item)