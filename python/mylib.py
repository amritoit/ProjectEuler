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
