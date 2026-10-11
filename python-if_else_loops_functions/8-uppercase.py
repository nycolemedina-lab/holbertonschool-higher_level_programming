#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        key = ord(str[i])
        if 97 <= key <= 122:
            key = key - 32
        print("{}".format(chr(key)), end="")
    print("")
