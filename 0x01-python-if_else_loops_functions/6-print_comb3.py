#!/usr/bin/python3
# Author - Tolulope Fakunle

for num1 in range(0, 10):
    for num2 in range(num1 + 1, 10):
        if num1 == 8 and num2 == 9:
            print("{}{}".format(num1, numt2))
        else:
            print("{}{}".format(num1, num2), end=", ")
