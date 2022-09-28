from PyQt5 import QtGui, QtWidgets, QtCore
import sys 
from UI.MainUI import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
# Create application with main window
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()


# Create class and set up when init with self.setupUi(MainWindow)
class UI(Ui_MainWindow):
    def __init__(self):
        self.setupUi(MainWindow)
        self.ChooseFile.clicked.connect(UI.ChooseFileButtonClicked)
        

    def ChooseFileButtonClicked(self):
        filename = QFileDialog.getOpenFileName(None, "Open File")
        print(filename[0])
def Window():
    ui = UI()
    MainWindow.show()

Window()

sys.exit(app.exec_())



