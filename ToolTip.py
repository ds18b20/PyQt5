#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Show Hello world window"""

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize


class HelloWindow(QMainWindow):
    def __init__(self):
        super(HelloWindow, self).__init__()

        self.setMinimumSize(QSize(320, 240))
        self.setWindowTitle("Window Title")

        py_button = QPushButton('Click me', self)
        py_button.clicked.connect(self.click_method)
        py_button.setToolTip('This is a tooltip for the QPushButton widget')
        py_button.resize(100, 32)
        py_button.move(50, 50)

    def click_method(self):
        self.dummy()
        print('Clicked PyQt5 button')

    def dummy(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit(app.exec_())
