# -*- coding: utf-8 -*-
__author__ = 'alex'

from PyQt4 import QtCore, QtGui


class MyThread(QtCore.QThread):
    x = 10
    # Атрибут класса
    mutex = QtCore.QMutex()
    # Мыаrекс

    def __init__(self, id, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.id = id

    def run(self):
        self.change_x()

    def change_x(self):
        m1 = QtCore.QMutexLocker(MyThread.mutex)
        # Блокируем
        print("x =", MyThread.x, "id -", self.id)
        MyThread.x += 5
        self.sleep(1)
        print("x =", MyThread.x, "id -", self.id)
        MyThread.x += 10
        print ( "x =", MyThread.x, "id -", self.id)
        MyThread.mutex.unlock()
        # Снимаем блокировку


class MyWindow(QtGui.QPushButton):
    def __init__(self):
        QtGui.QPushButton.__init__(self)
        self.setText(u"Гоу про")
        self.thread1 = MyThread(1)
        self.thread2 = MyThread(2)
        self.connect(self, QtCore.SIGNAL("clicked()"), self.on_start)

    def on_start(self):
        if not self.thread1.isRunning(): self.thread1.start()
        if not self.thread2.isRunning(): self.thread2.start()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    # Создаем экземпляр
    window.setWindowTitle(u"Использование класса QMutex")
    window.resize(300, 30)
    window.show()
    # Отображаем окно
    sys.exit(app.exec_()) #Запускаем цикл обработки