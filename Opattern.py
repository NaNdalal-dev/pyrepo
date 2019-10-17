n=int(input('Enter a number : '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if((i==1 and(j>1 and j<n))or (j==1 and(i>1 and i<n)) or (i==n and(j>1 and j<n)) or (j==n and(i>1 and i<n))):
            print("*",end='')
        else:
            print(end=' ')
    print()