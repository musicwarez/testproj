# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys
import login_form
import login
import main_window
import main
from Queue import Queue


class FirstWindow(login.LoginWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = login_form.Ui_LoginDialog()
        self.ui.setupUi(self)
        #self.thread = MyThread(self)


class MainWindow(main.MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)


class MainClass(FirstWindow, MainWindow):
    def __init__(self, parent=None):
        FirstWindow.__init__(self, parent)
        self.queue = Queue()
        self.fw = FirstWindow()
        self.main = MainWindow()
        print "Try connect"
        #self.connect(fw, QtCore.SIGNAL("logined()"), main.show)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MainClass()
    # desktop setup
    #desktop = QtGui.QApplication.desktop()
    #x = (desktop.width() - window.width()) // 2
    #y = (desktop.height() - window.height()) // 2
    #window.move(x, y)
    # desktop setup
    window.fw.show()
    window.main.connect(window.fw, QtCore.SIGNAL("logined()"), window.main.show)
    # Отображаем окно
    sys.exit(app.exec_()) #Запускаем цикл обработки