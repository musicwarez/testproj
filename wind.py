# -*- coding: utf-8 -*-

__author__ = 'alex'
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle(u"Это Пepвaя nрограмма")
window.resize(300, 70)
label = QtGui.QLabel(u"<center>Привет Пис !</center>")
btnQuit = QtGui.QPushButton(u"&Зaкpьrrь")
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)
window .setLayout(vbox)
QtCore.QObject.connect(btnQuit , QtCore.SIGNAL("clicked()"),
                       QtGui.qApp, QtCore.SLOT("quit()"))

window.show()
sys.exit(app.exec_())
