import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from user_input import *


class User(QMainWindow, Ui_mainWindow):
    dstNum = -1

    def __init__(self, parent=None):
        super(User, self).__init__(parent)
        self.setupUi(self)

        self.btnOK.setDisabled(True)
        self.txtEnter.textChanged.connect(self.checkEnter)
        self.btnOK.clicked.connect(self.saveDst)

    def checkEnter(self):
        self.btnOK.setEnabled(True) if self.txtEnter.text() != "" else self.btnOK.setDisabled(True)

    def saveDst(self):
        try:
            User.dstNum = int(self.txtEnter.text()) if 1 <= int(self.txtEnter.text()) <= 3 \
                else self.txtEnter.setText("Must be an integer between 1 and 3")
        except ValueError:
            self.txtEnter.setText("Must be an integer between 1 and 3")


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = User()

    currentForm.show()
    currentApp.exec_()
