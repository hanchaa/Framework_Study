import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.pbar = QProgressBar(self)
        self.btn = QPushButton("Start", self)
        self.timer = QBasicTimer()
        self.step = 0

        self.initUI()

    def initUI(self):
        self.pbar.setGeometry(30, 40, 200, 25)
        # self.pbar.setRange(0, 0)

        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doACtion)

        self.setWindowTitle("QProgressBar")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText("Finished")
            return

        self.step += 1
        self.pbar.setValue(self.step)

    def doACtion(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText("Start")
        else:
            self.timer.start(100, self)
            self.btn.setText("Stop")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec_()