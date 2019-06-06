
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