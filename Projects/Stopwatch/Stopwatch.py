import sys
from PyQt5.QtWidgets import QApplication,QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from PyQt5.QtCore import QTime, QTimer, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.start_button = QPushButton("Start",self)
        self.stop_button = QPushButton("Stop",self)
        self.reset_button = QPushButton("Reset",self)
        self.time = QTime(0, 0, 0, 0) #H M S MS
        self.time_label = QLabel("00:00:00.00", self)
        self.timer = QTimer(self)
        
        self.initUI()
        
    def initUI(self):
        self.setWindowIcon(QIcon("D:/Work/Python/Projects/Stopwatch/Stopwatch.png"))
        self.setStyleSheet("""
                        QWidget{
                            background-color: black;
                        }
                        QPushButton{
                              background-color: #2bfb9b;
                              font-size: 60px;
                              font-weight: bold;
                              padding: 15px;
                              margin: 75px, 10px; 
                              border: 3px solid;
                              border-radius: 30px;
                          }
                        QPushButton:hover{
                            background-color: green;
                        }
                        QLabel{
                            font-size: 150px;
                            font-weight: bold;
                            background-color: #2bfb9b;
                            border-radius: 30px;
                            color: black;
                        }  
                        """)
        self.setWindowTitle("Stopwatch")
        font_id = QFontDatabase.addApplicationFont("D:/Work/Python/Projects/Digital Clock/DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 100)

        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)
        
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)
    def start(self):
        self.timer.start(10)
    def stop(self):
        self.timer.stop()
    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))
    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))
def main():
    app = QApplication(sys.argv)
    watch = Stopwatch()
    watch.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
