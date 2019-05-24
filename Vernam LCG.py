def VernamLCG(openText, param, whatDo):

    alpha = [[65, 91], [97, 123], [1040, 1072], [1072, 1104]]

    Alpha = [chr(j) for i in alpha for j in range(i[0], i[1])] + [chr(1025)] + [chr(1105)] + [chr(32)] + [chr(46)] + [
        chr(44)] + [chr(33)] + [chr(37)] + [chr(35)] + [chr(40)] + [chr(41)] + [chr(45)] + [chr(47)]

    key = LCG(len(openText), param)
    res10 = ''
    res2 = ''
    key2 = ''
    text2 = ''
    for c, k in zip(openText, key):
        tmp = ''
        c = BIN(Alpha.index(c))
        c = '0' * (7-len(c)) + c
        k = BIN(Alpha.index(k))
        k = '0' * (7 - len(k)) + k
        key2 += k + "  "
        text2 += c + "  "
        for s1, s2 in zip(c, k):
            tmp += XOR(s1, s2)
        res2 += tmp + "  "
        res10 += Alpha[INT(tmp)]
    return res10 + "\n" + res2, key + "\n" + key2 + "\n" + openText + "\n" + text2


def XOR(s1, s2):
    if s1 == s2:
        return '0'
    if s1 != s2:
        return '1'


def BIN(s1):
    b = ''
    if s1 == 0:
        return '0'
    while s1 > 0:
        b = str(s1 % 2) + b
        s1 = s1 // 2
    return b


def INT(s1):
    decimal = 0
    for digit in s1:
        decimal = decimal * 2 + int(digit)
    return decimal

def LCG(n, param):

    return 1



