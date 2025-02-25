n=int(input('enter a fibanacci series: '))
a,b=0,1
count=0
while count<n:
    for num in range(a+1,b):
        if count<n:
            print(num,end=" ")
            count+=1
        else:
            break
    a,b=b,a+b