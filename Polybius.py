def Polyb(openText, whatDo):
    matrix =    {0 : [['a', 'b', 'c', 'd', 'e'],
                ['f', 'g', 'h', 'i', 'k'],
                ['l', 'm', 'n', 'o', 'p'],
                ['q', 'r', 's', 't', 'u'],
                ['v', 'w', 'x', 'y', 'z'],
                ['j', ' ', ',', '.', '']],

                1 : [['A', 'B', 'C', 'D', 'E'],
                ['F', 'G', 'H', 'I', 'K'],
                ['L', 'M', 'N', 'O', 'P'],
                ['Q', 'R', 'S', 'T', 'U'],
                ['V', 'W', 'X', 'Y', 'Z'],
                ['J', ' ', ',', '.', '']],

                2 : [['а', 'б', 'в', 'г', 'д', 'е'],
                ['ё', 'ж', 'з', 'и', 'й', 'к'],
                ['л', 'м', 'н', 'о', 'п', 'р'],
                ['с', 'т', 'у', 'ф', 'х', 'ц'],
                ['ч', 'ш', 'щ', 'ъ', 'ы', 'ь'],
                ['э', 'ю', 'я', ' ', ',', '.']],

                3 : [['А', 'Б', 'В', 'Г', 'Д', 'Е'],
                ['Ё', 'Ж', 'З', 'И', 'Й', 'К'],
                ['Л', 'М', 'Н', 'О', 'П', 'Р'],
                ['С', 'Т', 'У', 'Ф', 'Х', 'Ц'],
                ['Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
                ['Э', 'Ю', 'Я', ' ', ',', '.']]}

    res = [[], [], []]
    string_res = ''
    amount = len(openText)

    if whatDo == "Шифруем":

        for c in openText:

            flag = 0

            if c == " " or c == "." or c == ",":
                res[1].append(matrix[res[2][len(res[1])-1]])



            for i in range(len(matrix[0])):
                if c in matrix[0][i]:
                    res[1].append(i)
                    res[0].append(matrix[0][i].index(c))
                    res[2].append(0)
                    flag = 1
                    break
            if flag == 1:
                continue

            for i in range(len(matrix[1])):
                if c in matrix[1][i]:
                    res[1].append(i)
                    res[0].append(matrix[1][i].index(c))
                    res[2].append(1)
                    flag = 1
                    break
            if flag == 1:
                continue

            for i in range(len(matrix[2])):
                if c in matrix[2][i]:
                    res[1].append(i)
                    res[0].append(matrix[2][i].index(c))
                    res[2].append(2)
                    flag = 1
                    break
            if flag == 1:
                continue

            for i in range(len(matrix[3])):
                if c in matrix[3][i]:
                    res[1].append(i)
                    res[0].append(matrix[3][i].index(c))
                    res[2].append(3)
                    flag = 1
                    break
            if flag == 1:
                continue

        res[0] = res[0] + res[1]
        res[2] = res[2]*2
        i = 0

        while i < amount * 2 - 2:
            if res[2][i] == res[2][i + 1]:
                    if res[2][i] == 0:
                        string_res += matrix_en[res[0][i+1]][res[0][i]]
                    if res[2][i] == 1:
                        string_res += matrix_EN[res[0][i+1]][res[0][i]]
                    if res[2][i] == 2:
                        string_res += matrix_rus[res[0][i+1]][res[0][i]]
                    if res[2][i] == 3:
                        string_res += matrix_RUS[res[0][i+1]][res[0][i]]
                    i += 2
        return string_res

    if whatDo == "Расшифруем":

        return res
