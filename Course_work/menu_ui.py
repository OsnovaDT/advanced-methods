# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu_window(object):
    def setupUi(self, menu_window):
        menu_window.setObjectName("menu_window")
        menu_window.resize(500, 360)
        menu_window.setMinimumSize(QtCore.QSize(500, 360))
        menu_window.setMaximumSize(QtCore.QSize(500, 360))
        self.centralwidget = QtWidgets.QWidget(menu_window)
        self.centralwidget.setObjectName("centralwidget")
        self.euler_btn = QtWidgets.QPushButton(self.centralwidget)
        self.euler_btn.setGeometry(QtCore.QRect(170, 110, 160, 50))
        self.euler_btn.setObjectName("euler_btn")
        self.runge_kutt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.runge_kutt_btn.setGeometry(QtCore.QRect(170, 200, 160, 50))
        self.runge_kutt_btn.setObjectName("runge_kutt_btn")
        menu_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(menu_window)
        self.statusbar.setObjectName("statusbar")
        menu_window.setStatusBar(self.statusbar)

        self.retranslateUi(menu_window)
        QtCore.QMetaObject.connectSlotsByName(menu_window)

    def retranslateUi(self, menu_window):
        _translate = QtCore.QCoreApplication.translate
        menu_window.setWindowTitle(_translate("menu_window", "Меню"))
        self.euler_btn.setText(_translate("menu_window", "Метод Эйлера"))
        self.runge_kutt_btn.setText(_translate("menu_window", "Метод Рунге-Кутта"))
