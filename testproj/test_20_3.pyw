# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys
app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle(u"Bывoд окна по центру экрана")

window.move(window.width() * -2, 0)
window.show()
desktop = QtGui.QApplication.desktop()
x = (desktop.width() - window.frameSize().width()) // 2
y= (desktop.height() - window.frameSize().height()) // 2
window.move(x, y)
window.showFullScreen()
print window.isMaximized()
print window.isFullScreen()
sys.exit(app.exec_())