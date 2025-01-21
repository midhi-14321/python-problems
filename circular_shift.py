#Shifting Elements to the Right 
lst=[1,2,3,4,5]
n=len(lst)
last=lst[-1]
for i in range(n-1,0,-1):
    lst[i]=lst[i-1]
lst[0]=last
print(lst)