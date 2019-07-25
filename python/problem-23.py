# problem-23.py ---
# Filename: problem-23.py
# Description: https://projecteuler.net/problem=23
# Author: Amritendu Mondal
# Email:  amritoit@gmail.com
# Organization:  IIT Madras
# Created: Tue Jul 23 22:24:04 2019 (+0530)
# Last-Updated:
#           By:
#     Update #: 41
#

import itertools


def compute(limit):
    divisor_table = [0] * limit
    for i in range(1, limit):
        for j in range(i*2, limit, i):
            divisor_table[j] += i
    abundant_numbers = [divisor_table[i]
                        for i in range(1, limit) if divisor_table[i] > i]

    for i in range(0, len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            if(i+j < limit):
                divisor_table
                divisor_table[i+j] = -1
    print(divisor_table)

    result = sum(c for c in range(1, limit) if divisor_table[c] >= 0)
    return result


print(compute(20))
