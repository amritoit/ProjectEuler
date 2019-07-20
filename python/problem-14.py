# problem: https://projecteuler.net/problem=14
# solution:
# find size of collatz sequence starting with a number,
# there will be repeating number, hence caching those will improve performance.


import time
import eulerlib


def len_of_collatz_chain(n, cache):
    if cache.get(n) is not None:
        return cache.get(n) + 1
    n1 = n//2 if n % 2 == 0 else 3 * n + 1
    total_len_from_n = 1 + len_of_collatz_chain(int(n1), cache)
    cache[n] = total_len_from_n
    return total_len_from_n


def compute(n):
    cache = {1: 0}
    for i in range(n, 0, -1):
        len_of_collatz_chain(i, cache)
    return max(cache, key=cache.get)


start_time = time.time()
print("compute for 1000000, result =", compute(1000000),
      ", time taken - ", (time.time() - start_time), " seconds")
assert len_of_collatz_chain(13, {1: 0}) == 10
assert len_of_collatz_chain(5, {1: 0}) == 6
assert len_of_collatz_chain(20, {1: 0}) == 8
assert compute(1000000) == 837799
print("Bingo! all test case passed.")
