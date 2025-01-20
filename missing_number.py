lst=[1,2,4,5]
min_value=min(lst)
max_value=max(lst)
for i in range(min_value,max_value+1):
    if i not in lst:
        print(i,'is the missing number')
        