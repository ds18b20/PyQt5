#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Set window to center"""

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QDesktopWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # resize window
        self.resize(300, 200)
        # get window geometry
        qt_rectangle = self.frameGeometry()
        print('frameGeometry:{}'.format(qt_rectangle))
        # get desktop center
        center_point = QDesktopWidget().availableGeometry().center()
        print('center_point:{}'.format(center_point))
        # pass center position to /PyQt5.QtCore.QRect/
        qt_rectangle.moveCenter(center_point)
        # move to top left by center
        self.move(qt_rectangle.topLeft())
        print('qt_rectangle.topLeft:{}'.format(qt_rectangle.topLeft()))

        # set label
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(self)
        central_widget.setLayout(grid_layout)

        title = QLabel("Hello World from PyQt", self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        grid_layout.addWidget(title, 0, 0)

        # Set a title
        self.setWindowTitle("PyQt example")
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
