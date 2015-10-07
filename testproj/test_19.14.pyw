# -*- coding: utf-8 -*-
__author__ = 'alex'

from PyQt4 import QtCore, QtGui
import MyWindow


class MyThread(QtCore.QThread):
    def __init__(se1f, parent=None):
        QtCore.QThread.__init__(se1f, parent)

    def run(self):
        print("run() -")
        for i in range(1, 10):
            self.sleep(1)
            self.emit(QtCore.SIGNAL("mysigna1(QString)"), "i = %s" % i)

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel(u"Haжмитe кнопку д.пя запуска потока")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.button = QtGui.QPushButton(u"Зaпycтить процесс")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.mythread = MyThread()
        #Создаем экземпляр класса
        self.connect(self.button, QtCore.SIGNAL("clicked()"),
                     self.on_clicked)
        self.connect(self.mythread, QtCore.SIGNAL("started()"),
                     self.on_started)
        self.connect(self.mythread, QtCore.SIGNAL("finished()"),
                     self.on_finished)
        self.connect(self.mythread, QtCore.SIGNAL("mysigna1(QString)"),
                     self.on_change, QtCore.Qt.QueuedConnection)

    def on_clicked(self):
        print("on_clicked() -")
        self.button.setDisabled(True)
        # Делаем кнопкунеактивной
        self.mythread.start()
        # Запускаем поток

    def on_started(self):
        print("on_started() -")
        # Вьвывается при запуске потока
        self.label.setText(u"Bызвaм метод on_started()")

    def on_finished(self):
        print("on_finished() -")
        # Вызывается при завершении потока
        self.label.setText(u"Bызвaн метод on_finished()")
        self.button.setDisabled(False)
        #Делаем кнопку активной

    def on_change(self, s):
        print("on_change() -")
        self.label.setText(s)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    # Создаем экземпляр
    window.setWindowTitle(u"Использование класса QThread")
    window.resize(300, 70)
    window.show()
    # Отображаем окно
    sys.exit(app.exec_()) #Запускаем цикл обработки