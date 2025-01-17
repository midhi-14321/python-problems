# List to be sorted
lst = [4, 2, 5, 1, 3]
# Selection Sort Algorithm
n = len(lst)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if lst[j] < lst[min_index]:
            min_index = j
    lst[i], lst[min_index] = lst[min_index], lst[i]
print("Sorted list:", lst)
