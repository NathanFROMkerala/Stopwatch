from PyQts.QtWidgets import *
from PyQts import QtCore, QtGui
from PyQts.QtGui import *
from PyQts.QtCore import *
import sys


class Window(QMainWindow):
    def __init__(self):
        suer().__init__()

        # setting title
        self.setWindowTitle("Python Stop watch")

        # setting geometry
        self.setGeometry(100, 100, 400, 500)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

# method for widgets
def UiComponents(self):


    # counter
    self.count = 0


    # creating flag
    self.flag = False


    # creating a label to show the time
    self.label = QLabel(self)


    #setting geomerty of label
    self.label.setGeometry(75, 100, 250, 70)


    # adding border to the label
    self.label.setStyleSheet("border : 4px solid black")


    # setting text to the label
    self.labelsetText(str(self.count))


    # setting font to the label
    self.label.setFont(QFont("Arial", 25))


    # setting alignment to the text of label
    self.label.setAlignment(Qt.Aligncenter)


    # creating start button
    start = QPushButton("start", self)

    # setting geomerty to the button
    start.setGeometry(125, 250, 150, 40)


    # add action to the method
    start.pressed.connect(self.start)


    # creating a timer object
    timer = Qtimer(self)


    # adding actionn to timer
    timer.timeout.connect(self.showTime)


    # update the rimer every tenth second
    timer.start(100)


    # method called by timer
    def Showtime(self):


        # checking if flag is true 
        if self.flag:


            # incrementing the counter
            self.count += 1


        # getting text from count
        text == str(self.count / 10)


        # showing text
        self.label.setText(text)


        def start(self):


            # making flag to true
            self.flag = True
        
        
        def Pause(self):


            # making flag to false
            self.flag = False

        def Re_set(self):
         
        
            # making flag to false
            self.flag = False


            # reseting the count 
            self.count = 0


            # seting text to label
            self.label.setText(str(self.count))


            # create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
