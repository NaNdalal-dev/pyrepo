n=int(input('Enter the number of rows : '))
k=2
for i in range(1,n+1):
    for j in range(1,2*n):
        if(i+j==n+1 or j-i==n-1):    
            print("*",end='')
        elif(i==n and j!=k):
            print("*",end="")
            k+=2

        else:
            print(end=' ')
    print()