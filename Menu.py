#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Show Hello world window"""

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QAction
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon


class HelloWindow(QMainWindow):
    def __init__(self):
        super(HelloWindow, self).__init__()

        self.setMinimumSize(QSize(320, 240))
        self.setWindowTitle("Hello world")

        # Add button widget
        py_button = QPushButton('Click me', self)
        py_button.clicked.connect(self.click_method)
        py_button.setToolTip('This is a tooltip for the QPushButton widget')
        py_button.resize(100, 32)
        py_button.move(50, 50)
        
        # Create new action
        new_action = QAction(QIcon('new.png'), '&New', self)
        new_action.setShortcut('Ctrl+N')
        new_action.setStatusTip('New document')
        new_action.triggered.connect(self.new_call)

        # Create new action
        open_action = QAction(QIcon('open.png'), '&Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Open document')
        open_action.triggered.connect(self.open_call)

        # Create exit action
        exit_action = QAction(QIcon('exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.exit_call)

        # Create menu bar and add action
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(exit_action)

    def open_call(self):
        self.dummy()
        print('Open')

    def new_call(self):
        self.dummy()
        print('New')

    def exit_call(self):
        self.dummy()
        print('Exit app')

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
