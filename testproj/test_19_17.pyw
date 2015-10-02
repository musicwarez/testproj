# -*- coding: utf-8 -*-
__author__ = 'alex'

from PyQt4 import QtCore, QtGui
from Queue import Queue
import time


class MyThread(QtCore.QThread):
    def __init__(self, id, queue, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.id = id
        self.queue = queue

    def run(self):
        print "run()"
        while True:
            task = self.queue.get()
            # Получаем задание
            #self.sleep(1)
            # Имитируем обработку
            self.emit(QtCore.SIGNAL("taskDone(int, int)"),
                      task, self.id)
            # Передаем данные обратно
            self.queue.task_done()


class MyWindow(QtGui.QPushButton):
    def __init__(self, parent=None):
        QtGui.QPushButton.__init__(self)
        self.setText(u"Раздать задания")
        self.queue = Queue()
        # Создаем очередь
        self.threads = []
        for i in range(0, 2):
            # Создаем потоки и запускаем
            thread = MyThread(i, self.queue)
            # Ссылки на объекты потоков
            self.threads.append(thread)
            self.connect(thread, QtCore.SIGNAL("taskDone(int, int)"),
                         self.on_task_done, QtCore.Qt.QueuedConnection)
            print "thread.start()"
            thread.start()
            self.connect (self, QtCore.SIGNAL("clicked()"),
                          self.on_add_task)

    def on_add_task(self):
        print "on_add_task()"
        for i in range(0, 5):
            self.queue.put(i)
            # Добавляем задания в очередь
        #time.sleep(2)

    def on_task_done(self, data, id):
        print ("on_task_done task - ", data, "- MyThread_id =", id)
        # Выводим обработанные данные

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    # Создаем экземпляр
    window.setWindowTitle(u"Использование модуля queue")
    window.resize(300, 30)
    window.show()
    # Отображаем окно
    sys.exit(app.exec_()) #Запускаем цикл обработки