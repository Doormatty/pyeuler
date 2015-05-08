
def ordinal(y):
    output=''
    numbers=list(str(y))
    if (len(numbers)==2):
        if (numbers[len(numbers)-2]=='1'):
            if (numbers[1]=='0'):
                return 'ten'
            elif (numbers[1]=='1'):
                return 'eleven'
            elif (numbers[1]=='2'):
                return 'twelve'
            elif (numbers[1]=='3'):
                return 'thirteen'
            elif (numbers[1]=='4'):
                return 'fourteen'
            elif (numbers[1]=='5'):
                return 'fifteen'
            elif (numbers[1]=='6'):
                return 'sixteen'
            elif (numbers[1]=='7'):
                return 'seventeen'
            elif (numbers[1]=='8'):
                return 'eighteen'
            elif (numbers[1]=='9'):
                return 'nineteen'
        elif (numbers[0]=='2'):
            output+='twenty'
        elif (numbers[0]=='3'):
            output+='thirty'
        elif (numbers[0]=='4'):
            output+='forty'
        elif (numbers[0]=='5'):
            output+='fifty'
        elif (numbers[0]=='6'):
            output+='sixty'
        elif (numbers[0]=='7'):
            output+='seventy'
        elif (numbers[0]=='8'):
            output+='eighty'
        elif (numbers[0]=='9'):
            output+='ninety'
    if (len(numbers)>1):
        output+=' '
        i=1
    else:
        i=0
    if (numbers[i]=='1'):
        output+='one'
    elif (numbers[i]=='2'):
        output+='two'
    elif (numbers[i]=='3'):
        output+='three'
    elif (numbers[i]=='4'):
        output+='four'
    elif (numbers[i]=='5'):
        output+='five'
    elif (numbers[i]=='6'):
        output+='six'
    elif (numbers[i]=='7'):
        output+='seven'
    elif (numbers[i]=='8'):
        output+='eight'
    elif (numbers[i]=='9'):
        output+='nine'
    return output
    

def numstring(n):
    output=''  
    numbers=list(str(n))
    numbers.reverse()
    if (len(numbers)==0 and numbers[0]=='0'):
        return 'zero'
    if (len(numbers)==4):
        output+=ordinal(numbers[3])+' thousand'
    if (len(numbers)>=3):
        if (numbers[2]!='0'):
            if (numbers[1]=='0' and numbers[0]=='0'):
                output+=' '+ordinal(numbers[2])+' hundred'
            else:
                output+=ordinal(numbers[2])+' hundred and '
    if (len(numbers)>=2):
        output+=ordinal(int(numbers[1]+numbers[0])) 
    elif (len(numbers)==1):
        output+=ordinal(numbers[0])
    return output

count=0
for i in range (1,1001):
    number=numstring(i).replace(' ', '')
    count+=len(number)
print (count)


    
