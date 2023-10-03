#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numstr = repr(number)
lastNumStr = numstr[-1]
lastDigit = int(lastNumStr)
print(f"Last digit of {number} is {lastDigit }", end=' ')
if lastDigit > 5:
    print("and is greater than 5")
elif lastDigit == 0:
    print("and is zero")
elif lastDigit < 6 and not 0:
    print("and is less than 6 and not 0")
