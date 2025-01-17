#second largest number
lst=[10, 20, 15, 40, 30,35]
largest=second_largest=float('-inf')
for i in lst:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i!=largest:
        second_largest=i
print(second_largest)