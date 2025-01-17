#reverse a list
lst=[1,2,3,4,5]
reverse=[]
for i in range(len(lst)-1,-1,-1):
    reverse.append(i)
print(reverse)
