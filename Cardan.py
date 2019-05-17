from random import randint
from math import sqrt, ceil
import numpy as np

def toMatrix(txt, n):
    txt = txt[2:-2].split("], [")
    masKey = [[int(c) for c in k.split(", ")] for k in txt]
    if len(masKey) != n*n:
        return False
    count = {}
    for s in masKey:
        if len(s) != 2:
            return False
        if 0 > s[1] or 3 < s[1]:
            return False
        if 0 > s[0] or n*n <= s[0]:
            return False
        if s[0] in count.keys():
            count[s[0]] += 1
        else:
            count[s[0]] = 1

    for key in count.keys():
        if count[key] != 1:
            return False
    return masKey

def Cardan(openText, key, whatDo):
    res = ''
    n = len(openText)
    amount = ceil(sqrt(n))
    if amount % 2 != 0:
        amount += 1
    k = ceil(amount / 2)

    openText = openText.ljust(amount * amount)

    if key == '1' and whatDo != "Расшифруем":
        buf = [[c, randint(0, 3)] for c in range(k * k)]
    else:
        buf = toMatrix(key, k)

    matrix_example, coord = [[0] * amount for i in range(amount)], [[0, 0] for c in range(k * k)]
    i = 0
    for c in buf:
        if c[1] == 0:
            coord[i][0], coord[i][1] = c[0] // k, c[0] % k
            matrix_example[coord[i][0]][coord[i][1]] = 1
        elif c[1] == 1:
            coord[i][0], coord[i][1] = c[0] % k, amount - c[0] // k - 1
            matrix_example[coord[i][0]][coord[i][1]] = 1
        elif c[1] == 2:
            coord[i][0], coord[i][1] = amount - c[0] % k - 1, c[0] // k
            matrix_example[coord[i][0]][coord[i][1]] = 1
        elif c[1] == 3:
            coord[i][0], coord[i][1] = amount - c[0] // k - 1, amount - c[0] % k - 1
            matrix_example[coord[i][0]][coord[i][1]] = 1
        i += 1

    coord = sorted(coord)
    buf = sorted(buf)

    if whatDo == "Шифруем":
        txt_matrix = np.array([[''] * amount for i in range(amount)])
        i = 0
        for v in range(4):
            for c in coord:
                txt_matrix[c[0]][c[1]] = openText[i]
                i += 1
            txt_matrix = np.rot90(txt_matrix)
        for c in txt_matrix:
            for j in c:
                res += str(j)
        return res, str(buf) + "\n" + "\n" + str(np.array(matrix_example)) + "\n" + "\n" + str(txt_matrix)

    if whatDo == "Расшифруем":
        txt_matrix = np.array([[openText[i * amount + j] for j in range(amount)] for i in range(amount)])
        i = 0
        for v in range(4):
            for c in coord:
                res += txt_matrix[c[0]][c[1]]
                i += 1
            txt_matrix = np.rot90(txt_matrix)
        return res, str(buf) + "\n" + "\n" + str(np.array(matrix_example)) + "\n" + "\n" + str(txt_matrix)
