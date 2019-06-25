alpha_st = {1: 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
         0: 'abcdefghijklmnopqrstuvwxyz'}
alpha_ALL = {
    1: [('о', 0.1097), ('е', 0.0845), ('а', 0.0801), ("и", 0.0735), ("н", 0.067), ("т", 0.0626), ("с", 0.0547),
        ("р", 0.0473), ("в", 0.0454), ("л", 0.044), ("к", 0.0349), ("м", 0.0321), ("д", 0.0298), ("п", 0.0281),
        ("у", 0.0262), ("я", 0.0201), ("ы", 0.019), ("ь", 0.0174), ("г", 0.017), ("з", 0.0165), ("б", 0.0159),
        ("ч", 0.0144), ("й", 0.0121), ("х", 0.0097), ("ж", 0.0094), ("ш", 0.0073), ("ю", 0.0064), ("ц", 0.0048),
        ("щ", 0.0036), ("э", 0.0032), ("ф", 0.0026), ("ъ", 0.0004), ("ё", 0.0004)],
    0: [("e", 0.1270), ('t', 0.0906), ('a', 0.0817), ('o', 0.0751), ('i', 0.0697), ('n', 0.0675), ('s', 0.0633),
        ('h', 0.0609), ('r', 0.0599), ('d', 0.0425), ('l', 0.0403), ('c', 0.0278), ('u', 0.076), ('m', 0.0241),
        ('w', 0.0236), ('f', 0.0223), ('g', 0.0202), ('y', 0.0197), ('p', 0.0193), ('b', 0.0149), ('v', 0.0098),
        ('k', 0.0077), ('x', 0.0015), ('j', 0.0015), ('q', 0.001), ('z', 0.0005)]}


def permutations_table(input, table):  # перестановка по таблице

    output = []
    for index in table:
        output.append(input[index - 1])
    return output


def break_in_half(input):  # деление пополам

    left_input, right_input = input[:len(input) // 2], input[len(input) // 2:]
    return left_input, right_input


def circular_left_shift(bits, numberofbits):  # Циклический сдвиг влево

    shiftedbits = bits[numberofbits:] + bits[:numberofbits]
    return shiftedbits


def break_in_nbits(n, input):  # Разбиваем строку на подстроки n бит

    length = len(input)
    return [input[i * length // n: (i + 1) * length // n]
            for i in range(n)]


def XOR(bits1, bits2):  # Реализация XOR
    xor_result = []
    for index in range(len(bits1)):
        if bits1[index] == bits2[index]:
            xor_result.append(0)
        else:
            xor_result.append(1)
    return xor_result


def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + digit
    return decimal


def decimal_to_binary(decimal):
    b = [0, 0, 0, 0, 0, 0, 0, 0]
    if decimal == 0:
        return b
    i = 7
    while decimal > 0:
        b[i] = decimal % 2
        decimal = decimal // 2
        i -= 1
    return b


def sum_modn(arg1, arg2, n):
    tmp = 0
    res = []
    for i in range(1, n + 1):
        if arg1[n - i] == 1 and arg2[n - i] == 1:
            if tmp == 0:
                res.append(0)
            else:
                res.append(1)
            tmp = 1
        elif arg1[n - i] == 0 and arg2[n - i] == 1 or arg1[n - i] == 1 and arg2[n - i] == 0:
            if tmp == 0:
                res.append(1)
                tmp = 0
            else:
                res.append(0)
                tmp = 1
        else:
            if tmp == 1:
                res.append(1)
            else:
                res.append(0)
            tmp = 0
    return res[::-1]
