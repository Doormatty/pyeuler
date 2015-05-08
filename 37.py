import time
import math

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

def truncprime(n):
    n=str(n)
    for x in range(1,len(n)):
        if not ((isPrime(int(n[x:]))) and (isPrime(int(n[:len(n)-x])))):
                return False
    return True

prime_list=[]
f=open('primelist2.txt','r')
for i in range(1,100000):
    foo=str(f.readline())
    foo=foo[0:len(foo)-1] #Strip off the eol
    if ((foo[0] or foo[len(foo)])!=('1' or '4' or '6' or '8' or '9')):
        if truncprime(foo): prime_list.append(int(foo))
f.close()
pset=set(prime_list)
