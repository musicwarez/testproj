# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget() #Создаем окно
window.setWindowTitle(u"Зaгoлoвoк окна")
window.resize(300, 50)
app.setWindowIcon(QtGui.QIcon("020.jpg"))
window.setWindowIcon(QtGui.QIcon("020.jpg"))
window. show()
sys.exit(app.exec_()) #Запускаем цикл обработки