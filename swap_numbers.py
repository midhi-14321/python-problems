#swapping two numbers without third variable
print('method 1')
a=int(input('enter a number1: '))
b=int(input('enter a number2: '))
print('before swapping a,b:',a,b)
a=a+b
b=a-b
a=a-b
print('after swapping a,b:',a,b)
print('***************************')

#method 2
print('method 2')
a=int(input('enter a number1: '))
b=int(input('enter a number2: '))
a,b=b,a
print(a,b)
print('***************************')

#method three
print('method 3')
a=int(input('enter a number1: '))
b=int(input('enter a number2: '))
a=a*b
b=a//b
a=a//b
print(a,b)

