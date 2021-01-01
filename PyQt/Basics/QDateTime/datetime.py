import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# now = QDate.currentDate()
# print(now.toString(Qt.SystemLocaleShortDate))
#
# time = QTime.currentTime()
# print(time.toString('t AP h:m:s'))
#
# datetime = QDateTime.currentDateTime()
# print(datetime.toString('yyyy.M.d AP h:mm:ss'))


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.date = QDateTime.currentDateTime()
        self.setupUI()

    def setupUI(self):
        self.statusBar().showMessage(self.date.toString('yyyy년 MMMM d일 dddd AP h:mm:ss'))

        self.setWindowTitle('Date')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    app.exec_()