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
    
def iscircleprime(n):
    if not isPrime(n): return False
    n=str(n)
    for i in range(0,len(n)-1):
        n=n[1:]+n[0:1]
        if not isPrime(int(n)): return False
    return True

count=0
for i in range(1,1000000):
    if iscircleprime(i):
        count+=1
print (count)