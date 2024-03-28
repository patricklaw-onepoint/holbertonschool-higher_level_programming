#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
if digit > 5:
    str = "greater than 5"
elif digit == 0:
    str = "0"
else:
    str = "less than 6 and not 0"

print(f"Last digit of {number} is {digit} and is {str}")
