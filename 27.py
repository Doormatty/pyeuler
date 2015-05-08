import math
import time

def isPrime(n):
    if (n<0):
        return False
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
highx,highy,highprime=0,0,0  
for x in range (-999,1000):
    for y in range (-999,1000):
        primecount=0
        for n in range(0,1000):
            foo=(n*n)+(n*x)+y
            if isPrime(foo):
                primecount+=1
            else:  
                break
        if (primecount>highprime):
            #print ('New Possible Record: x=',x,' y=',y,' primecount=',primecount,sep='')
            highprime=primecount
            highx=x
            highy=y
print('n^2+',highx,'n+',highy,' has ',highprime,' primes in a row.',sep='')
print('Time:',time.time()-starttime)