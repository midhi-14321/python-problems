lst = [0, 1, 2, 0, 1, 5, 0]
total_sum = 0
lst1=[]

for i in range(len(lst)):
    if lst[i] == 0: 
        max=0# Check for zero
        for j in range(i + 1, len(lst)):
            if lst[j]==0:
                break
            else:
                total_sum+=lst[j]
        max=total_sum
        lst1.append(max)
        
             # Add the subsequent values
print(lst1)
print("Total sum:", total_sum)

