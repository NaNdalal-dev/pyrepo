
n=int(input('Enter the number pf rows'))
for row in range(0,n+1):
	val=row+1
	dec=n-1
	for j in range(val):
		print(val,end="")
		val-=1
		dec-=1
	print()
