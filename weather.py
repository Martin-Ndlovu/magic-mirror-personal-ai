from _datetime import datetime

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer


class Ui_WeatherWindow(object):

    # A function to close current window and show home window
    def closeCurrentShowMainWindow(self, main_window, weather_window):
        main_window.show()
        weather_window.close()


    def setupUi(self, WeatherWindow, MainWindow):
        WeatherWindow.setObjectName("WeatherWindow")
        WeatherWindow.resize(532, 602)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        WeatherWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(WeatherWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.homeButton = QtWidgets.QPushButton(self.centralwidget,
                                                clicked=lambda: self.closeCurrentShowMainWindow(MainWindow, WeatherWindow))

        self.homeButton.setGeometry(QtCore.QRect(10, 0, 93, 28))

        # set background
        self.centralwidget.setStyleSheet(
            "background-color: #2C3E50; color: #FFFFFF; font-size: 22px; font-family: Arial;")

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.homeButton.setFont(font)
        self.homeButton.setObjectName("homeButton")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(30, 40, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(30, 110, 256, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")

        self.temperature_in_f_Label = QtWidgets.QLabel(self.centralwidget)
        self.temperature_in_f_Label.setGeometry(QtCore.QRect(30, 170, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.temperature_in_f_Label.setFont(font)
        self.temperature_in_f_Label.setObjectName("temperature_in_f_Label")

        self.locationLabel = QtWidgets.QLabel(self.centralwidget)
        self.locationLabel.setGeometry(QtCore.QRect(30, 230, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.locationLabel.setFont(font)
        self.locationLabel.setObjectName("locationLabel")

        self.horizontalLine = QtWidgets.QFrame(self.centralwidget)
        self.horizontalLine.setGeometry(QtCore.QRect(0, 270, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.horizontalLine.setFont(font)
        self.horizontalLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontalLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalLine.setObjectName("horizontalLine")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(300, 30, 231, 201))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        # Add image to the scene
        image_path = "weather.jpeg"
        self.add_image_to_scene(image_path)

        self.rainfallLabel = QtWidgets.QLabel(self.centralwidget)
        self.rainfallLabel.setGeometry(QtCore.QRect(300, 240, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.rainfallLabel.setFont(font)
        self.rainfallLabel.setObjectName("rainfallLabel")

        self.humidityLabel = QtWidgets.QLabel(self.centralwidget)
        self.humidityLabel.setGeometry(QtCore.QRect(300, 280, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.humidityLabel.setFont(font)
        self.humidityLabel.setObjectName("humidityLabel")

        self.windLabel = QtWidgets.QLabel(self.centralwidget)
        self.windLabel.setGeometry(QtCore.QRect(300, 320, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.windLabel.setFont(font)
        self.windLabel.setObjectName("windLabel")

        self.pressureLabel = QtWidgets.QLabel(self.centralwidget)
        self.pressureLabel.setGeometry(QtCore.QRect(300, 360, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pressureLabel.setFont(font)
        self.pressureLabel.setObjectName("pressureLabel")

        self.sunriseLabel = QtWidgets.QLabel(self.centralwidget)
        self.sunriseLabel.setGeometry(QtCore.QRect(300, 400, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sunriseLabel.setFont(font)
        self.sunriseLabel.setObjectName("sunriseLabel")

        self.sunsetLabel = QtWidgets.QLabel(self.centralwidget)
        self.sunsetLabel.setGeometry(QtCore.QRect(300, 440, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sunsetLabel.setFont(font)
        self.sunsetLabel.setObjectName("sunsetLabel")

        self.moonriseLabel = QtWidgets.QLabel(self.centralwidget)
        self.moonriseLabel.setGeometry(QtCore.QRect(300, 480, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.moonriseLabel.setFont(font)
        self.moonriseLabel.setObjectName("moonriseLabel")

        self.cloudLabel = QtWidgets.QLabel(self.centralwidget)
        self.cloudLabel.setGeometry(QtCore.QRect(300, 520, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cloudLabel.setFont(font)
        self.cloudLabel.setObjectName("cloudLabel")

        self.todayPredLabel = QtWidgets.QLabel(self.centralwidget)
        self.todayPredLabel.setGeometry(QtCore.QRect(30, 290, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.todayPredLabel.setFont(font)
        self.todayPredLabel.setObjectName("todayPredLabel")

        self.day2PredLabel = QtWidgets.QLabel(self.centralwidget)
        self.day2PredLabel.setGeometry(QtCore.QRect(30, 350, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.day2PredLabel.setFont(font)
        self.day2PredLabel.setObjectName("day2PredLabel")

        self.day3PredLabel = QtWidgets.QLabel(self.centralwidget)
        self.day3PredLabel.setGeometry(QtCore.QRect(30, 400, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.day3PredLabel.setFont(font)
        self.day3PredLabel.setObjectName("day3PredLabel")

        self.day4PredLabel = QtWidgets.QLabel(self.centralwidget)
        self.day4PredLabel.setGeometry(QtCore.QRect(30, 460, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.day4PredLabel.setFont(font)
        self.day4PredLabel.setObjectName("day4PredLabel")

        self.day5Predlabel = QtWidgets.QLabel(self.centralwidget)
        self.day5Predlabel.setGeometry(QtCore.QRect(30, 510, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.day5Predlabel.setFont(font)
        self.day5Predlabel.setObjectName("day5Predlabel")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(280, 280, 16, 271))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        WeatherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WeatherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 532, 26))
        self.menubar.setObjectName("menubar")
        WeatherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WeatherWindow)
        self.statusbar.setObjectName("statusbar")
        WeatherWindow.setStatusBar(self.statusbar)

        # Update date and time every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000)  # Update every second

        # Initial update
        self.updateDateTime()

        try:
            self.get_weather_data(WeatherWindow)
        except:
            self.temperature_in_f_Label.setText("Failed to get weather data")
        QtCore.QMetaObject.connectSlotsByName(WeatherWindow)

    def add_image_to_scene(self, image_path):
        pixmap = QtGui.QPixmap(image_path)
        pixmap_item = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(pixmap_item)
        pixmap_item.setPos(0, 0)

    def retranslateUi(self, WeatherWindow, weather_data, city_name):
        weather_data = weather_data.split(',')

        temperature = weather_data[0]
        humidity = weather_data[1]
        rainfall = weather_data[2]
        wind = weather_data[3]
        pressure = weather_data[4]
        sunrise = weather_data[5]
        sunset = weather_data[6]
        clouds = weather_data[7]
        moon_phase = weather_data[8]
        moonrise = weather_data[9]
        day_length = weather_data[10]
        min_temp = weather_data[11]
        max_temp = weather_data[12]

        pred_days = self.get_next_days()

        _translate = QtCore.QCoreApplication.translate
        WeatherWindow.setWindowTitle(_translate("WeatherWindow", "Weather Status"))
        self.homeButton.setText(_translate("WeatherWindow", "Home"))
        self.dateLabel.setText(_translate("WeatherWindow", "Date"))
        self.timeLabel.setText(_translate("WeatherWindow", "Time"))
        self.temperature_in_f_Label.setText(_translate("WeatherWindow", "Temperature    {}".format(temperature)))
        self.locationLabel.setText(_translate("WeatherWindow", "{}".format(city_name)))
        self.rainfallLabel.setText(_translate("WeatherWindow", "Rainfall        {}".format(rainfall)))
        self.humidityLabel.setText(_translate("WeatherWindow", "Humidity      {}".format(humidity)))
        self.windLabel.setText(_translate("WeatherWindow", "Wind           {}".format(wind)))
        self.pressureLabel.setText(_translate("WeatherWindow", "Pressure      {}".format(pressure)))
        self.sunriseLabel.setText(_translate("WeatherWindow", "Sunrise        {}".format(sunrise)))
        self.sunsetLabel.setText(_translate("WeatherWindow", "Sunset         {}".format(sunset)))
        self.moonriseLabel.setText(_translate("WeatherWindow", "Moonrise      {}:05".format(moonrise)))
        self.cloudLabel.setText(_translate("WeatherWindow", "Day Length  {}".format(day_length)))
        self.todayPredLabel.setText(_translate("WeatherWindow", "Today   {}  18      30".format(clouds)))
        self.day2PredLabel.setText(_translate("WeatherWindow", "".join("{:<{width}} {}  20     32".format(pred_days[0][:3], clouds, width=11))))
        self.day3PredLabel.setText(_translate("WeatherWindow", "".join("{:<{width}} {}  19     32".format(pred_days[1][:3], clouds, width=11))))
        self.day4PredLabel.setText(_translate("WeatherWindow", "".join("{:<{width}} {}  20     30".format(pred_days[2][:3], clouds, width=11))))
        self.day5Predlabel.setText(_translate("WeatherWindow", "".join("{:<{width}} {}  16     28".format(pred_days[3][:3], clouds, width=11))))

    # ============== A FUNCTION TO UPDATE TIME EVERY SECOND ======================
    def updateDateTime(self):
        # Get current datetime
        current_datetime = datetime.now()

        # Separate date and time
        current_date = current_datetime.strftime("%A %d %B %Y")  # Format date as "Day DD Month Year"
        current_time = current_datetime.strftime("%H:%M:%S")  # Format time as "Hour:Minute:Second"

        self.dateLabel.setText(current_date)
        self.timeLabel.setText(current_time)

    # ================= A FUNCTION TO FETCH WEATHER DATA =================
    def get_weather_data(self, WeatherWindow):
        # Sending requests to get the IP Location Information
        # res = requests.get('https://ipinfo.io/')

        res = requests.get('http://ip-api.com/json/')

        # Receiving the response in JSON format
        data = res.json()

        # Extracting the Location of the City from the response
        citydata = data['city']
        cityName = data.get('city')

        # Passing the City name to the url
        url = 'https://wttr.in/{}?format=%t,%h,%p,%w,%P,%S,%s,%c,%C,%M,%D,%1,%h'.format(citydata)

        # Getting the Weather Data of the City
        res = requests.get(url)

        self.retranslateUi(WeatherWindow, res.text, cityName)

    def get_next_days(self):
        current_datetime = datetime.now()

        current_date = current_datetime.strftime("%A")

        day_index = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}

        days = list(day_index.keys())
        current_index = day_index[current_date] + 1

        pred_days = []

        for i in range(4):
            current_index = current_index % 7
            pred_days.append(days[current_index])
            current_index += 1

        return pred_days