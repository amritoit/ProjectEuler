# problem-67.py ---
# Filename: problem-67.py
# Description: https://projecteuler.net/problem=67
# Author: Amritendu Mondal
# Email:  amritoit@gmail.com
# Organization:  IIT Madras
# Created: Mon Jul 22 18:53:27 2019 (+0530)
# Last-Updated:
#           By:
#     Update #: 22
#
# solution: similar to problem 18 - https://projecteuler.net/problem=18
import time


def max_weight_of_paths(triangle):
    for i in range(len(triangle)-2, -1, -1):
        for j in range(0, len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]


def compute():
    input_f = open("p067_triangle.txt", "r")
    triangle = []
    for line in input_f:
        triangle.append(list(map(int, line.strip().split())))
    return max_weight_of_paths(triangle)


start_time = time.time()
print("compute result =", compute(),
      ", time taken - ", (time.time() - start_time), " seconds")
assert compute() == 7273
print("all test passed")
