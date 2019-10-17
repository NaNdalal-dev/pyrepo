n=int(input('Enter the number of rows: '))
str1=' '
for i in range(1,n+1):
	
	for j in range(i):
		
		print(str1,' * ',end='')
		str1=str1+''
		
	print()
