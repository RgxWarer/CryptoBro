from random import randint
alpha_a = {0: 'ABCDEFGHIJKLMNOPQRSTUYWXYZabcdefghijklmnopqrstuvwxyz',
        1: 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'}
alpha_b = {0: [],
        1: []}

def Alberti(openText, key, alpha, whatDo):
    text = ''

    if not alpha:
        for i in range(len(alpha_a)):
            alpha_b[i] = RandAlpa(alpha_a[i])
            for c, k in zip(alpha_b[i], alpha_a[i]):
                alpha += k + "-" + c + " "
            alpha += "\n"
    else:
        for i in range(len(alpha_a)):
            alpha_b[i] = RandAlpa(alpha_a[i])

    for c in openText:
        flag = 0
        for j in range(len(alpha_a)):
            if c in alpha_a[j]:
                text += alpha_b[j][alpha_a[j].index(c)]
                flag = 1
                continue
        if not flag:
            text += c



    return text, alpha

def RandAlpa(alpha):
    mas = [c for c in alpha]
    mas_rand = []
    for i in range(len(alpha)):
        k = randint(0, len(mas)-1)
        mas_rand.append(mas[k])
        del mas[k]
    return mas_rand