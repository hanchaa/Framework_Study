import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
label = QLabel("Hello, PyQT")
label.show()

print("Before event loop")
app.exec_()
print("After event loop")