#!/usr/bin/python3
def remove_char_at(str, n):
    strCpy = ""
    for i in range(len(str)):
        if i != n:
            strCpy += str[i]
    return strCpy
