# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, QtSql
import sys, login_form
from config import read_conf


class LoginWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.db = None
        self.thread = None
        self.ui = login_form.Ui_LoginDialog()
        self.ui.setupUi(self)
        self.center()

    def mysql_login(self, kwargs):
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName(kwargs["hostname"])
        self.db.setDatabaseName(kwargs["databasename"])
        self.db.setUserName(kwargs["username"])
        self.db.setPassword(kwargs["password"])
        if (self.db.open() == False):
            QtGui.QMessageBox.critical(None, "Database Error",
                                 self.db.lastError().text())
        else:
            print "Db connected successfully"
            self.db.close()
            self.emit(QtCore.SIGNAL("logined()"))
            self.close()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def login(self):
        conf = read_conf("conf.conf", "database")
        if self.ui.login_field.text():
            #print "username -", self.ui.login_field.text()
            conf["username"] = str(self.ui.login_field.text())
        if self.ui.password_field.text():
            conf["password"] = str(self.ui.password_field.text())
        print conf
        self.mysql_login(conf)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = LoginWindow()
    # desktop setup
    #desktop = QtGui.QApplication.desktop()
    #x = (desktop.width() - window.width()) // 2
    #y = (desktop.height() - window.height()) // 2
    #window.move(x, y)
    # desktop setup
    window.show()
    # Отображаем окно
    sys.exit(app.exec_()) #Запускаем цикл обработки
