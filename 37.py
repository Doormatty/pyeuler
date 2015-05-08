from eulerfunctions import isprime


def truncprime(n):
    n = str(n)
    for x in range(1, len(n)):
        if not ((isprime(int(n[x:]))) and (isprime(int(n[:len(n) - x])))):
            return False
    return True


prime_list = []
f = open('primelist2.txt', 'r')
for i in range(1, 100000):
    foo = str(f.readline())
    foo = foo[0:len(foo) - 1]  # Strip off the eol
    if (foo[0] or foo[len(foo)]) != ('1' or '4' or '6' or '8' or '9'):
        if truncprime(foo): prime_list.append(int(foo))
f.close()
pset = set(prime_list)
