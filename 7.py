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
        

starttime=time.time()
x=2
count=0
while (count<10001):
    if (isPrime (x)):
        count+=1
    x+=1
print ('Prime #',count,' - ',x-1)
print ('Time: ',time.time()-starttime)