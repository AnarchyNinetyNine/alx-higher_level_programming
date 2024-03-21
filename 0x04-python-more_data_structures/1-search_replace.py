#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda elem : elem if elem != search else replace, my_list))
