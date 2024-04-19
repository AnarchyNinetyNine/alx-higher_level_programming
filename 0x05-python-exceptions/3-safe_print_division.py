#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        quotion = int(a) / int(b)
    except ZeroDivisionError:
        quotion = None
    finally:
        print("Inside result: ", quotion)
        return quotion
