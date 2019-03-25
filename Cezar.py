def CezarFunk(openText, key, whatDo):

    alpha1 = 'abcdefghijklmnopqrstuvwxyz'
    alpha2 = 'ABCDEFGHIJKLMNOPQRSTUYWXYZ'
    alpha3 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alpha4 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    res = ""

    if whatDo == "Шифруем":

        for c in openText:
            if c in alpha1:
                res += alpha1[(alpha1.index(c) + key) % len(alpha1)]
            elif c in alpha2:
                res += alpha2[(alpha2.index(c) + key) % len(alpha2)]
            elif c in alpha3:
                res += alpha3[(alpha3.index(c) + key) % len(alpha3)]
            elif c in alpha4:
                res += alpha4[(alpha4.index(c) + key) % len(alpha4)]
            else:
                res += c
        return res

    if whatDo == "Расшифруем":

        for c in openText:
            if c in alpha1:
                res += alpha1[(alpha1.index(c) + (len(alpha1) - key)) % len(alpha1)]
            elif c in alpha2:
                res += alpha2[(alpha2.index(c) + (len(alpha2) - key)) % len(alpha2)]
            elif c in alpha3:
                res += alpha3[(alpha3.index(c) + (len(alpha3) - key)) % len(alpha3)]
            elif c in alpha4:
                res += alpha4[(alpha4.index(c) + (len(alpha4) - key)) % len(alpha4)]
            else:
                res += c
        return res
