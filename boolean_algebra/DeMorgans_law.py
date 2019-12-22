'''
DeMorgan's_law :
(A+B)`=A`.B`
(A.B)`=A`+B`
'''
A=int(input('Enter the boolean value for A(1/0):'))
if(A==1 or A==0):
	B=int(input('Enter the boolean value for B(1/0):'))
	if(B==0 or B==1):
		print('press 1 to prove (A+B)`=A`.B` ')
		print('press 2 to prove (A.B)`=A`+B` ')
		exp=int(input('My choice : '))
		if(exp==2 or exp==1):
			print('\nValue of A :',A)
			print('Value of B :',B)
			if((A==0 or A==1 or B==1 or B==0) and exp==1):
				print('\n(A+B)` :',int(not(A or B)))
				print('A`.B` :',int((not(A) and not(B))))
				if(not(A or B)==(not(A) and not(B))):
					print('\n(A+B)`==A`.B`')
					print('Therefore DeMorgan\'s law is satisfied')
				else:
					print('\n(A+B)`!=A`.B`')
					print('Therefore  DeMorgan\'s law is not satisfied')
			if((A==0 or A==1 or B==1 or B==0) and exp==2):
				print('(A.B)` :',int(not(A and B)))
				print('A`+B` :',int(not(A) or not(B)))
				if(not(A and B)==(not(A) or not(B))):
					print('\n(A.B)`==A`+B`')
					print('Therefore DeMorgan\'s law is satisfied')
				else:
					print('\n(A.B)`!=A`+B`')
					print('Therefore DeMorgan\'s law is not satisfied')	
				
	
		else:
			print('Invalid choice for operation')
	else:
		print(B,' is invalid option')
	
else:
	print(A,' is invalid option')
