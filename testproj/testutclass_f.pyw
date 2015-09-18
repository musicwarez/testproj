# -*- coding: utf-8 -*-
__author__ = 'alex'
# Вот это круть
from PyQt4 import QtCore, QtGui, uic
import sys, MyForm_


class MyDialog(QtGui.QDialog, MyForm_.Ui_MyForm):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.pushButton, QtCore.SIGNAL( "clicked()"),
                      QtGui.qApp.quit)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyDialog()
    window.show()
    # Отображаем окно
    sys.exit(app.exec_()) #Запускаем цикл обработки

