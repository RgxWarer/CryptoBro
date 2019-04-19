def Alberti(openText, key, whatDo):
    alpha_a = {0: 'ABCDEFGHIJKLMNOPQRSTUYWXYZabcdefghijklmnopqrstuvwxyz',
               1: 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'}
    alpha_b = {0: ['x', 'B', 'W', 'R', 'H', 'j', 'd', 'm', 'f', 'A', 'G', 'a', 'N', 'k', 'K', 'p', 'D', 'y', 'c', 'v', 'n', 'g', 'M', 'q', 'L', 'X', 'l', 'h', 'Y', 'r', 'o', 'U', 'i', 'J', 'S', 'w', 'O', 'Q', 'u', 'Y', 'b', 'I', 'Z', 'z', 'C', 'P', 's', 't', 'e', 'T', 'F', 'E'],
               1: ['У', 'т', 'Э', 'а', 'Б', 'Ц', 'Н', 'с', 'б', 'я', 'П', 'н', 'и', 'Ё', 'Г', 'Х', 'э', 'Ш', 'к', 'Т', 'ь', 'Е', 'м', 'р', 'ш', 'Р', 'ъ', 'ч', 'п', 'ю', 'Ж', 'Д', 'х', 'С', 'ц', 'й', 'М', 'Ч', 'щ', 'В', 'Ю', 'И', 'О', 'г', 'Ф', 'Л', 'л', 'Ъ', 'ы', 'А', 'Я', 'Й', 'е', 'о', 'ё', 'К', 'ж', 'з', 'Ы', 'у', 'З', 'Ь', 'Щ', 'д', 'ф', 'в']}
    text = ''
    alpha = ''

    for i in range(len(alpha_a)):
        n = 0
        for c, k in zip(alpha_b[i], alpha_a[i]):
            alpha += "|{} - {}| ".format(k, c)
            n += 1
            if n == 6:
                alpha += "\n"
                n = 0
        alpha += "\n"



    if whatDo == "Шифруем":

        for c in openText:
            flag = 0
            for j in range(len(alpha_a)):
                if c in alpha_a[j]:
                    text += alpha_b[j][(alpha_a[j].index(c)+key)%len(alpha_b[j])]
                    flag = 1
                    key += 1
                    continue
            if not flag:
                text += c
        return text, alpha

    if whatDo == "Расшифруем":
        for c in openText:
            flag = 0
            for j in range(len(alpha_b)):
                if c in alpha_b[j]:
                    text += alpha_a[j][(alpha_b[j].index(c)-key)%len(alpha_a[j])]
                    flag = 1
                    key += 1
                    continue
            if not flag:
                text += c
        return text, alpha

