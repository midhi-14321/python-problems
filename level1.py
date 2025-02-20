"""Write a program to check if a given number is positive, negative, or zero."""
num=eval(input('enter a number: '))
if num>0:
    print("positive")
elif num==0:
    print('zero')
else:
    print('negative')

"""Determine if a number is odd or even."""
num=eval(input('enter a number: '))
if num%2==0:
    print('even')
else:
    print('odd')

"""Check if a person is eligible to vote (age >= 18)"""
age=eval(input('enter a age: '))
if age>=18:
    print('eligible')
else:
    print('not eligible')

"""Write a program to find the greatest of two numbers."""
num1=eval(input('enter a number num1: '))
num2=eval(input('enter a number num2: '))
if num1>num2:
    print(f"{num1} is greatest")
else:
    print(f"{num2} is greatest")

"""Print "Pass" if a student scores more than 40 marks; otherwise, print "Fail."""
score=eval(input('enter a score: '))
if score>40:
    print('Pass')
else:
    print('Fail')

"""Write a program to display the day of the week based on a 
number input (1 for Monday, 2 for Tuesday, etc.). """
day=int(input("enter a day: "))
match day:
    case 1:
        result="monday"
    case 2:
        result="Tuesday"
    case 3:
        result="Wednesday"
    case 4:
        result="Thrusday"
    case 5:
        result="Friday"
    case 6:
        result="Saturday"
    case 7:
        result="Sunday"
    case _:
        result="Invalid Day"
print(result)

"""Implement a simple calculator to perform addition, 
subtraction, multiplication, and division."""
num1=eval(input('enter a number num1: '))
num2=eval(input('enter a number num2: '))
operation=input('enter a operation: ')
if operation=='+':
    result=num1+num2
elif operation=='-':
    result=num1-num2
elif operation=='*':
    result=num1*num2
else:
    if num2==0:
        print('zero divison error')
    else:
        result=num1/num2
print(f"{num1} {operation} {num2} = {result}")

"""Write a program to display the name of a month based on 
the month number (1 for January, 2 for February, etc.). """
month=int(input("enter a month: "))
match month:
    case 1:
        result="Jan"
    case 2:
        result="Feb"
    case 3:
        result="Mar"
    case 4:
        result="Apr"
    case 5:
        result="May"
    case 6:
        result="jun"
    case 7:
        result="July"
    case 8:
        result="Aug"
    case 9:
        result="Sep"
    case 10:
        result="Oct"
    case 11:
        result="Nov"
    case 12:
        result="Dec"
    case _:
        result="Invalid Month"
print(result)

"""Write a program to find the greatest of three numbers."""
num1=eval(input("enter a num1: "))
num2=eval(input("enter a num2: "))
num3=eval(input("enter a num3: "))
if ((num1>num2) and (num1>num3)):
    print(f"{num1} is greater")
elif ((num2>num1) and (num2>num3)):
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")

"""Check if a year is a leap year. """
yr=int(input('enter a number: '))
if ((yr%4==0 and yr%100!=0) or (yr%400==0)):
    print(f"{yr} is a leap year")
else:
    print(f"{yr} not a leap year")

"""Write a program to classify a character entered by the user 
as a vowel, consonant, or neither. """
char=input('enter a character: ').lower()
vowels='aeiou'
if char in vowels and len(char)==1:
    print("vowels")
elif char.isalpha() and len(char)==1:
    print('consonents')
else:
    print("neither")

"""Calculate the grade of a student based on the marks they 
score: """
marks=eval(input("enter a score: "))
if marks>=90 and score<=100:
    print("Grade A")
elif marks>=80 and marks<=89:
    print("Grade B")
elif marks>=70 and marks<=79:
    print("Grade C")
else:
    print("Fail")

"""Print all numbers from 1 to 100 using a  for  loop"""
for i in range(1,101):
    print(i)

"""Write a program to print the sum of the first  n  natural numbers."""
n=eval(input('enter a number: '))
sum=0
for i in range(1,n+1):
    sum+=i
print(f"sum of {n} natural numbers is:{sum}")

"""Print all even numbers between 1 and 50 using a  while loop."""
n=0
while n<=50:
    if n%2==0:
        print(n)
    else:
        pass
    n+=1

"""Write a program to display the multiplication table of a given 
number. First 20 """
num=eval(input('enter a table: '))
for i in range(1,21):
    print(f"{num} * {i} = {num*i}")

"""Reverse a number using a  while  loop. Also can we get the sum of all the digits."""
num=35781
n=num
sum=0
while num!=0:
    digit=num%10
    sum=sum+digit
    num=num//10
print(f"sum of {n} is: {sum}")

"""Write a program to count the number of digits in a given 
number using a  while  loop. """
num=eval(input('enter a number: '))
count=0
while num!=0:
    digit=num%10
    count+=1 
    num=num//10
print(count)

"""Write a program that keeps asking the user to enter numbers 
until they enter a negative number. Use a  while  loop."""
num=eval(input('enter a number: '))
while num>=0:
    num=eval(input('enter a number: '))

"""Print the first 10 terms of the Fibonacci series using a  for loop."""
a=0
b=1
for i in range(1,11):
    print(a)
    c=a+b 
    a=b 
    b=c

"""Check if a given number is a prime number using a  for loop"""
num=int(input('enter a number: '))
if num==1:
    print('1 is neither prime nor composite')
else:
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print('Prime')
    else:
        print("not a prime")

"""Write a program to calculate the factorial of a number using a while  loop"""
num=int(input('enter a number: '))
fact=1
count=num
while count!=0:
    fact=fact*count
    count-=1 
print(fact)

"""Print all numbers from 1 to 100 that are divisible by 3 and 5 using a  for  loop."""
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)
    else:
        pass

"""Implement a menu-driven program where the user can 
choose to: 
1.  Find the square of a number. 
2.  Find the cube of a number. 
3.  Exit. """
num=int(input('enter a number: '))
user=input('enter a request: ').lower()
if user=='square':
    result=num**2
elif user=='cube':
    result=num**3
else:
    result='exit'
print(result)

    