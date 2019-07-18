## problem:
## The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
## Find the sum of all the primes below two million.
import numpy as np
limit = 2000000;
i=2
all_numbers = np.arange(limit+1)
sum = 0
while i <= limit:    
    if(all_numbers[i]) != 1:
        k=1
        sum += i
        j = i
        while(j <= limit):
            all_numbers[j] = 1
            j = i*k
            k = k+1
    i = i + 1
print(sum)
