import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from user_input import *


class User(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(User, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = User()

    currentForm.show()
    currentApp.exec_()
