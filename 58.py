import math


def isPrime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
    return True


highprime = 0
highnum = 2
sprime = set()


def diagprimes(n):  # return the number of primes on the diagonals for a clockwise spiral of size n*n
    global highprime
    global sprime
    global highnum

    primecount = 0
    diaglen = int(((n - 1) / 2) + 2)

    startnum = highnum
    primecount += len(list(sprime))

    for n in range(startnum, diaglen + 1):
        nsqr = n * n * 4
        for i in range(1, 5):
            if i == 1:
                x = (nsqr - (10 * n) + 7)  #dr
            elif i == 2:
                x = (nsqr - (8 * n) + 5)  #dl
            elif i == 3:
                x = (nsqr - (6 * n) + 3)  #ul
            elif i == 4:
                x = (nsqr - (4 * n) + 1)  #ur

            if x > highprime and isPrime(x):
                primecount += 1
                sprime.add(x)
                highprime = x

    if diaglen > highnum:
        highnum = diaglen
    return primecount


n = 3
while True:
    x = diagprimes(n)

    if x < ((n * 2 - 1) / 10):
        print('Found!', n)
        break
    n += 2
    print(n, 'sided cube has', x, 'primes and', (n * 2 - 1), 'numbers, for a ratio of',
          math.ceil(x / (n * 2 - 1) * 100), '%')