# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow{\n"
"border-image: url(:/bg/background.jpg)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(490, 270, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-top-color: rgb(86, 86, 64);\n"
"border-right-color: rgb(86, 86, 64);\n"
"border-bottom-color: rgb(86, 86, 64);\n"
"border-left-color: rgb(86, 86, 64);\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.ItemDD = QtWidgets.QRadioButton(self.groupBox)
        self.ItemDD.setGeometry(QtCore.QRect(10, 20, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ItemDD.setFont(font)
        self.ItemDD.setChecked(True)
        self.ItemDD.setAutoExclusive(False)
        self.ItemDD.setObjectName("ItemDD")
        self.ItemRR = QtWidgets.QRadioButton(self.groupBox)
        self.ItemRR.setGeometry(QtCore.QRect(10, 50, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ItemRR.setFont(font)
        self.ItemRR.setAutoExclusive(False)
        self.ItemRR.setObjectName("ItemRR")
        self.ReviewButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReviewButton.setGeometry(QtCore.QRect(490, 381, 121, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ReviewButton.setFont(font)
        self.ReviewButton.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ReviewButton.setObjectName("ReviewButton")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(490, 410, 121, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ExitButton.setFont(font)
        self.ExitButton.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ExitButton.setObjectName("ExitButton")
        self.label_Current_Setting = QtWidgets.QLabel(self.centralwidget)
        self.label_Current_Setting.setGeometry(QtCore.QRect(50, 60, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_Current_Setting.setFont(font)
        self.label_Current_Setting.setObjectName("label_Current_Setting")
        self.ChooseFile = QtWidgets.QPushButton(self.centralwidget)
        self.ChooseFile.setGeometry(QtCore.QRect(490, 352, 121, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ChooseFile.setFont(font)
        self.ChooseFile.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.ChooseFile.setObjectName("ChooseFile")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 100, 118, 56))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_Project_Name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_Project_Name.setFont(font)
        self.label_Project_Name.setObjectName("label_Project_Name")
        self.gridLayout.addWidget(self.label_Project_Name, 0, 0, 1, 1)
        self.Project_Name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Project_Name.setFont(font)
        self.Project_Name.setObjectName("Project_Name")
        self.gridLayout.addWidget(self.Project_Name, 0, 1, 1, 1)
        self.label_Flie_Name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_Flie_Name.setFont(font)
        self.label_Flie_Name.setObjectName("label_Flie_Name")
        self.gridLayout.addWidget(self.label_Flie_Name, 1, 0, 1, 1)
        self.File_Name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.File_Name.setFont(font)
        self.File_Name.setObjectName("File_Name")
        self.gridLayout.addWidget(self.File_Name, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Review Item"))
        self.ItemDD.setText(_translate("MainWindow", "Detail Dessign"))
        self.ItemRR.setText(_translate("MainWindow", "Review Record"))
        self.ReviewButton.setText(_translate("MainWindow", "Review"))
        self.ExitButton.setText(_translate("MainWindow", "Exit"))
        self.label_Current_Setting.setText(_translate("MainWindow", "Current Setting"))
        self.ChooseFile.setText(_translate("MainWindow", "Choose File"))
        self.label_Project_Name.setText(_translate("MainWindow", "Project:"))
        self.Project_Name.setText(_translate("MainWindow", "None"))
        self.label_Flie_Name.setText(_translate("MainWindow", "File"))
        self.File_Name.setText(_translate("MainWindow", "None"))
import BackGround_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
