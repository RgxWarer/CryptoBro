def VernamLCG(openText, param, whatDo):

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
    tmp = param.split(" ")

    a = int(tmp[0])
    b = int(tmp[1])
    gamma = int(tmp[2])

    if b % 2 == 0:
        return None

    if a % 4 != 1:
        return None
    key = ''

    while len(key) < n:
        gamma = (a * gamma + b) % 2017
        key += bin(gamma)
    return key




