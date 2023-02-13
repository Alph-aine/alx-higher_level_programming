#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    new_set = set(my_list)
    new_list = list(new_set)
    sum_i = 0
    for i in new_list:
        sum_i += i
    return sum_i
