# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget(flags=QtCore.Qt.Dialog)
window.setWindowTitle(u"Bcплывaюшиe подсказки")
window.resize(300, 70)
button = QtGui.QPushButton (u"Закрьгrь окно", window)
button.setFixedSize(150, 30)
button.move(75, 20)
button.setToolTip (u"Это всплывающая подсказка для кнопки")
window.setToolTip(u"Этo всплывающая подсказка")


QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"),
                       window, QtCore.SLOT("close()"))
window.show()
sys.exit(app.exec_()) #Запускаем цикл обработки
QtCore.Q