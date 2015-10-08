# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, QtSql
import sys, main_window


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.db = None
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # Отображаем окно
    sys.exit(app.exec_()) #Запускаем цикл обработки