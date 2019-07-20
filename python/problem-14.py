# problem-14.py ---
# Filename: problem-14.py
# Description:
# Author: Amritendu Mondal
## Email:  amritoit@gmail.com
# Organization:  IIT Madras
# Created: Sun Jul 21 02:53:34 2019 (+0530)
# Last-Updated:
# By:
# Update #: 0
######################################################################

# problem: https://projecteuler.net/problem=14
# solution:
# find legth of collatz sequence of all number from zero to one million,
# there will be repeating number, hence caching those will improve performance.


import time
import mylib
import sys


@mylib.memoize
def len_of_collatz_chain(n):
    if n == 1:
        return 1
    n1 = n//2 if n % 2 == 0 else 3 * n + 1
    return 1 + len_of_collatz_chain(n1)


def compute(n):
    # vm will terminate program on crossing this limit.
    sys.setrecursionlimit(4000)
    return max(range(1, 1000000), key=len_of_collatz_chain)


start_time = time.time()
print("compute for 1000000, result =", compute(1000000),
      ", time taken - ", (time.time() - start_time), " seconds")
assert len_of_collatz_chain(13) == 10
assert len_of_collatz_chain(5) == 6
assert len_of_collatz_chain(20) == 8
assert compute(1000000) == 837799
print("Bingo! all test case passed.")
