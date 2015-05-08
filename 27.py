import math
import time
from eulerfunctions import isprime


starttime = time.time()
highx, highy, highprime = 0, 0, 0
for x in range(-999, 1000):
    for y in range(-999, 1000):
        primecount = 0
        for n in range(0, 1000):
            foo = (n * n) + (n * x) + y
            if isprime(foo):
                primecount += 1
            else:
                break
        if primecount > highprime:
            # print ('New Possible Record: x=',x,' y=',y,' primecount=',primecount,sep='')
            highprime = primecount
            highx = x
            highy = y
print('n^2+', highx, 'n+', highy, ' has ', highprime, ' primes in a row.', sep='')
print('Time:', time.time() - starttime)