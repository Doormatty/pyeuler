import time
import math
starttime=time.time()
y=1
sum=0
for i in range (1,101):
    y*=i
print (y)

numbers=str(y)
for i in range (0,len(numbers)):
    sum+=int(numbers[i:i+1])
print (sum)
print ('Time:',time.time()-starttime)