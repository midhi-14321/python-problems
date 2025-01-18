#factors of a number
num=int(input('enter a number: '))
factors=""
for i in range(1,num+1):
    if num%i==0:
        factors+=str(i)+" "
print(factors)