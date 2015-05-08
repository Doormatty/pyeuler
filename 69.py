import math
import eulerfunctions



def phi(n):
    count=0
    if n==1:
        return 1
    first=set(eulerfunctions.primefac(n))
    for foo in range(1,n):
        second=set(eulerfunctions.primefac(foo))
        if first.intersection(second)==set():
            count += 1
    return count


high = 0
highnum = 0
# for i in range(2, 1000001):
#
#     if eulerfunctions.isPrime(i):
#         x = i / phi(i)
#         #print i," - ",phi(i)
#         if x > high:
#             high = x
#             highnum = i

p=eulerfunctions.primegen()
for number,i in enumerate(p):
    if number % 1000 == 0:
        print number,i
    x = i / phi(i)
    if x > high:
        high = x
        highnum = i
    if i>1000000:
        break

print (highnum, high)
