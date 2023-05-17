#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    su, d = 0, 0
    for k in my_list:
        su += k[0] * k[1]
        d += k[1]
    return su / d
