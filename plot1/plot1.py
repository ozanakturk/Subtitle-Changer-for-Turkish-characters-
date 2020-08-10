# This is a test code for the EEE STAR Project written by Ozan Aktürk.
# I designed the layout via using Qt Designer. I saved it as a .ui file and then converted it to a .py file.
# I used line 20 and defined show_sine and show_cosine functions and linked those functions to sine and cosine buttons
# The other lines of code are generated automatically by pyuic5
# I exported sine and cosine plots by using matplotlib and numpy libraries in python


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 751)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plot = QtWidgets.QLabel(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(80, 0, 640, 480))
        self.plot.setText("")
        #self.plot.setPixmap(QtGui.QPixmap("sine_wave.jpg"))
        self.plot.setScaledContents(True)
        self.plot.setObjectName("plot")
        self.sine = QtWidgets.QPushButton(self.centralwidget)
        self.sine.setGeometry(QtCore.QRect(0, 490, 411, 91))
        self.sine.setObjectName("sine")
        self.cosine = QtWidgets.QPushButton(self.centralwidget)
        self.cosine.setGeometry(QtCore.QRect(420, 490, 381, 91))
        self.cosine.setObjectName("cosine")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.sine.clicked.connect(self.show_sine)
        self.cosine.clicked.connect(self.show_cosine)

    def show_sine(self):
        self.plot.setPixmap(QtGui.QPixmap("sine_wave.jpg"))

    def show_cosine(self):
        self.plot.setPixmap(QtGui.QPixmap("cosine_wave.jpg"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sine.setText(_translate("MainWindow", "Show sin(x)"))
        self.cosine.setText(_translate("MainWindow", "Show cos(x)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
