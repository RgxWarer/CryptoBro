import sys
import codecs
from Atbash import atbashFunc
from Scytale import ScytFunk
from Cezar import CezarFunk
from Polybius import Polyb
from Vigenеre import Vigener
from Gronsfeld import Gronsfeld
from Alberti import Alberti
from  Richelieu import Richelie
from  Pleifer_m import Pleifer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from window import *
import re




class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self.buf = None
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowIcon(QIcon('logo.png'))
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.Bt_Write.clicked.connect(self.WriteFunc)
        self.ui.Bt_Read.clicked.connect(self.ReadFunc)
        self.ui.bt_clear.clicked.connect(self.ClearFunc)
        self.ui.Bt_do.clicked.connect(self.DoFunc)
        self.ui.cryptosystem.activated.connect(self.hintFunc)

    def ClearFunc(self):
        self.ui.textEdit1.setText("")
        self.ui.textEdit2.setText("")
        self.ui.textEdit3.setText("")
        self.ui.textKey.setText("")
        self.ui.textKey.setDisabled(True)
        self.ui.hintField.setText("")
        self.ui.cryptosystem.setCurrentIndex(-1)
        self.ui.Bt_do.setEnabled(False)
        self.ui.textEdit4.setText('')

    def ReadFunc(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', "*.txt")
        if name != "":
            file = codecs.open(name, 'r', 'utf-8')
            text = file.read()
            self.ui.textEdit1.setText(text)
            file.close()

    def WriteFunc(self):
        name, _ = QFileDialog.getSaveFileName(self, 'Write File', "*.txt")
        if name != "":
            file = codecs.open(name, 'w', 'utf-8')
            text = str(self.ui.textEdit2.toPlainText())
            file.write(text)
            file.close()

    def Validator(self, valTxt, txtIn):
        if re.search(valTxt, txtIn):
            return False
        return True

    # -------------------------------------------------------------------------

    def DoFunc(self):
        system = self.ui.cryptosystem.currentText()
        whatDO = self.ui.do_smt.currentText()

        if system == "Атбаш":
            text = self.ui.textEdit1.toPlainText()
            result = atbashFunc(text, whatDO)
            self.ui.textEdit2.setText(result)

        elif system == "Скитала":
            key = self.ui.textKey.toPlainText()
            if key and self.Validator("[^\d]+", key):
                text = self.ui.textEdit1.toPlainText()
                result = ScytFunk(text, int(key), whatDO)
                self.ui.textEdit2.setText(result)
            else:
                self.ui.msgErr.setText("Недопустимый ключ!")
                self.ui.msgErr.exec()

        elif system == "Цезарь":
            key = self.ui.textKey.toPlainText()
            if key and self.Validator("[^\d]+", key):
                text = self.ui.textEdit1.toPlainText()
                result = CezarFunk(text, int(key), whatDO)
                self.ui.textEdit2.setText(result)
            else:
                self.ui.msgErr.setText("Недопустимый ключ!")
                self.ui.msgErr.exec()

        elif system == "Квадрат полибия":
            key = self.ui.textKey.toPlainText()
            text = self.ui.textEdit1.toPlainText()
            if key and self.Validator("[^a-zA-Zа-яА-ЯёЁ .,]+", key) and self.Validator("[^a-zA-Zа-яА-ЯёЁ .,]+", text):
                result, alpha = Polyb(text, key, whatDO)
                if result:
                    self.ui.textEdit2.setText(result)
                    self.ui.textEdit4.setText(str(alpha))
                else:
                    self.ui.msgErr.setText("Некорректный ввод")
                    self.ui.msgErr.exec()
            else:
                self.ui.msgErr.setText("Недопустимые входные данные!")
                self.ui.msgErr.exec()

        elif system == "Виженер":
            key = self.ui.textKey.toPlainText()
            if key and self.Validator("[^a-zA-Zа-яА-ЯёЁ]+", key):
                text = self.ui.textEdit1.toPlainText()
                result = Vigener(text, key, whatDO)
                if result:
                    self.ui.textEdit2.setText(result)
                else:
                    self.ui.msgErr.setText("Некорректный ввод ключа")
                    self.ui.msgErr.exec()
            else:
                self.ui.msgErr.setText("Недопустимый ключ!")
                self.ui.msgErr.exec()

        elif system == "Гронсфельд":
            key = self.ui.textKey.toPlainText()
            if key and self.Validator("[^\d]+", key):
                text = self.ui.textEdit1.toPlainText()
                result = Gronsfeld(text, key, whatDO)
                self.ui.textEdit2.setText(result)
            else:
                self.ui.msgErr.setText("Недопустимый ключ!")
                self.ui.msgErr.exec()

        elif system == "Альберти":
            key = self.ui.textKey.toPlainText()
            if key and self.Validator("[^\d]+", key):
                text = self.ui.textEdit1.toPlainText()
                result, text = Alberti(text, int(key), whatDO)
                self.ui.textEdit2.setText(result)
                self.ui.textEdit4.setText(str(text))

            else:
                self.ui.msgErr.setText("Недопустимый ключ!")
                self.ui.msgErr.exec()

        elif system == "Ришелье":
            key = self.ui.textKey.toPlainText()
            if key and self.Validator("[^\d(),]+", key):
                text = self.ui.textEdit1.toPlainText()
                result = Richelie(text, key, whatDO)
                if result:
                    self.ui.textEdit2.setText(result)
                else:
                    self.ui.msgErr.setText("Ошибка при записи ключа!")
                    self.ui.msgErr.exec()

            else:
                self.ui.msgErr.setText("Недопустимый ключ!")
                self.ui.msgErr.exec()

        elif system == "Плейфер":
            key = self.ui.textKey.toPlainText()
            text = self.ui.textEdit1.toPlainText()
            if key and self.Validator("[^a-zA-Zа-яА-ЯёЁ]+", key):
                result = Pleifer(text, key, whatDO)
                if result:
                    self.ui.textEdit2.setText(result)
                else:
                    self.ui.msgErr.setText("Некорректный ввод")
                    self.ui.msgErr.exec()
            else:
                self.ui.msgErr.setText("Недопустимые входные данные!")
                self.ui.msgErr.exec()

    def hintFunc(self):
        system = self.ui.cryptosystem.currentText()
        self.ui.textEdit4.setText('')
        if system == "Атбаш":
            self.ui.textKey.setText("Ключ не требуется")
            self.ui.textKey.setDisabled(True)

        elif system == "Скитала":
            self.ui.textKey.setEnabled(True)
            self.ui.textKey.setText("")
            self.ui.hintField.setText("Ключ - это число = диаметру трубки!")

        elif system == "Цезарь":
            self.ui.textKey.setEnabled(True)
            self.ui.textKey.setText("")
            self.ui.hintField.setText("Ключ -  это число = смещению!")

        elif system == "Квадрат полибия":
            self.ui.textKey.setEnabled(True)
            self.ui.textKey.setText("")
            self.ui.hintField.setText("Смещение алфавита")

        elif system == "Виженер":
            self.ui.textKey.setEnabled(True)
            self.ui.textKey.setText("")
            self.ui.hintField.setText("Только символы одного алфавита!")

        elif system == "Гронсфельд":
            self.ui.textKey.setEnabled(True)
            self.ui.textKey.setText("")
            self.ui.hintField.setText("Только цифры!")

        elif system == "Альберти":
            self.ui.textKey.setEnabled(True)
            self.ui.textKey.setText("")
            self.ui.hintField.setText("Ключ - число = начальное смещение!")

        elif system == "Ришелье":
            self.ui.textKey.setEnabled(True)
            self.ui.textKey.setText("")
            self.ui.hintField.setText("Ключ - строка = перестановки")

        self.ui.Bt_do.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())

# reg_ex = QRegExp("[a-zA-Zа-яА-ЯёЁ\s]+")
# text_validator = QRegExpValidator(reg_ex, self.ui.textEdit1)

# self.ui.textEdit1.setValidator(text_validator)
# valTxt = "[^a-zA-Zа-яА-ЯёЁ\s]+"
#            if self.Validator(valTxt, text):
#                result = atbashFunc(text, whatDO)
#                self.ui.textEdit2.setText(result)
#            else:
#                self.ui.msgErr.setText("Недопустимый ввод.")
#                self.ui.msgErr.exec()
