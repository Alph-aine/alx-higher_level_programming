#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv) - 1
    if size == 0:
        print("{} argument.".format(size))
    elif size == 1:
        print("{} argument:".format(size))
    else:
        print("{} arguments:".format(size))
    for i in range(1, size + 1):
        print("{}: {}".format(i, sys.argv[i]))
