#!/usr/bin/python3

def best_score(a_dictionary):
    keys = a_dictionary.keys() if a_dictionary else None
    return max([a_dictionary[key] for key in keys]) if keys else None
