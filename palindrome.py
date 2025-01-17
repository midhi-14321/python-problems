#check if a given string is a palindrome.
palindrome=input('enter a string: ')
reverse=""
for i in range(len(palindrome)-1,-1,-1):
    reverse+=palindrome[i]
if palindrome==reverse:
    print('palindrome')
else:
    print('not a palindrome')