n=int(input('Enter a number : '))
id=0
while(n!=0):
    r=n%10
    if(id<r):
        id=r
    n=n//10
print('Highest number in given number is :',id)