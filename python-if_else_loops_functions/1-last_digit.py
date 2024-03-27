#!/usr/bin/python3
import random	
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
strG = 'greater than 5'
strL = 'less than 6 and not 0'
str = f"{{strG} if digit > 5 else '0' if digit == 0 else {strL}}"
print(f"Last digit of {number} is {digit} and is {str}")
