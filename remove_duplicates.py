# remove duplicates
lst=[1,2,1,3,2]
unique=list(dict.fromkeys(lst))
for i in lst:
    if i not in unique:
        unique.append(i)
    else:
        pass
print(unique)
