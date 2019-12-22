'''
Distributive law :
A+(B.C)=(A+B).(A+C)
A.(B+C)=(A.B)+(A.C)
'''
print('Program to prove Distributive law ')
A=int(input('Enter the boolean value for A(1/0):'))
if(A==0 or A==1):
	B=int(input('Enter the boolean value for B(1/0):'))
	if(B==0 or B==1):
		C=int(input('Enter the boolean value for C(1/0):'))
		if(C==0 or C==1):
			print('\npress 1 to prove A+(B.C)=(A+B).(A+C) operation')
			print('press 2 to prove A.(B+C)=(A.B)+(A.C) operation')
			exp=int(input('My choice :'))
			if(exp==1 or exp==2):
				print('\nValue of A:',A)
				print('Value of B:',B)
				print('Value of C:',C)
				if((A==1 or B==1 or A==0 or B==0 or C==1 or C==0)and exp==1):
					print('\nA+(B.C) =',A or(B and C))
					print('(A+B).(A+C) =',((A or B)and (A or C)))
					if(A or(B and C)==((A or B)and (A or C))):
						print('\nA+(B.C)==(A+B).(A+C)')
						print('Therefore Distributive law is satisfied')
					else:
						print('(A or(B and C))!=((A or B)and (A or c))')
						print('Therefore Distributive law is not satisfied')	
			
				elif((A==1 or B==1 or A==0 or B==0 or C==1 or C==0)and exp==2):
					print('\nA.(B+C) =',A and(B or C))
					print('(A.B)+(A.C) =',((A and B) or (A and C)))
					if((A or(B and C))==((A or B)and (A or C))):
						print('\nA.(B+C) ==(A.B)+(A.C)')
						print('Therefore Distributive law is satisfied')
					else:
						print('(A or(B and C))!=((A or B)and (A or c))')
						print('Therefore Distributive law is not satisfied')

			
			else:
				print('Invalid choice for operation')

		else:
			print(C,' is invalid option')
	else:
		print(B,' is invalid option')
else:
	print(A,' is invalid option')
