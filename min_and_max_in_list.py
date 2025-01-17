#find the maximum and minimum numbers in a given list.
lst=[10, 20, 5, 40, 15]
max=-1
min=lst[0]
for i in lst:
    if i>max:
        max=i
    elif i<min:
        min=i
print('minimum value is:',min,'\nmaximum value is:',max)