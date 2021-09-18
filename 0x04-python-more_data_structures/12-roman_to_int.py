#!/usr/bin/python3


def roman_to_int(roman_string):
    sum = 0
    rom_num = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

    rom_len = len(roman_string)
    if rom_len == 0:
        return None
    for x in roman_string:
        if x not in rom_num:
            return None
    for i in range(0, rom_len):
        if roman_string[i] in rom_num:
            if i < (rom_len - 1):
                if rom_num[roman_string[i + 1]] and rom_num[roman_string[i]]\
                        < rom_num[roman_string[i + 1]]:
                    sum -= rom_num[roman_string[i]]
                else:
                    sum += rom_num[roman_string[i]]
            else:
                sum += rom_num[roman_string[i]]
        else:
            return None
    return sum
