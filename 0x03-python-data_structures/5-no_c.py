#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return None
    new_string = ""
    for x in my_string:
        if x not in "cC":
            new_string += x
    return new_string
