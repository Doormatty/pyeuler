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
            #f=5
            for f in range(5,r+1,6):
            #while (f<=r):
                if (n%f==0):
                    break
                if (n%(f+2)==0):
                    break
            else:
                yield n


highnum=0    
for i in range(7654321,1234567,-1):
    l=list(str(i))
    if (len(l)==len(set(l))) and (not '0' in l and not '9' in l and not '8' in l):
        print (l)
        if isPrime(i):
            highnum=i
            print('Answer:',i)
            break