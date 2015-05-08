import time

def repeater(d):
    output=[]
    n=1
    firstzero=True
    while True:
        foo=divmod(n,d)
        if foo[1]==0: return []      #if the remainder is zero, then this is a non-repeating fraction
        if foo in output: return output #if we've seen this remainder/divisor combo, then we're going to repeat
        if foo[0]==0:
            if firstzero==False: output.append(foo)
            firstzero=False
        else:
            output.append(foo)
            n-=(foo[0]*d)
        n*=10
    return foo    


starttime=time.time()
highrepeat=0
highnum=0
for i in range(1,1000):
    bar=len(repeater(i))
    if bar>highrepeat: 
        highrepeat=bar
        highnum=i
print ('1/',highnum,' has ',highrepeat,' repeating digits',sep='')
print ('Time to solve:',time.time()-starttime)