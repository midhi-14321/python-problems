# print prime numbers in the given range
num=int(input('enter a range: '))
if num>1:
    for i in range(1,num+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)
else:
    print('pls enter the range greater than 1')