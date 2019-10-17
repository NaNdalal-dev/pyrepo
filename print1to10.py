n=int(input('Enter a number :'))
for i in range(0,n+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
            else:
                pass
        else:
            print(i)
    else:
       pass         

    