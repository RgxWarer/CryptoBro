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
        Dialog.resize(1130, 400)

        self.cryptosystem = QtWidgets.QComboBox(Dialog)
        self.cryptosystem.setGeometry(QtCore.QRect(635, 30, 150, 22))
        self.cryptosystem.setObjectName("cryptosystem")

        self.do_smt = QtWidgets.QComboBox(Dialog)
        self.do_smt.setGeometry(QtCore.QRect(635, 60, 150, 22))
        self.do_smt.setObjectName("do_smt")

        self.lable1 = QtWidgets.QLabel(Dialog)
        self.lable1.setGeometry(QtCore.QRect(330, 10, 250, 20))
        self.lable1.setObjectName("lable1")
        self.lable1.setText("Поле для ввода обрабатываемого сообщения")

        self.textEdit1 = QtWidgets.QTextEdit(Dialog)
        self.textEdit1.setGeometry(QtCore.QRect(320, 30, 250, 120))
        self.textEdit1.setObjectName("textEdit1")

        self.lable2 = QtWidgets.QLabel(Dialog)
        self.lable2.setGeometry(QtCore.QRect(330, 225, 250, 20))
        self.lable2.setObjectName("lable2")
        self.lable2.setText("Результат работы программы")

        self.textEdit2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit2.setGeometry(QtCore.QRect(320, 250, 250, 120))
        self.textEdit2.setObjectName("textEdit2")

        self.lable3 = QtWidgets.QLabel(Dialog)
        self.lable3.setGeometry(QtCore.QRect(30, 10, 250, 15))
        self.lable3.setObjectName("lable3")
        self.lable3.setText("Для заметок")

        self.textEdit3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit3.setGeometry(QtCore.QRect(20, 30, 250, 340))
        self.textEdit3.setObjectName("textEdit3")

        self.lable4 = QtWidgets.QLabel(Dialog)
        self.lable4.setGeometry(QtCore.QRect(870, 10, 250, 15))
        self.lable4.setObjectName("lable4")
        self.lable4.setText("Служебная информация о работе шифра")

        self.textEdit4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit4.setGeometry(QtCore.QRect(860, 30, 250, 340))
        self.textEdit4.setObjectName("textEdit4")

        self.lable5 = QtWidgets.QLabel(Dialog)
        self.lable5.setGeometry(QtCore.QRect(620, 150, 250, 15))
        self.lable5.setObjectName("lable5")
        self.lable5.setText("Поле для ввода ключа")

        self.textKey = QtWidgets.QTextEdit(Dialog)
        self.textKey.setGeometry(QtCore.QRect(610, 170, 200, 60))
        self.textKey.setObjectName("textКеу")

        self.Bt_do = QtWidgets.QPushButton(Dialog)
        self.Bt_do.setGeometry(QtCore.QRect(630, 300, 150, 23))
        self.Bt_do.setObjectName("Bt_do")

        self.bt_clear = QtWidgets.QPushButton(Dialog)
        self.bt_clear.setGeometry(QtCore.QRect(630, 330, 150, 23))
        self.bt_clear.setObjectName("bt_clear")

        self.Bt_Read = QtWidgets.QPushButton(Dialog)
        self.Bt_Read.setGeometry(QtCore.QRect(340, 185, 100, 25))
        self.Bt_Read.setObjectName("Bt_Read")

        self.Bt_Write = QtWidgets.QPushButton(Dialog)
        self.Bt_Write.setGeometry(QtCore.QRect(450, 185, 100, 25))
        self.Bt_Write.setObjectName("Bt_Write")

        self.hintField = QtWidgets.QLabel(Dialog)
        self.hintField.setGeometry(QtCore.QRect(620, 215, 200, 60))
        self.hintField.setObjectName("hintField")

        self.msgErr = QMessageBox()
        self.msgErr.setIcon(QMessageBox.Question)
        self.msgErr.setText("Error")
        self.msgErr.setWindowTitle("Error")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CryptoBro"))

        self.Bt_do.setText(_translate("Dialog", "Старт"))
        self.bt_clear.setText(_translate("Dialog", "Очистить"))
        self.Bt_Write.setText(_translate("Dialog", "Запись в файл"))
        self.Bt_Read.setText(_translate("Dialog", "Чтение из файла"))

        list_Cipher = ["Атбаш", "Скитала", "Цезарь", "Квадрат полибия", "Виженер", "Гронсфельд", "Альберти", "Ришелье",
                       "Плейфер", "Вернам", "Кардано", "Хилл", "Гаммирование"]

        for i in list_Cipher:
            self.cryptosystem.addItem(i)

        list_Do = ["Шифруем", "Расшифруем"]
        for i in list_Do:
            self.do_smt.addItem(i)

        #self.textKey.setText('Поле для ввода ключа')
        #self.textEdit1.setText('Поле для ввода шифруемого(расшифруемого) текста')
        #self.textEdit2.setText('Результат шифрования(расшифрования) текста')
        #self.textEdit3.setText('Эталон для сравнивания')




        self.cryptosystem.setCurrentIndex(-1)

        self.textKey.setDisabled(True)
        self.textEdit1.setReadOnly(True)
        self.textEdit2.setReadOnly(True)
        self.Bt_do.setDisabled(True)
        self.textEdit1.setReadOnly(False)
        self.textEdit4.setReadOnly(True)