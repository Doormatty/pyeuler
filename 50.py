from eulerfunctions import *

runsum = 0
lowmark = 0
highmark = 0
prime_list = []
tlist = []
p = primegen()
x = next(p)
while x < 1000000:
    prime_list.append(x)
    x = next(p)

print('Generated Primes up to 1 million')

for i in prime_list:
    if i == 2:
        tlist.append(i)
        continue
    if sum(tlist) + i < 1000000:
        tlist.append(i)
    else:
        break

while not isprime(sum(tlist)):
    a = tlist.pop(0)

print('Final!')
print(tlist, 'sums to', sum(tlist))
    
        


    



