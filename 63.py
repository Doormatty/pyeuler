runsum=0
for i in range(1,100):
    for p in range (1,100):
        x=i**p
        if len(str(x))==p:
            runsum+=1
            print (i,'^',p,'=',x,sep='')
print(runsum)