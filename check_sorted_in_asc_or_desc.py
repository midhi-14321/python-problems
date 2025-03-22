lst = [1,2,7,4,5]

ascending = True
descending = True

for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
        ascending = False
        break

for i in range(len(lst) - 1):
    if lst[i] < lst[i + 1]:
        descending = False
        break

if ascending or descending:
    print("sorted")
else:
    print("not sorted")
