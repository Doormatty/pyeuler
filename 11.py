import time
f=open('11input.txt','r')
input=f.read()
f.close()
input=input.replace(' ', '')
input=input.replace('\n','')
square=[]
sum=0
temp=0
starttime=time.time()
for i in range (0,800,2):
    square.append(int(input[i:i+2]))
for i in range (0,400):
    if (i==0):
        i+=1
    #vertical down
    if (i<=339): #all but last three rows - going down
        temp=square[i]*square[i+20]*square[i+40]*square[i+60]
        if (temp>sum):
            sum=temp
    else: #only last three rows - going up
        temp=square[i]*square[i-20]*square[i-40]*square[i-60]
        if (temp>sum):
            sum=temp
    if (i%20<=16): # all but last 3 columns, going right
        temp=square[i]*square[i+1]*square[i+2]*square[i+3]
        if (temp>sum):
            sum=temp
    else: #only last 3 columns, going left
        temp=square[i]*square[i-1]*square[i-2]*square[i-3]
        if (temp>sum):
            sum=temp
    if ((i<=339) and (i%20<=16)): #diag right down
        temp=square[i]*square[i+21]*square[i+42]*square[i+63]
        if (temp>sum):
            sum=temp
    if ((i<=339) and (i%20>=3)): # diag left down
        temp=square[i]*square[i+19]*square[i+38]*square[i+57]
        if (temp>sum):
            sum=temp
    if ((i>=57) and (i%20<=16)): #diag right up
        temp=square[i]*square[i-21]*square[i-42]*square[i-63]
        if (temp>sum):
            sum=temp
    if ((i>=57) and (i%20>=3)): #diag left up
        temp=square[i]*square[i-19]*square[i-38]*square[i-57]
        if (temp>sum):
            sum=temp
print (sum)
print ('Time :',time.time()-starttime)