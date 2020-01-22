import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton("Dialog", self)
        self.frm = QFrame(self)

        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)

        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.frm.setStyleSheet("QWidget { background-color: %s}" % col.name())
        self.frm.setGeometry(130, 30, 100, 100)

        self.setWindowTitle("Color Dialog")
        self.setGeometry(300, 300, 250, 180)
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s}" % col.name())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec_()
