import tkinter
l=int(input('Enter a lower number : '))

for n in range(1,l+1):
    m=0
    for i in range(1,n):
        if(n%i==0):
            m=m+i
    if(n==m):
        print(m)
