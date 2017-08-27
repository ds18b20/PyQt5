#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Show Hello world window"""

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize


class HelloWindow(QMainWindow):
    def __init__(self):
        super(HelloWindow, self).__init__()

        self.setMinimumSize(QSize(320, 240))
        self.setWindowTitle("Hello world")
        # set name label
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.nameLabel.move(20, 20)
        # set line
        self.line = QLineEdit(self)
        self.line.resize(200, 32)
        self.line.move(80, 20)
        # set button
        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200, 32)
        pybutton.move(80, 60)

    def clickMethod(self):
        print('Your name: ' + self.line.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit(app.exec_())
