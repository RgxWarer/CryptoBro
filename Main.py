import sys
import codecs
from Atbash import atbashFunc
from Scytale import ScytFunk
from Cezar import CezarFunk
from Polybius import Polyb
from Vigenеre import Vigener
from Gronsfeld import Gronsfeld
from Alberti import Alberti
from Richelieu import Richelie
from Pleifer_m import Pleifer
from Vernam import Vernam
from Cardan import Cardan
from Hill import Hill
from Vernam_LCG import VernamLCG
from CryptoAnal import AnalysisWindow
from CryptoAnalPol import AnalysisPolWindow
from DES import DES
from GOST import GOST
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from window import *
import re

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self.buf = None
        self.fromFile = None
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowIcon(QIcon('logo.png'))
        self.ui = Ui_Dialog()
        self.ua = AnalysisWindow()
        self.up = AnalysisPolWindow()
        self.ui.setupUi(self)


        self.ui.Bt_Write.clicked.connect(self.WriteFunc)
        self.ui.Bt_Anal1.clicked.connect(self.AnalShow)
        self.ui.Bt_Anal2.clicked.connect(self.AnalShowPoly)
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
        self.ui.pbar.setValue(0)

    def ReadFunc(self):
        if self.ui.cryptosystem.currentText() in ["Гаммирование", 'DES', 'ГОСТ']:
            name, _ = QFileDialog.getOpenFileName(self, 'Open File')
            in_file = open(name, "rb")
            text = in_file.read()
            self.buf = bytearray(text)
            self.fromFile = 1
            text = text[:1000].decode("mbcs")
            self.ui.textEdit1.setPlainText(text)
            in_file.close()
        else:
            name, _ = QFileDialog.getOpenFileName(self, 'Open File', "*.txt")
            if name != "":
                file = codecs.open(name, 'r', 'utf-8')
                text = file.read()
                self.ui.textEdit1.setText(text)
                file.close()

    def WriteFunc(self):
        if self.ui.cryptosystem.currentText() in ["Гаммирование", 'DES', 'ГОСТ']:
            name, _ = QFileDialog.getSaveFileName(self, 'Open File')
            out_file = open(name, "wb")
            out_file.write(bytes(self.buf))
            out_file.close()
        else:
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

    def SetStatus(self, how_val):
        self.ui.pbar.setValue(how_val)

    def AnalShow(self):
        self.ua.show()

    def AnalShowPoly(self):
        self.up.show()

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
                try:
                    result = Pleifer(text, key, whatDO)
                    self.ui.textEdit2.setText(result)
                except:
                    self.ui.msgErr.setText("Ошибка при выполнении! Проверьте входные данные!")
                    self.ui.msgErr.exec()
            else:
                self.ui.msgErr.setText("Недопустимые входные данные!")
                self.ui.msgErr.exec()

        elif system == "Вернам":
            key = self.ui.textKey.toPlainText()
            text = self.ui.textEdit1.toPlainText()
            if key and self.Validator("[^a-zA-Zа-яА-ЯёЁ .,!()-/#%]+", key) and self.Validator("[^a-zA-Zа-яА-ЯёЁ .,!("
                                                                                              ")-/#%]+", text):
                try:
                    result, text2 = Vernam(text, key, whatDO)
                    self.ui.textEdit2.setText(result)
                    self.ui.textEdit4.setText(text2)
                except:
                    self.ui.msgErr.setText("Ошибка при выполнении! Проверьте входные данные!")
                    self.ui.msgErr.exec()
            else:
                self.ui.msgErr.setText("Недопустимые входные данные!")
                self.ui.msgErr.exec()

        elif system == "Кардано":
            key = self.ui.textKey.toPlainText()
            text = self.ui.textEdit1.toPlainText()
            if key and self.Validator("[^\d\[\], ]+", key):
                try:
                    result, text2 = Cardan(text, key, whatDO)
                    self.ui.textEdit2.setText(result)
                    self.ui.textEdit4.setText(text2)
                except:
                    self.ui.msgErr.setText("Ошибка при выполнении! Проверьте входные данные!")
                    self.ui.msgErr.exec()
            else:
                self.ui.msgErr.setText("Недопустимые входные данные!")
                self.ui.msgErr.exec()

        elif system == "Хилл":
            key = self.ui.textKey.toPlainText()
            text = self.ui.textEdit1.toPlainText()
            if key and self.Validator("[^\da-zA-Zа-яА-ЯёЁ .,]+", key) and self.Validator("[^\da-zA-Zа-яА-ЯёЁ .,]+",
                                                                                         text):
                try:
                    result, matrix = Hill(text, key, whatDO)
                    if result:
                        self.ui.textEdit2.setText(result)
                        self.ui.textEdit4.setText(matrix)
                    else:
                        self.ui.msgErr.setText("Некорректный ввод!")
                        self.ui.msgErr.exec()
                except:
                    self.ui.msgErr.setText("Ошибка при выполнении! Проверьте входные данные!")
                    self.ui.msgErr.exec()
            else:
                self.ui.msgErr.setText("Недопустимые входные данные!")
                self.ui.msgErr.exec()

        elif system == "Гаммирование":
            key = self.ui.textKey.toPlainText()
            if key and re.match("[0-9]* [0-9]* [0-9]*", key):
                if self.fromFile:
                    text = self.buf
                    key += " 1"
                elif whatDO == "Шифруем":
                    text = bytearray(self.ui.textEdit1.toPlainText().encode('mbcs'))
                    key += " 0"
                else:
                    text = self.buf
                    key += " 0"
                try:
                    result, self.buf = VernamLCG(text, key, whatDO)
                    self.ui.textEdit2.setText(result)
                except:
                    self.ui.msgErr.setText("Ошибка при выполнении! Проверьте входные данные!")
                    self.ui.msgErr.exec()
            else:
                self.ui.msgErr.setText("Недопустимые входные данные!")
                self.ui.msgErr.exec()

        elif system == "DES":
            key = self.ui.textKey.toPlainText()
            if key and re.match("[0-1]{56}", key) or key == '':
                if self.fromFile:
                    text = self.buf
                elif whatDO == "Шифруем":
                    text = bytearray(self.ui.textEdit1.toPlainText().encode('mbcs'))
                else:
                    text = self.buf
                try:
                    MyWin.setDisabled(self, True)
                    result, self.buf, key, msg = DES(text, key, whatDO, self.ui.pbar)
                    MyWin.setDisabled(self, False)
                    self.ui.textEdit2.setText(result)
                    self.ui.textKey.setText(key)
                    self.ui.textEdit4.setText(msg)

                except:
                    self.ui.msgErr.setText("Ошибка при выполнении! Проверьте входные данные!")
                    self.ui.msgErr.exec()
                    MyWin.setDisabled(self, False)

            else:
                self.ui.msgErr.setText("Недопустимые входные данные!")
                self.ui.msgErr.exec()

        elif system == "ГОСТ":
            key = self.ui.textKey.toPlainText()
            if key and re.match("[0-1]{256}", key) or key == '':
                if self.fromFile:
                    text = self.buf
                elif whatDO == "Шифруем":
                    text = bytearray(self.ui.textEdit1.toPlainText().encode('mbcs'))
                else:
                    text = self.buf
                try:
                    MyWin.setDisabled(self, True)
                    result, self.buf, key, msg = GOST(text, key, whatDO, self.ui.pbar)
                    MyWin.setDisabled(self, False)
                    self.ui.textEdit2.setText(result)
                    self.ui.textKey.setText(key)
                    self.ui.textEdit4.setText(msg)

                except:
                    self.ui.msgErr.setText("Ошибка при выполнении! Проверьте входные данные!")
                    self.ui.msgErr.exec()
                    MyWin.setDisabled(self, False)

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
            self.ui.hintField.setText("Ключ - строка = начало алфавита")

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

        elif system == "Плейфер":
            self.ui.textKey.setEnabled(True)
            self.ui.textKey.setText("")
            self.ui.hintField.setText("Ключ - строка = начало алфавита")

        elif system == "Вернам":
            self.ui.textKey.setEnabled(True)
            self.ui.textKey.setText("")
            self.ui.hintField.setText("Ключ - строка символов")

        elif system == "Кардано":
            self.ui.textKey.setEnabled(True)
            self.ui.textKey.setText("")
            self.ui.hintField.setText("Ключ - [символ, четверть]")

        elif system == "Хилл":
            self.ui.textKey.setEnabled(True)
            self.ui.textKey.setText("")
            self.ui.hintField.setText("Ключ - символы алфавита")

        elif system == "Гаммирование":
            self.buf = None
            self.fromFile = None
            self.ui.textKey.setEnabled(True)
            self.ui.textKey.setText("")
            self.ui.hintField.setText("Ключ - три числа")

        elif system == "DES":
            self.ui.pbar.setValue(0)
            self.buf = None
            self.fromFile = None
            self.ui.textKey.setEnabled(True)
            self.ui.textKey.setText("")
            self.ui.hintField.setText("Ключ - битовая последовательность")

        elif system == "ГОСТ":
            self.ui.pbar.setValue(0)
            self.buf = None
            self.fromFile = None
            self.ui.textKey.setEnabled(True)
            self.ui.textKey.setText("")
            self.ui.hintField.setText("Ключ - битовая последовательность")

        self.ui.Bt_do.setEnabled(True)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
