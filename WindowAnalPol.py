from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog_Anal_Pol(object):

    def setupUiAnalPol(self, AnalWinPol):
        AnalWinPol.setObjectName("Dialog")
        AnalWinPol.resize(1320, 400)

        self.Bt_Change = QtWidgets.QPushButton(AnalWinPol)
        self.Bt_Change.setGeometry(QtCore.QRect(690, 350, 100, 30))
        self.Bt_Change.setObjectName("Bt_Change")

        self.table = QtWidgets.QTableWidget(AnalWinPol)
        self.table.setGeometry(QtCore.QRect(800, 20, 500, 360))
        self.table.setObjectName("table")

        self.lable7 = QtWidgets.QLabel(AnalWinPol)
        self.lable7.setGeometry(QtCore.QRect(70, 330, 200, 20))
        self.lable7.setObjectName("lable7")
        self.lable7.setText("Верхняя гарница длины ключа:")

        self.textEdit4 = QtWidgets.QTextEdit(AnalWinPol)
        self.textEdit4.setGeometry(QtCore.QRect(120, 350, 50, 30))
        self.textEdit4.setObjectName("textEdit4")

        self.lable8 = QtWidgets.QLabel(AnalWinPol)
        self.lable8.setGeometry(QtCore.QRect(260, 330, 150, 20))
        self.lable8.setObjectName("lable8")
        self.lable8.setText("Предполагаемый ключ:")

        self.textEdit3 = QtWidgets.QTextEdit(AnalWinPol)
        self.textEdit3.setGeometry(QtCore.QRect(250, 350, 420, 30))
        self.textEdit3.setObjectName("textEdit3")

        self.lable6 = QtWidgets.QLabel(AnalWinPol)
        self.lable6.setGeometry(QtCore.QRect(240, 585, 100, 30))
        self.lable6.setObjectName("lable6")
        self.lable6.setText("Текущий алфавит:")

        self.lable3 = QtWidgets.QLabel(AnalWinPol)
        self.lable3.setGeometry(QtCore.QRect(100, 275, 200, 20))
        self.lable3.setObjectName("lable3")
        self.lable3.setText("Выбор метода поиска ключа:")

        self.lable4 = QtWidgets.QLabel(AnalWinPol)
        self.lable4.setGeometry(QtCore.QRect(300, 275, 200, 20))
        self.lable4.setObjectName("lable4")
        self.lable4.setText("Язык:")

        self.lable5 = QtWidgets.QLabel(AnalWinPol)
        self.lable5.setGeometry(QtCore.QRect(500, 275, 200, 20))
        self.lable5.setObjectName("lable5")
        self.lable5.setText("Частоты:")

        self.cryptosystem = QtWidgets.QComboBox(AnalWinPol)
        self.cryptosystem.setGeometry(QtCore.QRect(90, 300, 180, 22))
        self.cryptosystem.setObjectName("cryptosystem")

        self.lang = QtWidgets.QComboBox(AnalWinPol)
        self.lang.setGeometry(QtCore.QRect(290, 300, 180, 22))
        self.lang.setObjectName("lang")

        self.freqSet = QtWidgets.QComboBox(AnalWinPol)
        self.freqSet.setGeometry(QtCore.QRect(490, 300, 180, 22))
        self.freqSet.setObjectName("freqSet")

        self.lable1 = QtWidgets.QLabel(AnalWinPol)
        self.lable1.setGeometry(QtCore.QRect(30, 10, 200, 20))
        self.lable1.setObjectName("lable1")
        self.lable1.setText("Поле для ввода исходного текста")

        self.textEdit1 = QtWidgets.QTextEdit(AnalWinPol)
        self.textEdit1.setGeometry(QtCore.QRect(20, 30, 360, 200))
        self.textEdit1.setObjectName("textEdit1")

        self.lable2 = QtWidgets.QLabel(AnalWinPol)
        self.lable2.setGeometry(QtCore.QRect(390, 10, 250, 20))
        self.lable2.setObjectName("lable2")
        self.lable2.setText("Результат работы программы")

        self.textEdit2 = QtWidgets.QTextEdit(AnalWinPol)
        self.textEdit2.setGeometry(QtCore.QRect(400, 30, 360, 200))
        self.textEdit2.setObjectName("textEdit2")

        self.bt_clear = QtWidgets.QPushButton(AnalWinPol)
        self.bt_clear.setGeometry(QtCore.QRect(400, 240, 120, 25))
        self.bt_clear.setObjectName("bt_clear")

        self.Bt_Read = QtWidgets.QPushButton(AnalWinPol)
        self.Bt_Read.setGeometry(QtCore.QRect(120, 240, 120, 25))
        self.Bt_Read.setObjectName("Bt_Read")

        self.Bt_Write = QtWidgets.QPushButton(AnalWinPol)
        self.Bt_Write.setGeometry(QtCore.QRect(530, 240, 120, 25))
        self.Bt_Write.setObjectName("Bt_Write")

        self.Bt_do = QtWidgets.QPushButton(AnalWinPol)
        self.Bt_do.setGeometry(QtCore.QRect(260, 240, 120, 25))
        self.Bt_do.setObjectName("Bt_do")

        self.msgErr = QMessageBox()
        self.msgErr.setIcon(QMessageBox.Question)
        self.msgErr.setText("Error")
        self.msgErr.setWindowTitle("Error")

        self.retranslateUiAnalPol(AnalWinPol)
        QtCore.QMetaObject.connectSlotsByName(AnalWinPol)

    def retranslateUiAnalPol(self, AnalWin):
        _translate = QtCore.QCoreApplication.translate
        AnalWin.setWindowTitle(_translate("AnalWin", "CryptoBro"))

        self.Bt_do.setText(_translate("AnalWin", "Расшифровать"))
        self.bt_clear.setText(_translate("AnalWin", "Очистить"))
        self.Bt_Write.setText(_translate("AnalWin", "Запись в файл"))
        self.Bt_Read.setText(_translate("AnalWin", "Чтение из файла"))
        self.Bt_Change.setText(_translate("AnalWin", "Заменить"))

        list_Cipher = ["Метод индекса совпадений", "Автокорреляционный метод", "Тест Касиски"]
        list_lang = ["Английский", "Русский"]
        list_freq = ["Из Википедии", "Из файла"]

        for j, z in zip(list_lang, list_freq):
            self.lang.addItem(j)
            self.freqSet.addItem(z)

        for i in list_Cipher:
            self.cryptosystem.addItem(i)

        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Возможный ключ", "Результат декодирования"])
        self.table.resizeColumnsToContents()

        self.textEdit2.setReadOnly(True)
        self.textEdit3.setReadOnly(True)
        self.textEdit1.setReadOnly(False)
        self.textEdit4.setReadOnly(False)
        self.Bt_Change.setEnabled(False)