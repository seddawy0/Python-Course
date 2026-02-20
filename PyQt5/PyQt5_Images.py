print("##################### PyQt5 Images ######################")
import sys # System
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Images") # The title on the top left of the window
        self.setGeometry(700, 300, 500, 500) # x-axis, y-axis, width, height
        self.setWindowIcon(QIcon("D:\\Work\\Python\\PyQt5\\icon.jpg")) # The icon on the top left
        
        img_label = QLabel(self) # Self Refers to the 'window' object
        img_label.setGeometry(0, 0, 250, 250)
        
        pixmap = QPixmap("D:\\Work\\Python\\PyQt5\\icon.jpg")
        img_label.setPixmap(pixmap)
        
        img_label.setScaledContents(True) # Without this the photo won't be scaled 
        
        img_label.setGeometry((self.width()- img_label.width()) // 2, # To centerlized it to the window
                              (self.height()- img_label.height()) // 2,
                              (img_label.width()),
                              (img_label.height()))
def main():
    app = QApplication(sys.argv) # argv =  A list of command line arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # Window won't close unless I closed it by myself
if __name__ == "__main__":
    main()
print("#######################################################")