# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\victo\Desktop\Nova pasta\uis\logged.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebKitWidgets import *
import sip
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKit import *
from PyQt5.QtNetwork import *

class Ui_Logged(object):
    def setupUi(self, Logged):
        Logged.setObjectName("Logged")
        Logged.resize(1366, 768)
        Logged.setStyleSheet("background: transparent;")
        self.centralwidget = QtWidgets.QWidget(Logged)
        self.centralwidget.setStyleSheet("background: transparent;\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.background.setFont(font)
        self.background.setStyleSheet("background: transparent;\n"
"background-color: rgb(236, 240, 245);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.lat_preto = QtWidgets.QLabel(self.centralwidget)
        self.lat_preto.setGeometry(QtCore.QRect(0, 0, 361, 768))
        self.lat_preto.setStyleSheet("background: transparent;\n"
"background-color: rgb(34, 45, 50);\n"
"border-style: solid;\n"
"border-color: transparent;")
        self.lat_preto.setText("")
        self.lat_preto.setAlignment(QtCore.Qt.AlignCenter)
        self.lat_preto.setObjectName("lat_preto")
        self.sup_verde = QtWidgets.QLabel(self.centralwidget)
        self.sup_verde.setGeometry(QtCore.QRect(0, 0, 1366, 51))
        self.sup_verde.setStyleSheet("background: transparent;\n"
"background-color: rgb(255, 85, 0);\n"
"border-style: solid;\n"
"border-color: transparent;")
        self.sup_verde.setText("")
        self.sup_verde.setAlignment(QtCore.Qt.AlignCenter)
        self.sup_verde.setObjectName("sup_verde")

        self.web = QWebView(self.centralwidget)
        self.web.setGeometry(QtCore.QRect(361, 51, 1011, 721))
        self.web.setObjectName("web")

        Logged.setCentralWidget(self.centralwidget)

        self.retranslateUi(Logged)
        QtCore.QMetaObject.connectSlotsByName(Logged)

    def retranslateUi(self, Logged):
        _translate = QtCore.QCoreApplication.translate
        Logged.setWindowTitle(_translate("Logged", "Logged"))

