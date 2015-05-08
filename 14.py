import time
def collatz(n):
    chain=1
    while (n!=1):
        if (n%2==0):
            n/=2
        else:
            n=n*3+1
        chain+=1
    return chain

ccount=0
ncount=0
starttime=time.time()
for i in range (1,1000001):
    foo=collatz(i)
    if (foo>ccount):
        ccount=foo
        ncount=i
print (ncount)
print ('Time:',time.time()-starttime)