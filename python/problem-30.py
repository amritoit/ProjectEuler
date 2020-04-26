# problem-30.py --- 
# Filename: problem-30.py
# Description: 
# Author: 
# Email:  amritoit@gmail.com
# Organization:  Microsoft
# Created: Mon Apr 27 02:16:31 2020 (+0530)
# Last-Updated: Mon Apr 27 02:33:54 2020 (+0530)
#           By: ammondal
#     Update #: 28
# Lets determine the upper bound. We need to find a number x95 which gives us an x digit number. 
# We can do this by hand. Since 95 = 59049, we need at least 5 digits. 595 = 295245, 
# so with 5 digits we can make a 6 digit number. 6*95 = 354294. So 355000 seems like a reasonable upper bound to use.
# We could probably tighten is even further if we wanted.

import time

def compute1():
	ans = sum(i for i in range(2, 355001) if i == fifth_power_digit_sum(i))
	return str(ans)

def fifth_power_digit_sum(n):
	return sum(int(c)**5 for c in str(n))


def compute(p):
    s = 0
    for i in range(2,355001):
        n = i
        re = 0
        while n > 0:
            if n > 9:
                r = n%10
            else:
                r = n
            re += r**p
            n = n//10
        if re == i:
            s += re
    return s

assert compute(4) == 19316
print('all tests passed')

start_time = time.time()
print("compute result=", compute(5),
      ", time taken-", (time.time() - start_time), " seconds")

start_time = time.time()
print("compute result=", compute1(),
      ", time taken-", (time.time() - start_time), " seconds")
