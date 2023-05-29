#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for i in my_list:
            if n < x:
                print(i, end="")
                n += 1
            else:
                break
    except:
        print("print fail")
    finally:
        print("")
        return n
