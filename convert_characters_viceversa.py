# convert all lowercase letters in a string to uppercase and vice versa.
string=input('enter a string: ')
changed=''
for i in string:
    if i.isupper():
        changed+=i.lower()
    else:
        changed+=i.upper()
print(changed)