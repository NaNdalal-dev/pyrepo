'''
Absorption_law :
A+(A.B)=A
A.(A+B)=A
'''
A=int(input('Enter the boolean value for A(1/0):'))
if(A==1 or A==0):
	B=int(input('Enter the boolean value for B(1/0):'))
	if(B==0 or B==1):
		print('press 1 to prove A+(A.B)=A ')
		print('press 2 to prove A.(A+B)=A ')
		exp=int(input('My choice : '))
		if(exp==2 or exp==1):
			print('\nValue of A :',A)
			print('Value of B :',B)
			if((A==0 or A==1 or B==1 or B==0) and exp==1):
				print('\nA+(A.B) :',A or (A and B))
				print('A :',A)
				if((A or (A and B))==A):
					print('\nA+(A.B)==A')
					print('Therefore Absorption law is satisfied')
				else:
					print('\nA+(A.B)!=A')
					print('Therefore Absorption law is not satisfied')
			if((A==0 or A==1 or B==1 or B==0) and exp==2):
				print('A.(A+B) :',A and (A or B))
				print('A :',A)
				if((A or (A and B))==A):
					print('\nA.(A+B)==A')
					print('Therefore Absorption law is satisfied')
				else:
					print('\nA.(A+B)!=A')
					print('Therefore Absorption law is not satisfied')	
				
	
		else:
			print('Invalid choice for operation')
	else:
		print(B,' is invalid option')
	
else:
	print(A,' is invalid option')
