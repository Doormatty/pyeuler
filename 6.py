sumsquare=0
squaresum=0
for x in range(1,101):
    sumsquare=sumsquare+(x*x)
    squaresum+=x
squaresum=squaresum*squaresum
difference=squaresum-sumsquare
print ("Square of Sums: ",squaresum)
print ("Sum of Squares: ",sumsquare)
print ("Difference : ",difference)