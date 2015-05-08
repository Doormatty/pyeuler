import math
import sys
from eulerfunctions import compgen, primegen


p = primegen()
prime_list = []
for i in range(1, 1000):
    prime_list.append(next(p))
print('Primes to', prime_list[len(prime_list) - 1], 'have been pre-calculated')

d = compgen()
for i in d:
    if i % 2 == 0:
        continue
    for x in prime_list:
        if x > i:
            print(i, 'IS MOLD BREAKER')
            sys.exit()
        if i - x == 1:
            break
        foo = (i - x) / 2
        foo = math.sqrt(foo)
        if foo == int(foo):
            break