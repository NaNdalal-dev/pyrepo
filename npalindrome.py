num=int(input('Enter a number : '))


for n in range(0,num+1):
    m=n
    rev=0
    while(n!=0):
        r=n%10
        rev=(rev*10)+r
        n=n//10
    
    if(rev==m):
        print(rev)
