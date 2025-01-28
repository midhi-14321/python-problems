num=3
fact=True
while(num>0):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                fact=False
                break
        else:
            fact=True
if fact:
    print('prime')
else:
    print('not prime')
        
        
    