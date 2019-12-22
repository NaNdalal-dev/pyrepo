'''
Associative law:
A+(B+C)=(A+B)+c
A.(B.C)=(A.B).c
'''


print('Program to prove Associative law ')
A=int(input('Enter the boolean value for A(1/0):'))
if(A==0 or A==1):
	B=int(input('Enter the boolean value for B(1/0):'))
	if(B==0 or B==1):
		C=int(input('Enter the boolean value for C(1/0):'))
		if(C==0 or C==1):
			print('\npress 1 to prove A+(B+C)=(A+B)+c operation')
			print('press 2 to prove A.(B.C)=(A.B).c operation')
			exp=int(input('My choice :'))
			if(exp==1 or exp==2):
				print('\nValue of A:',A)
				print('Value of B:',B)
				print('Value of C:',C)
	
				if((A==1 or B==1 or A==0 or B==0 or C==1 or C==0)and exp==1):
					print('\nA+(B+C) =',(A or(B or C)))
					print('(A+B)+C =',((A or B) or C))
					if((A or(B or C))==((A or B) or C)):
						print('A+(B+C)==(A+B)+C')
						print('Therefore Associative law satisfied')
					else:
						print('A+(B+C)!=(A+B)+C')
						print('Therefore Associative law not satisfied')
				elif((A==1 or B==1 or A==0 or B==0 or C==1 or C==0)and exp==2):
					print('\nA.(B.C) =',(A and(B and C)))
					print('(A.B).C =',((A and B) and C))
					if((A and(B and C))==((A and B) and C)):
						print('A.(B.C)==(A.B).C')
						print('Therefore Associative law is satisfied')
					else:
						print('A.(B.C)!=(A.B).C')
						print('Therefore Associative law not satisfied')

			else:
				print('Invalid choice for operation')
		else:
			print(C,' is invalid option')
	else:
		print(B,' is invalid option')
else:
	print(A,' is invalid option')


