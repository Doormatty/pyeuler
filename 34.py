from eulerfunctions import factorial


output = []
for i in range(10, 99999):
    runsum = 0
    s = str(i)
    # print ('#',i)
    for n in range(0, len(s)):
        #print(int(s[n:n+1]),'->',factorial(int(s[n:n+1])))
        runsum += factorial(int(s[n:n + 1]))
    #print ('Sum:',runsum,'<->',i)
    if runsum == i:
        output.append(i)
    if i % 5000 == 0: print(i)
print(sum(output))