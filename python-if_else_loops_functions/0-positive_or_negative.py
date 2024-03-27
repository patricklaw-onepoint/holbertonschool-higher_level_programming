#!/usr/bin/python3
import random
number = random.randint(-10, 10)
str = f"{'positive' if number > 0 else 'negative' if number < 0 else 'zero'}"
print(f"{number} is {str}")
