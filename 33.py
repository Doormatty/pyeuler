output = []
for d in range(11, 100):
    for n in range(10, d):
        if n % 10 == 0 and d % 10 == 0: break
        for x in range(1, 10):
            td = str(d)
            tn = str(n)
            if (str(x) in td) and (str(x) in tn):
                tn = tn.replace(str(x), '', 1)
                td = td.replace(str(x), '', 1)
                if tn == '0' or td == '0': break  # Break out of the loop if one of the values is 0
                if (int(tn) / int(td)) == (n / d):
                    # print (n,'/',d,'=',n/d,'==',tn,'/',td,'=',int(tn)/int(td))
                    output.append((n, d))

# manually multiplied and reduced fraction by using Fractions class
                    

            
            