def Pleifer(openText, key, whatDo):
    alpha = [[65, 91], [97, 123], [1040, 1072], [1072, 1104]]

    Alpha = [chr(j) for i in alpha for j in range(i[0], i[1])] + [chr(1025)] + [chr(1105)] + [chr(32)] + [chr(46)] + [
        chr(44)]

    for i in key:
        Alpha.remove(i)
        Alpha = [i] + Alpha

    res = ""

    for i in range(len(openText)):
        try:
            tmp = openText[i + 1]
        except:
            tmp = "X"
        if openText[i] == tmp and openText != "X":
            Code(openText[i], Alpha.index("X"), Alpha)
        elif openText[i] == tmp and openText != "X":




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



