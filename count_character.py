#find how many times a specific character appears in a string.
string=input('enter a string: ')
word=input('enter a word: ')
print(string.count(word))
#normal method
count=0
for i in string:
    if i=='a':
        count+=1
print('a appears in a string',count)
