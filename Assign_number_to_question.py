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
        self.var = ['ABCD','<A><B><C><D>','[A][B][C][D]','{A}{B}{C}{D}']
        self.create_connection()
        self.comboBox.addItems(self.var)
        self.show()

    def create_connection(self):
        self.plainTextEdit.textChanged.connect(self.manipulation)
        self.comboBox.currentIndexChanged.connect(lambda: self.manipulation())

    def whichstyle(self):
        style = int(unicode(self.comboBox.currentIndex()))
        # print(style)
        if style == 0:
            return ['','A','B','C','D']

        elif style == 1:
            return ['','<A>','<B>','<C>','<D>']

        elif style ==2:
            return ['','[A]','[B]','[C]','[D]']

        elif style ==3:
            return ['','{A}','{B}','{C}','{D}']

    def manipulation(self):
        self.poll = self.whichstyle()

        self.ori = unicode(self.plainTextEdit.toPlainText()).encode('utf-8').lstrip("\n").rstrip('\n')
        print self.ori

        result = ''
        for a,b in zip(self.poll,['{0}'.format(answer) for answer in self.ori.split('\n')]):
            result += a + '.' + b + "\n"
        print result

        self.textBrowser.setText(result.decode('utf-8'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec_())