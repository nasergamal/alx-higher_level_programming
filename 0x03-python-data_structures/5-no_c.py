#!/usr/bin/python3
def no_c(my_string):
    ns = "".join([n for n in my_string if n not in "Cc"])
    return ns
