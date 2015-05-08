import time
import math
import itertools
import collections
import functools


#Loads first 10 million primes from file
global prime_list
prime_list = []
f = open('10Mprimes.txt', 'r')
for line in f:
    prime_list.append(int(line))
f.close()
cache_high=prime_list[-1]
prime_list=set(prime_list)


class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)


#Checks if a number is Prime
@memoized
def isPrime(n):
    if n == 1:
        return False
    elif n <= cache_high:
        return n in prime_list
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False

    #elif prime_list[-1] > math.floor(math.sqrt(n)):  # Does the cache hold numbers large enough to help us?
    #    return n in prime_list
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

#Returns a Prime Number Generator
def primegen():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


#returns a list of the prime factors of a number
@memoized
def primefac(n):
    #if isPrime(n):
    #    return []
    faclist = []
    p = primegen()
    x = next(p)
    while n != 1:
        if n % x == 0:
            faclist.append(x)
            n /= x
        else:
            if isPrime(n):
                faclist.append(int(n))
                return faclist
            x = next(p)
    return faclist



#Returns a Composite Number Generator
def compgen(x=4):
    for n in itertools.count(x):
        if n < 4:
            continue
        elif n % 2 == 0:
            yield n
        elif n % 3 == 0:
            yield n
        else:
            r = math.floor(math.sqrt(n))
            for f in range(5, int(r + 1), 6):
                if n % f == 0:
                    yield n
                if n % (f + 2) == 0:
                    yield n

#checks if a number is square
def issquare(n):
    return n == int(math.sqrt(n))

#checks if a number is triangular
def istriangle(n):
    return issquare(n * 8 + 1)


#checks if a number is pentagrammic                
def ispenta(n):
    n = (math.sqrt(n * 24 + 1) + 1) / 6
    return n == int(n)

#checks if a number is hexagonal    
def ishexa(n):
    n = (math.sqrt(n * 8 + 1) + 1) / 4
    return n == int(n)

#Returns a triangular number generator
def trigen():
    i = 1
    n = 0
    while True:
        n += i
        yield n
        i += 1

#Returns a square number generator
def squaregen():
    i = 1
    while True:
        yield i ** 2
        i += 1


#returns a pentagonal number generator
def pentagen():
    i = 1
    while True:
        yield int(i / 2 * (3 * i - 1))
        i += 1

#returns a hexagonal number generator
def hexagen():
    i = 1
    while True:
        yield i * (2 * i - 1)
        i += 1

#returns a heptagonal number generator
def heptagen():
    i = 1
    while True:
        yield int(i * (5 * i - 3) / 2)
        i += 1

#returns an octagonal number generator
def octagen():
    i = 1
    while True:
        yield i * (3 * i - 2)
        i += 1

#checks if a string is a palindrome       
def check_palindrome(input, case=True, strip=True):
    bar = ascii(input)
    if (strip):
        bar = bar.replace(' ', '')
    if (case):
        bar = bar.upper()
    length = len(bar)
    if (length % 2 == 0):
        if ((bar[:(length // 2)]) == (bar[length:(length // 2 - 1):-1])):
            return True
    else:
        if ((bar[:(length // 2)]) == (bar[length:(length // 2):-1])):
            return True
    return False





def prime_bench(limit=1000):
    start=time.time()
    #p=gen_primes()
    p=primegen()
    for i in range(limit):
        p.next()
    end=time.time()
    print "Total time:",end-start
