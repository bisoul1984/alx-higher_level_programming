#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numb = 0
    den = 0

    for tupi in my_list:
        numb += tupi[0] * tupi[1]
        den += tupi[1]

    return (numb / den)
