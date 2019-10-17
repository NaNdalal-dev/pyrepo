def rfun(n):
    if(n==1):
        return 1
    f=n*rfun(n-1)
    return f
k=rfun(5)    
print(k)