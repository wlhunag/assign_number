# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playtext.ui'
#
# Created: Tue Jan 07 11:47:44 2014
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
        Form.resize(674, 312)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setAcceptDrops(True)
        Form.setToolTip(_fromUtf8(""))
        Form.setAutoFillBackground(True)
        self.gridLayout_6 = QtGui.QGridLayout(Form)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout_4.addWidget(self.comboBox, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.checkBox_2 = QtGui.QCheckBox(Form)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout_2.addWidget(self.checkBox_2, 0, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_2.addWidget(self.checkBox, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 1, 0, 1, 2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.plainTextEdit = QtGui.QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout_3.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout_3.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 2, 0, 1, 2)
        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QObject.connect(self.plainTextEdit, QtCore.SIGNAL(_fromUtf8("textChanged()")), self.textBrowser.reload)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "考古題加編號", None))
        self.label.setText(_translate("Form", "花色：", None))
        self.checkBox_2.setText(_translate("Form", "序列後加點", None))
        self.checkBox.setToolTip(_translate("Form", "方便在word 中自動編號", None))
        self.checkBox.setText(_translate("Form", "答案選項縮排", None))
        self.label_3.setText(_translate("Form", "將題目貼在此處", None))
        self.label_2.setText(_translate("Form", "以下結果已自動複製到剪貼簿...", None))
        self.plainTextEdit.setToolTip(_translate("Form", "將複製下來的考古題貼在此處", None))

