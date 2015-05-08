import time
import math
import sys

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
    
def TriNum(n):
    return sum(range(1,n+1))

def factor(n):
    factors=[]
    if (n==1):
        return [1]
    if (n==2):
        return [1,2]
    for i in range(1,n//2+1):
        if (n%i==0):
            factors.append(i)
    factors.append(n)
    return factors

starttime=time.time()
i=12373
while True:
    print (i)
    testnum=TriNum(i)
    if (testnum%2==0):
        numdiv=len(factor(testnum))
        if (numdiv>500):
            break
    i+=1
print (i,'th Triangle # is: ',TriNum(i))
print ('Time :',time.time()-starttime)

        