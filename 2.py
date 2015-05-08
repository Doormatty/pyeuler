a, bar = 0, 1
total=0
while (bar<=4000000):
  if (bar%2==0):
    total=total+bar
  a, bar = bar, a+bar
print (total)
    