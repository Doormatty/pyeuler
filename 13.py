sum=0
f=open('13input.txt','r')
for line in f:
  sum+=int(line)
f.close()
s=str(sum)
print (s[0:10])

