#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    for num in sys.argv[1:]:
        res += int(num)
    print(res)
