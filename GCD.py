#lcm of two numbers
num1=int(input('enter a num1: '))
num2=int(input('enter a num2: '))
greater=max(num1,num2)
while True:
    if greater%num1==0 and greater%num2==0:
        lcm=greater
        break
    greater+=1
print(f"lcm of {num1} and {num2} is {lcm}")

#GCD of two numbers
num1=int(input('enter a num1: '))
num2=int(input('enter a num2: '))
n1=num1
n2=num2
while num2!=0:
    num1,num2=num2,num1%num2
print(f"GCD of {n1} and {n2} is: {num1}")
    