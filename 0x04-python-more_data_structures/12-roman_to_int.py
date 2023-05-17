#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return
    su = 0
    vald = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        if roman_string[i] not in vald:
            return 0
        if i == len(roman_string) - 1:
            su += vald[roman_string[i]]
        else:
            if vald[roman_string[i]] < vald[roman_string[i + 1]]:
                su -= vald[roman_string[i]]
            else:
                su += vald[roman_string[i]]
    return su
