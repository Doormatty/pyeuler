from numpy import *
import time

def sumdiag(x,y,dir): #(0=left,1=right)
    sum=0
    for i in range(0,lines-y):
        if (dir==0):
            sum+=m[i+y][x]
        else:
            sum+=m[i+y][x+i]
    return sum

# Reads an arbatrary sized triangle into an array
lines=0
f=open('18input.txt','r')
for line in f:
    lines+=1
f.seek(0)   #Reset the file pointer
m=zeros((lines,lines), dtype=int) #Create the destination array
for i in range(0,lines):
    m[i][0:i+1]=f.readline().split()
f.close

#print (m)
print('Matt\'s Method')
print(m[0][0],end='')
x,sum=0,0
sum+=m[0][0]
for y in range(1,lines):
    if (sumdiag(x,y,0)<sumdiag(x,y,1)):
        x+=1
    print (' -> ',end='')
    sum+=m[y][x]
    print (m[y][x],end='')
print ('\nTotal:',sum)
print ('')

print ('Carly\'s Method')
x,sum=0,0
print(m[0][0],end='')
sum+=m[0][0]
for y in range(0,lines-1):
    print (' -> ',end='')
    if (m[y+1][x]>m[y+1][x+1]):
        sum+=m[y+1][x]
        print(m[y+1][x],end='')
    else:
        sum+=m[y+1][x+1]
        print(m[y+1][x+1],end='')
        x+=1
print ('\nTotal:',sum)
print ('')

def recurse(y,x):  #Performs a triangle recursion, and just returns max sum
    if ((y+1)==(lines-1)):   
        return (m[y][x]+max(m[y+1][x],m[y+1][x+1]))
    else:
        return (m[y][x]+max(recurse(y+1,x),recurse(y+1,x+1)))
    
def recursepath(y,x):  #Same as recurse(), but returns path taken
    if ((y+1)==(lines-1)):   
        foo=max(m[y+1][x],m[y+1][x+1])
        return m[y][x]+foo,foo
    else:
        L=recursepath(y+1,x)
        R=recursepath(y+1,x+1)
        if (L[0]>R[0]):
            if (y==0):
                path=((m[0][0],m[y+1][x])+L[1:len(L)])
            else:
                path=((m[y+1][x],)+L[1:len(L)])
            return (m[y][x]+L[0],)+path
        else:
            if (y==0):
                path=((m[0][0],m[y+1][x+1])+R[1:len(R)])
            else:
                path=((m[y+1][x+1],)+R[1:len(R)])
            return (m[y][x]+R[0],)+path
            
            
print ('Brute Force')
foo=recursepath(0,0)
print (foo[1],'-> ',end='')
for i in range(2,len(foo)-1):
    print(foo[i],'-> ',end='')
print (foo[len(foo)-1])
print ('Total:',foo[0])
        
    
    
    