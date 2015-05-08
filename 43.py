import itertools
runsum=0
pandig=itertools.permutations('0123456789')
for number in pandig:
    if number[0]=='0':
        next
    if  (int(number[1]+number[2]+number[3])%2!=0):
        next
    elif  (int(number[2]+number[3]+number[4])%3!=0):
        next
    elif  (int(number[3]+number[4]+number[5])%5!=0):
        next
    elif  (int(number[4]+number[5]+number[6])%7!=0):
        next
    elif  (int(number[5]+number[6]+number[7])%11!=0):
        next
    elif  (int(number[6]+number[7]+number[8])%13!=0):
        next
    elif  (int(number[7]+number[8]+number[9])%17!=0):
        next
    else:
        runsum+=int(number[0]+number[1]+number[2]+number[3]+number[4]+number[5]+number[6]+number[7]+number[8]+number[9])
print (runsum)