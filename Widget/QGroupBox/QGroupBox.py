import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(self.createFirstExclusiveGroup(), 0, 0)
        grid.addWidget(self.createSecondExclusiveGroup(), 1, 0)
        grid.addWidget(self.createNonExclusiveGroup(), 0, 1)
        grid.addWidget(self.createPushButtonGroup(), 1, 1)

        self.setLayout(grid)

        self.setWindowTitle("QGroupBox")
        self.setGeometry(300, 300, 480, 200)
        self.show()

    def createFirstExclusiveGroup(self):
        groupbox = QGroupBox("Exclusive Radio Buttons")

        radio1 = QRadioButton("Radio1")
        radio2 = QRadioButton("Radio2")
        radio3 = QRadioButton("Radio3")
        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        groupbox.setLayout(vbox)

        return groupbox

    def createSecondExclusiveGroup(self):
        groupbox = QGroupBox("Exclusive Radio Buttons")
        groupbox.setCheckable(True)
        groupbox.setChecked(False)

        radio1 = QRadioButton("Radio1")
        radio2 = QRadioButton("Radio2")
        radio3 = QRadioButton("Radio3")
        radio1.setChecked(True)
        checkbox = QCheckBox("Independent Checkbox")
        checkbox.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addWidget(checkbox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def createNonExclusiveGroup(self):
        groupbox = QGroupBox("Non-Exclusive Checkboxes")
        groupbox.setFlat(True)

        checkbox1 = QCheckBox("Checkbox1")
        checkbox2 = QCheckBox("Checkbox2")
        checkbox2.setChecked(True)
        tristatebox = QCheckBox("Tri-state Button")
        tristatebox.setTristate(True)

        vbox = QVBoxLayout()
        vbox.addWidget(checkbox1)
        vbox.addWidget(checkbox2)
        vbox.addWidget(tristatebox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def createPushButtonGroup(self):
        groupbox = QGroupBox("Push Buttons")
        groupbox.setCheckable(True)
        groupbox.setChecked(True)

        pushbutton = QPushButton("Normal Button")
        togglebutton = QPushButton("ToggleButton")
        togglebutton.setCheckable(True)
        togglebutton.setChecked(True)
        flatbutton = QPushButton("Flat Button")
        flatbutton.setFlat(True)
        popbutton = QPushButton("Pop Button")
        menu = QMenu(self)
        menu.addAction("First Item")
        menu.addAction("Second Item")
        menu.addAction("Third Item")
        menu.addAction("Fourth Item")
        popbutton.setMenu(menu)

        vbox = QVBoxLayout()
        vbox.addWidget(pushbutton)
        vbox.addWidget(togglebutton)
        vbox.addWidget(flatbutton)
        vbox.addWidget(popbutton)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec_()