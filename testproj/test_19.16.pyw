# -*- coding: utf-8 -*-
__author__ = 'alex'

from PyQt4 import QtCore, QtGui
import MyWindow


class MyThread1(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.count = 0

    def run(self):
        print("MyThread1 run() -")
        self.exec_()

    def on_start(self):
        print("MyThread1 on_start() -")
        self.count += 1
        self.emit(QtCore.SIGNAL("s1(int)"),
                      self.count)
        #self.sleep(1) # Имитируем процесс


class MyThread2(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        print("MyThread2 run() -")
        self.exec_()

    def on_change(self, i):
        print("MyThread2 on_change() -")
        i += 10
        self.emit(QtCore.SIGNAL("s2(const QString&)"), "%d" % i)

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel(u"Haжмитe кнопку")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.button = QtGui.QPushButton(u"Сгенерировать сигнал")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)

        self.thread1 = MyThread1()
        self.thread2 = MyThread2()
        self.thread1.start()
        self.thread2.start()

        self.connect(self.button, QtCore.SIGNAL("clicked()"),
                     self.thread1.on_start)
        self.connect(self.thread1, QtCore.SIGNAL("s1(int)"),
                     self.thread2.on_change)
        self.connect(self.thread2, QtCore.SIGNAL("s2(const QString&)"),
                     self.label, QtCore.SLOT("setText(const QString&)"))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    # Создаем экземпляр
    window.setWindowTitle(u"Обмен сигналами между потоками")
    window.resize(345, 70)
    window.show()
    # Отображаем окно
    sys.exit(app.exec_()) #Запускаем цикл обработки