import time
import math
starttime=time.time()
y=2
sum=0
for i in range (0,999):
    y*=2
print (y)

numbers=str(y)
for i in range (0,len(numbers)):
    sum+=int(numbers[i:i+1])
print (sum)
print ('Time:',time.time()-starttime)