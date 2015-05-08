import time
starttime=time.time()
def divisors(y):
    divs=[]
    for i in range(1,y//2+1):
        if (y%i==0): divs.append(i)
    return divs
    
def isamicable(n):
    first=sum(divisors(n))
    second=sum(divisors(first))
    if (n==second and first!=n):
        return True
    return False

numsum=0
for i in range (1,10001):
    if (isamicable(i)):
        print (i)
        numsum+=i
print ('Total:',numsum)
print ('Time:',time.time()-starttime)