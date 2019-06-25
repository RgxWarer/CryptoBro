from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog_Anal(object):

    def setupUiAnal(self, AnalWin):
        AnalWin.setObjectName("Dialog")
        AnalWin.resize(1100, 620)

        self.lable6 = QtWidgets.QLabel(AnalWin)
        self.lable6.setGeometry(QtCore.QRect(20, 450, 100, 30))
        self.lable6.setObjectName("lable5")
        self.lable6.setText("Заменить букву:")

        self.textEdit4 = QtWidgets.QTextEdit(AnalWin)
        self.textEdit4.setGeometry(QtCore.QRect(20, 480, 30, 30))
        self.textEdit4.setObjectName("textEdit4")

        self.Bt_Change = QtWidgets.QPushButton(AnalWin)
        self.Bt_Change.setGeometry(QtCore.QRect(60, 480, 80, 30))
        self.Bt_Change.setObjectName("Bt_Change")

        self.textEdit5 = QtWidgets.QTextEdit(AnalWin)
        self.textEdit5.setGeometry(QtCore.QRect(150, 480, 30, 30))
        self.textEdit5.setObjectName("textEdit5")

        self.table = QtWidgets.QTableWidget(AnalWin)
        self.table.setGeometry(QtCore.QRect(240, 280, 500, 300))
        self.table.setObjectName("table")

        self.lable6 = QtWidgets.QLabel(AnalWin)
        self.lable6.setGeometry(QtCore.QRect(240, 585, 100, 30))
        self.lable6.setObjectName("lable5")
        self.lable6.setText("Текущий ключ:")

        self.textEdit3 = QtWidgets.QTextEdit(AnalWin)
        self.textEdit3.setGeometry(QtCore.QRect(360, 585, 380, 30))
        self.textEdit3.setObjectName("textEdit3")

        self.lable3 = QtWidgets.QLabel(AnalWin)
        self.lable3.setGeometry(QtCore.QRect(20, 275, 200, 20))
        self.lable3.setObjectName("lable3")
        self.lable3.setText("Настройка работы программы:")

        self.lable4 = QtWidgets.QLabel(AnalWin)
        self.lable4.setGeometry(QtCore.QRect(20, 330, 200, 20))
        self.lable4.setObjectName("lable4")
        self.lable4.setText("Язык:")

        self.lable5 = QtWidgets.QLabel(AnalWin)
        self.lable5.setGeometry(QtCore.QRect(20, 385, 200, 20))
        self.lable5.setObjectName("lable5")
        self.lable5.setText("Частоты:")

        self.cryptosystem = QtWidgets.QComboBox(AnalWin)
        self.cryptosystem.setGeometry(QtCore.QRect(20, 300, 150, 22))
        self.cryptosystem.setObjectName("cryptosystem")

        self.lang = QtWidgets.QComboBox(AnalWin)
        self.lang.setGeometry(QtCore.QRect(20, 355, 150, 22))
        self.lang.setObjectName("lang")

        self.freqSet = QtWidgets.QComboBox(AnalWin)
        self.freqSet.setGeometry(QtCore.QRect(20, 410, 150, 22))
        self.freqSet.setObjectName("freqSet")

        self.lable1 = QtWidgets.QLabel(AnalWin)
        self.lable1.setGeometry(QtCore.QRect(30, 10, 200, 20))
        self.lable1.setObjectName("lable1")
        self.lable1.setText("Поле для ввода исходного текста")

        self.textEdit1 = QtWidgets.QTextEdit(AnalWin)
        self.textEdit1.setGeometry(QtCore.QRect(20, 30, 360, 200))
        self.textEdit1.setObjectName("textEdit1")

        self.lable2 = QtWidgets.QLabel(AnalWin)
        self.lable2.setGeometry(QtCore.QRect(390, 10, 250, 20))
        self.lable2.setObjectName("lable2")
        self.lable2.setText("Результат работы программы")

        self.textEdit2 = QtWidgets.QTextEdit(AnalWin)
        self.textEdit2.setGeometry(QtCore.QRect(400, 30, 360, 200))
        self.textEdit2.setObjectName("textEdit2")

        self.bt_clear = QtWidgets.QPushButton(AnalWin)
        self.bt_clear.setGeometry(QtCore.QRect(400, 240, 120, 25))
        self.bt_clear.setObjectName("bt_clear")

        self.Bt_Read = QtWidgets.QPushButton(AnalWin)
        self.Bt_Read.setGeometry(QtCore.QRect(120, 240, 120, 25))
        self.Bt_Read.setObjectName("Bt_Read")

        self.Bt_Write = QtWidgets.QPushButton(AnalWin)
        self.Bt_Write.setGeometry(QtCore.QRect(530, 240, 120, 25))
        self.Bt_Write.setObjectName("Bt_Write")

        self.Bt_do = QtWidgets.QPushButton(AnalWin)
        self.Bt_do.setGeometry(QtCore.QRect(260, 240, 120, 25))
        self.Bt_do.setObjectName("Bt_do")

        self.msgErr = QMessageBox()
        self.msgErr.setIcon(QMessageBox.Question)
        self.msgErr.setText("Error")
        self.msgErr.setWindowTitle("Error")

        self.retranslateUiAnal(AnalWin)
        QtCore.QMetaObject.connectSlotsByName(AnalWin)

    def retranslateUiAnal(self, AnalWin):
        _translate = QtCore.QCoreApplication.translate
        AnalWin.setWindowTitle(_translate("AnalWin", "CryptoBro"))

        self.Bt_do.setText(_translate("AnalWin", "Расшифровать"))
        self.Bt_Change.setText(_translate("AnalWin", "Заменить"))
        self.bt_clear.setText(_translate("AnalWin", "Очистить"))
        self.Bt_Write.setText(_translate("AnalWin", "Запись в файл"))
        self.Bt_Read.setText(_translate("AnalWin", "Чтение из файла"))

        list_Cipher = ["Шифр простой замены", "Шифр Цезаря"]
        list_lang = ["Английский", "Русский"]
        list_freq = ["Из Википедии", "Из файла"]

        for i, j, z in zip(list_Cipher, list_lang, list_freq):
            self.cryptosystem.addItem(i)
            self.lang.addItem(j)
            self.freqSet.addItem(z)

        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Предполагаемый ключ", "Результат декодирования"])
        self.table.resizeColumnsToContents()

        self.textEdit2.setReadOnly(True)
        self.textEdit3.setReadOnly(True)
        self.textEdit1.setReadOnly(False)
        self.textEdit4.setReadOnly(True)
        self.textEdit5.setReadOnly(True)
        self.Bt_Change.setDisabled(True)

