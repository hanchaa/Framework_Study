import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Communicate(QObject):
    closeApp = pyqtSignal()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.c = Communicate()

        self.initUI()

    def initUI(self):
        self.c.closeApp.connect(self.close)

        self.setWindowTitle("Emitting Signal")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mousePressEvent(self, e):
        self.c.closeApp.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec_()
