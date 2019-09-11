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
        self.btnOK.setGeometry(QtCore.QRect(240, 70, 71, 32))
        self.btnOK.setObjectName("btnOK")
        self.edtEnter = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.edtEnter.setGeometry(QtCore.QRect(50, 70, 171, 31))
        self.edtEnter.setObjectName("edtEnter")
        self.lblEnter = QtWidgets.QLabel(self.centralwidget)
        self.lblEnter.setGeometry(QtCore.QRect(50, 40, 271, 16))
        self.lblEnter.setObjectName("lblEnter")
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
        self.lblEnter.setText(_translate("mainWindow", "Please enter the destination number below:"))


