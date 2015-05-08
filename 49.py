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

for x in range(1000,3334):
    if isPrime(x):
        for y in range(1000,3334):
            if set(str(x))==set(str(y+x)) and isPrime(x+y):
                if set(str(x))==set(str(y+y+x)) and isPrime(x+y+y):
                    print(x,y+x,y+y+x)