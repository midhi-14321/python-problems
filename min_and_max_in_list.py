#find the maximum and minimum numbers in a given list.
lst=[10, 20, 5, 40, -1]
max=-1
min=lst[0]
for i in lst:
    if i>max:
        max=i
    elif i<min:
        min=i
print('minimum value is:',min,'\nmaximum value is:',max)

# find min and max values in nested list
lst2=[[8,4,9],[1,6,3],[7,9,28]]
for i in lst2:
    max=float('-inf')
    min=float('inf')
    for j in i:
        if j>max:
            max=j
        if j<min:
            min=j
    print(f"max and min numbers in {i} index list is: {max,min}")

# sum of numbers in a nested list
lst=[[8,4,9],[1,6,3],[7,9,28]]
for i in lst:
    sum=0
    for j in i:
        sum+=j
    print(f"sum of {i} index list is: {sum}")