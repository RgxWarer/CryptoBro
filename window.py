# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(570, 400)

        self.cryptosystem = QtWidgets.QComboBox(Dialog)
        self.cryptosystem.setGeometry(QtCore.QRect(350, 30, 150, 22))
        self.cryptosystem.setObjectName("cryptosystem")

        self.do_smt = QtWidgets.QComboBox(Dialog)
        self.do_smt.setGeometry(QtCore.QRect(350, 60, 150, 22))
        self.do_smt.setObjectName("do_smt")

        self.textEdit1 = QtWidgets.QTextEdit(Dialog)
        self.textEdit1.setGeometry(QtCore.QRect(20, 30, 250, 120))
        self.textEdit1.setObjectName("textEdit1")

        self.textEdit2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit2.setGeometry(QtCore.QRect(20, 250, 250, 120))
        self.textEdit2.setObjectName("textEdit2")

        self.textKey = QtWidgets.QTextEdit(Dialog)
        self.textKey.setGeometry(QtCore.QRect(330, 170, 200, 60))
        self.textKey.setObjectName("textКеу")

        self.Bt_do = QtWidgets.QPushButton(Dialog)
        self.Bt_do.setGeometry(QtCore.QRect(350, 300, 150, 23))
        self.Bt_do.setObjectName("Bt_do")

        self.bt_clear = QtWidgets.QPushButton(Dialog)
        self.bt_clear.setGeometry(QtCore.QRect(350, 330, 150, 23))
        self.bt_clear.setObjectName("bt_clear")

        self.Bt_Read = QtWidgets.QPushButton(Dialog)
        self.Bt_Read.setGeometry(QtCore.QRect(40, 185, 100, 25))
        self.Bt_Read.setObjectName("Bt_Read")

        self.Bt_Write = QtWidgets.QPushButton(Dialog)
        self.Bt_Write.setGeometry(QtCore.QRect(150, 185, 100, 25))
        self.Bt_Write.setObjectName("Bt_Write")

        self.hintField = QtWidgets.QLabel(Dialog)
        self.hintField.setGeometry(QtCore.QRect(330, 110, 200, 50))
        self.hintField.setObjectName("hintField")

        self.hintField = QtWidgets.QLabel(Dialog)
        self.hintField.setGeometry(QtCore.QRect(330, 110, 200, 50))
        self.hintField.setObjectName("hintField")

        self.msgErr = QMessageBox()
        self.msgErr.setIcon(QMessageBox.Question)
        self.msgErr.setText("Error")
        self.msgErr.setWindowTitle("Error")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CryptoPro"))

        self.Bt_do.setText(_translate("Dialog", "Старт"))
        self.bt_clear.setText(_translate("Dialog", "Очистить"))
        self.Bt_Write.setText(_translate("Dialog", "Запись в файл"))
        self.Bt_Read.setText(_translate("Dialog", "Чтение из файла"))

        list_Cipher = ["Атбаш", "Скитала", "Цезарь", "Квадрат полибия"]
        for i in list_Cipher:
            self.cryptosystem.addItem(i)

        list_Do = ["Шифруем", "Расшифруем"]
        for i in list_Do:
            self.do_smt.addItem(i)



        self.cryptosystem.setCurrentIndex(-1)

        self.textKey.setDisabled(True)
        self.textEdit1.setReadOnly(True)
        self.textEdit2.setReadOnly(True)
        self.Bt_do.setDisabled(True)