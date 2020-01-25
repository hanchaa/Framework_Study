import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        x = 0
        y = 0

        self.text = "x: {0}, y: {1}".format(x, y)
        self.label = QLabel(self.text, self)

        self.initUI()

    def initUI(self):
        self.label.move(20, 20)

        self.setMouseTracking(True)

        self.setWindowTitle("Reimplementing event handler")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_F:
            self.showFullScreen()
        elif e.key() == Qt.Key_N:
            self.showNormal()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        self.text = "x: {0}, y: {1}".format(x, y)
        self.label.setText(self.text)
        self.label.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec_()
