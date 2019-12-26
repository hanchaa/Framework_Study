import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("radiobutton.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.groupBox_rad1.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad2.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad3.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad4.clicked.connect(self.groupboxRadFunction)

    def groupboxRadFunction(self):
        if self.groupBox_rad1.isChecked():
            print("GroupBox_rad1 Chekced")
        elif self.groupBox_rad2.isChecked():
            print("GroupBox_rad2 Checked")
        elif self.groupBox_rad3.isChecked():
            print("GroupBox_rad3 Checked")
        elif self.groupBox_rad4.isChecked():
            print("GroupBox_rad4 Checked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

