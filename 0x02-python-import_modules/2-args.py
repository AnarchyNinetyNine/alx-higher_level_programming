#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    elem = len(sys.argv) - 1
    if elem == 0:
        print("0 arguments.")
    else:
        print("{} argument{}".format(elem, "." if elem == 1 else "s:"))
        for i in range(elem):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
