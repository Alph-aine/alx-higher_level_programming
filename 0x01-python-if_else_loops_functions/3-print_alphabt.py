#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    exception = chr(c)
    if exception == 'e' or exception == 'q':
        continue
    print("{}".format(exception), end='')
