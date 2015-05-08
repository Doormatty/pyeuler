from fractions import Fraction
import math

runsum=0
x=Fraction(0)
for i in range(0,1001):
    x=1/(2+x)
    y=x+1
    if len(str(y.numerator))>len(str(y.denominator)):
        print ('Expansion #',i+1,'is',y.numerator,'/',y.denominator)
        runsum+=1
print ('Total # of fractions where N has more digits than D=',runsum)




