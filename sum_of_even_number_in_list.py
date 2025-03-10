# sum of even numbers in list
def digit_sum(n):
    sum=0
    temp=n
    while temp!=0:
        digit=temp%10
        sum+=digit
        temp//=10
    return sum
lst=[23,39,242,56]
result=[]
for i in lst:
    if i%2==0:
        res=digit_sum(i)
        result.append(res)
print(result)
