#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    ldigit = number % 10
else:
    ldigit = number % -10

if ldigit == 0:
    state = "0"
elif ldigit > 5:
    state = "greater than 5"
else:
    state = "less than 6 and not 0"

print(f"Last digit of {number} is {ldigit} and is {state}")
