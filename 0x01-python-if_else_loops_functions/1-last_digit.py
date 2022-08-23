#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_to_str = repr(number)
last_digit_str = num_to_str[-1]
lastd = int(last_digit_str)
if number > 0 and lastd > 5:
    print("Last digit of", number, "is", lastd, "and is greater than 5")
elif lastd == 0:
    print("Last digit of", number, "is", lastd, "and is 0")
elif number > 0 and lastd < 6:
    print("Last digit of", number, "is", lastd, "and is less than 6 and not 0")
elif number < 0:
    print("Last digit of", number, "is", -lastd, "and is less than 6 and not 0")
elif number < 6 and number < 0:
    print("Last digit of", number, "is-", -lastd, "and is less than 6 and not 0")
