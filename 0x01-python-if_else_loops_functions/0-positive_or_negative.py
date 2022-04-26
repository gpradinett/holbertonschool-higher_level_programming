#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("is positive")
elif number == 0:
    print("iz zero")
elif number < 0:
    print("is negative")
