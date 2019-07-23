# problem-21.py ---
# Filename: problem-21.py
# Description: https://projecteuler.net/problem=21
# Author: Amritendu Mondal
# Email:  amritoit@gmail.com
# Organization:  IIT Madras
# Created: Tue Jul 23 20:54:08 2019 (+0530)
# Last-Updated:
#           By:
#     Update #: 76
#
# solution: I first compute a table of sum-of-proper-divisors,
# then I use it to test which numbers are amicable.
# Note: the proper-divisor-sum of each number by brute force is unacceptably slow in Python.


import time


def compute(limit):
    divisor_table = [0] * limit
    for i in range(1, len(divisor_table)):
        for j in range(i*2, len(divisor_table), i):
            divisor_table[j] += i

    count = 0
    for i in range(1, limit):
        j = divisor_table[i]
        if i < j and j < limit and divisor_table[j] == i:
            count += i + j
    return int(count)


assert compute(500) == 504
assert compute(100) == 0
assert compute(0) == 0
assert compute(285) == 504
start_time = time.time()
print("compute(10000)=", compute(10000), ", time taken-",
      (time.time() - start_time), " seconds")

print("Bingo! all test passed")
