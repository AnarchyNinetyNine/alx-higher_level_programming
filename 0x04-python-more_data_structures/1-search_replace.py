#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list or search not in my_list:
        return None
    new_list = list(map(lambda elem : elem if elem != search else replace, my_list))
    return new_list
