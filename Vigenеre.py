def Vigener(openText, key, whatDo):
    alpha = {0: 'ABCDEFGHIJKLMNOPQRSTUYWXYZabcdefghijklmnopqrstuvwxyz',
             1: 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'}

    if whatDo == "Шифруем":
        DO = 1
    else:
        DO = -1

    if ord(key[0]) <= 127:
        alpha_i = 0
    else:
        alpha_i = 1

    code_key, amount_key, no_alph = encode(key, alpha[alpha_i])

    if no_alph:
        return 0

    code_text, amount_text, no_alph = encode(openText, alpha[alpha_i])

    iter = 0
    res = []
    text = ''


    for i in code_text:
        res.append((i+DO*code_key[iter]) % len(alpha[alpha_i]))
        iter += 1
        if iter >= amount_key:
            iter = 0


    k = 0
    for i in range(len(openText)):
        if not no_alph or no_alph[0][0] != i:
            text += alpha[alpha_i][res[k]]
            k += 1
        else:
            text += no_alph[0][1]
            del no_alph[0]
    return text

def encode(Text, alpha):
    amount = 0
    i = 0
    no_alph = []
    code = []

    for c in Text:
        flag = 0
        if c in alpha:
                amount += 1
                code.append(alpha.index(c))
                flag = 1
        if not flag:
            no_alph.append([i, c])
        i += 1
    return code, amount, no_alph




