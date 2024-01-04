#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(97, 123):
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(c) - num), end="")
    print()
