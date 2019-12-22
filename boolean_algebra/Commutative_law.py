'''
Commutative law:
A+B=B+A
A.B=B.A
'''
print('Program to prove commutative law ')
A=int(input('Enter the boolean value for A(1/0):'))
if(A==0 or A==1):
	B=int(input('Enter the boolean value for B(1/0):'))
	if(B==0 or B==1):
		print('press 1 to prove A.B=B.A operation')
		print('press 2 to prove A+B=B+A operation')
		exp=int(input('My choice :'))

		print('\nValue of A:',A)
		print('Value of B:',B)

		if((A==1 or B==1 or A==0 or B==0)and exp==1):
			print('\nA.B =',(A and B))
			print('B.A =',(B and A))
			if((A and B)==(B and A)):
				print('A.B==B.A')
				print('Commutative law satisfied')
			else:
				print('A.B!=B.A')
				print('Commutative law not satisfied')

		elif((A==1 or B==1 or A==0 or B==0)and exp==2):
			print('\nA+B =',(A or B))
			print('B+A =',(B or A))
			if((A or B)==(B or A)):
				print('A+B==B+A')
				print('Commutative law satisfied')
			else:
				print('A.B!=B.A')
				print('Commutative law not satisfied')

	else:
		print(B,' is invalid option')
else:
	print(A,' is invalid option')

