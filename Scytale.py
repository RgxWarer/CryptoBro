def ScytFunk(openText, key, whatDo):

    amount = len(openText)
    column = (amount - 1) // key + 1
    mas = []
    index = 0
    res = ""

    if whatDo == "Шифруем":

        for i in range(key):
            mas.append([])
            for j in range(column):
                if index < amount:
                    mas[i].append(openText[index])
                    index += 1
                else:
                    mas[i].append(chr(152))

        for i in range(column):
            for j in range(key):
                res += mas[j][i]

        return res

    if whatDo == "Расшифруем":

        if len(openText) < key:
            while key - len(openText) > 0:
                openText += chr(152)
                amount += 1
        for j in range(column):
            for i in range(key):
                if j == 0:
                    mas.append([])
                if index < amount:
                    mas[i].append(openText[index])
                    index += 1
                else:
                    mas[i].append(chr(152))

        for i in range(key):
            for j in range(column):
                if mas[i][j] != chr(152):
                    res += mas[i][j]

        return res

