#check for password validation 
str='Password@@123'
upper=0
lower=0
special=0
digit=0
n=len(str)
for i in str:
    value=ord(i)
    if (value>=65 and value<=90):
        upper+=1
    elif (value>=97 and value<=122):
        lower+=1
    elif (value>=48 and value<=57):
        digit+=1
    else:
        special+=1

if ((upper>=1) and (lower>=1) and (digit>=1) and (special==1) and (n>=8) and (n<=16)):
    print("Password is valid")
else:
    print('password is invalid')

    

