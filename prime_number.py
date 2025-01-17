# check prime number or not
num=int(input('enter a number: '))
for j in range(2,num):
    if num%j==0:
        print('not a prime number')
        break
else:
     print('prime number')
