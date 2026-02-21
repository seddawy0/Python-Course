print("##################### PyQt5 Buttons ######################")
import sys # System
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI") # The title on the top left of the window
        self.setGeometry(700, 300, 500, 500) # x-axis, y-axis, width, height
        self.setWindowIcon(QIcon("D:\\Work\\Python\\PyQt5\\icon.jpg")) # The icon on the top left
        self.button = QPushButton("Click Me!", self)
        self.label = QLabel("Hello", self)
        self.initUI()
        
    def initUI(self):
            self.button.setGeometry(150, 200, 200, 100)
            self.button.setStyleSheet("font-size: 25px;")
            self.button.clicked.connect(self.on_click) # Signal
            self.label.setGeometry(150, 300, 200, 150)
            self.label.setStyleSheet("font-size: 40px;"
                                     "color: blue;")
    def on_click(self): 
        print("Button Clicked!")
        self.button.setStyleSheet("font-size: 25px;"
                                 "background-color: #2bfb73;")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)
        self.label.setText("GoodBye!")
        
def main():
    app = QApplication(sys.argv) # argv =  A list of command line arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # Window won't close unless I closed it by myself
if __name__ == "__main__":
    main()
print("##########################################################")