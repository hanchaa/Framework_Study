import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.slider = QSlider(Qt.Horizontal, self)
        self.dial = QDial(self)

        self.initUI()

    def initUI(self):
        self.slider.move(30, 30)
        self.slider.setRange(0, 50)
        self.slider.setSingleStep(2)

        self.dial.move(30, 50)
        self.dial.setRange(0, 50)

        btn = QPushButton("Default", self)
        btn.move(35, 160)

        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)
        btn.clicked.connect(self.button_clicked)

        self.setWindowTitle("QSlider and QDial")
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec_()