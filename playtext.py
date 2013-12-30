# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playtext.ui'
#
# Created: Mon Dec 30 22:57:30 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(540, 334)
        Form.setAcceptDrops(True)
        Form.setToolTip(_fromUtf8(""))
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 100, 531, 211))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.horizontalLayoutWidget)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.textBrowser = QtGui.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.horizontalLayout.addWidget(self.textBrowser)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 131, 41))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout.addWidget(self.comboBox)
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(150, 20, 131, 21))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 70, 211, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 161, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.checkBox_2 = QtGui.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(150, 40, 111, 16))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QObject.connect(self.plainTextEdit, QtCore.SIGNAL(_fromUtf8("textChanged()")), self.textBrowser.reload)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "考古題加編號", None))
        self.plainTextEdit.setToolTip(_translate("Form", "將複製下來的考古題貼在此處", None))
        self.label.setText(_translate("Form", "花色：", None))
        self.checkBox.setToolTip(_translate("Form", "方便在word 中自動編號", None))
        self.checkBox.setText(_translate("Form", "答案選項縮排", None))
        self.label_2.setText(_translate("Form", "以下結果已自動複製到剪貼簿...", None))
        self.label_3.setText(_translate("Form", "將題目貼在此處", None))
        self.checkBox_2.setText(_translate("Form", "序列後加點", None))

