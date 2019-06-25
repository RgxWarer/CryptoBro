import random
import sys
from functools import partial
from math import gcd
from operator import itemgetter
from collections import Counter
from collections import OrderedDict
import codecs
import re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from window import *
from WindowAnalPol import Ui_Dialog_Anal_Pol
from resources import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mdates


class AnalysisPolWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):

        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog_Anal_Pol()
        self.ui.setupUiAnalPol(self)

        self.ui.Bt_Write.clicked.connect(self.WriteFunc)
        self.ui.Bt_Change.clicked.connect(self.Change_Let)
        self.ui.lang.activated.connect(self.LangChange)
        self.ui.freqSet.activated.connect(self.FreqChange)
        self.ui.Bt_Read.clicked.connect(self.ReadFunc)
        self.ui.bt_clear.clicked.connect(self.ClearFunc)
        self.ui.Bt_do.clicked.connect(self.DoFunc)
        self.ui.table.cellClicked.connect(self.cell_was_clicked)

        self.ui.textEdit4.setText('10')
        self.alpha_sort_old = OrderedDict(alpha_ALL[self.ui.lang.currentIndex()])
        self.alpha_sort_new = None
        self.alpha_old = list(self.alpha_sort_old.keys())
        self.alpha_stand = alpha_st[self.ui.lang.currentIndex()]
        self.alpha_new = None

    def ClearFunc(self):
        self.ui.Bt_Change.setEnabled(False)
        self.ui.textEdit1.setText("")
        self.ui.textEdit2.setText("")
        self.ui.textEdit3.setText("")
        self.ui.textEdit4.setText("10")
        self.ui.table.setRowCount(0)
        self.ui.textEdit3.setReadOnly(True)

    def LangChange(self):

        self.alpha_sort_old = OrderedDict(alpha_ALL[self.ui.lang.currentIndex()])
        self.alpha_old = list(self.alpha_sort_old.keys())
        self.alpha_stand = alpha_st[self.ui.lang.currentIndex()]

    def FreqChange(self):

        if self.ui.freqSet.currentIndex():
            name, _ = QFileDialog.getOpenFileName(self, 'Open File', "*.txt")
            if name != "":
                file_freq = codecs.open(name, 'r', 'utf-8')
                text_freq = file_freq.read()
                freq = self.frequency(text_freq, self.alpha_sort_old)
                self.alpha_sort_old = OrderedDict(sorted(freq.items(), key=itemgetter(1), reverse=True))
                self.alpha_old = list(self.alpha_sort_old.keys())
                file_freq.close()
        else:
            self.LangChange()

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

    def DoFunc(self):

        self.ui.textEdit3.setReadOnly(False)
        self.ui.Bt_Change.setEnabled(True)

        text = self.ui.textEdit1.toPlainText().lower()
        try:
            lens = int(self.ui.textEdit4.toPlainText())
        except:
            self.ui.msgErr.setText("Проверьте значение верхней границы длины ключа!")
            self.ui.msgErr.exec()
            return 0

        clear_text = ''

        for c in text:
            if c in self.alpha_stand:
                clear_text += c

        func_key = {0: partial(self.IndexKey, clear_text, lens),
                    1: partial(self.AutoCorr, clear_text, lens),
                    2: partial(self.kasiski_test, clear_text)}

        len_key = func_key[self.ui.cryptosystem.currentIndex()]()

        key = []
        in_table = []
        for i in range(len_key):
            text_i = clear_text[i::len_key]
            freq = self.frequency(text_i, self.alpha_sort_old)
            self.alpha_sort_new = OrderedDict(sorted(freq.items(), key=itemgetter(1), reverse=True))
            self.alpha_new = list(self.alpha_sort_new.keys())
            mark = []
            for i in range(len(self.alpha_stand)):
                n, m = self.alpha_stand.index(self.alpha_new[i]), self.alpha_stand.index(
                    list(self.alpha_old)[i])
                mark.append(((n - m) % len(self.alpha_stand) + len(self.alpha_stand)) % len(self.alpha_stand))
            key.append(list(Counter(mark).keys())[0])
            in_table.append(list(Counter(mark).keys())[:3])

            text_i = ''

        self.fill_table(in_table, key, clear_text)
        self.ui.textEdit2.setText(self.change_simple(text, key))
        self.ui.textEdit3.setText(self.InTXT(key))

    def InTXT(self, arg):

        key_txt = ''
        for i in arg:
            key_txt += self.alpha_stand[i]
        return key_txt

    def InINT(self, arg):

        key_int = []
        for i in arg:
            key_int += [self.alpha_stand.index(i)]
        return key_int

    def frequency(self, arg1, arg2):

        freq = {}

        for c in arg2.keys():
            freq[c] = 0
        for c in arg1:

            if c in arg2.keys():
                freq[c] += 1

        amount = sum(freq.values())

        for c in freq:

            if freq[c] != 0:
                freq[c] /= amount
        return freq

    def change_simple(self, text, key):

        res = ''
        iter = 0

        for c in text:
            flag = 0
            if c in self.alpha_stand:
                res += self.alpha_stand[(self.alpha_stand.index(c) - key[iter]) % len(self.alpha_stand)]
                iter += 1
            else:
                res += c
            if iter == len(key):
                iter = 0

        return res

    def IndexKey(self, text, len_key):

        good = 0
        last = 1

        for i in range(2, len_key):

            temp = Counter(text[::i])
            amount = sum(temp.values())
            for j in list(temp.keys()):
                temp[j] = temp[j] * (temp[j] - 1) / (amount * (amount - 1))
            same_index = sum(temp.values())
            if abs(same_index - 0.0553) < last:
                good = i
                last = abs(same_index - 0.0553)
        return good

    def AutoCorr(self, text, len_key):

        good = 0
        last = 1

        for i in range(2, len_key):

            amount = 1
            temp = text[i:] + text[:i]

            for j in range(len(text)):
                if text[j] == temp[j]:
                    amount += 1
            same_index = amount / len(text)

            if abs(same_index - 0.0553) < last:
                good = i
                last = abs(same_index - 0.0553)
        return good

    def kasiski_test(self, text):  # Code partially provided

        trigraphList = []
        distanceList = []

        for i in range(len(text) - 1):
            currentTrigraph = text[i:i + 3]
            if currentTrigraph not in trigraphList:
                trigraphList.append(currentTrigraph)
            else:
                previousIndex = text.find(currentTrigraph)
                distance = i - previousIndex
                distanceList.append(distance)
        dCount = Counter(distanceList)
        topCount = dCount.most_common(10)
        my_gcd = topCount[0][0]
        for i in range(1, len(topCount)):
            if topCount[i][1] > 1:
                my_gcd = gcd(my_gcd, topCount[i][0])
        return my_gcd

    def fill_table(self, perm, key, text):

        self.ui.table.setRowCount(len(perm) * 3)

        for i in range(len(perm)):
            for j in range(3):
                temp = [] + key
                temp[i] = perm[i][j]
                self.ui.table.setItem(i * 3 + j, 1, QTableWidgetItem(self.change_simple(text, temp)))
                self.ui.table.setItem(i * 3 + j, 0, QTableWidgetItem(self.InTXT(temp)))
        self.ui.table.resizeColumnsToContents()

    def cell_was_clicked(self):

        row = self.ui.table.currentItem().row()
        key = list(self.ui.table.item(row, 0).text())
        self.ui.textEdit2.setText(self.change_simple(self.ui.textEdit1.toPlainText().lower(), self.InINT(key)))
        self.ui.textEdit3.setText(''.join(key))

    def Change_Let(self):

        key = list(self.ui.textEdit3.toPlainText())
        try:
            self.ui.textEdit2.setText(self.change_simple(self.ui.textEdit1.toPlainText().lower(), self.InINT(key)))
        except:
            self.ui.msgErr.setText("Убедитесь в правильности введенного ключа!")
            self.ui.msgErr.exec()
            return 0
