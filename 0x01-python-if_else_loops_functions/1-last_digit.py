#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ldigit = ((number * -1) % 10) * -1
else:
    ldigit = number % 10

print(f"Last digit 0f {number:d} is {ldigit:d} and is", end=" ")

if ldigit > 5:
    print("greater than 5")

elif ldigit == 0:
    print("0")

else:
    print("less than 6 and not 0")
