def atbashFunc(openText, whatDO):

    alpha1 = 'abcdefghijklmnopqrstuvwxyz'
    alpha2 = 'ABCDEFGHIJKLMNOPQRSTUYWXYZ'
    alpha3 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alpha4 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    res = ""

    for c in openText:
            if c in alpha1:
                res += alpha1[len(alpha1) - alpha1.index(c) - 1]
            elif c in alpha2:
                res += alpha2[len(alpha2) - alpha2.index(c) - 1]
            elif c in alpha3:
                res += alpha3[len(alpha3) - alpha3.index(c) - 1]
            elif c in alpha4:
                res += alpha4[len(alpha4) - alpha4.index(c) - 1]
            else:
                res += c
    return res

