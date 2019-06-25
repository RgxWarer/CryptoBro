def Gronsfeld(openText, key, whatDo):
    alpha = {0: 'ABCDEFGHIJKLMNOPQRSTUYWXYZabcdefghijklmnopqrstuvwxyz',
             1: 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'}

    if whatDo == "Шифруем":
        DO = 1
    else:
        DO = -1

    text = ''
    iter = 0

    for c in openText:
        flag = 0
        for j in range(len(alpha)):
            if c in alpha[j]:
                text += alpha[j][(alpha[j].index(c) + DO*int(key[iter])) % len(alpha[j])]
                flag = 1
                iter += 1
                continue
        if not flag:
            text += c
        if iter >= len(key):
            iter = 0
    return text
