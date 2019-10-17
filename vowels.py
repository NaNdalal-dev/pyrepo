sen=input("Type a sentence :")
string=sen.lower()
print('Sentence you entered :',string)
vowel=0
consonant=0
blank=0
list1=['a','e','i','o','u']
for char in string:
    if char in list1:
        vowel+=1
    else:
        consonant+=1
print('Number of vowels in the sentence are : ',vowel)
print('Number of consonants in the sentence are :',consonant)
