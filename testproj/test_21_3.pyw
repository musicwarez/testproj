# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

@QtCore.pyqtSlot()
def on_clicked_button2(self):
    print(u"Сигнал получен кнопкой 2")

class MyWindow(QtGui.QWidget):
    @QtCore.pyqtSlot()
    def on_clicked_button2(self):
        print(u"Сигнал получен кнопкой 2")

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.button1 = QtGui.QPushButton(u"КНoпкa 1 Нажми меня")
        self.button2 = QtGui.QPushButton(u"КНопка 2")
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        self.setLayout(vbox)
        self.resize(300, 100)
        # Передача сигнала от кнопки l к кнопке 2
        self.connect(self.button1, QtCore.SIGNAL("clicked()"),
                     self.button2, QtCore.SIGNAL("clicked()"))
        # Сnособ l 14 параметра)
        self.connect(self.button2, QtCore.SIGNAL("clicked()"),
                     self, QtCore.SLOT("on_clicked_button2()"))
        # Способ 2 (3 параметра)
        #self.connect(self.button2, QtCore.SIGNAL("clicked()"),
        #             QtCore.SLOT("on_clicked_button2()"))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    # Отображаем окно
    sys.exit(app.exec_()) #Запускаем цикл обработки
