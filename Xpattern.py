n=int(input('Enter a number :'))
for i in range(0,n+1):
    for j in range(0,n+1):
        if(i==j or i+j==n):
            print("*",end="")
        else:
            print(end=" ")
    print()