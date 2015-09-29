# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt, SIGNAL
import time
__author__ = 'alex'


class MyWindow(QtGui.QPushButton):
    def __init__(self):
        QtGui.QPushButton.__init__(self)
        self.setText (u"Закрыть окно")
        self.connect(self, SIGNAL("clicked()"), QtGui.qApp.quit)

    def load_data(self, sp):
        for i in range(1, 11):
            # Имитируем процесс
            QtCore.QThread.msleep(100)
            print "log i ", i
            # Что-то загружаем
            sp.showMessage(u"Загрузка данных {0}%".format(i * 10) ,
                            Qt.AlignHCenter | Qt.AlignBottom, Qt.black)
            QtGui.qApp.processEvents() # Запускаем оборот цикла

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    splash = QtGui.QSplashScreen(QtGui.QPixmap("img.png"))
    splash.showMessage(u"Загрузка данных ... 0%",
                       Qt.AlignCenter | Qt.AlignBottom, Qt.black)
    splash.show()
    QtGui.qApp.processEvents()
    window = MyWindow()
    # Создаем экземпляр
    window.setWindowTitle(u"Использование класса QSplashScreen")
    window.resize(300, 30)
    window.load_data(splash)
    splash.finish(splash)
    window.show()
    # Отображаем окно
    sys.exit(app.exec_()) #Запускаем цикл обработки