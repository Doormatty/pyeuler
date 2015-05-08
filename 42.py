def istrinum(n):
    x=1
    while True:
        y=sum(range(1,x+1))
        if n==y: 
            return True
        elif (y>n):
            return False
        x+=1
        
f=open('42input.txt','r')
names=str(f.read())
names=names.replace("\"",'')
names=names.split(',')
names.sort()
highnum=0
highword=''
for line in names:
    line2=line[:len(line)]
    runsum=0
    for char in line2:
        runsum+=(ord(char)-64)
    if istrinum(runsum):
        highnum+=1
print (highnum)