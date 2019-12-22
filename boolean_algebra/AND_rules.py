
'''
logical AND rules:
A.A=A
A.0=0
A.1=A
A.A`=0
'''
print('Program to check out logical AND rules ')

A=int(input('Enter a boolean expression (1/0) : '))
print('Value of A :',A,'\n')
if(A==1 or A==0):
	print('A.A=',(A and A))
	print('A.0=',(A and 0))
	print('A.1=',(A and 1))
	print('A.A`=',int(A and not(A)))#not keyword is used to negotiate the expression
	
else:
	print(A,'is invalid value')
