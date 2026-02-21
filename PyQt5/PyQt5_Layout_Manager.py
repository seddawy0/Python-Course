print("##################### PyQt5 Layout Managers ######################")
import sys # System
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI") # The title on the top left of the window
        self.setGeometry(700, 300, 500, 500) # x-axis, y-axis, width, height
        self.setWindowIcon(QIcon("D:\\Work\\Python\\PyQt5\\icon.jpg")) # The icon on the top left
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)
        label1.setStyleSheet("background-color: #992bfb;"
                             "font-weight: bold;")
        label2.setStyleSheet("background-color: #fb2b53;"
                             "font-weight: bold;")
        label3.setStyleSheet("background-color: #2bfbf7;"
                             "font-style: italic;")
        label4.setStyleSheet("background-color: #2bfb8f;"
                             "font-weight: bold;")
        label5.setStyleSheet("background-color: #effb2b;"
                             "font-weight: bold;")
        # VERTICAL
        # vbox = QVBoxLayout()
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)
        # central_widget.setLayout(vbox)
        
        # HORIZONTAL
        # hbox = QHBoxLayout()
        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)
        # central_widget.setLayout(hbox)
        
        # GRID
        grid = QGridLayout()
        grid.addWidget(label1, 0, 0) # row_num, column_num
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 0, 2)
        grid.addWidget(label4, 1, 0)
        grid.addWidget(label5, 1, 1)
        central_widget.setLayout(grid)
        
def main():
    app = QApplication(sys.argv) # argv =  A list of command line arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # Window won't close unless I closed it by myself
if __name__ == "__main__":
    main()
print("################################################################")