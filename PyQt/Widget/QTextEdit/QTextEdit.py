import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.lbl1 = QLabel("Enter  your sentence:")
        self.te = QTextEdit()
        self.lbl2 = QLabel("The number of words is 0")

        self.initUI()

    def initUI(self):
        self.te.setAcceptRichText(False)

        self.te.textChanged.connect(self.text_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.te)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle("QTextEdit")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def text_changed(self):
        text = self.te.toPlainText()
        self.lbl2.setText("The number of words is " + str(len(text.split())))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec_()