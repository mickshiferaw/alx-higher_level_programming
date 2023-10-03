#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_to_str = repr(number)
last_digit_str = num_to_str[-1]
la = int(last_digit_str)
if number > 0 and la > 5:
    print("Last digit of", number, "is", la, "and is greater than 5")
elif la == 0:
    print("Last digit of", number, "is", la, "and is 0")
elif number > 0 and la < 6:
    print("Last digit of", number, "is", la, "and is less than 6 and not 0")
elif number < 0:
    print("Last digit of", number, "is", -la, "and is less than 6 and not 0")
elif number < 6 and number < 0:
    print("Last digit of", number, "is", -la, "and is less than 6 and not 0")
