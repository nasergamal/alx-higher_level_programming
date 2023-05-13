#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    mx = 0
    for i in my_list:
        mx = i if i > mx else mx
    return mx
