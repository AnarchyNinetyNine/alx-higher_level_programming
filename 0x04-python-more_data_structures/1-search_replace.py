#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list or search not in my_list:
        return None
    new_list = my_list[:]
    new_list.insert(my_list.index(search), replace)
    return new_list
