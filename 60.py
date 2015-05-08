import itertools
import math

#Checks if a number is Prime
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

def primecheck (x,y):
    x0=str(x)
    x1=str(y)
    c1=int(x0+x1)
    ic1=int(x1+x0)
    if (c1 not in pset) or (ic1 not in pset):
        return False
    else:
        return True


prime_list=[]
pset=set()
olist=[]
f=open('10Mprimes2.txt','r')
highnum=0

for i in range(0,1400):
    prime_list.append(int(f.readline()))
f.close

f=open('10Mprimes2.txt','r')
for i in range(0,9000000):
    highnum=int(f.readline())
    pset.add(highnum)
f.close

print(highnum)

print ('Finished prime preload')

combo=itertools.combinations(prime_list,2)
for x in combo:
    if not primecheck(x[0],x[1]):
        continue
    else:
        olist.append([x[0],x[1]])
    
print (len(olist),'Double primes found')    
    
for i in olist:
    for f in prime_list:
        if f in i:
            continue
        else:
            if primecheck(i[0],f) and primecheck(i[1],f):
                i.append(f)
                break

print (len(olist),'Triple primes found')

print ('Going into cleanup with',len(olist),'items.')

for i in olist:
    i.sort()
for i in olist:
    if olist.count(i)>1:
        olist.remove(i)

print ('Finished Output list cleanup with',len(olist),'items.')

olist=[i for i in olist if len(i)==3]

for i in olist:
    for f in prime_list:
        if f in i:
            continue
        else:
            if primecheck(i[0],f) and primecheck(i[1],f) and primecheck(i[2],f):
                i.append(f)
                break

print (len(olist),'Quad primes found')

print ('Going into cleanup with',len(olist),'items.')

for i in olist:
    i.sort()
for i in olist:
    if olist.count(i)>1:
        olist.remove(i)

print ('Finished Output list cleanup with',len(olist),'items.')

olist=[i for i in olist if len(i)==4]

print ('Beginning fifth prime check')

for i in olist:
    for f in prime_list:
        if f in i:
            continue
        else:
            if primecheck(i[0],f) and primecheck(i[1],f) and primecheck(i[2],f) and primecheck(i[3],f):
                i.append(f)
                break
            
olist=[i for i in olist if len(i)==5]
o2list=[sum(i) for i in olist
o2list.sort()

print (o2list[0])

        


