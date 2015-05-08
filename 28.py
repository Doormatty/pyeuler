def sumdiags(n): #return the sum of the diagonals for a clockwise spiral of size n*n
   diaglen=int(((n-1)/2)+1)
   ur,ul,dr,dl=0,0,0,0
   for n in range(2,diaglen+1):
       ur+=(n*n*4)-(4*n)+1
       dr+=(n*n*4)-(10*n)+7
       ul+=(n*n*4)-(6*n)+3
       dl+=(n*n*4)-(8*n)+5
   return (ur+dr+ul+dl+1)