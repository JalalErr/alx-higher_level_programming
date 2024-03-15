#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
if number < 0:
    numbr = number * -1
    digit = (numbr % 10) * -1
else:
    digit = number % 10
message = "Last digit of"
if digit == 0:
    print(f"{message} {number} is 0")
elif digit != 0 and digit < 6:
    print(f"{message} {number} is {digit} and is less than 6 and not 0")
else:
    print(f"{message} {number} is {digit} and is greater than 5")
