#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            uppercase_c = chr(ord(c) -32)
            print("{}".format(uppercase_c), end="")
        else:
            print("{}".format(c), end="")
    print("")
