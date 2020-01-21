import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel("QTimeEdit")

        timeedit = QTimeEdit(self)
        timeedit.setTime(QTime.currentTime())
        timeedit.setTimeRange(QTime(3, 00, 00), QTime(23, 30, 00))
        timeedit.setDisplayFormat("hh:mm:ss")

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(timeedit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle("QTimeEdit")
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
        app = QApplication(sys.argv)
        ex = MyWindow()
        app.exec_()