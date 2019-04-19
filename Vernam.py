def Vernam(openText, key, whatDo):

    alpha = [[65, 91], [97, 123], [1040, 1072], [1072, 1104]]

    Alpha = [chr(j) for i in alpha for j in range(i[0], i[1])] + [chr(1025)] + [chr(1105)] + [chr(32)] + [chr(46)] + [
        chr(44)]
    if len(key) != len(openText):
        return False
    res = ''

    for c, k in zip(openText, key):
        tmp = '0b'
        c = BIN(Alpha.index(c))
        c = '0'*(7-len(c)) + c
        k = BIN(Alpha.index(k))
        k = '0' * (7 - len(k)) + k
        for s1, s2 in zip(c, k):
            tmp += XOR(s1, s2)
        res += Alpha[int(tmp, 2) % len(Alpha)]
    return res

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

