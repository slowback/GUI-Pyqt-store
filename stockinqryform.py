# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stockinqryform.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.showlist = QtWidgets.QTextEdit(Form)
        self.showlist.setGeometry(QtCore.QRect(10, 10, 371, 271))
        self.showlist.setObjectName("showlist")
        self.close = QtWidgets.QPushButton(Form)
        self.close.setGeometry(QtCore.QRect(360, 260, 16, 21))
        self.close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon)
        self.close.setObjectName("close")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))