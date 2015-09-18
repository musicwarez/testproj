# -*- coding: utf-8 -*-
__author__ = 'alex'

from PyQt4 import QtCore, QtGui, uic


class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        uic.loadUi("MyForm.ui", self)
        self.connect(self.pushButton, QtCore.SIGNAL( "clicked()"),
                      QtGui.qApp.quit)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyDialog()
    window.show()
    # Отображаем окно
    sys.exit(app.exec_()) #Запускаем цикл обработки

