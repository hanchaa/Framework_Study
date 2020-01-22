import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.textEdit = QTextEdit()

        self.initUI()

    def initUI(self):
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon("open.png"), "Open", self)
        openFile.setShortcut("Ctrl+Q")
        openFile.setStatusTip("Open New File")
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(openFile)

        self.setWindowTitle("File Dialog")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "./")

        if fname[0]:
            f = open(fname[0], "r")

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec_()
