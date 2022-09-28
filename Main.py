from PyQt5 import QtGui, QtWidgets, QtCore
import sys 
from UI import MainUI



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def Window():
    ui = MainUI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
Window()
sys.exit(app.exec_())