def Polyb(openText, key, whatDo):

    Eng = [[65, 91], [97, 123], [48, 58]]
    Rus = [[1040, 1072], [1072, 1104], [48, 58]]

    index = [8,  ]

    matrix = {0: [chr(j) for i in Eng for j in range(i[0], i[1])] + [chr(32)] + [chr(46)],

              1: [chr(j) for i in Rus for j in range(i[0], i[1])] + [chr(1105)] + [chr(1025)] + [chr(32)] + [chr(46)] + [chr(44)] + [chr(33)] + [chr(39)]}

    Alpha = []
    for i in range(index[key][1]):
        Alpha.append([])
        for j in range(index[key][0]):
            Alpha[i].append(matrix[key][i*index[key][0] + j])
    res = [[], []]
    string_res = ''
    amount = len(openText)

    if whatDo == "Шифруем":

        for c in openText:
            flag = 0
            for i in range(len(Alpha)):
                if c in Alpha[i]:
                    res[1].append(i)
                    res[0].append(Alpha[i].index(c))
                    flag = 1
            if not flag:
                return 0



        res[0] = res[0] + res[1]
        i = 0

        while i < amount * 2 - 2:
                string_res += Alpha[res[0][i]][res[0][i + 1]]
                i += 2
        return string_res

    if whatDo == "Расшифруем":
        return res
