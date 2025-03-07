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

# swapping number method 4
lst=[9,0,1,5,33]
low=0
high=len(lst)-1
while low<high:
    lst[low],lst[high]=lst[high],lst[low]
    low=low+1
    high=high-1
print(lst)