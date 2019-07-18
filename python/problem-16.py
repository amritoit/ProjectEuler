## 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
## What is the sum of the digits of the number 2^1000?

## soluton: calculate 2^1000, as python can handle big integer, it will give the result in a string.
## take all digit from that string and sum up.

def compute(power):
    result = 2**power
    total  = sum(int(c) for c in str(result))
    return total

assert compute(15) == 26
assert compute(1000) == 1366
print("all test passed")
