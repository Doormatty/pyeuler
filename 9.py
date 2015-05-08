import sys
import time
starttime=time.time()
for a in range (1,1000):
    for b in range (a,1000):
        for c in range (b,1000):
            if ((a+b+c)==1000):
                if ((a*a+b*b)==(c*c)):
                    print ('A=',a,' B=',b,' C=',c)
                    print (a,'+',b,'+',c,'=',(a+b+c))
                    print (a,'^2 +',b,'^2 =',c,'^2')
                    print (a*a,'+',b*b,'=',c*c)
                    print ('Time: ',time.time()-starttime)
                    sys.exit()
            elif ((a+b+c)>1000):
                break
                
                    