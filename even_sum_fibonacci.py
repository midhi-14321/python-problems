# sum of even fibonacci numbers
num=int(input('enter a limit: '))
a=0
b=1
even_sum=0
for i in range(num):
    # print(a)
    if a%2==0:
        even_sum+=a
    c=a+b
    a=b
    b=c
print(even_sum)
