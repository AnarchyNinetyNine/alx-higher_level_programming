#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda e : e if replace == search else e, my_list))
