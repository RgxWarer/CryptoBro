from random import randint


def Alberti(openText, key, alpha, buf, whatDo):
    alpha_a = {0: 'ABCDEFGHIJKLMNOPQRSTUYWXYZabcdefghijklmnopqrstuvwxyz',
               1: 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'}
    alpha_b = {0: [],
               1: []}
    text = ''

    if not alpha:
        for i in range(len(alpha_a)):
            alpha_b[i] = RandAlpa(alpha_a[i])
            n = 0
            for c, k in zip(alpha_b[i], alpha_a[i]):
                alpha += " |" + k + " - " + c + "| "
                n += 1
                if n == 5:
                    alpha += "\n"
                    n = 0
            alpha += "\n"
    else:
       alpha_b = buf

    if whatDo == "Шифруем":

        for c in openText:
            flag = 0
            for j in range(len(alpha_a)):
                if c in alpha_a[j]:
                    text += alpha_b[j][(alpha_a[j].index(c)+key)%len(alpha_b[j])]
                    flag = 1
                    continue
            if not flag:
                text += c
        return text, alpha, alpha_b

    if whatDo == "Расшифруем":
        for c in openText:
            flag = 0
            for j in range(len(alpha_b)):
                if c in alpha_b[j]:
                    text += alpha_a[j][(alpha_b[j].index(c)-key)%len(alpha_a[j])]
                    flag = 1
                    continue
            if not flag:
                text += c
        return text, alpha, alpha_b


def RandAlpa(alpha):
    mas = [c for c in alpha]
    mas_rand = []
    for i in range(len(alpha)):
        k = randint(0, len(mas)-1)
        mas_rand.append(mas[k])
        del mas[k]
    return mas_rand