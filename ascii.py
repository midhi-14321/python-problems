#print the next aplha if letter is vowel in given string else print the same letter using ascii values
str='midhi'
res=''
vowel='aeiou'
for i in str:
    value=ord(i)
    if ((value>=97 and value<=122) and (i in vowel)):
        res=res+chr(value+1)
    else:
        res=res+i
print(res)