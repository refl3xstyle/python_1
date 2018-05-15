#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, pickle
from PyQt5.QtWidgets import QApplication, QWidget
from GraphGUI.ui_MainWindow import *



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())