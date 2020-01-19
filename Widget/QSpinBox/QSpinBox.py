import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.lbl = QLabel("QSpinBox")
        self.spinbox = QSpinBox()
        self.lbl2 = QLabel("0")

        self.initUI()

    def initUI(self):
        self.spinbox.setMinimum(-10)
        self.spinbox.setMaximum(30)
        self.spinbox.setSingleStep(2)

        self.spinbox.valueChanged.connect(self.value_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl)
        vbox.addWidget(self.spinbox)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle("QSpinBox")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def value_changed(self):
        self.lbl2.setText(str(self.spinbox.value()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec_()