#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        i = len(my_list) - 1
        max_i = i
        while i:
            j = 0
            while j < i:
                if my_list[j] > my_list[j + 1]:
                    temp = my_list[j]
                    my_list[j] = my_list[j + 1]
                    my_list[j + 1] = temp
                j += 1
            i -= 1
        return my_list[max_i]
