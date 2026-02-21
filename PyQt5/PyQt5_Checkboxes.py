print("##################### PyQt5 Checkboxes ######################")
import sys # System
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI") # The title on the top left of the window
        self.setGeometry(700, 300, 500, 500) # x-axis, y-axis, width, height
        self.setWindowIcon(QIcon("D:\\Work\\Python\\PyQt5\\icon.jpg")) # The icon on the top left
        self.checkbox = QCheckBox("Do you love programming?", self)
        self.initUI()
    def initUI(self):
        self.checkbox.setGeometry(10, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Times New Roman;")
        # self.checkbox.setChecked(True) # Will make it checked as a defult 
        self.checkbox.setChecked(False) # Will make it NOT checked as a defult 
        self.checkbox.stateChanged.connect(self.checkbox_checked)
    def checkbox_checked(self, state):
        if state == Qt.Checked:
            print("You love programming")
        else:
            print("You don't love programming")
def main():
    app = QApplication(sys.argv) # argv =  A list of command line arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # Window won't close unless I closed it by myself
if __name__ == "__main__":
    main()
print("############################################################")