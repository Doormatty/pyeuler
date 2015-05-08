f=open('22input.txt','r')
names=str(f.read())
names=names.replace("\"",'')
names=names.split(',')
names.sort()
runsum=0
for i in range(0,len(names)):
    tsum=0
    for c in names[i]:
        tsum+=(ord(c)-64)
    runsum+=(tsum*(i+1))
print (runsum)

    

    