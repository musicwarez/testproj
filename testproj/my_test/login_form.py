# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_form.ui'
#
# Created: Tue Oct  6 11:59:22 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName(_fromUtf8("LoginDialog"))
        LoginDialog.resize(258, 163)
        self.buttonBox = QtGui.QDialogButtonBox(LoginDialog)
        self.buttonBox.setGeometry(QtCore.QRect(-120, 120, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayoutWidget = QtGui.QWidget(LoginDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 40, 190, 62))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.login_label = QtGui.QLabel(self.formLayoutWidget)
        self.login_label.setObjectName(_fromUtf8("login_label"))
        self.gridLayout.addWidget(self.login_label, 0, 0, 1, 1)
        self.password_field = QtGui.QLineEdit(self.formLayoutWidget)
        self.password_field.setEchoMode(QtGui.QLineEdit.Password)
        self.password_field.setObjectName(_fromUtf8("password_field"))
        self.gridLayout.addWidget(self.password_field, 1, 1, 1, 1)
        self.password_label = QtGui.QLabel(self.formLayoutWidget)
        self.password_label.setObjectName(_fromUtf8("password_label"))
        self.gridLayout.addWidget(self.password_label, 1, 0, 1, 1)

        self.login_field = QtGui.QLineEdit(self.formLayoutWidget)
        self.login_field.setObjectName(_fromUtf8("login_field"))
        #Field validator begin
        #regex=QtCore.QRegExp("\w{3,15}$")
        #validator=QtGui.QRegExpValidator(regex, self.login_field)
        #self.login_field.setValidator(validator)
        #Field validator end

        self.gridLayout.addWidget(self.login_field, 0, 1, 1, 1)
        self.label = QtGui.QLabel(LoginDialog)
        self.label.setGeometry(QtCore.QRect(50, 10, 171, 17))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(LoginDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), LoginDialog.login)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QtGui.qApp.quit)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Залогинтесь:", None))
        self.login_label.setText(_translate("LoginDialog", "Логин", None))
        self.password_label.setText(_translate("LoginDialog", "Пароль", None))
        self.label.setText(_translate("LoginDialog", "Введите пароль и логин", None))

