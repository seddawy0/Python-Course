print("##################### PyQt5 Line Edits ######################")
import sys # System
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI") # The title on the top left of the window
        self.setGeometry(700, 300, 500, 500) # x-axis, y-axis, width, height
        self.setWindowIcon(QIcon("D:\\Work\\Python\\PyQt5\\icon.jpg")) # The icon on the top left
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit" ,self)
        self.initUI()
        
    def initUI(self):
        self.line_edit.setGeometry(10 ,10, 200, 40)
        self.button.setGeometry(210, 10, 100, 40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;")
        self.line_edit.setPlaceholderText("Enter your name")
        self.button.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;")
        
        self.button.clicked.connect(self.submit)
    
    def submit(self):
        text = self.line_edit.text()
        print(f"Hello, {text}")
        
def main():
    app = QApplication(sys.argv) # argv =  A list of command line arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # Window won't close unless I closed it by myself
if __name__ == "__main__":
    main()
print("#############################################################")