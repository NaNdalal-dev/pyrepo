'''
Operations on sets:
1)Union(|)
2)Intersection(&)
3)Difference(-)
4)Symmetric difference(-|-)
'''

vowels={'a','e','i','o','u'}#universal set

setA={'a','e','i'}	#set1

setB={'a','o','u'}#set2

print('Total set :',vowels)
print('set A :',setA)
print('set b :',setB)
print()
#union operation
print(setA,'union',setB,':')
print(setA.union(setB))
'''or you can use | symbol for union operation
print(setA|setB)'''

print()
print(setA,'intersection',setB,':')

print(setA.intersection(setB))
'''#or
print(setA&setB)'''


print()
print('difference between',setA,'and',setB,':')
print(setA.difference(setB))
'''
or use setA-setB
'''
print()
print('symmetric difference between',setA,'and',setB,':')
print((setA.difference(setB)).union(setB.difference(setA)))
'''
or use (setA-setB)|(setB-setA) 
'''
if((setA and setB)<vowels):
	print('\n\n',setA,setB,'are subsets of',vowels)
else:
	print('\n\n',setA,setB,'are not subsets of',vowels)

print('\ncompliment of setA :')
print(vowels-setA)
print('\ncompliment of setB :')
print(vowels-setB)
