# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_input.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(598, 300)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOK = QtWidgets.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(320, 70, 81, 32))
        self.btnOK.setMinimumSize(QtCore.QSize(81, 32))
        self.btnOK.setObjectName("btnOK")
        self.lblEnter = QtWidgets.QLabel(self.centralwidget)
        self.lblEnter.setGeometry(QtCore.QRect(50, 40, 261, 16))
        self.lblEnter.setObjectName("lblEnter")
        self.txtEnter = QtWidgets.QLineEdit(self.centralwidget)
        self.txtEnter.setGeometry(QtCore.QRect(50, 70, 261, 31))
        self.txtEnter.setObjectName("txtEnter")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.btnOK.setText(_translate("mainWindow", "OK"))
        self.lblEnter.setText(_translate("mainWindow", "Please enter a destination number below:"))


