lst=[1,2,4,10,6]
flag=False
for i in range(len(lst)-1):
    if lst[i]<lst[i+1]:
        flag=True
    if lst[i]>lst[i+1] :
        flag=False
        break
    
if flag:
    print('sorted')
else:
    print('not sorted')
        