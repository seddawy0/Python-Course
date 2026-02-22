print("##################### PyQt5 CSS Styles ######################")
import sys # System
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI") # The title on the top left of the window
        # We don't need it anymore because we have a layout manager
        # self.setGeometry(700, 300, 500, 500) # x-axis, y-axis, width, height 
        self.setWindowIcon(QIcon("D:\\Work\\Python\\PyQt5\\icon.jpg")) # The icon on the top left
        self.button1 = QPushButton("#1") # We don't need to add self here because we use layout manager)
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        
        central_widget.setLayout(hbox)
        
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        
        self.setStyleSheet("""
                          QPushButton{
                              font-size: 20px;
                              font-family: Arial;
                              padding: 15px 50px;
                              margin: 25px; 
                              border: 3px solid;
                              border-radius: 20px;
                          } 
                          QPushButton#button1{
                              background-color: #b32300;
                          }
                          QPushButton#button2{
                              background-color: #ffff3c;
                          }
                          QPushButton#button3{
                              background-color: #3cff5e;
                          }
                          QPushButton#button1:hover{
                              background-color: #8e3cff;
                          }
                          QPushButton#button2:hover{
                              background-color: #3ce5ff;
                          }
                          QPushButton#button3:hover{
                              background-color: #ff3c8c;
                          }
                    """)
def main():
    
    app = QApplication(sys.argv) # argv =  A list of command line arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # Window won't close unless I closed it by myself
if __name__ == "__main__":
    main()
print("#############################################################")