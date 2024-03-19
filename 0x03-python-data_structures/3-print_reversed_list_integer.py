#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rangeList = [x for x in range(len(my_list))]
    rangeList.reverse()
    for i in rangeList:
        print("{:d}".format(my_list[i]))
