n=int(input('Enter a number : '))
for i in range(2,n+2):
    if(i%2!=0 and i%n==0):
        print(n)
        i+=1
       