from eulerfunctions import *


def Selecting(n, r):
    if r > n:
        return 0
    nfac = math.factorial(n)
    rfac = math.factorial(r)
    nrfac = math.factorial(n - r)
    return nfac / (rfac * nrfac)


count = 0

for x in range(1, 101):
    for y in range(1, x):
        if Selecting(x, y) > 1000000:
            count += 1

print(count)
            