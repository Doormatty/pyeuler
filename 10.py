import time
import math
from eulerfunctions import isprime



starttime = time.time()
sum = 0
for i in range(1, 2000001):
    if isprime(i):
        sum += i
print('Answer :', sum)
print('Time :', time.time() - starttime)