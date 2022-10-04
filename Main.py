from concurrent.futures import thread
from PyQt5 import QtWidgets,QtCore
import sys
from UI.MainUI import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSignal
import time

from Review_list import*
import Debug
from ReviewFilesList import *
import Settings as SettingsModule
from Report.Report_process_all_files import *


msg_welcome = ["Let me know which file you want to review",
 "Click choose file button to select your file",
 "Please close and save all .docx and .xlsx files to avoid losing data! DD review tool will close them without saving"]

msg_review = ["Reviewing","Reviewing.","Reviewing..","Reviewing..."]

msg_reviewing = ["DD has not been reviewed yet, please wait",
"DD has not been reviewed yet, please wait.",
"DD has not been reviewed yet, please wait..",
"DD has not been reviewed yet, please wait...",]

msg_choose_wrong = ["Only review .docx file", "Choose file again!!"]

class ReviewTool(QtWidgets.QMainWindow):
    msg = "Welcome"
    def __init__(self):
        super().__init__()
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        self.ConnectButtonToFunction()
        self.Project_Name = "None"
        self.File_Name_With_Extension = "None"
        self.File_Name = "None"
        self.Full_Path_File_Recent_Choose = "None"
        self.ReviewMode = 1 # 0: None 1: DD only, 2 RR only, 3 DD and RR
        self.thread = {}
        self.thread[1] = ThreadClass(index=1)
        self.thread[2] = ThreadClass(index=2)
        self.thread[2].Get_UI_Ob(self.UI)
        self.thread[2].start()



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
        
        self.Project_Name = self.Full_Path_File_Recent_Choose.replace("C:/Projects/","").split("/")[0]
        
        
        if ".docx" not in self.File_Name_With_Extension:
            ReviewTool.msg = "ChooseWrong"
        else:
            ReviewTool.msg = "You choose " + str(self.File_Name_With_Extension)
        self.Set_Current_Text()

    def Close(self):
        self.close()

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
    def Set_Current_Text(self):
        self.UI.File_Name.setText(self.File_Name_With_Extension)
        self.UI.File_Name.setAlignment(QtCore.Qt.AlignRight)
        self.UI.File_Name.adjustSize()

        self.UI.Project_Name.setText(self.Project_Name)
        self.UI.File_Name.setAlignment(QtCore.Qt.AlignRight)
        self.UI.Project_Name.adjustSize()
        


    def Review(self):
        if ".docx" in self.Full_Path_File_Recent_Choose:
            if self.thread[1].isRunning() == False:
                self.thread[1] = ThreadClass(index=1)
                self.thread[1].Set_Para(self.Full_Path_File_Recent_Choose,self.ReviewMode)
                self.thread[1].start()
                ReviewTool.msg = "StartReview"
            else:
                ReviewTool.msg = "Reviewing"
        else:
            ReviewTool.msg = "ChooseWrong"
        self.Set_Current_Text()


class ThreadClass(QtCore.QThread):
    signal = pyqtSignal(int)
    def __init__(self,index):
        super().__init__()
        self.index = index

    def Set_Para(self,DDpath,ReviewMode):
        self.DDpath = DDpath
        self.ReviewMode = ReviewMode

    def Get_UI_Ob(self,UI_Ob):
        self.UI_Ob = UI_Ob
    def run(self):
        if self.index == 1:
            SettingsModule.ReadSettings()
            Debug.ReviewMode = str(self.ReviewMode)
            try:
                Review_DD(self.DDpath,True)
            except:
                Kill_Excel_Word_Processes()
                Review_DD(self.DDpath,True)
            ReviewTool.msg = "Complete"
        elif self.index == 2:
            cnt = 0
            delay = 2
            
            while True:
                if "You choose " in ReviewTool.msg or ReviewTool.msg == "Welcome":
                    delay = 2
                else:
                    delay = 1
                self.UI_Ob.msg.setText(Get_Text(ReviewTool.msg,cnt))
                time.sleep(delay)
                cnt =cnt + 1

def Get_Text(input_text,cnt):
    Text = input_text
    if input_text == "Welcome":
        idx = cnt%len(msg_welcome)
        return msg_welcome[idx]
    elif input_text == "StartReview":
        idx = cnt%len(msg_review)
        return msg_review[idx]
    elif input_text == "Reviewing":
        idx = cnt%len(msg_reviewing)
        return msg_reviewing[idx]
    elif input_text == "ChooseWrong":
        idx = cnt%len(msg_choose_wrong)
        return msg_choose_wrong[idx]
    else:
        return Text

def Kill_Excel_Word_Processes():
    for proc in psutil.process_iter():
        if proc.name() == "EXCEL.EXE" or proc.name() == "WINWORD.EXE":
            proc.kill()

def main():
    app = QtWidgets.QApplication(sys.argv)
    RvOB = ReviewTool()
    RvOB.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()




