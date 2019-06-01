from math import sqrt, ceil


def bezout(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
    return x, y


def Det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def Minor(matrix, i, j):
    tmp = [row for k, row in enumerate(matrix) if k != i]
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    return tmp


def Determinant(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    elif size == 2:
        return Det2(matrix)
    return sum((-1) ** j * matrix[0][j] * Determinant(Minor(matrix, 0, j))
               for j in range(size))


def Mult(a, b, amount):
    result = [[sum(a * b for a, b in zip(A_row, B_col)) % amount
               for B_col in zip(*b)]
              for A_row in a]
    return result


def Out_Txt(a):
    txt = '['
    for row in a:
        txt += str(row) + "\n"
    txt += "]"
    return txt


def Hill(openText, key, whatDo):
    alpha = [[65, 91], [97, 123], [1040, 1072], [1072, 1104], [48, 58]]

    Alpha = [chr(j) for i in alpha for j in range(i[0], i[1])] + [chr(1025)] + [chr(1105)] + [chr(32)] + [chr(46)] + \
            [chr(44)]
    amount = len(Alpha)

    n = sqrt(len(key))
    if n % 1 != 0:
        n = ceil(n)
        key = key.ljust(n ** 2)
    n = int(n)
    index_key = []
    for c in key:
        index_key.append(Alpha.index(c))
    matrix_key = []
    index = 0
    for i in range(n):
        matrix_key.append([])
        for j in range(n):
            matrix_key[i].append(index_key[index])
            index += 1

    m = len(openText)
    if m % n != 0:
        m = m + n - m % n
        openText = openText.ljust(m)
    index_txt = []
    for c in openText:
        index_txt.append(Alpha.index(c))
    matrix_text = []
    index = 0
    for i in range(m // n):
        matrix_text.append([])
        for j in range(n):
            matrix_text[i].append(index_txt[index])
            index += 1

    res = []
    res_txt = ''

    det_key = Determinant(matrix_key) % amount
    if det_key == 0:
        return None

    if whatDo == "Шифруем":
        for c in matrix_text:
            res += Mult([c], matrix_key, amount)

        for c in res:
            for k in c:
                res_txt += Alpha[k]

        return res_txt, Out_Txt(matrix_key) + "\n" + Out_Txt(matrix_text)

    if whatDo == "Расшифруем":

        invert = (bezout(det_key % amount, amount)[0] % amount + amount) % amount
        invert_matrix = []
        if n == 1:
            invert_matrix.append([invert])
        else:
            for i in range(n):
                invert_matrix.append([])
                for j in range(n):
                    koef = (-1) ** (i + j)
                    invert_matrix[i].append(koef * Determinant(Minor(matrix_key, i, j)) * invert % amount)

        invert_matrix = [list(x) for x in zip(*invert_matrix)]

        for c in matrix_text:
            res += Mult([c], invert_matrix, amount)

        for c in res:
            for k in c:
                res_txt += Alpha[k]
        return res_txt, Out_Txt(matrix_key) + "\n" + Out_Txt(invert_matrix) + "\n" + Out_Txt(matrix_text)
