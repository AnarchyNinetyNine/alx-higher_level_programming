#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    listCopy = my_list.copy()
    listCopy.sort()
    return listCopy[-1]
