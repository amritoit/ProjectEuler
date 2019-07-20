## problem: https://projecteuler.net/problem=12
## solution: the catch of this problem is to find no of divisor of any number efficiently.
## the BF approach will not work as the no we want to calculate for is very high.
## So what we should do is find numbers from 1 to sqrt(n) which can divide n, now we know
## if any one of these divided n then there must be another number which will divide n,
## so we will count it twice.
# https://www.geeksforgeeks.org/total-number-divisors-given-number/

import itertools
import eulerlib

def no_of_divisor(n):
    (is_perfect_square, sqroot) = eulerlib.is_square(n)
    count = sum(2 for i in range(1, sqroot+1) if n%i==0)
    count = count - 1 if is_perfect_square else count # this is because 4*4 =16, we will end up counting 4 twice.
    return count

def compute(divisor_count):
    number = 0
    for i in itertools.count(1):
        number = number + i # This is the ith triangle number, i.e. num = 1 + 2 + ... + i = i * (i + 1) / 2
        if(no_of_divisor(number) > divisor_count):
            return number


import time
start_time = time.time()
print("compute for 500, result =", compute(500), ", time taken - ", (time.time() - start_time), " seconds")
assert compute(500) ==  76576500
assert compute(4) == 28
assert no_of_divisor(28) == 6
assert no_of_divisor(21) == 4
assert no_of_divisor(1) == 1
assert no_of_divisor(2) == 2
assert no_of_divisor(76576500) == 576
print("Bingo! all tests passed.")
