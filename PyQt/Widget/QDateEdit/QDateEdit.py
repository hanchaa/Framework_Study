import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel("QDateEdit")

        dateedit = QDateEdit(self)
        dateedit.setDate(QDate.currentDate())
        dateedit.setMinimumDate(QDate(1900, 1, 1))
        dateedit.setMaximumDate(QDate(2100, 12, 31))

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(dateedit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle("QDateEdit")
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec_()