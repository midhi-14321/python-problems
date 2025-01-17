#merge two lists
lst1=[1,2,3]
lst2=[4,5,6]
merged_lst=lst1[:]
for i in lst2:
    merged_lst.append(i)
print(merged_lst) #method 1
print(lst1+lst2) #method2
lst1.extend(lst2)
print(lst1) #method3