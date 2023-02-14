#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        return None
    try:
        count = 0
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            count += 1
        print()
        return count
    except IndexError:
        print()
        return count
