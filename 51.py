from eulerfunctions import *

prime_list = []
tlist = []
count = 0
tstr = ''
gen = primegen()

while len(tlist) < 8:
    tempprime = next(gen)
    strprime = str(tempprime)
    if len(strprime) < 6:
        continue
    for i in range(10):  # Checking to see which digits are multiples
        if strprime.count(str(i)) > 2:
            # print ('Candidate:',tempprime,'has multiple',str(i))
            if strprime.endswith(str(i)):
                #print ('Failure.  Multiple number occurs as LSD.')
                continue
            tlist.append(tempprime)
            for x in range(10):
                tnum = int(strprime.replace(str(i), str(x)))
                if isprime(tnum) and tnum > 100000:
                    #print ('By substituting',str(x),'in place of',str(i),':',tnum,'is also prime.  This is the',len(tlist),'substituted prime in this family.')
                    tlist.append(tnum)
        if len(tlist) > 8:
            break
        tlist = []
print(tlist)
                    

        