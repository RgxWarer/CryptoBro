import random
import sys
from operator import itemgetter
from collections import Counter
from collections import OrderedDict
import codecs
import re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from window import *
from WindowAnal import Ui_Dialog_Anal
from resources import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mdates


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None):
        dpi = 80
        fig = plt.figure(dpi=dpi, figsize=(300 / dpi, 600 / dpi))
        self.axes = fig.add_subplot(111)
        plt.title('График частот')

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def setPlot(self):
        fig = self.figure
        plt.cla()
        plt.title('График частот')
        fig.savefig('barshoris.png')

    def plot(self, arg1, arg2, arg3):
        fig = self.figure
        mpl.rcParams.update({'font.size': 9})

        ax = plt.axes()
        ax.xaxis.grid(True, zorder=1)

        xs = range(len(arg1))

        plt.barh([x + 0.3 for x in xs], [d for d in arg1.values()],
                 height=0.2, color='red', alpha=0.7, label='Шифротекст',
                 zorder=2)

        plt.barh([x + 0.05 for x in xs], [arg2[d] for d in arg3],
                 height=0.2, color='blue', alpha=0.7, label='Эталон',
                 zorder=2)
        plt.yticks(xs, arg1.keys(), rotation=10)

        plt.legend(loc='upper right')
        fig.savefig('barshoris.png')


class AnalysisWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):

        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog_Anal()
        self.ui.setupUiAnal(self)

        self.ui.Bt_Write.clicked.connect(self.WriteFunc)
        self.ui.Bt_Change.clicked.connect(self.Change_Let)
        self.ui.lang.activated.connect(self.LangChange)
        self.ui.cryptosystem.activated.connect(self.SetCrypt)
        self.ui.freqSet.activated.connect(self.FreqChange)
        self.ui.Bt_Read.clicked.connect(self.ReadFunc)
        self.ui.bt_clear.clicked.connect(self.ClearFunc)
        self.ui.Bt_do.clicked.connect(self.DoFunc)
        self.ui.table.cellClicked.connect(self.cell_was_clicked)

        self.alpha_sort_old = OrderedDict(alpha_ALL[self.ui.lang.currentIndex()])
        self.alpha_sort_new = None
        self.alpha_old = list(self.alpha_sort_old.keys())
        self.alpha_stand = alpha_st[self.ui.lang.currentIndex()]
        self.alpha_new = None
        self.m = PlotCanvas(self)
        self.m.move(780, 10)

    def SetCrypt(self):

        if self.ui.cryptosystem.currentIndex():
            self.ui.textEdit4.setReadOnly(True)
            self.ui.textEdit5.setReadOnly(True)
            self.ui.Bt_Change.setDisabled(True)
        else:
            self.ui.textEdit4.setReadOnly(False)
            self.ui.textEdit5.setReadOnly(False)
            self.ui.Bt_Change.setDisabled(False)

    def ClearFunc(self):

        self.ui.textEdit1.setText("")
        self.ui.textEdit2.setText("")
        self.ui.textEdit3.setText("")
        self.ui.textEdit4.setText("")
        self.ui.textEdit5.setText("")
        self.ui.textEdit4.setReadOnly(True)
        self.ui.textEdit5.setReadOnly(True)
        self.ui.Bt_Change.setDisabled(True)
        self.m.setPlot()
        self.ui.table.setRowCount(0)

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

    def getAlpha(self, freq_alph):

        alpha = ''
        for i in range(len(self.alpha_stand)):
            alpha += freq_alph[self.alpha_old.index(self.alpha_stand[i])]
        return alpha

    def Change_Let(self):

        let1 = self.ui.textEdit4.toPlainText().lower()
        let2 = self.ui.textEdit5.toPlainText().lower()
        if let1 not in self.alpha_stand or let2 not in self.alpha_stand:
            self.ui.msgErr.setText("Убедитесь в правильности введенных букв замены!")
            self.ui.msgErr.exec()

        self.alpha_new[self.alpha_old.index(let1)], self.alpha_new[self.alpha_old.index(let2)] = \
            self.alpha_new[self.alpha_old.index(let2)], self.alpha_new[self.alpha_old.index(let1)]
        self.Encrypt(self.ui.textEdit1.toPlainText().lower())

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

        self.ui.textEdit4.setReadOnly(False)
        self.ui.textEdit5.setReadOnly(False)
        self.ui.Bt_Change.setDisabled(False)

        text = self.ui.textEdit1.toPlainText().lower()

        freq = self.frequency(text, self.alpha_sort_old)
        self.alpha_sort_new = OrderedDict(sorted(freq.items(), key=itemgetter(1), reverse=True))
        self.alpha_new = list(self.alpha_sort_new.keys())
        self.Encrypt(text)

    def Encrypt(self, text):

        self.m.setPlot()
        self.m.plot(OrderedDict(reversed(list(self.alpha_sort_new.items()))),
                    OrderedDict(reversed(list(self.alpha_sort_old.items()))),
                    list(self.alpha_new)[::-1])

        if self.ui.cryptosystem.currentText() == "Шифр Цезаря":

            mark = []
            for i in range(len(self.alpha_stand)):
                n, m = self.alpha_stand.index(self.alpha_new[i]), self.alpha_stand.index(
                    list(self.alpha_old)[i])
                mark.append(((n - m) % len(self.alpha_stand) + len(self.alpha_stand)) % len(self.alpha_stand))
            perm = list(Counter(mark).keys())
            self.alpha_new = self.alpha_stand[perm[0]:] + self.alpha_stand[:perm[0]]
            res = self.change_simple(text, self.alpha_new, self.alpha_stand)
            self.fill_table(perm, text)
            self.ui.textEdit3.setText(self.alpha_new)

        else:

            res = self.change_simple(text, self.alpha_new, self.alpha_old)
            self.fill_table(1, text)
            self.ui.textEdit3.setText(self.getAlpha(self.alpha_new))

        self.ui.textEdit2.setText(res)

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

    def change_simple(self, text, alpha_1, alpha_2):

        res = ''
        for c in text:
            if c in alpha_1:
                n = alpha_1.index(c)
                res += alpha_2[n]
            else:
                res += c
        return res

    def cell_was_clicked(self):

        row = self.ui.table.currentItem().row()

        if self.ui.cryptosystem.currentText() == "Шифр Цезаря":

            self.alpha_new = list(self.ui.table.item(row, 0).text())
            res = self.change_simple(self.ui.textEdit1.toPlainText().lower(), self.alpha_new, self.alpha_stand)
            self.ui.textEdit3.setText(''.join(self.alpha_new))

        else:

            self.alpha_new = []
            temp = self.ui.table.item(row, 0).text()
            for i in range(len(self.alpha_stand)):
                self.alpha_new.append(temp[self.alpha_stand.index(self.alpha_old[i])])

            res = self.change_simple(self.ui.textEdit1.toPlainText().lower(), self.alpha_new, self.alpha_old)
            self.ui.textEdit3.setText(self.getAlpha(self.alpha_new))

        self.ui.textEdit2.setText(res)

    def fill_table(self, perm, text):

        if self.ui.cryptosystem.currentText() == "Шифр Цезаря":

            for i in range(len(self.alpha_new)):
                if i not in perm:
                    perm.append(i)

            self.ui.table.setRowCount(len(self.alpha_new))

            for i in range(len(perm)):
                temp = self.alpha_stand[perm[i]:] + self.alpha_stand[:perm[i]]
                self.ui.table.setItem(i, 1, QTableWidgetItem(self.change_simple(text[:40], temp, self.alpha_stand)))
                self.ui.table.setItem(i, 0, QTableWidgetItem(temp))
        else:

            self.ui.table.setRowCount(0)
            rowPosition = self.ui.table.rowCount()
            self.ui.table.insertRow(rowPosition)

            self.ui.table.setItem(rowPosition, 1, QTableWidgetItem(
                self.change_simple(text[:40], self.alpha_new, self.alpha_old)))
            self.ui.table.setItem(rowPosition, 0, QTableWidgetItem(self.getAlpha(self.alpha_new)))

            for i in range(len(self.alpha_stand) - 1):

                if self.alpha_sort_new[self.alpha_new[i]] - self.alpha_sort_new[self.alpha_new[i + 1]] < 0.01:
                    self.ui.table.insertRow(rowPosition)
                    temp = [] + self.alpha_new
                    temp[i], temp[i + 1] = temp[i + 1], temp[i]
                    self.ui.table.setItem(rowPosition, 1, QTableWidgetItem(
                        self.change_simple(text[:40], temp, self.alpha_old)))
                    self.ui.table.setItem(rowPosition, 0, QTableWidgetItem(self.getAlpha(temp)))

        self.ui.table.resizeColumnsToContents()
