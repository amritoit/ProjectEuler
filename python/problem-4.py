# problem-3.py ---
# Filename: problem-3.py
# Description: problem: https://projecteuler.net/problem=3
# Author: Amritendu Mondal
# Email:  amritoit@gmail.com
# Organization:  IIT Madras
# Created: Thu Jul 25 22:43:31 2019 (+0530)
# Last-Updated:
#           By:
#     Update #: 21
#

# solution: bf approach will work as computation is fast.


import time


def compute(lower_limit, upper_limit):
    a = max(i*j
            for i in range(upper_limit, lower_limit, -1)
            for j in range(i, lower_limit, -1) if str(i*j) == str(i*j)[::-1])
    return a


start_time = time.time()
print("compute result =", compute(100, 999),
      ", time taken - ", (time.time() - start_time), " seconds")
assert compute(100, 999) == 906609

print("all test case passed")
