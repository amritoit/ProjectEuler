# problem-15.py ---
# Filename: problem-15.py
# Description: https://projecteuler.net/problem=15
# Author: Amritendu Mondal
# Email:  amritoit@gmail.com
# Organization:  IIT Madras
# Created: Sun Jul 21 03:01:43 2019 (+0530)
# Last-Updated:
# By:
# Update #: 0
######################################################################
# problem: https://projecteuler.net/problem=15
import mylib


@mylib.memoize
def no_of_path_in_grid(m, n):
    if(m == 0 and n == 0):
        return 1
    elif(m < 0 or n < 0):
        return 0
    else:
        return no_of_path_in_grid(m, n-1) + no_of_path_in_grid(m-1, n)


assert no_of_path_in_grid(2, 2) == 6
assert no_of_path_in_grid(20, 20) == 137846528820
print("Bingo! all test passed")

# solution 2


def compute():
    return str(mylib.binomial(40, 20))


assert compute() == "137846528820"
print("Again Bingo! all test passed")
