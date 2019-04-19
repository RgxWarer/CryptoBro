def Pleifer(openText, key, whatDo):
    alpha = [[65, 91], [97, 123], [1040, 1072], [1072, 1104]]

    Alpha = [chr(j) for i in alpha for j in range(i[0], i[1])] + [chr(1025)] + [chr(1105)] + [chr(32)] + [chr(46)] + [
        chr(44)]

    for i in key:
        Alpha.remove(i)
        Alpha = [i] + Alpha

    res = ""
    i = 0
    if whatDo == "Шифруем":
        while i < len(openText):
            try:
                tmp = openText[i + 1]
            except:
                tmp = "X"
            if openText[i] not in Alpha:
                res += openText[i]
            elif openText[i] == tmp and openText[i] != "X":
                res += Code(Alpha.index(openText[i]), Alpha.index("X"), Alpha) + chr(152)
            elif openText[i] == tmp and openText[i] == "X":
                res += Code(Alpha.index(openText[i]), Alpha.index("Y"), Alpha) + chr(152)
            elif openText[i] != tmp:
                res += Code(Alpha.index(openText[i]), Alpha.index(tmp), Alpha)
                i += 1
            i += 1
        return res


    if whatDo == "Расшифруем":
        while i < len(openText):
            if openText[i] not in Alpha and openText[i] != chr(152):
                res += openText[i]
            elif openText[i+2] == chr(152):
                res += Code(Alpha.index(openText[i]), Alpha.index(openText[i+1])[-1:], Alpha)
                i += 2
            else:
                res += Code(Alpha.index(openText[i]), Alpha.index(openText[i+1]), Alpha)
                i += 1
            i += 1
        return res


def Code(s1,s2,Alpha):
    if s1 % 11 == s2 % 11:
        s1 += 11 % len(Alpha)
        s2 += 11 % len(Alpha)
    elif s1 // 11 == s2 // 11:
        s1 += 1 % len(Alpha)
        s2 += 1 % len(Alpha)
    else:
        tmp = s1
        s1 = (s1//11)*11 + s2 % 11
        s2 = (s2//11)*11 + tmp % 11

    return Alpha[s1] + Alpha[s2]

def DeCode(s1,s2,Alpha):
    if s1 % 11 == s2 % 11:
        s1 -= 11 % len(Alpha)
        s2 -= 11 % len(Alpha)
    elif s1 // 11 == s2 // 11:
        s1 -= 1 % len(Alpha)
        s2 -= 1 % len(Alpha)
    else:
        tmp = s1
        s1 = (s1//11)*11 + s2 % 11
        s2 = (s2//11)*11 + tmp % 11

    return Alpha[s1] + Alpha[s2]




