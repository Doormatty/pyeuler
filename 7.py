import time
from eulerfunctions import isprime

starttime = time.time()
x = 2
count = 0
while count < 10001:
    if isprime(x):
        count += 1
    x += 1
print('Prime #', count, ' - ', x - 1)
print('Time: ', time.time() - starttime)