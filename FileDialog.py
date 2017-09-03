#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Show Hello world window"""

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtWidgets import QPushButton
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import QSize


class HelloWindow(QMainWindow):
    def __init__(self):
        super(HelloWindow, self).__init__()
        self.title = 'Add Text to PDF'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

        self.button_text = 'Select PDF File'
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        py_button = QPushButton(self.button_text, self)
        py_button.clicked.connect(self.click_method)
        py_button.resize(100, 32)
        py_button.move(50, 50)

        self.show()

        # self.open_file_name_dialog()
        # self.open_file_names_dialog()
        # self.save_file_dialog()

    def click_method(self):
        file_path = self.open_file_name_dialog()

    def dummy(self):
        pass

    def open_file_name_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(parent=self,
                                                   caption="QFileDialog.getOpenFileNames()",
                                                   directory="",
                                                   filter="All Files (*);;Python Files (*.py)",
                                                   options=options)
        if file_path:
            print(file_path)
            return file_path

    def open_file_names_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path_list, _ = QFileDialog.getOpenFileNames(parent=self,
                                                caption="QFileDialog.getOpenFileNames()",
                                                directory="",
                                                filter="All Files (*);;Python Files (*.py)",
                                                options=options)
        if file_path_list:
            print(file_path_list)
            return file_path_list

    def save_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(parent=self,
                                                   caption="QFileDialog.getOpenFileNames()",
                                                   directory="",
                                                   filter="All Files (*);;Python Files (*.py)",
                                                   options=options)
        if file_path:
            print(file_path)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit(app.exec_())
