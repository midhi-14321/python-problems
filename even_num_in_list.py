#find even numbers in a lst
lst=[1,2,3,4,5,6]
even=[]
for i in lst:
    if i%2==0:
        even.append(i)
print(even)