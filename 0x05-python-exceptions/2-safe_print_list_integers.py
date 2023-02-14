#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if my_list is None:
        return None
    count = 0
    i = 0
    while i < x:
        try:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end='')
                count += 1
        except TypeError:
            continue
        i += 1
    print()
    return count
