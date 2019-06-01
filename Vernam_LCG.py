import sys
def VernamLCG(openText, param, whatDo):

    param = [int(c) for c in param.split()]

    amount = len(openText)
    res10 = bytearray(b'')
    res10 += openText

    i = 0
    j = 0

    key = LCG(amount, param)

    for c in openText:
        tmp = ''
        c = BIN(c)
        c = '0' * (8-len(c)) + c
        k = BIN(key[j])
        k = '0' * (8 - len(k)) + k
        for s1, s2 in zip(c, k):
            tmp += XOR(s1, s2)
        res10[i] = INT(tmp)
        i += 1
        if param[3] == 1:
            if j == 63:
                param[2] = key[63]
                key = LCG(amount, param)
                j = 0
            else:
                j += 1
        else:
                j += 1

    return res10.decode('mbcs'), res10

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

def LCG(amount, param):
    a = int(param[0])
    b = int(param[1])
    gamma = int(param[2])
    key = []
    if param[3] == 1:
        n = 64
    else:
        n = amount
    while len(key) < n:
        gamma = (a * gamma + b) % 16661
        key.append(gamma % 256)
    return key




