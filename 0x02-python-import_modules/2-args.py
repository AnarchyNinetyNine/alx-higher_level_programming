#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    elem = len(sys.argv) - 1
    if elem == 0:
        print("0 arguments.")
    elif elem == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(elem))
    for i in range(elem):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
