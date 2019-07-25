# problem-20.py ---
# Filename: problem-20.py
# Description: https://projecteuler.net/problem=20
# Author: Amritendu Mondal
# Email:  amritoit@gmail.com
# Organization:  IIT Madras
# Created: Tue Jul 23 01:40:58 2019 (+0530)
# Last-Updated:
#           By:
#     Update #: 17
#
import time
import mylib


def compute(n):
    result = mylib.factorial(n)
    return sum(int(i) for i in str(result))


assert compute(10) == 27
assert compute(100) == 648
start_time = time.time()
print("compute =", compute(100), ", time taken - ",
      (time.time() - start_time), " seconds")
assert compute(100) == 648
print("all test passed")
