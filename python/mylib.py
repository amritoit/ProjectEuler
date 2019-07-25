# my-lib.py ---
## Filename: my-llib.py
# Description:
# Author: Amritendu Mondal
## Email:  amritoit@gmail.com
# Organization:  IIT Madras
# Created: Sun Jul 21 02:53:34 2019 (+0530)
# Last-Updated:
# By:
# Update #: 0
######################################################################


# Decorator. The underlying function must take only positional arguments, no keyword arguments.
import math


class memoize(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        else:
            val = self.func(*args)
            self.cache[args] = val
            return val


def binomial(n, k):
    assert 0 <= k <= n
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def factorial(n):
    return math.factorial(n)


def is_leap_year(year):  # if the input year is a leap year or not
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    return False
