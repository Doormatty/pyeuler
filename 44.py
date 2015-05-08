import math
def ispenta(n):
    n=(math.sqrt(n*24+1)+1)/6
    return n==int(n)

def pentagen():
    i=1
    while True:
       yield int(i/2*(3*i-1))
       i+=1


penlist=[]
d=pentagen()
for i in d:
    penlist.append(i)
    for z in penlist:
        if (i-z<=0):
            break
        if ispenta(i-z) and ispenta(z+i):
            print (i,z,'->',abs(i-z))