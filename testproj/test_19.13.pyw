# -*- coding: utf-8 -*-
__author__ = 'alex'

from PyQt4 import QtCore, QtGui
import MyWindow
import time

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.MyWidget = MyWindow.MyWindow()
        self.MyWidget.vbox.setMargin(0)
        self.button = QtGui.QPushButton(u"Запустить процесс")
        mainBox = QtGui.QVBoxLayout()
        mainBox.addWidget(self.MyWidget)
        mainBox.addWidget(self.button)
        self.setLayout(mainBox)
        self.connect (self.button, QtCore.SIGNAL( "clicked()") ,
                      self.on_clicked)

    def on_clicked(self):
        self.button.setDisabled(True)
        for i in range(1, 10):
            QtGui.qApp.processEvents()
            print("step -", i)
            time.sleep(1)
        self.button.setDisabled(False)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyDialog()
    # Создаем экземпляр
    window.setWindowTitle(u"Приемущества OOП-cтиля")
    window.resize(300, 100)
    window.show()
    # Отображаем окно
    sys.exit(app.exec_()) #Запускаем цикл обработки