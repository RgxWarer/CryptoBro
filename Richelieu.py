def Richelie(openText, key, whatDo):
    res = ""
    jump = 0
    i = 0
    f = 0
    amount = 0

    if key[0] == '(' and key[-1] == ')':
        while i < len(key)-1:
            if key[i] == '(' and key[i+1] == ')':
                return False
            elif key[i] == '(' and not f:
                f = 1
            elif key[i] == '(' and f:
                return False
            elif key[i] == '(' and key[i+1] == ')':
                return False
            elif key[i] == ')' and not f:
                return False
            elif key[i] == ')' and key[i+1] != '(':
                return False
            elif key[i] == ')' and key[i+1] == '(':
                f = 0
            i += 1

    key = key[1:-1].split(")(")
    a_key = []
    i = 0
    for c in key:
        a_key.append([])
        for k in c.split(","):
            a_key[i].append(int(k))
        i += 1
    for c in a_key:
        amount += len(c)
        for k in c:
            if k > len(c) or k <= 0 or c.count(k) != 1:
                return False

    if amount != len(openText):
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

