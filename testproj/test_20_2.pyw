# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys
app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle(u"Bывoд окна по центру экрана")
desktop = QtGui.QApplication.desktop()
x = (desktop.width() - window.width()) // 2
y = (desktop.height() - window.height()) // 2
window.move(x, y)

window.show()
sys.exit(app.exec_()) #Запускаем цикл обработки