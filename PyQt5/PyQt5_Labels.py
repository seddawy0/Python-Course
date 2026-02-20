print("##################### PyQt5 Labels ######################")
import sys # System
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI") # The title on the top left of the window
        self.setGeometry(700, 300, 500, 500) # x-axis, y-axis, width, height
        self.setWindowIcon(QIcon("D:\\Work\\Python\\PyQt5\\icon.jpg")) # The icon on the top left
        
        label = QLabel("Hello World", self)
        label.setFont(QFont("Times New Roman", 50))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: black;" # CSS Properties
                            "background-color: #2bfbfb;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        # label.setAlignment(Qt.AligntTop) VERTICALLY TOP
        # label.setAlignment(Qt.AlignBottom) VERTICALLY BOTTOM
        # label.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER
        # label.setAlignment(Qt.AlignRight) # HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignLeft) # HORIZONTALLY LEFT
        # label.setAlignment(Qt.AlignHCenter) # HORIZONTALLY Center
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # CENTER 
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER & TOP
        # label.setAlignment(Qt.AlignCenter) # CENTER 
def main():
    app = QApplication(sys.argv) # argv =  A list of command line arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # Window won't close unless I closed it by myself
if __name__ == "__main__":
    main()
print("#########################################################")