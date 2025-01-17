lst=[1,2,3,4,5,1,2,2]
count=0
for i in lst:
    if i==2:
        count+=1
print(count)
#using count method
count1=lst.count(1)
print(count1)