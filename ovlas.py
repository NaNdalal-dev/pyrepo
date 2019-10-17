sen=input("type a sentence :")
string=sen.lower()
print('Sentence you entered :',string)
count=0
list1=['a','e','i','o','u']
for char in string:
    if char in list1:
        count+=1
print(count)