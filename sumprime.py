n=int(input('Enter a number : '))
sum=0
while(n!=0):
    r=n%10
    if(r>1):
        for i in range(2,r):
            if(r%i==0):
                break
        else:
            sum+=r        
        
    else:
        break
        
    
    n=n//10
print('Sum of prime numbers : ',sum)