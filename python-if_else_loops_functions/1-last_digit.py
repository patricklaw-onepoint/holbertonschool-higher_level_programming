#!/usr/bin/python3
import random	
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
str = f"{'greater than 5' if digit > 5 else '0' if digit == 0 else 'less than 6 and not 0'}"
print(f"Last digit of {number} is {digit} and is {str}")
