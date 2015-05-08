#Note:  This program will take ~5 days to run to compleation.  Look at using (2n)!/(n!)^2 based equation instead of brute force method

import time

n=20
starttime=time.time()
counter=1
numbers=[0]*n
while True:
    if (numbers[0]==n):  #Is the leftmost digit the highest it can be?  If so, we're done
        break
    numbers[n-1]+=1  #Since we're not done, we can at least add 1
    counter+=1 # Increment the counter
    if (numbers[n-1]>n): # If right number is maxed out, then time for carrying
        for i in range(1,n): # Iterate over the list from left to right, skipping the leftmost digit
            if (numbers[i]>=n): # is the number maxed out?
                numbers[i-1]+=1 # increment the number before it
                for x in range (i,n):
                    numbers[x]=numbers[i-1] # Set all the numbers after it to the value of the number we incremented
                break
print (N,'*',N,'cube:', counter,' Time:',time.time()-starttime,'seconds')
    
                    

                
                
            
    
        
        
        
    