num=int(input('enter a number: '))
count=0
sum=0
while(num>0):
    digit=num%10
    sum=sum+digit
    count=count+1
    num=num//10
avg=sum//count
print('average of digits is:',avg)