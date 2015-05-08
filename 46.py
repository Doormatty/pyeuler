import itertools
import math
import sys

#Returns a Composite Number Genarator
def compgen(x=4):
    for n in itertools.count(x):
        if (n<4):
            continue
        elif (n%2==0):
            yield n
        elif (n%3==0):
            yield n
        else:
            r=math.floor(math.sqrt(n))
            for f in range(5,r+1,6):
                if (n%f==0):
                    yield n
                if (n%(f+2)==0):
                    yield n
                    
def primegen(x=1):
    for n in itertools.count(x):
        if (n==1):
            continue
        elif (n%2==0):
            continue
        elif (n<4):
            yield n
        elif (n<9):
            yield n
        elif (n%3==0):
            continue
        else:
            r=math.floor(math.sqrt(n))
            for f in range(5,r+1,6):
                if (n%f==0):
                    break
                if (n%(f+2)==0):
                    break
            else:
                yield n

p=primegen()
prime_list=[]
for i in range(1,1000):
    prime_list.append(next(p))
print ('Primes to',prime_list[len(prime_list)-1],'have been pre-calculated')

d=compgen()
for i in d:
    if i%2==0: continue
    for x in prime_list:
        if (x>i):
            print (i,'IS MOLD BREAKER')
            sys.exit()
        if (i-x==1): break
        foo=(i-x)/2
        foo=math.sqrt(foo)
        if foo==int(foo):
            break