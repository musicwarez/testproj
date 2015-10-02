# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


def show_modal_window():
    global modalWindow
    modalWindow = QtGui.QWidget(windowl, QtCore.Qt.Window)
    modalWindow.setWindowTitle(u"Moдaльнoe окно")
    modalWindow.resize(200, 50)
    modalWindow.setWindowModality(QtCore.Qt.WindowModal)
    modalWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
    modalWindow.move(windowl.geometry().center() -
    modalWindow.rect().center() - QtCore.QPoint(4, 30))
    modalWindow.show()

app = QtGui.QApplication(sys.argv)
windowl = QtGui.QWidget()
windowl.setWindowTitle(u"Обычное окно")
windowl.resize(300, 100)
button = QtGui.QPushButton(u"Открьть модальное окно")
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"),
                       show_modal_window)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(button)
windowl.setLayout(vbox)
windowl.show()
window2 = QtGui.QWidget()
window2.setWindowTitle(u"Этo окно не будет блокировано при WindowModal")
window2.resize(500, 100)
window2.show()
sys.exit(app.exec_()) #Запускаем цикл обработки