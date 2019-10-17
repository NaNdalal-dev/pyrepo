import number
n=int(input('Enter a lower number :'))
n2=int(input('Enter a upper number :'))
for i in range(n,n2+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
            
        else:
            print(i)
    else:
       None         

    