# problem-22.py ---
# Filename: problem-22.py
# Description: https://projecteuler.net/problem=22
# Author: Amritendu Mondal
# Email:  amritoit@gmail.com
# Organization:  IIT Madras
# Created: Tue Jul 23 21:45:59 2019 (+0530)
# Last-Updated:
#           By:
#     Update #: 30
#


import time


def compute():
    input_f = open("p022_names.txt", "r")
    line = input_f.readline().replace('"', '')
    names = sorted(line.split(","))
    result = sum((i+1) * (ord(ch)-ord("A")+1)
                 for (i, name) in enumerate(names)
                 for ch in name)
    return result


start_time = time.time()
print("compute result=", compute(),
      ", time taken-", (time.time() - start_time), " seconds")
assert compute() == 871198282
print("all test passed")
