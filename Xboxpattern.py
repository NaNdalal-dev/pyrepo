n=int(input("Enter a number : "))
for i in range(n):
    for j in range(n):
        if(i==j or i==0 or i==n-1 or i+j==n-1 or j==0 or j==n-1):
            print("*",end='')
        else:
            print(end=' ')
    print()