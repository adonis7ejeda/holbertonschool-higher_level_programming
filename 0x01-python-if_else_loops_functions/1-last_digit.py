#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if last > 5:
    s = "and is greater than 5"
elif last == 0:
    s = "and is 0"
else:
    s = "and is less than 6 and not 0"
print("Last digit of {:d} is {:d} {:s}".format(number, last, s))
