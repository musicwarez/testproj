# -*- coding: utf-8 -*-
__author__ = 'alex'

from PyQt4 import QtCore, QtGui
import MyWindow

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.MyWidget = MyWindow.MyWindow()
        self.MyWidget.vbox.setMargin(0)
        self.button = QtGui.QPushButton(u"Изменить надпись")
        mainBox = QtGui.QVBoxLayout()
        mainBox.addWidget(self.MyWidget)
        mainBox.addWidget(self.button)
        self.setLayout(mainBox)
        self.connect (self.button, QtCore.SIGNAL( "clicked()") ,
                      self.on_clicked)

    def on_clicked(self):
        self.MyWidget.label.setText(u"Новая запись")
        self.button.setDisabled(True)


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