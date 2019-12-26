import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("checkbox.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.chk_1.stateChanged.connect(self.chkFunction)
        self.chk_2.stateChanged.connect(self.chkFunction)
        self.chk_3.stateChanged.connect(self.chkFunction)
        self.chk_4.stateChanged.connect(self.chkFunction)

        self.groupchk_1.stateChanged.connect(self.groupchkFunction)
        self.groupchk_2.stateChanged.connect(self.groupchkFunction)
        self.groupchk_3.stateChanged.connect(self.groupchkFunction)
        self.groupchk_4.stateChanged.connect(self.groupchkFunction)

    def chkFunction(self):
        if self.chk_1.isChecked(): print("chk_1 isChecked")
        if self.chk_2.isChecked(): print("chk_2 isChecked")
        if self.chk_3.isChecked(): print("chk_3 isChecked")
        if self.chk_4.isChecked(): print("chk_4 isChecked")

    def groupchkFunction(self):
        if self.groupchk_1.isChecked(): print("groupchk_1 isChecked")
        if self.groupchk_2.isChecked(): print("groupchk_2 isChecked")
        if self.groupchk_3.isChecked(): print("groupchk_3 isChecked")
        if self.groupchk_4.isChecked(): print("groupchk_4 isChecked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
