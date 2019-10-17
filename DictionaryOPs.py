var={
    'a':1,
    'b':2
    }
print(" var : ",var)
print(" Type : ",type(var))#prints var type
print("Setting a default a :",var.setdefault('a'))#sets a as default
print("Setting a default c :",var.setdefault('c',3))
print("Setting a default d :",var.setdefault('d',4))
print()
print("keys in ",var," are : ",var.keys())#prints keys in var
print("Values in ",var,"are : ",var.values())#prints values in var
print()
get=var.get('a')
print("Getting the values of a : ",get)
print()
print("Var : ",var)
print('\nVar items : ',var.items())
print()
print("Before update : ",var)
var.update({'a':0,'b':1,'c':2,'d':3})

print("After update :",var)
print()
var2=var.copy()
print("Copying var to var2 \n var2 : ",var2)#copy
print()
print("Removing Value a ",var.pop('a'))#removes user defined element 
print("Var : ",var)
print("Popping a element : ",var.popitem())#removes a element from last
set1={'a','b'}
print("Set1 :",set1)
dict1=dict.fromkeys('abcd',0)
print("Converting set to dictionary :")
print("Dict1 : ",dict1)
print()
var.clear()
print("Clearing the Dictionary",var)
