from PyQt5 import QtWidgets,QtCore
import sys

from UI.MainUI import *
from PyQt5.QtWidgets import QFileDialog

from Review_list import*
import Debug
from ReviewFilesList import *
import Settings as SettingsModuleModul
from Report.Report_process_all_files import *

class ReviewTool():
    def __init__(self,MainWindow):
        self.MainWindow = MainWindow
        self.UI = Ui_MainWindow()
        self.UI.setupUi(MainWindow)
        self.ConnectButtonToFunction()
        self.Project_Name = "None"
        self.File_Name_With_Extension = "None"
        self.File_Name = "None"
        self.Full_Path_File_Recent_Choose = "None"
        self.ReviewMode = 1 # 0: None 1: DD only, 2 RR only, 3 DD and RR


    # Functions control button
    def ConnectButtonToFunction(self):
        self.UI.ChooseFileButton.clicked.connect(self.ChooseFileButtonClicked)
        self.UI.ReviewButton.clicked.connect(self.Review)
        self.UI.ExitButton.clicked.connect(self.Close)
        self.UI.ItemDD.clicked.connect(self.GetReviewItemValue)
        self.UI.ItemRR.clicked.connect(self.GetReviewItemValue)
        


    def ChooseFileButtonClicked(self):
        filename = QFileDialog.getOpenFileName(None, "Open File")
        FullPathFile = filename[0]
        self.Full_Path_File_Recent_Choose = FullPathFile
        if self.Full_Path_File_Recent_Choose != "None" and "/" in self.Full_Path_File_Recent_Choose:
            self.File_Name_With_Extension = self.Full_Path_File_Recent_Choose.split("/")[-1]

        self.Set_Current_Setting_Area()

    def Close(self):
        self.MainWindow.close()


    # Functions get value 
    def GetReviewItemValue(self):
        if self.UI.ItemDD.isChecked() == True and self.UI.ItemRR.isChecked() == True:
            self.ReviewMode = 3
        elif self.UI.ItemDD.isChecked() == False and self.UI.ItemRR.isChecked() == True:
            self.ReviewMode = 2
        elif self.UI.ItemDD.isChecked() == True and self.UI.ItemRR.isChecked() == False:
            self.ReviewMode = 1
        else: 
            self.ReviewMode = 0

    # Functions set value
    def Set_Current_Setting_Area(self):
        self.UI.File_Name.setText(self.File_Name_With_Extension)
        self.UI.File_Name.setAlignment(QtCore.Qt.AlignRight)
        self.UI.File_Name.adjustSize()

        self.UI.Project_Name.setText(self.Project_Name)
        self.UI.File_Name.setAlignment(QtCore.Qt.AlignRight)
        self.UI.Project_Name.adjustSize()
    def Review(self):
        SettingsModule.ReadSettings()
        print(self.Full_Path_File_Recent_Choose)
        Debug.ReviewMode = str(self.ReviewMode)
        if self.Full_Path_File_Recent_Choose != "None" and ".docx" in self.Full_Path_File_Recent_Choose:
            Review_DD(self.Full_Path_File_Recent_Choose,True)
        else:
            print("???? File has not choose yet")
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    RvOB = ReviewTool(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
