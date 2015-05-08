from eulerfunctions import isprime

def iscircleprime(n):
    if not isprime(n):
        return False
    n = str(n)
    for i in range(0, len(n) - 1):
        n = n[1:] + n[0:1]
        if not isprime(int(n)):
            return False
    return True


count = 0
for i in range(1, 1000000):
    if iscircleprime(i):
        count += 1
print(count)