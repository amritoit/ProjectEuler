# problem-20.py ---
# Filename: problem-20.py
# Description: https://projecteuler.net/problem=29
# Author: Amritendu Mondal
# Email:  amritoit@gmail.com
# Organization:  Microsoft
# Created: Tue Jul 23 01:40:58 2019 (+0530)
# Last-Updated:
#           By:
#     Update #: 36
#

import time


def compute(low, high):
    store = {}
    for i in range(low, high+1):
        for j in range(low, high+1):
            a = i**j
            if a not in store:
                store[i**j] = 1
    return len(store.keys())

def compute1():
    seen = set(a**b for a in range(2, 101) for b in range(2, 101))
    return str(len(seen))


start_time = time.time()
print("compute result=", compute(2,100),
      ", time taken-", (time.time() - start_time), " seconds")

assert compute1() == '9183'

print("compute result=", compute1(),
      ", time taken-", (time.time() - start_time), " seconds")

print("all test passed")
