num=int(input('Enter a number :'))
ams=0
n=n1=n2=num
count=0
while(n!=0):
    n=n//10
    count+=1

while(n1!=0):
    r=n1%10
    ams=ams+r**count
    n1=n1//10
if(n2==ams):
    print(n2,' is amstrong number. ')
else:
    print(n2,' is not amstrong number. ')
