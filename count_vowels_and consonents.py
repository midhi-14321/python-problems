# count no of vowels and consonents
string=input('enter a string: ')
vowels=0
consonents=0
for i in string:
    if i in 'aeiou':
        vowels+=1
    else:
        consonents+=1
print('vowels=',vowels,'consonents =',consonents)
