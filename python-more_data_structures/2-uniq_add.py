#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    seen = []


    for x in my_list:
        if x not in seen:
            seen.append(x)
            total += x

    return total
