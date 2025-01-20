lst2=[1,2,3,4,5,6]
count=0
for i in lst2:
    if i>=2:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            count+=1
print(count)