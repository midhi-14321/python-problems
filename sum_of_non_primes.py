##sum of non prime numbers in a digit
n=int(input('enter a number: '))
temp=n
sum=0
while temp>0:
    digit=temp%10
    if digit>1:
        for i in range(2,digit):
            if digit%i==0:
                sum+=digit
                break
            
    temp=temp//10
print(sum)
    
        