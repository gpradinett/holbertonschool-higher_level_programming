#!/usr/bin/python3
for first_digit in range(0, 9):
    for last_digit in range(1, 10):
        if last_digit > first_digit:
            if first_digit != 8 or last_digit != 9:
                print("{}{}".format(first_digit, last_digit), end=", ")
            else:
                print("{}{}".format(first_digit, last_digit))
