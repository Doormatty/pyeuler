temp,runsum=0,0
for i in range (2,10000000):
    for x in str(i):
        temp+=int(x)**5
    if temp==i: runsum+=i
    temp=0