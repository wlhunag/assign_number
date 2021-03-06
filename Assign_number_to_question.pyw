#-*- coding: utf-8-*-
import time

from PyQt4.QtCore import Qt


__author__ = 'Aaron'
import sys

from PyQt4.QtGui import *
from playtext import Ui_Form


class MW(QWidget,Ui_Form):
    def __init__(self,parent = None):
        super(MW,self).__init__(parent)
        self.setupUi(self)
        self.clipboard = QApplication.clipboard()
        #嘗試全域快鍵，似乎在視窗失去焦點時就不支援了
        #網路上說要用 QxtGlobalShortcut 才有全局快捷鍵
        self.copyaction = QAction('copy',self)
        self.copyaction.setShortcut(QKeySequence('Ctrl+C,D'))


        #TODO:  讓視窗內容大小隨視窗調整
        self.var = [u'無邊框','< >','[ ]','{ }',u"無選項"]
        self.create_connection()
        self.comboBox.addItems(self.var)
        self.comboBox.setCurrentIndex(1)

        self.show()

    def create_connection(self):
        self.plainTextEdit.textChanged.connect(self.manipulation)
        self.comboBox.currentIndexChanged.connect(lambda: self.manipulation())
        self.checkBox.toggled.connect(lambda: self.manipulation())
        self.checkBox_2.toggled.connect(lambda: self.manipulation())
        #嘗試全域快鍵
        self.copyaction.triggered.connect(lambda: self.glohot())

    def glohot(self):
        print "Global hotkey success!!"
        print unicode(self.clipboard.text())

    def whichstyle(self):
        style = int(unicode(self.comboBox.currentIndex()))
        # print(style)
        if style == 0:
            return ['A','B','C','D']

#print
        elif style == 1:
            return ['<A>','<B>','<C>','<D>']

        elif style == 2:
            return ['[A]','[B]','[C]','[D]']

        elif style == 3:
            return ['{A}','{B}','{C}','{D}']

        elif style == 4:
            return ['','','','']

    def manipulation(self):
        self.poll = self.whichstyle()

        self.ori = unicode(self.plainTextEdit.toPlainText()).encode('utf-8').lstrip("\n").rstrip('\n')
        print self.ori

        if self.checkBox.isChecked():
            tab = "\t"
        else:
            tab = ""

        if self.checkBox_2.isChecked():
            dot = "."
        else:
            dot = ""

        modifytext = self.ori.split('\n')
        #題目先獨立出來
        result = modifytext[0] + '\n'
        #再拼湊答案選項
        try:
            for a,b in zip(self.poll,['{0}'.format(answer) for answer in self.ori.split('\n')[1:]]):
                result += tab + a + dot + b + "\n"
            print result

        except:
            print "內容不是考古題吧!"

        self.textBrowser.setText(result.decode('utf-8'))

        self.plainTextEdit.setFocus()
        self.plainTextEdit.selectAll()

        #自動複製到剪貼簿
        clipboard = QApplication.clipboard()
        clipboard.setText(result.decode('utf-8'))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    #測試splashScreen
    # img = QPixmap(r"G:\logo.png".decode('utf-8'))
    # img2 = QPixmap(r"C:\Users\Aaron\Pictures\green.bmp".decode('utf-8'))

    img = QPixmap(r"resources\logo.png".decode('utf-8'))
    splash = QSplashScreen(img)
    # splash.setMask(QPixmap(img2).mask())
    app.processEvents()

    #設定文字大小
    font = QFont(splash.font())
    font.setPointSize(font.pointSize()+15)
    splash.setFont(font)

    splash.show()
    for i in range(6):
        splash.showMessage(u"連線伺服器.{} ".format('.'*i), Qt.AlignBottom | Qt.AlignLeft,Qt.black)
        time.sleep(0.4)
    splash.showMessage(u"資料讀取中，請稍後......",Qt.AlignBottom, Qt.black)
    app.processEvents()
    time.sleep(1.5)
    window = MW()
    splash.finish(window)
    splash.hide()

    sys.exit(app.exec_())