import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel("QDateTimeEdit")

        datetimeedit = QDateTimeEdit(self)
        datetimeedit.setDateTime(QDateTime.currentDateTime())
        datetimeedit.setDateTimeRange(QDateTime(1900, 1, 1, 00, 00, 00), QDateTime(2100, 12, 31, 23, 59, 59))
        datetimeedit.setDisplayFormat("yyyy.MM.dd ap h:mm:ss")

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(datetimeedit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle("QDateTimeEdit")
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec_()