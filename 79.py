i=[]
f=open('79input.txt','r')
for line in f:
    i.append(line[:-1])
f.close()

o={}
for n in set(''.join(i)):
    o[int(n)]=set()
    
for n in i:
    o[int(n[0])].add(int(n[1]))
    o[int(n[0])].add(int(n[2]))
    o[int(n[1])].add(int(n[2]))

o=sorted(o,key=o.get)
o.reverse()
print (''.join([str(x) for x in o]))

