import random
from resources import *

# ___________________________key generation________________________________________________ #

round_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
table_key_64_to_56 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3,
                      60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37,
                      29, 21, 13, 5, 28, 20, 12, 4]
table_key_56_to_48 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41,
                      52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

# ___________________________round function________________________________________________#

EXPANSION_TABLE = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19,
                   20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
SBOX = [
    # Box-1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # Box-2

    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],

    # Box-3

    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]

    ],

    # Box-4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],

    # Box-5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # Box-6

    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]

    ],
    # Box-7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # Box-8

    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]

]
PERMUTATION_TABLE = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13,
                     30, 6, 22, 11, 4, 25]

# ___________________________encryption____________________________________________________#


INITIAL_PERMUTATION_TABLE = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14,
                             6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11,
                             3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
INVERSE_PERMUTATION_TABLE = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62,
                             30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19,
                             59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]


def key_to_64(key_64):
    for i in range(8):
        if sum(key_64[i * 8:(i + 1) * 8 - 1]) % 2 == 0:
            key_64.insert((i + 1) * 8 - 1, 1)
        else:
            key_64.insert((i + 1) * 8 - 1, 0)
    return key_64


def generate_keys(key_64bits):
    round_keys = []
    pc1_out = permutations_table(key_64bits, table_key_64_to_56)  # Первая перестановка. Из 64 бит в 56
    L0, R0 = break_in_half(pc1_out)  # Делим ключ на две половины
    for roundnumber in range(16):
        newL = circular_left_shift(L0, round_shifts[roundnumber])
        newR = circular_left_shift(R0, round_shifts[roundnumber])
        roundkey = permutations_table(newL + newR, table_key_56_to_48)  # Вторая перестановка. Из 56 бит в 48
        round_keys.append(roundkey)
        L0 = newL
        R0 = newR
    return round_keys


def round_func(pre32bits, key48bits):
    result = []
    expanded_left_half = permutations_table(pre32bits, EXPANSION_TABLE)  # Расширение 32 битной строки до 48
    xor_value = XOR(expanded_left_half, key48bits)
    bits6list = break_in_nbits(8, xor_value)  # Разбиваем строку 48 бит на 8 строк по 6 бит
    for sboxcount, bits6 in enumerate(bits6list):
        first_last = binary_to_decimal(bits6[:1] + bits6[len(bits6) - 1:])
        middle = binary_to_decimal(bits6[1:5])
        sboxvalue = decimal_to_binary(SBOX[sboxcount][first_last][middle])
        result += sboxvalue[4:]
    final32bits = permutations_table(result, PERMUTATION_TABLE)  # перестановка P
    return final32bits


def encryption(bit_text_64, roundkeys, whatDo):
    p_text_64 = permutations_table(bit_text_64, INITIAL_PERMUTATION_TABLE)
    left_txt, right_txt = break_in_half(p_text_64)
    for round in range(16):
        if whatDo == 'Шифруем':
            newR = XOR(left_txt, round_func(right_txt, roundkeys[round]))
            newL = right_txt
        else:
            newL = XOR(right_txt, round_func(left_txt, roundkeys[round]))
            newR = left_txt
        right_txt = newR
        left_txt = newL
    i_text_64 = permutations_table(left_txt + right_txt, INVERSE_PERMUTATION_TABLE)
    return i_text_64

def DES(openText, input, whatDo, Progress):
    key = []
    if input is '':
        random.seed()
        for i in range(56):
            key.append(random.randint(0, 1))
    else:
        for i in input:
            key.append(int(i))

    key_64 = key_to_64(key[:])
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

    roundkeys = generate_keys(key_64)

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

    return res[:1000].decode('mbcs'), res, ''.join(map(str, key)), "Исходный ключ: " + str(
        key) + "\n" + "С корректирующими битами: " + "\n" + str(
        key_64) + "\n" + "Длина текста: " + str(amount_bytes_old)


"""t1 = DES(bytearray(bytes('Мама мыла раму', 'mbcs')), '10000000001011101000110101101100000111011111001110011111',
         "Шифруем")
t2 = DES(t1, '10000000001011101000110101101100000111011111001110011111',
         "Расшифруем")
print(str(t1.decode('mbcs')) + '\n' + str(t2.decode('mbcs')) + str(len(t1)) + str(len(t2)) + str(
    len(bytes('Мама мыла раму', 'mbcs'))))"""
