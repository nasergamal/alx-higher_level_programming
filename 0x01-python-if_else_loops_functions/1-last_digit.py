#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    ld = number % 10
elif number < 0:
    ld = (number % 10)
    ld = ld - 10 if (ld > 0) else ld
else:
    ld = number
if ld > 5:
    val = "and is greater than 5"
elif ld < 6 and ld != 0:
    val = "and is less than 6 and not 0"
else:
    val = "and is 0"
print (f'Last digit of {number} is {ld} {val}')
