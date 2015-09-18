# -*- coding: utf-8 -*-
__author__ = 'alex'

from PyQt4 import QtCore, QtGui, uic
import sys

app = QtGui.QApplication(sys.argv)
window = uic.loadUi("MyForm.ui")
QtCore.QObject.connect(window.pushButton, QtCore.SIGNAL( "clicked()") ,
                      QtGui.qApp.quit)
window.show()
# Отображаем окно
sys.exit(app.exec_()) #Запускаем цикл обработки