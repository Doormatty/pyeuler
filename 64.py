import math

#def contfrac(x):
#    xsqr=math.sqrt(x)
#    m=[]
#    d=[]
#    a=[]
#    m.append(0)
#    d.append(1)
#    a.append(math.floor(xsqr))
#    print ('m[0]=',m[0],sep='')
#    print ('d[0]=',d[0],sep='')
#    print ('a[0]=',a[0],sep='')
#    for i in range(1,10):
#        m.append(int(d[i-1]*a[i-1]-m[i-1]))
#        d.append(int((x-m[i]**2)/d[i-1]))
#        a.append(math.floor((a[0]+m[i])/d[i]))
#        print ('m[',i,']=',m[i],sep='')
#        print ('d[',i,']=',d[i],sep='')
#        print ('a[',i,']=',a[i],sep='')
        
def contfracper(x):
    xsqr=math.sqrt(x)
    if int(xsqr)==xsqr:
        return 0
    olist=[]
    olist.append((0,1,math.floor(xsqr)))
    i=0
    while True:
        i+=1
        m=int(olist[i-1][1]*olist[i-1][2]-olist[i-1][0])
        d=int((x-m**2)/olist[i-1][1])
        a=math.floor((olist[0][2]+m)/d)
        if (m,d,a) in olist:
            break
        else:
            olist.append((m,d,a))
#    print ('Square root of',x,'-> ',end='')
#    print (olist[0][2],';',sep='',end='')
#    for i in range(1,len(olist)):
#        print (olist[i][2],',',sep='',end='')
#    print ('...')
#    print ('Period:',len(olist)-1)
    return len(olist)-1

runsum=0
for i in range(1,10001):
    if contfracper(i)%2!=0:
        runsum+=1
print (runsum)