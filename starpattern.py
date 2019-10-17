n=int(input('Enter number of rows: '))
for i in range(1,n+1):
	for j in range(i):
		print("*",end=" ")
	print()
for i in range(1,n):
	for j in range(i,n):
		print("*",end=' ')
		
	print()
