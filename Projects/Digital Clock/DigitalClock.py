import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from PyQt5.QtCore import QTime, QTimer, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
        self.update_time()
        
    def initUI(self):
        self.setGeometry(600, 300, 700, 150)
        self.setWindowIcon(QIcon("D:/Work/Python/Projects/Digital Clock/clock.png"))
        self.setStyleSheet("background-color: black;")
        self.time_label.setStyleSheet("color: #05ff00;"
                                      "font-size: 150px;")
        self.setWindowTitle("Digital Clock Program")
        font_id = QFontDatabase.addApplicationFont("D:/Work/Python/Projects/Digital Clock/DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 100)
        self.time_label.setFont(my_font)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignCenter)
        
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)
    
def main():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
