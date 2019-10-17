num=int(input('Enter upper number : '))
num2=int(input('Enter lower number : '))
print('Palindrome numbers in the given interval are :')
for n in range(num,num2+1):
    m=n
    rev=0
    while(n!=0):
        r=n%10
        rev=(rev*10)+r
        n=n//10
    
    if(rev==m):
        print(rev)
