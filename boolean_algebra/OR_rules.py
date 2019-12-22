
'''
logical OR rules:
A+A=A
A+0=A
A+1=1
A.+A`=1
'''
print('Program to check out logical OR rules ')

A=int(input('Enter a boolean expression (1/0) : '))
print('Value of A :',A,'\n')

if(A==1 or A==0):
	print('A+A=',(A or A))
	print('A+0=',(A or 0))
	print('A+1=',(A or 1))
	print('A+A`=',int(A or not(A)))#not keyword is used to negotiate the expression
	
else:
	print('invalid expression')
