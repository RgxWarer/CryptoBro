import random
from math import ceil

from resources import *

SBOX = [[4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3],
        [14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9],
        [5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11],
        [7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3],
        [6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2],
        [4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 15, 14],
        [13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12],
        [1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12]]


def generate_keys(key_256bits):
    round_keys = break_in_nbits(8, key_256bits)
    round_keys += round_keys * 2 + round_keys[::-1]
    return round_keys


def round_func(text32bits, key32bits):
    result = []
    sum_value = sum_modn(text32bits, key32bits, 32)
    bits4list = break_in_nbits(8, sum_value)  # Разбиваем строку 32 бит на 8 строк по 4 бит
    for sboxcount, bits4 in enumerate(bits4list):
        sboxvalue = decimal_to_binary(SBOX[sboxcount][binary_to_decimal(bits4)])
        result += sboxvalue[4:]
    return circular_left_shift(result, 11)


def encryption(bit_text_64, roundkeys, whatDo):
    left_txt, right_txt = break_in_half(bit_text_64)
    for round in range(32):
        if whatDo == 'Шифруем':
            newR = XOR(left_txt, round_func(right_txt, roundkeys[round]))
            newL = right_txt
        else:
            newL = XOR(right_txt, round_func(left_txt, roundkeys[round]))
            newR = left_txt
        right_txt = newR
        left_txt = newL
    return left_txt + right_txt


def GOST(openText, input, whatDo, Progress):
    key_256 = []
    if input is '':
        random.seed()
        for i in range(256):
            key_256.append(random.randint(0, 1))
    else:
        for i in input:
            key_256.append(int(i))

    res = bytearray(b'')
    amount_bytes_old = len(openText)

    if whatDo == "Шифруем":
        musor = 8 - len(openText) % 8
        for i in range(musor):
            if i == musor - 1:
                openText.append(musor)
            else:
                openText.append(0)

    amount_bytes_new = len(openText)

    roundkeys = generate_keys(key_256)

    step = 100 / (amount_bytes_new // 8)
    long_old = 0
    long_new = step


    for i in range(0, amount_bytes_new // 8):
        byte_text_64 = openText[i * 8:(i + 1) * 8]
        bit_text_64 = []
        for c in byte_text_64:
            bit_text_64 += decimal_to_binary(c)
        if whatDo == 'Шифруем':
            chiper_bit = encryption(bit_text_64, roundkeys, whatDo)
        else:
            chiper_bit = encryption(bit_text_64, roundkeys[::-1], whatDo)
        for c in range(8):
            res.append(binary_to_decimal(chiper_bit[c * 8:(c + 1) * 8]))

        if int(long_new) - int(long_old) == 1:
            Progress.setValue(int(long_new))
        long_new += step
        long_old += step
        if int(long_new) > 100:
            long_new = 100

    if whatDo == "Расшифруем":
        musor = res[-1]
        flag = 1
        for i in range(2, musor + 1):
            if res[-i] != 0:
                flag = 0
                break
        if flag:
            res = res[:-musor]
        amount_bytes_old = len(res)

    return [res[:1000].decode('mbcs'), res, ''.join(map(str, key_256)), "Исходный ключ: " + str(
        key_256) + "\n" + "Длина текста: " + str(amount_bytes_old)]

"""
t1 = GOST(bytearray(bytes('Мама мыла раму', 'mbcs')), '10000000001011101000110101101100000111011111001110011111',
          "Шифруем")
t2 = GOST(t1, '10000000001011101000110101101100000111011111001110011111',
          "Расшифруем")
print(str(t1.decode('mbcs')) + '\n' + str(t2.decode('mbcs')) + str(len(t1)) + str(len(t2)) + str(
    len(bytes('Мама мыла раму', 'mbcs'))))
"""