# sum of even fibonacci series
a=0
b=1
even_sum=0
limit=int(input('enter a limit: '))
for i in range(1,limit+1):
    print(a)
    c=a+b
    a=b
    b=c
    if a%2==0:
        even_sum+=a
print('sum of even fibonacci series is:',even_sum)

