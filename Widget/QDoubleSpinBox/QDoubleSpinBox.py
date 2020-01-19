import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.lbl1 = QLabel("QDoubleSpinBox")
        self.dspinbox = QDoubleSpinBox()
        self.lbl2 = QLabel("$ 0.0")

        self.initUI()

    def initUI(self):
        self.dspinbox.setRange(0, 100)
        self.dspinbox.setSingleStep(0.5)
        self.dspinbox.setPrefix("$ ")
        self.dspinbox.setDecimals(1)

        self.dspinbox.valueChanged.connect(self.value_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.dspinbox)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle("QDoubleSpinBox")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def value_changed(self):
        self.lbl2.setText("$ " + str(self.dspinbox.value()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec_()
