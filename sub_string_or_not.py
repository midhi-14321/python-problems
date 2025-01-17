# check string is substring or not
string=input('enter a string: ')
sub_string=input('enter a substring: ')
if sub_string in string:
    print('yes it is a sub string')
else:
    print('not a substring')
#using find method
if string.find(sub_string)!=-1:
    print('yes')
else:
    print("no")