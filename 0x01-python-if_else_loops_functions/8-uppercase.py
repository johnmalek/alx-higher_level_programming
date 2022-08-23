#!/usr/bin/python3
def uppercase(str):
   for n in range(len(str)):
       ascii_value = ord(str[n])
       if ascii_value >= 97 and ascii_value <= 122:
           ascii_value -= 32
       print("{}".format(chr(ascii_value)), end="")
    print()


uppercase("best")
uppercase("Best School 98 Battery street")
