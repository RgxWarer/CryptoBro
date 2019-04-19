def Richelie(openText, key, whatDo):
    res = ""
    jump = 0

    key = key[1:-1].split(")(")
    a_key = []
    i = 0
    for c in key:
        a_key.append([])
        for k in c.split(","):
            a_key[i].append(int(k))
        i += 1
    for c in a_key:
        for k in c:
            if k > len(c) or k <= 0 or c.count(k) != 1:
                return False

    if whatDo == "Шифруем":

        for c in a_key:
            for k in c:
                res += openText[k+jump-1]
            jump += len(c)
        return res

    if whatDo == "Расшифруем":

        for c in a_key:
            for k in set(c):
                res += openText[c.index(k) + jump]
            jump += len(c)
        return res

