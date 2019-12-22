'''
COMPLIMENT rule:
(A`)`=A
'''
print('Program to check out compliment of a value')
A=int(input('Enter a boolean expression (1/0) : '))
print('Value of A :',A,'\n')
if(A==0 or A==1):
	print('A :',int(A))
	print('A` :',int(not(A)))#not keyword is used to negotiate the expression 
	print('(A`)`:',int(not(not(A))))
else:
	print(A,' is invalid value')
