lst=[1,2,1,3,2]
new_lst=[]
for i in lst:
    count=0
    for j in lst:
        if(i==j):
            count+=1
    if count>1 and i not in new_lst:
        new_lst.append(i)
print(new_lst)
