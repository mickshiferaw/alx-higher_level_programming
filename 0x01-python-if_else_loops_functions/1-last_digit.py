#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_to_str = repr(number)
last_digit_str = num_to_str[-1]
last_di = int(last_digit_str)
if last_di > 5:
    print("Last digit of", number, "is", last_di, "and is greater than 5")
elif last_di == 0:
    print("Last digit of", number, "is", last_di, "and is 0")
elif last_di < 6 and last_di != 0:
    print("Last digit of", number, "is", last_di, "and is less than 6 and not 0")
