# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import re


ln = [str(i).upper() for i in QtGui.QImageReader.supportedImageFormats()]

print ln