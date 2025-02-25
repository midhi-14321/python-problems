n=int(input('enter a number: '))
temp=n
sum=0
while temp>0:
    digit=temp%10
    if digit>=1 and digit%2!=0:
        sum+=digit
    temp=temp//10
print(sum)
    
        