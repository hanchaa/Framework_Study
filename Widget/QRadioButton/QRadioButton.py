import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        rbtn1 = QRadioButton("First Button", self)
        rbtn1.move(50, 50)
        rbtn1.setChecked(True)

        rbtn2 = QRadioButton(self)
        rbtn2.move(50, 70)
        rbtn2.setText("Second Button")

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("QRadioButton")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec_()