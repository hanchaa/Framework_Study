import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton("Dialog", self)
        self.le = QLineEdit(self)

        self.initUI()

    def initUI(self):
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.le.move(120, 30)
        # self.le.setEnabled(False)

        self.setWindowTitle("Input Dialog")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name:")

        if ok:
            self.le.setText(str(text))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec_()
