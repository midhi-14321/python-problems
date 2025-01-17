#remove all spaces from a string
string=input('enter a string: ')
no_space=""
for i in string:
    if i!=' ':
        no_space+=i
print(no_space)
print(string.replace(" ",""))