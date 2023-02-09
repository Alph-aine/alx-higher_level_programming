#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    size = len(sys.argv) - 1
    if size == 0:
        print("0")
    elif size == 1:
        print("{:d}".format(int(sys.argv[1])))
    else:
        for i in range(1, size + 1):
            count += int(sys.argv[i])
        print("{}".format(count))
