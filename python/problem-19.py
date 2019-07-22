# problem-19.py ---
# Filename: problem-19.py
# Description:  https://projecteuler.net/problem=19
# Author: Amritendu Mondal
# Email:  amritoit@gmail.com
# Organization:  IIT Madras
# Created: Mon Jul 22 21:12:56 2019 (+0530)
# Last-Updated:
#           By:
#     Update #: 70
#
# solution: we know that 1900, 1st jan is monday, so we will calculate the no of days of each
# month from 1901. If no of days mod 7 is 0 then its a sunday.

import time
import mylib

month_to_days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}


def compute():
    no_of_days = 12*30 + 7 - 2
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            no_of_days += month_to_days.get(month-1) if month > 1 else 0
            if month == 3 and mylib.is_leap_year(year):
                no_of_days += 1
            if (no_of_days+1) % 7 == 0:
                count += 1
            if(month == 12):
                no_of_days += 31
    return count


start_time = time.time()
print("compute =", compute(), ", time taken - ",
      (time.time() - start_time), " seconds")
assert compute() == 171
print("all test passed")
