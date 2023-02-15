#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            element1 = my_list_1[i]
            element2 = my_list_2[i]
            if (isinstance(element1, (int, float))
                    and isinstance(element2,  (int, float))):
                if element2 == 0:
                    result.append(0)
                    print("division by 0")
                else:
                    result.append(element1 / element2)
            else:
                result.append(0)
                print("wrong type")
        except IndexError:
            result.append(0)
            print("out of range")
        finally:
            pass
    return result
