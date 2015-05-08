import math

def ispenta(n):
    n=(math.sqrt(n*24+1)+1)/6
    return n==int(n)
    
def ishexa(n):
    n=(math.sqrt(n*8+1)+1)/4
    return n==int(n)

def issquare(n):
    return (n==int(math.sqrt(n)))

def istriangle(n):
    return (issquare(n*8+1))

def trigen():
    i=1
    n=0
    while True:
        n+=i
        yield n
        i+=1

d=trigen()
n=0
for i in d:
    n+=1
    if ishexa(i) and ispenta(i):
        print (n,'->',i)