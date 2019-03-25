import sys
import codecs
from Atbash import atbashFunc
from Scytale import ScytFunk
from Cezar import CezarFunk
from Polybius import Polyb
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from window import *
import re


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
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
        self.ui.textKey.setText("")
        self.ui.cryptosystem.setCurrentIndex(-1)
        self.ui.Bt_do.setEnabled(False)

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
            if self.Validator("[^\d]+", key):
                text = self.ui.textEdit1.toPlainText()
                result = ScytFunk(text, int(key), whatDO)
                self.ui.textEdit2.setText(result)
            else:
                self.ui.msgErr.setText("Недопустимый ключ!")
                self.ui.msgErr.exec()

        elif system == "Цезарь":
            key = self.ui.textKey.toPlainText()
            if self.Validator("[^\d]+", key):
                text = self.ui.textEdit1.toPlainText()
                result = CezarFunk(text, int(key), whatDO)
                self.ui.textEdit2.setText(result)
            else:
                self.ui.msgErr.setText("Недопустимый ключ!")
                self.ui.msgErr.exec()

        elif system == "Квадрат полибия":
            text = self.ui.textEdit1.toPlainText()
            result = Polyb(text, whatDO)
            self.ui.textEdit2.setText(result)

    def hintFunc(self):
        system = self.ui.cryptosystem.currentText()
        self.ui.textEdit1.setReadOnly(False)
        if system == "Атбаш":
            self.ui.textKey.setText("Ключ не требуется")
            self.ui.textKey.setDisabled(True)

        if system == "Скитала":
            self.ui.textKey.setEnabled(True)
            self.ui.textKey.setText("")

        if system == "Цезарь":
            self.ui.textKey.setEnabled(True)
            self.ui.textKey.setText("")

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
