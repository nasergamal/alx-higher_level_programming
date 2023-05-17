#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return
    su = 0
    for i in range(len(roman_string)):
        if i == len(roman_string) - 1:
            if roman_string[i] == 'I':
                su += 1
            elif roman_string[i] == 'V':
                su += 5
            elif roman_string[i] == 'X':
                su += 10
            elif roman_string[i] == 'L':
                su += 50
            elif roman_string[i] == 'C':
                su += 100
            elif roman_string[i] == 'D':
                su += 500
            return su
        if roman_string[i] == 'I':
            if roman_string[i + 1] == 'V':
                su += 5
                i += 1
            elif roman_string[i + 1] == 'X':
                su += 9
                i += 1
            else:
                su += 1
            continue
        elif roman_string[i] == 'V':
            su += 5
        elif roman_string[i] == 'X':
            if roman_string[i + 1] == 'L':
                su += 40
                i += 1
            elif roman_string[i + 1] == 'C':
                su += 90
                i += 1
            else:
                su += 10
            continue
        elif roman_string[i] == 'L':
            su += 50
        elif roman_string[i] == 'C':
            if roman_string[i + 1] == 'D':
                su += 400
                i += 1
            elif roman_string[i + 1] == 'M':
                su += 900
                i += 1
            else:
                su += 100
        elif roman_string[i] == 'D':
            su += 500
        elif roman_string[i] == 'M':
            su += 1000
    return su
