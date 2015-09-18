# -*- coding: utf-8 -*-
__author__ = 'alex'
from PyQt4 import QtCore, QtGui

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel(u"Пpивeт, мир ")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.btnQuit = QtGui.QPushButton(u"&Зaкpьrь окно")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.connect (self. btnQuit, QtCore.SIGNAL( "clicked()") ,
                      QtGui.qApp.quit)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    # Создаем экземпляр
    window.setWindowTitle(u"OOП-cтиль класса создания окна")
    window.resize(300, 70)
    window.show()
    # Отображаем окно
    sys.exit(app.exec_()) #Запускаем цикл обработки