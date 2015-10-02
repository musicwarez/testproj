# -*- coding: utf-8 -*-
__author__ = 'alex'

from PyQt4 import QtCore, QtGui
import MyWindow


class MyThread(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = False
        self.count = 0

    def run(self):
        self.running = True
        while self.running: # Проверяем значение флага
            self.count += 1
            self.emit(QtCore.SIGNAL ("mysignal(QString) "),
                      "count  = %s" % self.count)
            self.sleep(1) # Имитируем процесс

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel(u"Haжмитe кнопку дnя запуска потока")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.btnStart = QtGui.QPushButton(u"Зaпycтить поток")
        self.btnStop = QtGui.QPushButton(u"Ocтaнoвить поток")
        self.btnClean = QtGui.QPushButton(u"Атчыстить")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnStart)
        self.vbox.addWidget(self.btnStop)
        self.vbox.addWidget(self.btnClean)
        self.setLayout(self.vbox)
        self.mythread = MyThread()
        self.connect(self.btnStart, QtCore.SIGNAL("clicked()"),
                     self.on_start)
        self.connect(self.btnStop, QtCore.SIGNAL("clicked()"),
                     self.on_stop)
        self.connect(self.btnClean, QtCore.SIGNAL("clicked()"),
                     self.on_clean)
        self.connect (self.mythread, QtCore.SIGNAL ("mysignal(QString) "),
                      self.on_change, QtCore.Qt.QueuedConnection)

    def on_start(self):
        print("on_start() -")
        if not self.mythread.isRunning():
            self.mythread.start()
            self.btnClean.setDisabled(not self.mythread.running)
            self.btnStart.setDisabled(not self.mythread.running)
            self.btnStop.setDisabled(self.mythread.running)
            # Запускаем поток

    def on_clean(self):
        print("on_clean() -")
        #if not self.mythread.isRunning():
        self.mythread.count = 0
        self.label.setText(u"Чыста")

    def on_stop(self):
        print("on_stop() -")
        self.mythread.running = False # Изменяем флаг выполнения
        self.btnClean.setDisabled(self.mythread.running)
        self.btnStart.setDisabled(self.mythread.running)
        self.btnStop.setDisabled(not self.mythread.running)

    def on_change(self, s):
        self.label.setText(s)

    def closeEvent(self, event):
        print("closeEvent() -")
        # ВЫЗывается при закрытии окна
        self.hide()
        # СКрываем окно
        self.mythread.running = False # Изменяем флаг выполнения
        self.mythread.wait(5000)
        # Даем время, чтобы закончить
        event.accept()
        # Закрываем окно


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    # Создаем экземпляр
    window.setWindowTitle(u"Зaпycк и остановка потока")
    window.resize(300, 100)
    window.show()
    # Отображаем окно
    sys.exit(app.exec_()) #Запускаем цикл обработки