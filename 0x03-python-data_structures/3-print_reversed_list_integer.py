#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    rangeList = [x for x in range(len(my_list))]
    rangeList.reverse()
    for i in rangeList:
        print("{:d}".format(my_list[i]))
