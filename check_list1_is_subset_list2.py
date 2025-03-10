# check lst1 is subset of lst2
lst1=[202,89,112,88]
lst2=[89,202,112,88,65,100]
flag=True
for i in range(len(lst1)):
    if lst1[i] not in lst2:
        flag=False
        print('it is not a subset')
        break
if flag:
    print('it is a subset')