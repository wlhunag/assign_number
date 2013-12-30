#-*- coding: utf-8-*-
__author__ = 'Aaron'
import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from playtext import Ui_Form


class MW(QWidget,Ui_Form):
    def __init__(self,parent = None):
        super(MW,self).__init__(parent)
        self.setupUi(self)
        self.create_connection()
        self.var = ['A','<A>','[A]','{A}']
        self.comboBox.addItems(self.var)
        self.show()

    def create_connection(self):
        self.plainTextEdit.textChanged.connect(self.manipulation)

    def manipulation(self):
        self.ori = unicode(self.plainTextEdit.toPlainText()).encode('utf-8').lstrip("\n").rstrip('\n')
        poll = ['','A','B','C','D']
        print self.ori

        for a,b in zip(poll,['\t{0}'.format(answer) for answer in self.ori.split('\n')]):
            result = "\n".join(a + '.' + b)
        print result
        self.textBrowser.setText(result.decode('utf-8'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec_())