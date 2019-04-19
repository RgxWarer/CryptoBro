def Polyb(openText, key, whatDo):
    alpha = [[65, 91], [97, 123], [1040, 1072], [1072, 1104]]

    Alpha = [chr(j) for i in alpha for j in range(i[0], i[1])] + [chr(1025)] + [chr(1105)] + [chr(32)] + [chr(46)] + [chr(44)]

    for i in key:
        Alpha.remove(i)
        Alpha = [i] + Alpha

    res = [[], []]
    string_res = ''

    if whatDo == "Шифруем":

        for c in openText:
            res[0].append(Alpha.index(c) // 11)
            res[1].append(Alpha.index(c) % 11)

        res[0] = res[0] + res[1]
        i = 0

        while i < len(openText) * 2:
            string_res += Alpha[(res[0][i]*11+res[0][i + 1])]
            i += 2
        return string_res, Alpha

    if whatDo == "Расшифруем":

        for c in openText:
            res[0].append(Alpha.index(c) // 11)
            res[1].append(Alpha.index(c) % 11)

        res[0] = res[0] + res[1]
        i = 0

        while i < len(openText) * 2:
            string_res += Alpha[(res[0][i]*11+res[0][i + 1])]
            i += 2
        return string_res, Alpha

