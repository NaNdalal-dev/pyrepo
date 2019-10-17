num=int(input('Enter a number :'))
for n in range(0,num+1):
    i=n
    ams=0
    dt=len(str(n))
    while(n!=0):
        r=n%10
        ams=ams+r**dt
        n=n//10
    if(i==ams):
        print(i)



    
    
