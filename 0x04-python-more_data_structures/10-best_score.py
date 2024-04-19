#!/usr/bin/python3

def best_score(a_dictionary):
    keys = list(a_dictionary.keys()) if a_dictionary else None
    values = list(a_dictionary.values()) if a_dictionary else None
    bst = max(values) if values else None
    return keys[values.index(bst)] if bst else None
