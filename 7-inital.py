#328 sec on 1.6Ghz Atom Netbook
import time
starttime=time.time()
x=2
count=0
while (count<10001):
    for y in range (2,(x//2+1)):
        if (x%y==0):
            break
    else:
        count+=1
        #print(count,' - ',x)
    x+=1
print ('Prime #',count,' - ',x-1)
print ('Time: ',time.time()-starttime)