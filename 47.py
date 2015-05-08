import math
import itertools

def isPrime(n):
    if (n==1):
        return False
    elif (n<4):
        return True
    elif (n%2==0):
        return False
    elif (n<9):
        return True
    elif (n%3==0):
        return False
    else:
        r=math.floor(math.sqrt(n))
        f=5
        while (f<=r):
            if (n%f==0):
                return False
            if (n%(f+2)==0):
                return False
            f+=6
    return True

def primegen(x=1):
    for n in itertools.count(x):
        if (n==1):
            continue
        elif (n==2):
            yield n
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

def primefac(n):
    if isPrime(n):
        return [n]
    faclist=[]
    p=primegen()
    x=next(p)
    while n!=1:
        if n%x==0:
            faclist.append(x)
            n=n/x
        else:
            if isPrime(n):
                faclist.append(int(n))
                return faclist
            x=next(p)
    return faclist
 
i=4
a=set(primefac(i))
b=set(primefac(i-1))
c=set(primefac(i-2))
d=set(primefac(i-3))
while True:
    if (len(a)>=4 and len(b)>=4 and len(c)>=4 and len(d)>=4):
        print (i,i+1,i+2,i+3)
    i+=1
    d=c
    c=b
    b=a
    a=set(primefac(i))
    