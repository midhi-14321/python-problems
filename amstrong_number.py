# find amstrong number or not
num=int(input('enter a number: '))
temp=num
num1=str(num)
n=len(num1)
sum=0
while num>0:
    digit=num%10
    sum=sum+digit**n
    num=num//10
if sum==temp:
    print('amstrong number')
else:
    print('not a amstrong number')



