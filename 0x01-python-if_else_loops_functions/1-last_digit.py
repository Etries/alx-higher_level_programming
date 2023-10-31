#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number
if number < 0:
    x = number * -1
n = int(x % 10)
if n > 5 and number > 0:
    print(f"Last digit of {number} is {n} and is greater than 5")
elif n == 0:
    print(f"Last digit of {number} is {n} and is 0")
elif number < 0 and n !=0 or n < 6 and n != 0:
    if number < 0:
        print(f"Last digit of {number} is -{n} and is less than 6 and not zero")
    else:
        print(f"Last digit of {number} is {n} and is less than 6 and not zero")
